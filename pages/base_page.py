from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Action():
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger

    def click_element(self, locator):
        """
        Waits for an element to be clickable and clicks it.

        Args:
            locator: The XPath of the element to click.
        """
        try:
            element = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, locator)))
            element.click()
            self.logger.info(f"Clicked element: {locator}")
        except Exception as e:
            self.logger.error(f"Failed to click element: {locator} - {e}")
    
    def wait_for_element_visible(self, locator):
        """
        Waits for an element to be visible and returns it.

        Args:
            locator: The XPath of the element to find.
        """
        try:
            return WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.XPATH, locator)))
        except Exception as e:
            self.logger.error(f"Failed to wait for element visible: {locator} - {e}")

    def wait_for_element_present(self, locator):
        """
        Waits for an element to be present and returns it.

        Args:
            locator: The XPath of the element to find.
        """
        try:
            return WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH, locator)))
        except Exception as e:
            self.logger.error(f"Failed to wait for element present: {locator} - {e}")

    def scroll_down(self, times):
        """
        Scrolls down the page a specified number of times.

        Args:
            times (int): Number of times to scroll down.
        """
        try:
            for i in range(times):
                self.driver.execute_script("""
                    window.scrollTo({
                        top: window.scrollY + 200,
                        behavior: 'smooth'
                    });
                """)
                sleep(1)
                self.logger.info(f"Scrolled down {i+1} time(s)")
        except Exception as e:
            self.logger.error(f"Failed to scroll_down - {e}")
