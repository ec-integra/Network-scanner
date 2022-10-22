import logging.config
from .settings import logger_config
logging.config.dictConfig(logger_config)

app_logger = logging.getLogger('app_logger')