from selenium.webdriver.common.keys import Keys
from pages.base_page import Action
from time import sleep

class HomePage(Action):
    SEARCH_BUTTON = '//a[contains(@class,"ScInteractableBase")][2]/div'
    SEARCH_INPUT = '//input[@type="search"]'
    STREAMER = '(//button[contains(@class,"tw-link")])[4]'
    

    def click_search_button(self):
        """
        Clicks the search button on the home page.
        """
        self.click_element(self.SEARCH_BUTTON)
        self.logger.info(f"Click search button")

    def input_search_field(self, keywords):
        """
        Inputs the search term and submits it.

        Args:
            keywords: The keyword to search for.
        """
        search_input = self.wait_for_element_visible(self.SEARCH_INPUT)
        search_input.clear()
        search_input.send_keys(keywords)
        search_input.send_keys(Keys.RETURN)
        self.logger.info(f"Search term entered: {keywords}")

    def select_streamer(self):
        """
        Clicks to select a streamer from the search results.
        """
        self.click_element(self.STREAMER)
        self.logger.info(f"Select streamer")

    def scroll_search_results_page(self, times):
        """
        Scrolls down the results page.

        Args:
            times (int): Number of times to scroll.
        """
        sleep(5)
        self.scroll_down(times)


