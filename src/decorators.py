import functools
import logging
import pandas as pd

logger = logging.getLogger(__name__)

def log(func):
    @functools.wraps(func)
    def wrapper_func(*args, **kwargs):
        try:
            logger.info(f"Running {func.__name__}\n")
            output = func(*args, **kwargs)

            if isinstance(output, pd.DataFrame):
                logger.debug(f"{func.__name__} result: Columns = {output.columns}, Shape = {output.shape}\n")
            
            elif isinstance(output, tuple):
                logger.info(f"{func.__name__} returns a tuple. Now showing various items returned in the tuple. \n")
                item_count = 0
                for item in output:
                    item_count += 1
                    if isinstance(item, pd.DataFrame):
                        logger.debug(f"{func.__name__} item number {item_count}: Columns = {item.columns}, Shape = {item.shape}\n")
                    else:
                        logger.debug(f"{func.__name__} item number {item_count}: {item}\n")
            else:
                logger.debug(f"{func.__name__} result: {output}\n")
                
            return output
        
        except Exception as e:
            logger.error(f"Error in {func.__name__}: {e}\n")
            raise

    return wrapper_func