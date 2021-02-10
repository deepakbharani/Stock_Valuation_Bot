"""
Author: Bharani Deepak
Info  : This script reads the financial data  from the folder "inputs"
"""

import os

# source_path is the path where this script is saved
source_path = os.path.dirname(__file__)
source_path = source_path.replace('/','\\')

# files inside "input" folder is defined in tuple
input_data = ('balance_sheet.txt','cash_flow.txt','income_statement.txt')

# Set path for all the financial files inside "inputs" folder
path = []
for file in input_data:
    path.append(os.path.join(source_path,'inputs\\',file))

for i in range(len(path)):
    with open(path[i],'r') as bs:
        print("Data Read")
