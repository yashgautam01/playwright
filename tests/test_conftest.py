from playwright.sync_api import sync_playwright
import pytest

def test_example(page):
    page.goto("https://google.com/ncr")
    assert page.title() == "Google"


    