from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import xmlrunner

class TestScrabble(unittest.TestCase):

    def test_case(self):
        try:
            driver.get("https://pl.wikipedia.org/wiki/Wikipedia:Strona_g%C5%82%C3%B3wna")
            self.assertTrue(True)
        except:
            self.assertFalse(False)

        
if __name__ == '__main__':
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)
    unittest.main()
        
