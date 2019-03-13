import unittest
from drivers import driver
from page.baidu_page import BaiduPage
import pytest
import allure

class BaseSetup(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = driver.init()
        cls.baidu_page = BaiduPage(cls.driver)
        cls.driver.get("https://www.baidu.com/")

    def setUp(self):
        pass

    def teardown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()