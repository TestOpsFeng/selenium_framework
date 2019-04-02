import unittest
from drivers import driver
from page.baidu_page import BaiduPage
from page.register_page import RegesterPage
from time import sleep
from utils.allow_flash import allow_flash
from utils.yaml_utils import get

class BaseSetup(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = driver.init()
        cls.baidu_page = BaiduPage(cls.driver)
        cls.register_page = RegesterPage(cls.driver)


    def setUp(self):
        pass

    def teardown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        sleep(5)
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()