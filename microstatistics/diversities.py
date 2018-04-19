from scipy.misc import comb
import math
from math import log
import numpy as np
def simpson(pI):
    """Calculate the Simpson diversity index for a given column. Required
     arguments: pI - the proportion of samples containing species I. Returns
     a float with values between 0 and 1"""
    l = list(pI) # a list which contains the data from each column/sample;
    N = np.sum(l) # the N for a column/sample - the total number of individuals
    sim1 = 0 # a running sum for easier result processing

    for x in l:
        sim1 += x * (x - 1)
    sim2 = 1 - (sim1 / (N * (N-1)))

    return sim2

H_list, lnE_list, lnS_list, lnN_list = [],[],[],[] # SHEBI lists

def SHEBI(pI):
    """Calculate the SHE values for the SHE index and append them to their
	respective lists as lnE_list etc"""
    l = list(pI)
    N = np.sum(l)
    S = len(pI)
    lnN_list.append(math.log(N))

    HList = list()
    for x in range(len(pI)):
        p = (l[x]/np.sum(pI)) * math.log((l[x]/np.sum(pI)))
        HList.append(p)
    H = -1 * np.sum(HList)
    H_list.append(H)

    lnS = math.log(S)
    lnE = H - lnS 

    lnS_list.append(lnS)
    lnE_list.append(lnE)

def shannon(pI):
    """Calculate the Shannon-Wiener / Shannon-Weaver / Shannon entropy for a
    given sample. Required arguments: pI - the proportion of samples containing
    species I. Returns a float with a maximum value of log(S) where S is the
    species richness"""
    l = list(pI)
    N = np.sum(l)

    H = 0
    for x in range(len(pI)):
        H += -1 * ((l[x] / np.sum(pI)) * math.log(( l[x] / np.sum(pI))))

    return H

def proportion(pI, row):
    """Calculate the percentage of a given species within a sample; does not
    suffer by the off by one error, so use accordingly. Requires a  COMPLETE
    list of values - with zeroes in place in order to function properly.  """

    l = list(pI) # a list which contains the data from each column/sample;
    N = np.sum(l) # the N for a column/sample - the total number of individuals
    specie = int(l[row])

    prop =  specie * 100  / N

    return prop

def hurlbert_diversity(pI, n=100):
    """Calculate diversity according to Houlbert. Requires a list of values and
    a correction size n (default 100). Reduces a sample to size n and calculates
     the expected species richness for the respective n"""
    l = list(pI)
    N = np.sum(l)
    S = len(pI)
    hurlbert = 0

    for i in range(S):
        hurlbert += 1 - (comb(N - pI[i], n) / comb(N, n))

    return hurlbert

def fisher(pI):
    """Calculates the Fisher alpha diversity index, which asnp.sumes a logarithmic
    abundance model. Required arguments: pI - the proportion of samples
    containing species I. Returns a float with values between 0 and 20."""
    l = list(pI)
    N = np.sum(l)
    s = len(pI)
    a = 20

    if (N > s):
        while abs(a * log(1 + N / a) - s) > 0.01:
            a = a - (a * log(1 + N / a) - s) / (log(1 + N / a) - N / (a + N))
            if a <= 0:
                a = 1
        return a
    else:
        return 999

def equitability(pI, N=0):
    """Calculates (Pielou's) Equitability. Returns a float with a maximum value
    between 0 and 1. Required arguments: pI - the proportion of samples
    containing species I."""
    l = list(pI)
    N = np.sum(l)
    S = len(pI)

    H = 0
    for x in range(len(pI)):
        H += -1 * ((l[x] / np.sum(pI)) * math.log(( l[x] / np.sum(pI))))

    J = 0
    J = ( H / (math.log(S)))

    return J

def bfoi_index(pI, oxic_row):
    """Calculate the bfoi. Does NOT suffer from the off by one error - use
    accordingly. Requires a list of values from a column, as well as the number
    of the oxic row. """

    l = list(pI) # a list which contains the data from each column/sample;

    oxic = l[oxic_row - 1]  # oxic_row - 1 is used to correct the off by one error
    disoxic = l[oxic_row] # assigns the value of oxic_row in order to correct the off by one error
    suboxic = l[oxic_row+1] # assigns a value to suboxic in relation to the position of oxic_row in the list
    if oxic == 0:
        bfoi = 50 * ( suboxic / (disoxic + suboxic) -1) # formula to use when oxic species are equal to 0
    else:
        bfoi = 100 * oxic / (oxic + disoxic) # formula when oxic species are not equal to 0
    return bfoi
