from data.enums import Urls
from src.ui.locators.main_page_locators import MainLocators
from src.ui.pages.base.driver_actions import DriverActions


class MainPage:

    def __init__(self):
        self._driver_actions = DriverActions()
        self._locators = MainLocators()

    def visit_main_page(self) -> None:
        self._driver_actions.visit(Urls.MAIN_PAGE)

    def go_to_registration(self) -> None:
        self._driver_actions.click(self._locators.BUTTON_GO_TO_REGISTRATION)
