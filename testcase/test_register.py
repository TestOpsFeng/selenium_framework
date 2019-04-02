import allure
import barnum
from  testcase.base_setup import BaseSetup
from utils import yaml_utils
import os
from utils.allow_flash import allow_flash

url_regerister = yaml_utils.get("constant.yaml", "url_regerister")
autoitExe_file = os.path.split(os.path.realpath(__file__))[0] + "/../autoit/upload_img.exe"

class Testregister(BaseSetup):

    @allure.testcase("Test PhpWind Register")
    def test_register(self):
        allow_flash(self.driver, yaml_utils.get("constant.yaml", "host"))
        username = barnum.create_name(False).lower()
        email = barnum.create_email()
        self.register_page.get(url_regerister)
        self.register_page.read_law()
        self.register_page.input_info(username,"123456",email)
        self.register_page.submit()
        self.register_page.upload_icon(autoitExe_file)
        self.register_page.skip()
        self.register_page.skip()
        self.register_page.skip()
        self.register_page.toProfile()
        result = self.register_page.get_name()
        self.assertEqual(result,username)



