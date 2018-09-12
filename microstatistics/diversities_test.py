import unittest
import numpy.testing as nptest
import pandas as pd
from diversities import *

lst = [[5,10,15],[20,25,30],[35,40,45]]
df = pd.DataFrame(lst)

class TestDiversities(unittest.TestCase):
    def test_dfProportion(self):
    # Test whether proportions are calculated properly on a dataframe
        nptest.assert_array_almost_equal(
            dfProportion(df),
            np.array([
                [0.08333333, 0.13333333, 0.16666667],
                [0.33333333, 0.33333333, 0.33333333],
                [0.58333333, 0.53333333, 0.5       ]
            ]),
        )
    
    def test_dfShannon(self):
        # Test the return values with the Shannon diversity index
        nptest.assert_array_almost_equal(
            dfShannon(df),
            [0.887694275799104, 0.9701157839869381, 1.0114042647073518]
        )

    def test_dfSimpson(self):
        # Test the return values with the Simpson diversity index
        nptest.assert_almost_equal(
            dfSimpson(df),
            [0.5416666666666666, 0.5866666666666667, 0.6111111111111112]
        )
    
    # # def test_dfFisher(self):
    # #     # Test the return values with the Fisher alpha diversity index
    # #     nptest.assert_array_almost_equal()

    def test_dfHurlbert(self):
        # Test the return values with the Hurlbert diversity index using a 
        # correction size of 20
        nptest.assert_almost_equal(
            dfHurlbert(df, 20),
            [2.879486193763983, 2.9646565395761715, 2.984163372119101]
        )

    def test_dfEquitability(self):
        # Test the return values with the actual equitability 
        nptest.assert_almost_equal(
            dfEquitability(df),
            [0.8080141510844469, 0.8830374409547586, 0.920619835714305]
        )
    
    def test_dfBFOI(self):
        # Test the return values with the BFOI values
        nptest.assert_almost_equal(
            dfBFOI(df),
            [20.0, 28.571428571428573, 33.333333333333336]
        )