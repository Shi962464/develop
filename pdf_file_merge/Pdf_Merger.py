# -*- coding: utf-8 -*-
import os
from PyPDF2 import PdfMerger


def merge_pdf(file_path, output_path):
    merger = PdfMerger()
    name = [f for f in os.listdir(file_path) if f.endswith('.pdf')]
    name.sort()
    for file in name:
        merger.append(os.path.join(file_path, file))
    merger.write(output_path)
    merger.close()


if __name__ == '__main__':
    folder = r'C:\Users\Administrator\Desktop\Python资料及其他\Python_Study\StudyPython\Pyton之自动化脚本炼金术\pdf_file_merge\test_pdf'
    output = r'C:\Users\Administrator\Desktop\Python资料及其他\Python_Study\StudyPython\Pyton之自动化脚本炼金术\pdf_file_merge\test_pdf_output\merge.pdf'
    merge_pdf(folder, output)
