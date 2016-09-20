import logging
import logging.config

LOG_CFG_PATH="~/itest/config/logging.conf"
LOGGER_NAME="itest"

logging.config.fileConfig(LOG_CFG_PATH)
logger = logging.getLogger(LOGGER_NAME)

def debug(str):
    logger.debug(str)

def info(str):
    logger.info(str)

def warn(str):
    logger.warn(str)

def error(str):
    logger.error(str)

def critical(str):
    logger.critical(str)

