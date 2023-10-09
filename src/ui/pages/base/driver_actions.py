import platform
from typing import Tuple

from selene import browser
from selene.elements import SeleneElement
from selene.support import by
from selene.support.conditions import be, have
from selene.support.jquery_style_selectors import s
from selenium.webdriver import Keys


class DriverActions:

    def __init__(self):
        self.shared_driver = browser

    @staticmethod
    def find_element(locator: str) -> SeleneElement:
        return s((by.xpath(locator)))

    def visit(self, url: str) -> None:
        self.shared_driver.open_url(url)

    # pylint: disable=unsupported-binary-operation
    def set_text(self, locator: str, value: str | int) -> None:
        self.wait_for_element_visibility(locator)
        self.find_element(locator).should(be.visible).should(be.enabled).type(str(value))

    def set_text_enter(self, locator: str, value: str) -> None:
        self.find_element(locator).should(be.visible).should(be.enabled).type(value).press_enter()

    def remove_text(self, locator: str | Tuple):
        keys = Keys.COMMAND if platform.system() == 'Darwin' else Keys.CONTROL
        self.find_element(locator).should(be.visible).should(be.enabled).click(). \
            type(keys, 'a').type(Keys.BACKSPACE)
        return self

    # pylint: disable=unsupported-binary-operation
    def check_element_text(self, locator: str, text: str | int) -> None:
        self.find_element(locator).should(be.visible).should(have.exact_text(str(text)))

    def click(self, locator: str) -> None:
        self.find_element(locator).should(be.clickable).should(be.enabled).click()

    def wait_for_element_visibility(self, locator: str) -> None:
        self.find_element(locator).should(be.visible)

    def click_with_js(self, locator):
        script = f'document.querySelector("{locator}").click()'
        self.shared_driver.execute_script(script)
