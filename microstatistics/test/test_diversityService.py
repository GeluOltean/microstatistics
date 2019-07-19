from unittest import TestCase
from pandas import DataFrame
from numpy import testing

from microstatistics.util.diversities import SHANNON, FISHER, SIMPSON, EQUITABILITY, HURLBERT
from microstatistics.util.diversityService import DiversityService


class TestDiversityService(TestCase):
    TESTDATAFRAME = DataFrame([
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ])

    def test_compute_index(self):
        to_test_shannon = DiversityService.compute_index(TestDiversityService.TESTDATAFRAME, SHANNON)
        shannon = [float(0.566086), float(0.655976), float(0.702919), float(0.729843), float(0.746033),
                           float(0.755983), float(0.762104), float(0.765783), float(0.767858), float(0.768858)]
        for x, y in zip(to_test_shannon, shannon):
            testing.assert_almost_equal(x, y, 6)

        to_test_fisher = DiversityService.compute_index(TestDiversityService.TESTDATAFRAME, FISHER)
        fisher = [float(1.283882), float(1.171275), float(1.089987), float(1.027996), float(0.978817), float(0.938626),
                  float(0.905011), float(0.876369), float(0.851592), float(0.829887)]
        for x, y in zip(to_test_fisher, fisher):
            testing.assert_almost_equal(x, y, 6)

        to_test_simpson = DiversityService.compute_index(TestDiversityService.TESTDATAFRAME, SIMPSON)
        simpson = [float(0.291667), float(0.357143), float(0.398438), float(0.425926), float(0.445000), float(0.458678),
                   float(0.468750), float(0.476331), float(0.482143), float(0.486667)]
        for x, y in zip(to_test_simpson, simpson):
            testing.assert_almost_equal(x, y, 6)

        to_test_equitability = DiversityService.compute_index(TestDiversityService.TESTDATAFRAME, EQUITABILITY)
        equitability = [float(0.515273), float(0.597095), float(0.639824), float(0.664332), float(0.679068),
                        float(0.688125), float(0.693697), float(0.697045), float(0.698934), float(0.699844)]
        for x, y in zip(to_test_equitability, equitability):
            testing.assert_almost_equal(x, y, 6)

        to_test_hurlbert = DiversityService.compute_index(TestDiversityService.TESTDATAFRAME, HURLBERT, 5)
        hurlbert = [float(1.833333), float(1.961538), float(2.017857), float(2.044001), float(2.055921),
                    float(2.060606), float(2.061430), float(2.060140), float(2.057692), float(2.054629)]
        for x, y in zip(to_test_hurlbert, hurlbert):
            testing.assert_almost_equal(x, y, 6)

    def test_compute_bfoi(self):
        testing.assert_almost_equal(
            DiversityService.compute_bfoi(TestDiversityService.TESTDATAFRAME)[0],
            float(9.090909090909092)
        )

    def test_compute_morphogroups(self):
        to_test_morphogroups = DiversityService.compute_morphogroups(TestDiversityService.TESTDATAFRAME)[0]
        morphogroups = [float(8.333333), float(14.285714), float(18.750000), float(22.222222), float(25.000000),
                        float(27.272727), float(29.166667), float(30.769231), float(32.142857), float(33.333333)]
        for x, y in zip(to_test_morphogroups, morphogroups):
            testing.assert_almost_equal(x, y, 6)

    def test_compute_linkage(self):
        to_test_linkage = DiversityService.compute_linkage(data=TestDiversityService.TESTDATAFRAME)[0]
        linkage = [float(0), float(1), float(0.45), float(2)]
        for x, y in zip(to_test_linkage, linkage):
            testing.assert_almost_equal(x, y)
