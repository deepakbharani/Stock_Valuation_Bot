"""
Author : Bharani Deepak
Info   : This Subclass performs Discounted Cashflow Valuation analysis
"""

from ProfitabilityRatio import *
import yfinance as yf

class DCF(ProfitabilityRatio):

    def __init__(self):

        super().__init__()
        # Get stock related data from yfinance module
        self.stock_ticker = 'AAPL'
        self.tic = yf.Ticker(self.stock_ticker)
        self.sharesoutstanding = self.tic.info.get('sharesOutstanding')
