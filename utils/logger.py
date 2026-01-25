import logging


def get_logger(name):
    """
    Creates a named logger with INFo level
    Works with pytest log_cli=True or standalone scripts
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    return logger
