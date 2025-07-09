import logging
import os
from datetime import datetime

RUN_TIME_FOLDER = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
LOG_BASE_DIR = os.path.join(os.getcwd(), "logs", RUN_TIME_FOLDER)

def setup_logger(name: str) -> logging.Logger:
    """
    Create and return a logger with file output.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d - %(funcName)s() - %(message)s'
        )
        os.makedirs(LOG_BASE_DIR, exist_ok=True)

        # Console handler
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        logger.addHandler(ch)

        # File handler: logs/YYYY-MM-DD_HH-MM-SS/module_name.log
        file_path = os.path.join(LOG_BASE_DIR, f"{name}.log")
        fh = logging.FileHandler(file_path, mode='a', encoding='utf-8')
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger