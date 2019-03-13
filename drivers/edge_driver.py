import os

from selenium import webdriver
from selenium.webdriver.edge.options import Options

def init():
    fileNamePath = os.path.split(os.path.realpath(__file__))[0]+"/driver_exec/"
    path = os.path.join(fileNamePath, 'MicrosoftWebDriver.exe')
    print("MicrosoftWebDriver",path)
    return webdriver.Edge(executable_path=path)