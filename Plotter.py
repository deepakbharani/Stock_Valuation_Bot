"""
Author : Bharani Deepak
Info   : This Subclass contains Methods and Attributes for plotting the results
Purpose: plot
"""

# from LiquidityRatio import *
# from Log import *
from matplotlib import pyplot as plt

#plt.xkcd()

class Plotter():

    def __init__(self):
        pass

    def twoDplot(self,labeltext,xlabel,ylabel,title,array,xaxis = None):

        if xaxis is None:
            xaxis = np.arange(1,len(array)+1)
        else:
            xaxis = xaxis

        plt.plot(xaxis,array,label = labeltext, color = '#444444',marker = 'o')
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(True)
        plt.legend()
        plt.show()
