from selenium.webdriver.common.by import By
from page.base_page import BasePage

class BaiduPage(BasePage):
    input_search = (By.XPATH,'//*[@id="kw"]')
    btn_search = (By.XPATH,'//*[@id="su2"]')


    def search(self):
        self.send_keys(self.input_search,"nihao")
        self.click(self.btn_search)