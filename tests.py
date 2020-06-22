from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import xmlrunner

class Test(unittest.TestCase):

    def test_case(self):
        try:
            driver.get("https://www.iban.com/exchange-rates")
            self.assertTrue(True)
        except:
            self.assertFalse(False)

    def test_case2(self):
        try:
            driver.get("https://pl.wikipedia.org/wiki/Wikipedia:Strona_g%C5%82%C3%B3wna")
            trs = driver.find_elements_by_xpath("//tr")
            counter = 0
            for tr in trs[1:]:
                try:
                    exists = (self.decode(tr.get_attribute('innerHTML')))
                    if(exists): counter += 1
                except TypeError:
                    continue 
            self.assertTrue(counter)
        except:
            self.assertFalse(0)

        
if __name__ == '__main__':
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)
    unittest.main()
