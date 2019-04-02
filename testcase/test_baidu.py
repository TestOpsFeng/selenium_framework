import unittest

import allure
from  testcase.base_setup import BaseSetup
from utils import yaml_utils

url = yaml_utils.get("constant.yaml","url_baidu")
class TestBaidu(BaseSetup):

    @allure.testcase("Test baidu search")
    def test_search(self):
        self.baidu_page.get(url)
        self.baidu_page.search()
        self.assertEqual("a","b")