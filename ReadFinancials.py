"""
Author: Bharani Deepak
Info  : This script reads the financial data  from the folder "inputs"
"""

import os

# source_path = Path where the script is saved 
source_path = os.path.dirname(__file__)
source_path = source_path.replace('/','\\')

# files inside "input" folder is defined in tuple
input_data = ('balance_sheet.txt','cash_flow.txt','income_statement.txt')

balance_sheet = os.path.join(source_path,'inputs\\',input_data[0])
print(balance_sheet)

with open(balance_sheet,'r') as bs:
    for l in bs:
        print(l.strip())
