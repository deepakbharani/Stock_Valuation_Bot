"""
Author : Bharani Deepak
Info   : This Subclass performs Discounted Cashflow Valuation analysis
"""

from ProfitabilityRatio import *
import yfinance as yf
import numpy as np

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('logfile.log')
file_handler.setLevel(logging.ERROR)
logger.addHandler(file_handler)

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
        self.beta = self.tic.info.get('beta')
        self.sharesoutstanding = self.tic.info.get('sharesOutstanding')
        self.cagr_tot_rev_gr = self.cagr_tot_revenue_gr()

        # Current Market price
        self.cmp = self.get_current_price()

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

        self.waac = self.wacc()

        self.today_value = self.terminal_value()

        # Calculate intrinsic Value of the Stock
        logger.info("Calculating intrinsic value")
        self.intrinsic_value = self.today_value / self.sharesoutstanding
        logger.info("Intrinsic Value is : %f", self.intrinsic_value)

        # Calculate Margin of Safety
        self.margin_of_safety = ((self.intrinsic_value - self.cmp)/self.cmp)*100
        logger.info("Margin of Safety is : %f", self.margin_of_safety)


    def get_current_price(self):
        self.stock_data = self.tic.history(period='1d')
        return self.stock_data['Close'][0]

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

    def terminal_value(self):

        logger.info("Calculating Terminal Value")
        self.terminal_value = self.free_cashflow[-1] * (1 + self.perpetual_growth / 100) / (
                    (self.wacc / 100) - (self.perpetual_growth / 100))
        self.present_terminal_value = self.terminal_value / self.discount_factor[-1]
        self.today_value = (sum(self.present_value)+self.present_terminal_value)*0.0001

        return self.today_value

    # Calculate CAGR of the growth rate of total_revenue
    def cagr_tot_revenue_gr(self):
        self.G_tot_revenue = np.array(Base.percentage_growth(self.tot_revenue))
        return self.G_tot_revenue.mean()

    def wacc(self):
        logger.info("Calculating Weighted average cost of capital")
        self.total_equity = self.shareholder_equity + self.long_term_debt
        self.weighted_equity_capital = np.divide(self.shareholder_equity,self.total_equity)
        self.weight_debt_capital = np.divide(self.long_term_debt,self.total_equity)
        self.ror_equity_capital = self.risk_free_return + (self.beta*(self.expected_return-self.risk_free_return))
        self.ror_debt_capital = self.rate_of_interest_expense*(1-(self.corp_tax / 100))
        self.wacc = (self.weighted_equity_capital*self.ror_equity_capital) + (self.weight_debt_capital*self.ror_debt_capital)
        self.wacc = self.wacc.mean()

        return self.wacc

