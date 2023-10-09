from typing import Tuple

from data.models.account import Account
from src.logger.logger import log_debug


class CommandPipeline:

    @staticmethod
    def execute_commands(steps: Tuple, options: Account, final_step_name: str):
        for step in steps:
            log_debug('Trying to execute step', {'step': step.step_name})
            step.execute(options)
            if step.step_name == final_step_name:
                break
