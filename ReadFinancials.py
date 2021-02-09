"""
Author: Bharani Deepak
Info  : This script reads the financial data  from the folder "inputs"
"""

import os

source_path = os.path.dirname(__file__)
source_path = source_path.replace('/','\\')

# files inside "input" folder is defined in tuple
input_data = ('balance_sheet.txt','cash_flow.txt','income_statement.txt')


for file in input_data:
    path = []
    path.append(os.path.join(source_path,'inputs\\',file))
    print(file,path)



# with open(path[0],'r') as bs:
#     for l in bs:
#         print(l.strip())
