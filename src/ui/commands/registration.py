from typing import Tuple

from src.ui.commands.single_commands.registration import SetPetInfo, SetPetIssues, Registration


def get_registration_commands() -> Tuple:
    return (
        SetPetInfo(),
        SetPetIssues(),
        Registration()
    )
