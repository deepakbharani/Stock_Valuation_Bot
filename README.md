# Stock_Valuation_Bot

This project is developed to create an efficient and conservative "Stock Valuation Bot"
which uses the financial data in the form of .txt (typically copy pasted from yahoo finance) to 
derive a fair value of the stock. 

In this example Apple(AAPL) stock is valuated

# Base.py
Base.py is the base class which reads the financial statements as .txt files and formats the data to create a data 
frame which can be used for further analysis

# BalancesheetAnalysis.py
This Subclass helps to analyse the Balance sheet which is now available as a dataframe from Base class method 'listformatter'

# logfile.log
Log file 
