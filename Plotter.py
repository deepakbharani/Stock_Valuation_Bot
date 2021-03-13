"""
Author : Bharani Deepak
Info   : This Subclass contains Methods and Attributes for plotting the results
Purpose: plot
"""

import numpy as np
from matplotlib import pyplot as plt

plt.xkcd()

class Plotter():

    def __init__(self):
        self.xaxis = ["2017","2018","2019","2020"]

    def twoDplot(self,classname,*args):

        if classname is "SolvencyRatio":

            # Extract args
            self.debt2equity = args[0]
            self.int_cov_ratio = args[1]

            # Plot the results
            figs,axs = plt.subplots(len(args))
            figs.suptitle("Solvency Ratios")
            axs[0].plot(self.xaxis, self.debt2equity, label="Debt to Equity", color='blue', marker='o')
            axs[0].grid(True)
            axs[0].set_title("Debt to Equity")
            axs[0].set_xlabel("Year")
            axs[0].set_ylabel("Debt to Equity")
            axs[0].legend()
            axs[1].plot(self.xaxis, self.int_cov_ratio[:-1], label="Interest coverage ratio", color='purple', marker='o')
            axs[1].grid(True)
            axs[1].set_title("Interest coverage ratio")
            axs[1].set_xlabel("Year")
            axs[1].set_ylabel("Interest coverage ratio")
            axs[1].legend()
            plt.show()

        elif classname is "ProfitabilityRatio":

            # Extract args
            self.roa = args[0]
            self.roe = args[1]
            self.net_prft_margin = args[2]
            self.opr_income_margin = args[3]

            # Plot the results
            figp,axs = plt.subplots(int(len(args)/2),int(len(args)/2))
            figp.suptitle("Profitability Ratio")
            # Plot Return on Assets
            axs[0,0].plot(self.xaxis, self.roa, label="Return on Assets", color='blue', marker='o')
            axs[0,0].grid(True)
            axs[0,0].set_title("Return on Assets")
            axs[0,0].set_xlabel("Year")
            axs[0,0].set_ylabel("Return on Assets")
            axs[0,0].legend()
            # Plot Return on Equity
            axs[0,1].plot(self.xaxis, self.roe, label="Return on Equity", color='red', marker='o')
            axs[0,1].grid(True)
            axs[0,1].set_title("Return on Equity")
            axs[0,1].set_xlabel("Year")
            axs[0,1].set_ylabel("Return on Equity")
            axs[0,1].legend()
            # Plot Net Profit Margin
            axs[1,0].plot(self.xaxis, self.net_prft_margin[:-1], label="Net Profit Margin", color='green', marker='o')
            axs[1,0].grid(True)
            axs[1,0].set_title("Net Profit Margin")
            axs[1,0].set_xlabel("Year")
            axs[1,0].set_ylabel("Net Profit Margin")
            axs[1,0].legend()
            # Plot Operating Income Margin
            axs[1,1].plot(self.xaxis, self.opr_income_margin[:-1], label="Operating Income Margin", color='purple', marker='o')
            axs[1,1].grid(True)
            axs[1,1].set_title("Operating Income Margin")
            axs[1,1].set_xlabel("Year")
            axs[1,1].set_ylabel("Operating Income Margin")
            axs[1,1].legend()
            plt.show()

        else:

            # Extract args
            self.cur_ratio = args[0]
            self.cshratio = args[1]
            self.op_cashflow_ratio= args[2]
            self.inv_turnover_ratio = args[3]

            # Plot the results
            figl,axs = plt.subplots(int(len(args)/2),int(len(args)/2))
            figl.suptitle("Liquidity Ratio")
            # Plot Return on Assets
            axs[0,0].plot(self.xaxis, self.cur_ratio, label="Current Ratio", color='blue', marker='o')
            axs[0,0].grid(True)
            axs[0,0].set_title("Current Ratio")
            axs[0,0].set_xlabel("Year")
            axs[0,0].set_ylabel("Current Ratio")
            axs[0,0].legend()
            # Plot Return on Equity
            axs[0,1].plot(self.xaxis, self.cshratio, label="Cash Ratio", color='red', marker='o')
            axs[0,1].grid(True)
            axs[0,1].set_title("Cash Ratio")
            axs[0,1].set_xlabel("Year")
            axs[0,1].set_ylabel("Cash Ratio")
            axs[0,1].legend()
            # Plot Net Profit Margin
            axs[1,0].plot(self.xaxis, self.op_cashflow_ratio, label="Operating Cashflow Ratio", color='green', marker='o')
            axs[1,0].grid(True)
            axs[1,0].set_title("Operating Cashflow Ratio")
            axs[1,0].set_xlabel("Year")
            axs[1,0].set_ylabel("Operating Cashflow Ratio")
            axs[1,0].legend()
            # Plot Operating Income Margin
            axs[1,1].plot(self.xaxis, self.inv_turnover_ratio, label="Inventor Turnover Ratio", color='purple', marker='o')
            axs[1,1].grid(True)
            axs[1,1].set_title("Inventor Turnover Ratio")
            axs[1,1].set_xlabel("Year")
            axs[1,1].set_ylabel("Inventor Turnover Ratio")
            axs[1,1].legend()
            plt.show()


    def scatter_plot(self,labeltext,xlabel,ylabel,title,x,xaxis = None):

        if xaxis is None:
            xaxis = np.arange(1,len(x)+1)
        else:
            xaxis = xaxis

        plt.scatter(xaxis,x,label = labeltext, color = '#444444',marker = 'o')
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(True)
        plt.legend()
        plt.show()

