from unittest import TestCase
from pandas import Series
from numpy import testing
from numpy import float

from microstatistics.util.diversities import df_shannon, df_bfoi, df_equitability, df_fisher, df_hurlbert, df_proportion, df_simpson


class TestDiversities(TestCase):
    TESTSERIES = Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_df_shannon(self):
        testing.assert_almost_equal(
            df_shannon(TestDiversities.TESTSERIES),
            float(2.151281720651836)
        )

    def test_df_fisher(self):
        testing.assert_almost_equal(
            df_fisher(TestDiversities.TESTSERIES),
            float(3.576655453138995)
        )

    def test_df_simpson(self):
        testing.assert_almost_equal(
            df_simpson(TestDiversities.TESTSERIES),
            float(0.8727272727272728)
        )

    def test_df_proportion(self):
        correct = [float(0.018182), float(0.036364), float(0.054545), float(0.072727), float(0.090909), float(0.109091), float(0.127273), float(0.145455), float(0.163636), float(0.181818)]
        to_test = df_proportion(TestDiversities.TESTSERIES)
        for x, y in zip(to_test, correct):
            testing.assert_almost_equal(x, y, 6)

    def test_df_hurlbert(self):
        testing.assert_almost_equal(
            df_hurlbert(TestDiversities.TESTSERIES, 3),
            float(2.679245283018868)
        )

    def test_df_equitability(self):
        testing.assert_almost_equal(
            df_equitability(TestDiversities.TESTSERIES),
            float(0.9342897802984251)
        )

    def test_df_bfoi(self):
        testing.assert_almost_equal(
            df_bfoi(TestDiversities.TESTSERIES),
            float(33.333333333333336)
        )
