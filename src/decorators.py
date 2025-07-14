import functools
import logging
import pandas as pd


def log(func):
    @functools.wraps(func)
    def wrapper_func(*args, **kwargs):
        logger = logging.getLogger(func.__module__)
        try:
            logger.info(f"Running {func.__name__}\n")
            output = func(*args, **kwargs)
            return output
        except Exception as e:
            logger.exception(f"Error in {func.__name__}: {e}\n")
            raise
    return wrapper_func