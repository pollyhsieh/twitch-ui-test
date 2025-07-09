from pages.base_page import Action

class StreamPage(Action):
    SCREEN_PEOPLE_VIEW = "(//div[contains(@class,'player-controls')]//div[contains(@class,'InjectLayout-sc')])[1]"

    def wait_until_ready(self):
        """
        Waits until a element appears that confirms the stream is fully loaded.

        Args:
            timeout: Max seconds to wait
        """
        self.logger.info("Waiting for stream player to load")
        return self.wait_for_element_present(self.SCREEN_PEOPLE_VIEW)
