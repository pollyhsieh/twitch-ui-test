import pytest
from utils.helpers import go_to_twitch
from pages.home_page import HomePage
from pages.stream_page import StreamPage
from utils.helpers import take_screenshot
from utils.logging_decorator import log_testcase, step

@log_testcase
@pytest.mark.ui
def test_twitch_mobile_stream(driver, **kwargs):
    logger = kwargs["logger"]

    # Step 1: Go to Twitch
    step("Step 1: Go to Twitch.", logger)
    go_to_twitch(driver, logger) 
    home_page = HomePage(driver, logger)

    # Step 2: Click search icon
    step("Step 2: Click search icon.", logger)
    home_page.click_search_button()

    # Step 3: Input StarCraft II
    step("Step 3: Input search keyword: StarCraft II.", logger)
    home_page.input_search_field("StarCraft II")

    # Step 4: Scroll down 2 times
    step("Step 4: Scroll down 2 times in search results page.", logger)
    home_page.scroll_search_results_page(2)

    # Step 5: Select one streamer
    step("Step 5: Select a streamer from results", logger)
    home_page.select_streamer()

    # Step 6: On the streamer page wait until all is load and take a screenshot
    step("Step 6: Check streamer page is load and take screenshot.", logger)
    stream_page = StreamPage(driver, logger)
    assert stream_page.wait_until_ready(), "Stream did not load successfully"
    take_screenshot(driver, "streamer_page.png")
