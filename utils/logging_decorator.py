import functools
from utils.logger import setup_logger
from utils.helpers import take_screenshot

def log_testcase(func):
    """
    Logs test start, catches errors, and takes a screenshot if it fails.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger = setup_logger(func.__name__)
        logger.info(f"== Start test case: {func.__name__} ==")
        kwargs["logger"] = logger

        try:
            return func(*args, **kwargs)
        except AssertionError as e:
            # Only take screenshot if it's a UI test with a driver
            driver = kwargs.get("driver") or (args[0] if args else None)
            if driver:
                take_screenshot(driver, f"{func.__name__}_failed")
            logger.error(f"❌❌❌ TEST FAILED ❌❌❌: {e}")
            raise
        except Exception as e:
            logger.exception(f"Unexpected error in {func.__name__}")
            raise
    return wrapper

def step(message: str, logger):
    '''
    Log a test step message.
    '''
    logger.info(f"[Test Case Step] {message}")