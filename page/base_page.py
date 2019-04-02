from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver.remote.webelement import WebElement
from utils import yaml_utils
from utils.logger import logger
from collections import namedtuple
from selenium.webdriver.support.select import Select

Locator = namedtuple('Locator','by loc')
class BasePage(object):
    wait_time = yaml_utils.get("constant.yaml", "wait_elements_time")

    def __init__(self, driver: RemoteWebDriver):
        self.driver = driver

    def get(self,url):
        self.driver.get(url)

    def find_element(self, locator, time=wait_time) -> WebElement:
        '''等待并查找元素，等待时间在constant.yaml中设置'''
        try:
            logger.info("Find element by: %s", locator)
            element = WebDriverWait(self.driver, time).until(
                EC.element_to_be_clickable(locator))
            return element
        except TimeoutException:
            logger.error('Could not find Element by: %s',locator)
            raise TimeoutException('Could not find Element by: %s'%   str(locator))
        except NoSuchElementException:
            logger.error('Could not find Element by: %s' % locator)
            raise NoSuchElementException('Could not find Element by：%s'%   str(locator))

    def find_elements(self, locator, time=wait_time) -> list:
        '''等待并查找元素集合，等待时间在constant.yaml中设置'''
        try:
            logger.info("Find element by: %s", locator)
            WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))
            element = self.driver.find_elements(*locator)
            return element
        except TimeoutException:
            logger.error('Could not find Element by: %s' , locator)
            raise TimeoutException('Could not find Element by：%s' %   str(locator))
        except NoSuchElementException:
            logger.error('Could not find Element by: %s' , locator)
            raise NoSuchElementException('Could not find Element by：%s' % str(locator))

    def click(self, locator):
        '''点击元素'''
        element = self.find_element(locator)
        logger.info("Click %s,By: %s", self.get_text(element), locator)
        element.click()

    def send_keys(self, locator, text):
        '''发送文本'''
        element = self.find_element(locator)
        logger.info("Input Text: \"%s\" ,To: %s", text, locator)
        element.send_keys(text)

    def get_text(self, element):
        '''获取文本'''
        if isinstance(element, WebElement):
            return element.text
        else:
            return self.find_element(element).text

    def select_by_index(self,locator,num):
        '''通过index选择'''
        element = self.find_element(locator)
        logger.info("Select by index: \"%s\" ,To: %s", str(num), locator)
        Select(element).select_by_index(num)

    def select_by_visible_text(self,locator,text):
        '''通过text选择'''
        element = self.find_element(locator)
        logger.info("Select by text: \"%s\" ,To: %s", text, locator)
        Select(element).select_by_visible_text(text)

    def select_by_value(self, locator, value):
        '''通过value选择'''
        element = self.find_element(locator)
        logger.info("Select by value: \"%s\" ,To: %s", value, locator)
        Select(element).select_by_value(value)
