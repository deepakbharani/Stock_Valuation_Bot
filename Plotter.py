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
            fig,axs = plt.subplots(len(args))
            fig.suptitle("Solvency Ratios")
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
            #plt.show()

        elif classname is "ProfitabilityRatio":

            # Extract args
            self.roa = args[0]
            self.roe = args[1]

            # Plot the results
            fig,axs = plt.subplots(len(args))
            fig.suptitle("Profitability Ratio")
            axs[0].plot(self.xaxis, self.roa, label="Return on Assets", color='blue', marker='o')
            axs[0].grid(True)
            axs[0].set_title("Return on Assets")
            axs[0].set_xlabel("Year")
            axs[0].set_ylabel("Return on Assets")
            axs[0].legend()
            axs[1].plot(self.xaxis, self.roe, label="Return on Equity", color='purple', marker='o')
            axs[1].grid(True)
            axs[1].set_title("Return on Equity")
            axs[1].set_xlabel("Year")
            axs[1].set_ylabel("Return on Equity")
            axs[1].legend()
            plt.show()



        #
        # plt.plot(xaxis,array,label = labeltext, color = '#444444',marker = 'o')
        # plt.title(title)
        # plt.xlabel(xlabel)
        # plt.ylabel(ylabel)
        # plt.grid(True)
        # plt.legend()
        # plt.show()

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

