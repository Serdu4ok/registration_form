import pytest

from data.enums import State
from data.steps_enums import RegistrationSteps
from src.ui.flow.main_flow import MainFlow


@pytest.mark.positive
class TestRegistrationPositive:

    @pytest.fixture(autouse=True)
    # pylint: disable=attribute-defined-outside-init
    def pre_test(self):
        self.main_flow = MainFlow()

    def test_registration(self):
        self.main_flow.client_registration()

    @pytest.mark.parametrize('state', State.get_state_list())
    def test_register_with_all_states(self, state):
        user_options = self.main_flow.factories.user_factory.user_options(state=state)
        self.main_flow.client_registration(user_options, RegistrationSteps.SET_PET_INFO)
