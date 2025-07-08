import logging
from pathlib import Path

root_dir = Path(__file__).parent.parent
log_file = root_dir / "logs.log"

def setup_logger():
    logger = logging.getLogger()

    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(filename=log_file,
                                       mode="a",
                                       encoding="utf-8")
    
    console_formatter = logging.Formatter("{asctime} - {name} - {levelname} - {message}",
                                  style="{", datefmt="%Y-%m-%d %H:%M")
    
    file_formatter = logging.Formatter("{asctime} - {name} - {levelname} - {message}\n{exc_info}",
                                  style="{", datefmt="%Y-%m-%d %H:%M")
    
    file_handler.setFormatter(fmt=file_formatter)
    console_handler.setFormatter(fmt=console_formatter)

    logger.setLevel("DEBUG")
    console_handler.setLevel("INFO")
    file_handler.setLevel("DEBUG")
    
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger