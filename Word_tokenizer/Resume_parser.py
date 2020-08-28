# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 18:36:52 2020

@author: himanshu_bhujbal
"""


import glob
import pandas as pd
import io
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')
nltk.download('stopwords')


pdf_dir = "\\Word_tokenizer" #enter the path where pdf profile are kept

def extract_text_from_pdf(pdf_path):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle)
    page_interpreter = PDFPageInterpreter(resource_manager, converter)

    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh, 
                                      caching=True,
                                      check_extractable=True):
            page_interpreter.process_page(page)

        text = fake_file_handle.getvalue()

    # close open handles
    converter.close()
    fake_file_handle.close()

    if text:
        return text

   


#this for loop is to extract all the data form PDF and save it into a variable and then append it into a csv    
for file in glob.glob("%s/*.pdf" % pdf_dir): # this line of code is looking for pdf file in the given path
     if __name__ == '__main__':        
        df2 = extract_text_from_pdf(file)
        f = open("Summary_of_profile.csv", "a")
        f.write(df2)
        f.close()
        
        
        