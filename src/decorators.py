import functools
import logging
import pandas as pd
from itertools import islice

def debug(func, output, logger):
    if isinstance(output, pd.DataFrame):
        logger.debug(f"{func.__name__} result: Columns = {output.columns}, Shape = {output.shape}\n")
        logger.debug(f"{func.__name__} dataframe snippet: {output.head()}\n")

    elif isinstance(output, tuple):
        logger.info(f"{func.__name__} returns a tuple. Now showing various items returned in the tuple. \n")
        item_count = 0
        for item in output:
            item_count += 1
            if isinstance(item, pd.DataFrame):
                logger.debug(f"{func.__name__} item number {item_count}: Columns = {item.columns}, Shape = {item.shape}\n")
                logger.debug(f"{func.__name__} dataframe snippet: {item.head()}\n")
            else:
                logger.debug(f"{func.__name__} item number {item_count}: {item}\n")

    elif isinstance(output, dict):
        logger.info(f"{func.__name__} returns a dictionary, now showing keys")
        logger.debug(f"{func.__name__} keys: {output.keys()}")

    else:
        logger.debug(f"{func.__name__} result: {output}\n")


def log(debug_logs: bool = False):
    def decorator(func):
            @functools.wraps(func)
            def wrapper_func(*args, **kwargs):
                logger = logging.getLogger(func.__module__)
                try:
                    logger.info(f"Running {func.__name__}\n")
                    output = func(*args, **kwargs)
                    if debug_logs:
                        debug(func=func, output=output, logger=logger)
                    return output
                
                except Exception as e:
                    logger.error(f"Error in {func.__name__}: {e}\n")
                    raise

            return wrapper_func
    return decorator