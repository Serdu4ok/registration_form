from data.models.account import Account
from data.steps_enums import RegistrationSteps
from src.factories.factories import Factories
from src.ui.flow.client_registration import ClientRegistrationFlow
from src.ui.pages_helper import PagesHelper


class MainFlow:

    def __init__(self):
        self.register_flow = ClientRegistrationFlow()
        self.pages = PagesHelper()
        self.factories = Factories()

    def client_registration(self, account_options: Account = None,
                            final_step_name: RegistrationSteps = RegistrationSteps.LAST_FLOW_STEP) -> Account:
        account_options = account_options if account_options else self.factories.user_factory.user_options()
        self.pages.main.visit_main_page()
        self.pages.main.go_to_registration()
        return self.register_flow.register_client(account_options, final_step_name)
