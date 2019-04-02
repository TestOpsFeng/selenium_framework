from urllib.parse import quote_plus as url_quoteplus
from urllib.parse import urlsplit
from selenium.webdriver.common.by import By as WebBy
from selenium.webdriver.support.ui import Select as WebSelect


def allow_flash(driver, url):
    def _base_url(url):
        if url.find("://") == -1:
            url = "http://{}".format(url)
        urls = urlsplit(url)
        return "{}://{}".format(urls.scheme, urls.netloc)

    def _shadow_root(driver, element):
        return driver.execute_script("return arguments[0].shadowRoot", element)

    base_url = _base_url(url)
    driver.get("chrome://settings/content/siteDetails?site={}".format(url_quoteplus(base_url)))

    root1 = driver.find_element(WebBy.TAG_NAME, "settings-ui")
    shadow_root1 = _shadow_root(driver, root1)
    root2 = shadow_root1.find_element(WebBy.ID, "container")
    root3 = root2.find_element(WebBy.ID, "main")
    shadow_root3 = _shadow_root(driver, root3)
    root4 = shadow_root3.find_element(WebBy.CLASS_NAME, "showing-subpage")
    shadow_root4 = _shadow_root(driver, root4)
    root5 = shadow_root4.find_element(WebBy.ID, "advancedPage")
    root6 = root5.find_element(WebBy.TAG_NAME, "settings-privacy-page")
    shadow_root6 = _shadow_root(driver, root6)
    root7 = shadow_root6.find_element(WebBy.ID, "pages")
    root8 = root7.find_element(WebBy.TAG_NAME, "settings-subpage")
    root9 = root8.find_element(WebBy.TAG_NAME, "site-details")
    shadow_root9 = _shadow_root(driver, root9)
    root10 = shadow_root9.find_element(WebBy.ID, "plugins")  # Flash
    shadow_root10 = _shadow_root(driver, root10)
    root11 = shadow_root10.find_element(WebBy.ID, "permission")
    WebSelect(root11).select_by_value("allow")
