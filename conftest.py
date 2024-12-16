import os
import subprocess
from datetime import datetime

import pytest

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

import sys 

sys.dont_write_bytecode = True

# Chrome Start

@pytest.fixture(autouse=True)
def browser_setup(request):
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager' 
    options.add_argument("--headless")
    service = Service(executable_path=ChromeDriverManager().install())
    request.cls.driver = webdriver.Chrome(service=service, options=options)

# Chrome End

# Firefox Start

# @pytest.fixture(scope="class", autouse=True)
# def browser_setup(request):
#     options = webdriver.FirefoxOptions()
#     options.page_load_strategy = 'eager' 
#     options.add_argument("--headless")
#     service = Service(executable_path=GeckoDriverManager().install())
#     request.cls.driver = webdriver.Firefox(service=service, options=options)

# Firefox End


# @pytest.hookimpl(trylast=True)
# def pytest_sessionfinish(session, exitstatus):
#     today = datetime.now()
#     folderName = today.strftime("%Y-%m-%d")
#     fileName = today.strftime("%Y-%m-%d::%H:%M")
#     s = subprocess.getstatusoutput(f'allure generate AllureReport --name Stage --single-file -o reports/{folderName}/{fileName}')