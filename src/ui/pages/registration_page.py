from typing import List

from data.enums import PetType, Urls
from data.models.account import Account
from src.ui.locators.registration_locators import RegistrationLocators
from src.ui.pages.base.driver_actions import DriverActions


class RegistrationPage:

    def __init__(self):
        self._driver_actions = DriverActions()
        self._locators = RegistrationLocators()

    def visit_registration_page(self) -> None:
        self._driver_actions.visit(Urls.REGISTRATION)

    def select_pet_type(self, pet_type: PetType) -> None:
        self._driver_actions.click(self._locators.RADIO_PET_TYPE.format(pet_type))

    def set_pet_name(self, pet_name: str) -> None:
        self._driver_actions.set_text(self._locators.INPUT_PET_NAME, pet_name)

    def select_state(self, state: str) -> None:
        self._driver_actions.click(self._locators.SELECT_STATE.format(state))

    def select_pet_issues(self, pet_issues: List) -> None:
        for issue in pet_issues:
            self._driver_actions.click(self._locators.SELECT_PET_ISSUE.format(issue))

    def set_email(self, email: str) -> None:
        self._driver_actions.set_text(self._locators.INPUT_EMAIL, email)

    def set_password(self, password: str) -> None:
        self._driver_actions.set_text(self._locators.INPUT_PASSWORD, password)

    def submit_registration_form(self) -> None:
        self._driver_actions.click_with_js(self._locators.BUTTON_SUBMIT)

    def submit_info_form(self) -> None:
        self._driver_actions.click(self._locators.BUTTON_INFO_SUBMIT)

    def remove_pet_name(self) -> None:
        self._driver_actions.remove_text(self._locators.INPUT_PET_NAME)

    def wait_for_registration_page(self):
        self._driver_actions.wait_for_element_visibility(self._locators.INPUT_EMAIL)

    def set_pet_info(self, account_options: Account) -> None:
        self.select_pet_type(account_options.pet.pet_type)
        self.set_pet_name(account_options.pet.pet_name)
        self.select_state(account_options.state)
