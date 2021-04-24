"""
Author : Bharani Deepak
Info   : This Script initiates the stock valuation
"""
if __name__ == "__main__":

    import time
    print(f"Program Started at {time.perf_counter()} ")

    from Valuation import *
    from Result import *
    from fpdf import FPDF

    # Creating object for class DCF
    obj = Result()

    print(f"Program Ended at {time.perf_counter()} ")