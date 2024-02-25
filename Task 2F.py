import numpy as np
import matplotlib.dates as mdates
import matplotlib.pyplot as plt

def polyfit(dates, levels, p):
    # Convert dates to float using date2num
    x = mdates.date2num(dates)

    # Find coefficients of best-fit polynomial of degree p
    poly_coeff = np.polyfit(x, levels, p)

    # Convert coefficients into a polynomial that can be evaluated
    poly = np.poly1d(poly_coeff)

    # Determine the shift of the date (time) axis
    d0 = dates[0]

    return poly, d0

