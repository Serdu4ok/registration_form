import logging
import sys
from typing import Dict, Any

import structlog
from structlog import get_logger


def log_debug(name: str, data: Dict[str, Any]):
    get_logger().debug(name, **data)


def log_info(name: str, data: Dict[str, Any]):
    get_logger().info(name, **data)


def set_logging():
    logging.basicConfig(stream=sys.stdout, format="%(message)s", level=int(10))
    logging.getLogger('faker').setLevel(logging.ERROR)
    logging.getLogger('selenium').setLevel(logging.WARNING)
    logging.getLogger('urllib3').setLevel(logging.WARNING)
    structlog.configure(
        processors=[
            structlog.processors.TimeStamper(fmt="%Y-%m-%d %H:%M.%S"),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.JSONRenderer(indent=2, ensure_ascii=False)
        ],
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )
