import os

from src.logger.logger import set_logging

set_logging()


def get_root_path() -> str:
    return os.path.dirname(os.path.abspath(__file__))


pytest_plugins = [
    'src.fixtures.set_up_ui'
]
