import pytest
from playwright.sync_api import Playwright

@pytest.fixture(scope="session")
def page(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=300)
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()
    context.close()
    browser.close()