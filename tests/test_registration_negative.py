import pytest

from data.enums import GeneralConstants
from data.messages.ui_page_messages.ui_errors import RegistrationErrors
from data.steps_enums import RegistrationSteps
from src.ui.data_checker import DataCheckerUi
from src.ui.flow.main_flow import MainFlow


@pytest.mark.negative
class TestRegistrationNegative:

    @pytest.fixture(autouse=True)
    # pylint: disable=attribute-defined-outside-init
    def pre_test(self):
        self.main_flow = MainFlow()
        self.data_checker = DataCheckerUi()
        self.errors = RegistrationErrors()

    def test_registration_with_shot_password(self):
        account_options = self.main_flow.factories.user_factory.user_options()
        self.main_flow.pages.registration.visit_registration_page()
        self.main_flow.pages.registration.set_pet_info(account_options)
        self.main_flow.pages.registration.remove_pet_name()
        self.data_checker.validate_messages(self.errors.empty_pet_name)

    def test_to_long_pet_name(self):
        self.main_flow.pages.registration.visit_registration_page()
        self.main_flow.pages.registration.set_pet_name(GeneralConstants.LONG_MSG_25)
        self.data_checker.validate_messages(self.errors.max_len_pet_name)

    def test_submit_empty_registration(self):
        self.main_flow.client_registration(final_step_name=RegistrationSteps.SET_PET_ISSUES)
        self.main_flow.pages.registration.wait_for_registration_page()
        self.main_flow.pages.registration.submit_registration_form()
        self.data_checker.validate_messages([self.errors.required_email, self.errors.required_password])

    def test_submit_shot_password(self):
        self.main_flow.client_registration(final_step_name=RegistrationSteps.SET_PET_ISSUES)
        self.main_flow.pages.registration.wait_for_registration_page()
        self.main_flow.pages.registration.set_email(GeneralConstants.DEFAULT_EMAIL.value)
        self.main_flow.pages.registration.set_password('1')
        self.main_flow.pages.registration.submit_registration_form()
        self.data_checker.validate_messages([self.errors.shot_password])

    def test_submit_invalid_email(self):
        self.main_flow.client_registration(final_step_name=RegistrationSteps.SET_PET_ISSUES)
        self.main_flow.pages.registration.wait_for_registration_page()
        self.main_flow.pages.registration.set_email(GeneralConstants.INVALID_EMAIL.value)
        self.main_flow.pages.registration.submit_registration_form()
        self.data_checker.validate_messages([self.errors.invalid_email])
