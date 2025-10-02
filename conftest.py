import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")        # fixture is resuable piece of code
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)       # in this we are launching the browser
        yield browser                                     # we let the browser be used in tests
        browser.close()                                  # after the tests are done we close the browser

@pytest.fixture                                     # fixture means setup and teardown
def page(browser):                                   # in this we are creating a new page for each test
    page = browser.new_page()                     # we let the page be used in tests
    yield page                                   # after the test is done we close the page
    page.close()
