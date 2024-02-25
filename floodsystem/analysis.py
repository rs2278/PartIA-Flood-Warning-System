from matplotlib import dates
import numpy as np

def polyfit(dates1, levels, p):
    x = dates.date2num(dates1)
    y = levels
    p_coeff = np.polyfit(x - x[0], y, p)

    poly = np.poly1d(p_coeff)

    return poly, x[0]