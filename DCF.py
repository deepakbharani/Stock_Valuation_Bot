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
        self.G_cagr_tot_rev_gr = self.cagr_tot_revenue_gr()

    # Calculate CAGR of the growth rate of total_revenue
    def cagr_tot_revenue_gr(self):
        self.G_tot_revenue = np.array(Base.percentage_growth(self.tot_revenue))
        return self.G_tot_revenue.mean()

