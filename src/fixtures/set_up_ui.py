import os
from datetime import datetime

import pytest
from selene import browser
from selene import config
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from conftest import get_root_path
from src.logger.logger import log_debug


def get_local_chrome() -> webdriver.chrome:
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    chrome_service = ChromeService(ChromeDriverManager().install())
    return webdriver.Chrome(service=chrome_service, options=options)


@pytest.fixture(scope='function', autouse=True)
def driver(request):
    webdriver_main = get_local_chrome()
    webdriver_main.implicitly_wait(1)
    webdriver_main.maximize_window()
    request.cls.driver = webdriver_main
    browser.set_driver(webdriver_main)

    config.timeout = 30
    yield browser
    browser.quit()


@pytest.fixture(scope='function', autouse=True)
# pylint: disable=redefined-outer-name
def driver_cleanup(request):
    driver = request.cls.driver
    driver.delete_all_cookies()
    yield
    driver.delete_all_cookies()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
# pylint: disable=redefined-outer-name
def pytest_runtest_makereport(item, call):  # pylint: disable=unused-argument
    outcome = yield
    rep = outcome.get_result()
    if rep.outcome == 'failed':
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
            test_name = str(item).split(' ')[1][:-1]
            browser.take_screenshot(f'{get_root_path()}/reports/screenshots',
                                    f'{test_name}_{timestamp}')

        except AttributeError:
            log_debug('Screenshot error', {'error': 'Failed to take screenshot'})


# Define a hook to run before starting all tests
def pytest_sessionstart():
    dir_path = f'{get_root_path()}/reports/screenshots'

    for file in os.listdir(dir_path):
        file_path = os.path.join(dir_path, file)
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
