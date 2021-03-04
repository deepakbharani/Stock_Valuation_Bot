"""
Author : Bharani Deepak
Info   : This Subclass performs Discounted Cashflow Valuation analysis
"""

from ProfitabilityRatio import *
import yfinance as yf
import numpy as np

class DCF(ProfitabilityRatio):

    def __init__(self):

        super().__init__()

        # Valuation parameters
        self.years_to_forcast = 5
        self.num_period = 4
        self.risk_free_return = 4
        self.expected_return = 10
        self.corp_tax = 30
        self.perpetual_growth = 2.5
        self.discount_factor = []
        self.present_value = []

        # Get stock related data from yfinance module
        self.stock_ticker = 'AAPL'
        self.tic = yf.Ticker(self.stock_ticker)
        self.sharesoutstanding = self.tic.info.get('sharesOutstanding')
        self.cagr_tot_rev_gr = self.cagr_tot_revenue_gr()

        # Calculate ratio of net income to total revenue
        self.net_income_to_tot_revenue = np.divide(self.net_income,self.tot_revenue) * 100
        self.avg_net_income_to_tot_revenue = self.net_income_to_tot_revenue.mean()

        # Calculate ratio of free cash flow to net income
        self.free_cashflow_to_net_income = np.divide(self.free_cashflow,self.net_income) * 100
        self.avg_free_cashflow_to_net_income = self.free_cashflow_to_net_income.mean()

        # Calculate discount factor and the present value of projected free cashflow
        self.discount_factor, self.present_value = self.forcast()

        # Calculate rate of interest expense
        self.rate_of_interest_expense = (self.interest_expense[:-1]/self.long_term_debt) * 100

    def forcast(self):

        logger.info("Forecasting total revenue, net income and free cashflow for the next five years")

        for i in range(self.years_to_forcast):

            # forecast total revenue for next five years
            self.revenue_forcast = self.tot_revenue[-1] + ((self.tot_revenue[-1]*self.cagr_tot_rev_gr)/100)
            self.tot_revenue = np.append(self.tot_revenue,self.revenue_forcast)

            # forecast net income for the next five years
            self.net_income_forecast = self.net_income[-1] + ((self.net_income[-1] * self.avg_net_income_to_tot_revenue) / 100)
            self.net_income = np.append(self.net_income, self.net_income_forecast)

            # forecast free cash flow for next five years
            self.free_cashflow_forecast = (self.net_income[-1]*self.avg_free_cashflow_to_net_income / 100)
            self.free_cashflow = np.append(self.free_cashflow, self.free_cashflow_forecast)

            # Calculate Discount Factor
            self.discount_factor.append((1+(self.expected_return/100))**(i+1))

            # Calculate present value of future free cashflow
            self.present_value.append(self.free_cashflow[-1] / self.discount_factor[i])

        return np.array(self.discount_factor), np.array(self.present_value)


    # Calculate CAGR of the growth rate of total_revenue
    def cagr_tot_revenue_gr(self):
        self.G_tot_revenue = np.array(Base.percentage_growth(self.tot_revenue))
        return self.G_tot_revenue.mean()

