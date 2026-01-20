import logging


def get_logger(name):
    """
    Creates a named logger with INFo level
    Works with pytest log_cli=True or standalone scripts
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    """
    Logging in StreamHandler way but commented it as we want pytest client logging
    # Avoid duplicate handlers if already exists
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    logger.propagate = True
    """

    return logger
