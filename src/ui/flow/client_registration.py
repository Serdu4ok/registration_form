from data.models.account import Account
from data.steps_enums import RegistrationSteps
from src.ui.commands.registration import get_registration_commands
from src.ui.pipeline import CommandPipeline


class ClientRegistrationFlow:
    def __init__(self):
        self.pipeline = CommandPipeline()

    def register_client(self, account_options: Account,
                        final_step_name: RegistrationSteps = RegistrationSteps.LAST_FLOW_STEP) -> Account:
        self.pipeline.execute_commands(get_registration_commands(), account_options, final_step_name)
        return account_options
