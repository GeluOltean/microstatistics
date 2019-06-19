import numpy as np
import math
from scipy.special import comb
from scipy import optimize
from pandas import Series


def df_proportion(series: Series) -> Series:
    summed = series.sum()
    return series.apply(lambda x: x if x == 0 else x / summed)


def df_shannon(series: Series) -> float:
    """Applies the formula for Shannon's entropy to a pandas Series."""
    proportions = df_proportion(series)
    return proportions.apply(lambda x: x if x == 0 else -1 * (x * math.log(x))).sum()


def df_simpson(series: Series) -> float:
    """Applies the formula for Simpson's diversity to a pandas Series."""
    proportions = df_proportion(series)
    return 1 - proportions.apply(lambda x: x if x == 0 else x * x).sum()


def df_fisher(series: Series) -> float:
    """Applies the formula for Fisher's alpha diversity to a pandas Series."""
    d = 1
    summed = series.sum()
    length = series.count()

    def fisher_func_prime(a):
        return 1 / (summed + a) + length / (a ** 2) - 1 / a

    def fisher_func(a):
        return np.log(summed + a) - np.log(a) - length / a

    return optimize.newton(fisher_func, d, fisher_func_prime, maxiter=1000)


def df_hurlbert(series: Series, correction: int = 100) -> float:
    """Applies the formula for Hurlbert's Index to a pandas Series. Requires currying when using dataframe.apply() in
    order to work appropriately, as it requires a second parameter describing the size to correct down to. """
    summed = series.sum()
    return series.apply(lambda x: x if x == 0 else 1 - (comb(summed - x, correction) / comb(summed, correction))).sum()


def df_equitability(series: Series) -> float:
    """Applies the formula for Pielou's Equitability to a pandas Series."""
    length = (series.replace(0, np.nan)).count()
    return df_shannon(series) / math.log(length)


def df_bfoi(series: Series) -> float:
    """Applies the formula for the Benthic Foraminifera Oxygenation Index (Kaiho) to a pandas Series."""
    oxic = series[0]
    disoxic = series[1]
    suboxic = series[2]
    if oxic == 0:
        return 50 * (suboxic / (disoxic + suboxic) - 1)
    else:
        return 100 * oxic / (oxic + disoxic)
