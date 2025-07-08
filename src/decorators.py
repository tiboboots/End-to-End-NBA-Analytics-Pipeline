import functools
import logging
import pandas as pd

logger = logging.getLogger(__name__)

def log(func):
    @functools.wraps(func)
    def wrapper_func(*args, **kwargs):
        try:
            logger.info(f"Running {func.__name__}")
            output = func(*args, **kwargs)

            if isinstance(output, pd.DataFrame):
                logger.debug(f"{func.__name__} result: {output.columns} {output.shape}")
            else:
                logger.debug(f"{func.__name__} result: {output}")
                
            return output
        
        except Exception as e:
            logger.error(f"Error in {func.__name__}: {e}")
            raise

    return wrapper_func