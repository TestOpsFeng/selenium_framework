from drivers import chrome_driver
from drivers import edge_driver
from drivers import firefox_driver
from utils import yaml_utils
from utils.logger import logger
def init(name=yaml_utils.get("constant.yaml","driver")):
    logger.info("Current driver is: %s",name)
    if "chrome" == name:
        return chrome_driver.init()
    if "firefox" == name:
        return firefox_driver.init()
    if "edge" == name:
        return edge_driver.init()
