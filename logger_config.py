import logging
import graypy

def setup_logger(name='my_logger'):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    graylog_handler = graypy.GelfUDPHandler('localhost', 12201)  # Use the appropriate host and port
    logger.addHandler(graylog_handler)

    return logger