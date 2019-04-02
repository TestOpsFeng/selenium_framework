import os
from time import sleep

from selenium.webdriver.common.by import By
from page.base_page import BasePage, Locator
import barnum

btn_read_law = Locator(By.ID, 'regbutton')
input_user = Locator(By.ID, 'regname')
input_pwd = Locator(By.ID, 'regpwd')
input_pwd_repeat = Locator(By.ID, 'regpwdrepeat')
input_mail = Locator(By.ID, 'regemail')
select_province_address = Locator(By.ID, 'province_apartment')
select_city_address = Locator(By.ID, 'city_apartment')
select_area_address = Locator(By.ID, 'area_apartment')
btn_submit = Locator(By.XPATH, '//button[@onclick="checkAll();"]')
btn_icon_type1 = Locator(By.XPATH,'//label[@for="facetype1"]')
btn_icon_type2 = Locator(By.XPATH,'//label[@for="facetype2"]')
btn_icon_type3 = Locator(By.XPATH,'//label[@for="facetype3"]')
btn_skip =Locator(By.XPATH,'//*[text()="跳过"]')
btn_to_profile =Locator(By.XPATH,'//*[text()="前往个人中心"]')
label_name =Locator(By.XPATH,'//p[@class="mb10"]')
class RegesterPage(BasePage):

    def read_law(self):
        self.click(btn_read_law)

    def input_info(self,username,pwd,email):
        self.send_keys(input_user, username)
        self.send_keys(input_pwd, pwd)
        self.send_keys(input_pwd_repeat, pwd)
        self.send_keys(input_mail, email)
        self.select_by_index(select_province_address, 2)
        self.select_by_index(select_province_address, 1)
        self.select_by_index(select_province_address, 2)

    def submit(self):
        self.click(btn_submit)

    def upload_icon(self, autoitExe_file):
        sleep(3)
        os.system(autoitExe_file)

    def skip(self):
        self.click(btn_skip)

    def toProfile(self):
        self.click(btn_to_profile)

    def get_name(self):
        return self.get_text(label_name)

