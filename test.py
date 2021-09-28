from dataloader import DataLoader
from analysis import *
import unittest

data_root = "./Data"
data = DataLoader(data_root)
analysis = Analysis(data)


class TestAnalysis(unittest.TestCase):
    def test_loc_info(self):
        self.assertEqual(analysis.find_loc_detail("ATL"), ['Lat: 33.77942', 'Long: -84.41116', 'Owned by Carvana'])
        self.assertEqual(analysis.find_loc_detail("TOL"), ['Lat: 33.44013', 'Long: -112.26205', 'Owned by Carvana'])

    def test_capacity(self):
        self.assertEqual(analysis.find_trips_detail("ATL"),
                         {'Origin Trips': ['ATL to WIND (216 weekly capacity)'],
                           'Destination Trips': ['WIND to ATL (189 weekly capacity)']})
        self.assertEqual(analysis.find_trips_detail("TOL"),
                         {'Origin Trips': ['TOL to BM (27 weekly capacity)', 'TOL to CCL (189 weekly capacity)',
                                            'TOL to HOLXD (351 weekly capacity)', 'TOL to LAV (45 weekly capacity)',
                                            'TOL to TMPVM (180 weekly capacity)', 'TOL to TUC (27 weekly capacity)'],
                           'Destination Trips': ['CCL to TOL (189 weekly capacity)',
                                                 'HOLXD to TOL (351 weekly capacity)',
                                                 'LAV to TOL (45 weekly capacity)',
                                                 'TMPVM to TOL (108 weekly capacity)',
                                                 'TUC to TOL (27 weekly capacity)']}
                         )


