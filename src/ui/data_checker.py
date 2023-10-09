from typing import List, Dict

from data.enums import State
from src.ui.locators.registration_locators import RegistrationLocators
from src.ui.pages.base.driver_actions import DriverActions


class DataCheckerUi:

    def __init__(self):
        self._registration = RegistrationLocators()
        self._driver_actions = DriverActions()

    def verify_text(self, error_data: dict) -> None:
        self._driver_actions.check_element_text(error_data['locator'], error_data['text'])

    # pylint: disable=unsupported-binary-operation
    def validate_messages(self, messages: List[str] | Dict[str, str]) -> None:
        messages = [messages] if isinstance(messages, Dict) else messages
        for message in messages:
            self.verify_text(message)

    def check_info_about_vet_has_seen(self) -> None:
        self._driver_actions.wait_for_element_visibility(self._registration.INFO_ABOUT_VET_SEEN)

    def check_online_state_restriction(self, state: State) -> None:
        self._driver_actions.wait_for_element_visibility(self._registration.INFO_ONLINE_RESTRICTION.format(state))
