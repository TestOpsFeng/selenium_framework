import os

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def init():
    fileNamePath = os.path.split(os.path.realpath(__file__))[0]+"/driver_exec/"
    path = os.path.join(fileNamePath, 'geckodriver.exe')
    firefox_option = Options()
    return webdriver.Firefox(executable_path=path,firefox_options=firefox_option)