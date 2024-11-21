import logging
import graypy

def setup_logger(name='my_logger'):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    graylog_handler = graypy.GELFUDPHandler('localhost', 12201)
    logger.addHandler(graylog_handler)

    return logger