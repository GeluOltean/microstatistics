from unittest import TestCase
from pandas import DataFrame
from numpy import testing


class TestDiversityService(TestCase):
    TESTDATAFRAME = DataFrame([
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [1, 11, 12, 13, 14, 15, 16, 17, 18, 19],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ])

    def test_compute_index(self):
        self.fail()

    def test_compute_bfoi(self):
        self.fail()

    def test_compute_percentages(self):
        self.fail()

    def test_compute_morphogroups(self):
        self.fail()

    def test_compute_linkage(self):
        self.fail()

    def test_compute_nmds(self):
        self.fail()
