import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def init():
    fileNamePath = os.path.split(os.path.realpath(__file__))[0] + "/driver_exec/"
    path = os.path.join(fileNamePath, 'chromedriver.exe')
    chrome_options = Options()
    # chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
    # chrome_options.add_argument('--start-maximized')  # 指定浏览器分辨率
    # chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
    # chrome_options.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
    # # chrome_options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
    # chrome_options.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
    # chrome_options.add_argument('--disable-extensions')
    # chrome_options.add_argument('lang=zh_CN.UTF-8')
    return webdriver.Chrome(executable_path="/usr/bin/chromedriver", chrome_options=chrome_options)
