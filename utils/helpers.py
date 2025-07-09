import os
from utils.logger import LOG_BASE_DIR
from utils.config import TWITCH_URL

# =======================
# UI Helper Functions
# =======================

def go_to_twitch(driver, logger=None):
    '''
    Navigate to the Twitch homepage.
    '''
    if logger:
        logger.info(f"Go to Twitch: {TWITCH_URL}")
    driver.get(TWITCH_URL)

def take_screenshot(driver, name: str):
    '''
    Capture a screenshot of the current page and save it to the log directory.
    '''
    path = os.path.join(LOG_BASE_DIR, f"{name}.png")
    driver.save_screenshot(path)
    return path
