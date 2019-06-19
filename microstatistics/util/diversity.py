import numpy as np
import math
from scipy.special import comb


def df_proportion(frame):
    """Calculates the proportion for each cell in a column. Requires a dataframe object as input. Returns a dataframe
    containing the results. """
    holder = frame.copy()
    for i in range(len(holder.T)):
        holder[i] = holder[i].apply(lambda x: x if x == 0 else x / holder[i].sum())
    return holder


def df_shannon(frame):
    """Calculates the Shannon-Wiener entropy for each column in a dataframe. Requires a	dataframe object as input.
    Returns a list containing the results. """
    results = []
    holder = df_proportion(frame)
    for i in range(len(holder.T)):
        holder[i] = holder[i].apply(lambda x: x if x == 0 else -1 * (x * math.log(x)))
    for i in range(len(holder.T)):
        results.append(holder[i].sum())
    return results


def df_simpson(frame):
    """Calculates the Simpson diversity index for each column in a dataframe. Requires a dataframe object as input.
    Returns a list containing the results. """
    results = []
    holder = df_proportion(frame)
    for i in range(len(holder.T)):
        holder[i] = holder[i].apply(lambda x: x if x == 0 else x * x)
    for i in range(len(holder.T)):
        results.append(1 - holder[i].sum())
    return results


def df_fisher(frame):
    """Calculates the Fisher alpha diversity assuming a logarithmic abundance model for each column in a dataframe.
    Requires a dataframe object as input. Returns a list containing the results. """
    results = []
    holder = frame.copy()
    holder = holder.replace(0, np.nan)
    for i in range(len(holder.T)):
        summed = holder[i].sum()
        length = holder[i].count()
        fisher = 20
        while abs(fisher * math.log(1 + summed / fisher) - length) > 0.01:
            fisher = fisher - (fisher * math.log(1 + summed / fisher) - length) / (
                    math.log(1 + summed / fisher) - summed / (fisher + summed))
        if fisher <= 0:
            fisher = 1
        results.append(fisher)
    return results


def df_hurlbert(frame, correction=100):
    """Calculates the Hurlbert diversity by reducing the columns of a dataframe to a chosen	size. Requires a dataframe
    object and a correction size as input. Returns a list containing the results. """
    results = []
    holder = frame.copy()
    for i in range(len(holder.T)):
        summed = holder[i].sum()
        holder[i] = holder[i].apply(
            lambda x: x if x == 0 else 1 - (comb(summed - x, correction) / comb(summed, correction)))
    for i in range(len(holder.T)):
        results.append(holder[i].sum())
    return results


def df_equitability(frame):
    """Calculates Pielou's equitability for each column in a chosen dataframe. Requires a dataframe object as input.
    Returns a list containing the results. """
    results = []
    holder = frame.copy()
    holder = holder.replace(0, np.nan)
    shannon = df_shannon(frame)
    for i in range(len(holder.T)):
        length = holder[i].count()
        equitability = shannon[i] / math.log(length)
        results.append(equitability)
    return results


def df_bfoi(frame):
    """Calculates the Benthic Foraminifera Oxygenation Index according to Kaiho. Requires a dataframe object as
    input. Returns a list containing the results. """
    results = []
    holder = frame.copy()
    for i in range(len(holder.T)):
        oxic = holder[i][0]
        disoxic = holder[i][1]
        suboxic = holder[i][2]
        if oxic == 0:
            bfoi = 50 * (suboxic / (disoxic + suboxic) - 1)
        else:
            bfoi = 100 * oxic / (oxic + disoxic)
        results.append(bfoi)
    return results
