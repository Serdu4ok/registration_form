from enum import Enum


class RegistrationSteps(str, Enum):
    SET_PET_INFO = 'set_pet_info'
    SET_PET_ISSUES = 'set_pet_issues'
    REGISTRATION = 'registration'

    LAST_FLOW_STEP = REGISTRATION
