import unittest
# import main
import data

class dataTest(unittest.TestCase):
    # def test_import(self): #1.1
    #     self.assertTrue(data.stats.all) # Test file name/path is correct

    def test_import(self): #1.2
        self.assertTrue(data.stats.all) # Test a file has been imported correctly/Test empty or invalid file


    def test_startDate(self): #2.1
        self.assertGreater(data.accidentByHour(), "1/07/2019") #Check Valid Date

    # def test_infoByTime(self): #2.2
    #     self.assertIn("3", data.infoByTime()) # Test infoByTime loads data

    # def test_accidentByHour(self): #2.3
    #     self.assertIn("3", data.accidentByHour()) # Test accidentByHour loads data

    # def test_keywordByTime(self): #2.4
    #     self.assertIn("3", data. keywordByTime()) # Test keywordByTime loads data

    # def test_weekdayAnalysis(self): #2.5
    #     self.assertIn("3", data.weekdayAnalysis()) # Test weekdayAnalysis loads data

    # def test_alcoholType(self): #2.6
    #     self.assertIn("3", data.alcoholType()) # Test alcoholType loads data

    # def test_validKeyword(self): #2.7
    #     self.assertIn(self, data.keywordByTime()) # Test keyword is valid



    # def test_infoByTimeDisply(self): #3.1
    #     self.assertIn("3", data.infoByTime()) # Test infoByTime displays info

    # def test_accidentByHourDisplay(self): #3.2
    #     self.assertIn("3", data.accidentByHour()) # Test accidentByHour displays info

    # def test_keywordByTimeDisplay(self): #3.3
    #     self.assertIn("3", data.keywordByTime()) # Test keywordByTime displays info

    # def test_weekdayAnalysisDisplay(self): #3.4
    #     self.assertIn("3", data.weekdayAnalysis()) # Test weekdayAnalysis displays info

    # def test_alcoholTypeDisplay(self): #3.5
    #     self.assertIn("3", data.alcoholType()) # Test alcoholType displays info

if __name__ == '__main__':
    unittest.main
