from selene.support.shared import browser
import pytest

@pytest.fixture()
def set_browser_size_window():
    browser.config.window_height = 1280
    browser.config.window_width = 1280

@pytest.fixture()
def open_browser(set_browser_size_window):
    browser.config.base_url = 'https://demoqa.com'
