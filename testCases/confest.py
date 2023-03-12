# from selenium import webdriver
# import pytest

# @pytest.fixture()
# def setup():
#     # self.driver = webdriver.chrome()
#     driver = webdriver.Chrome(executable_path="driver/chromedriver.exe")
#     driver.maximize_window()
#     return driver
# -------------------------------------

from selenium import webdriver
import pytest
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture()
def setup(true=None):
    options = Options()
    options.add_argument('--disable-gpu')
    options.add_argument('--mute-audio')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--disable-infobars')
    options.add_argument('--ignore-certificate-errors-spki-list')
    options.add_argument('--no-sandbox')
    options.add_argument('--no-zygote')
    options.add_argument('--log-level=3')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--disable-web-security')
    options.add_argument('--disable-features=VizDisplayCompositor')
    options.add_argument('--disable-breakpad')
    # Set desired capabilities to ignore SSL stuffs
    desired_capabilities = options.to_capabilities()
    desired_capabilities['acceptInsecureCerts'] = True
    service = ChromeService(executable_path="driver/chromedriver.exe")
    options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})

    driver = webdriver.Chrome(service=service, options=options,
                              service_args=["--verbose", "--log-path=chromerun.log"]
                              )
    driver.maximize_window()

    return driver
# desired_capabilities=desired_capabilities
