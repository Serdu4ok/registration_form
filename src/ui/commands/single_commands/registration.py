from data.data_set import ONLINE_STATE_RESTRICTION, INFO_ABOUT_VET
from data.messages.ui_page_messages.ui_info import RegistrationInfo
from data.models.account import Account
from data.steps_enums import RegistrationSteps
from src.ui.data_checker import DataCheckerUi
from src.ui.pages.registration_page import RegistrationPage


class BaseRegistration:
    def __init__(self, step_name: RegistrationSteps, step_number: int):
        self.registration = RegistrationPage()
        self.step_name = step_name
        self.step_number = step_number
        self.data_checker = DataCheckerUi()
        self.notifications = RegistrationInfo()


class SetPetInfo(BaseRegistration):

    def __init__(self):
        super().__init__(RegistrationSteps.SET_PET_INFO, 1)

    def execute(self, account_options: Account) -> None:
        self.data_checker.validate_messages(self.notifications.PET_INFO_MSG)
        self.registration.select_pet_type(account_options.pet.pet_type)
        self.registration.set_pet_name(account_options.pet.pet_name)
        self.registration.select_state(account_options.state)
        if account_options.state in ONLINE_STATE_RESTRICTION:
            self.data_checker.check_online_state_restriction(account_options.state)
            self.registration.submit_info_form()
        if account_options.state in INFO_ABOUT_VET:
            self.data_checker.check_info_about_vet_has_seen()
            self.registration.submit_info_form()
        self.registration.submit_registration_form()


class SetPetIssues(BaseRegistration):

    def __init__(self):
        super().__init__(RegistrationSteps.SET_PET_ISSUES, 2)

    def execute(self, account_options: Account) -> None:
        self.data_checker.validate_messages(self.notifications.issue_info_msg(account_options.pet.pet_name))
        self.registration.select_pet_issues(account_options.pet.pet_issues)
        self.registration.submit_registration_form()


class Registration(BaseRegistration):

    def __init__(self):
        super().__init__(RegistrationSteps.REGISTRATION, 3)

    def execute(self, account_options: Account) -> None:
        self.data_checker.validate_messages(self.notifications.create_acc_info_msg(account_options.pet.pet_name))
        self.registration.set_email(account_options.email)
        self.registration.set_password(account_options.password)
        self.registration.submit_registration_form()

    # TODO: add next steps
