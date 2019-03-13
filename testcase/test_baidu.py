import unittest

import allure
from  testcase.base_setup import BaseSetup

class TestBaidu(BaseSetup):

    @allure.testcase("Test baidu search")
    def test_search(self):
        self.baidu_page.search()
        self.assertEqual("a","b")