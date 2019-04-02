from selenium.webdriver.common.by import By
from page.base_page import BasePage,Locator


class BaiduPage(BasePage):
    input_search = Locator(By.XPATH,'//*[@id="kw"]')
    btn_search = Locator(By.XPATH,'//*[@id="su"]')


    def search(self):
        self.send_keys(self.input_search,"nihao")
        self.click(self.btn_search)