import pytest

from pages.Portfolio import Portfolio

@pytest.mark.smoke
def test_Portfolio(page):
    P = Portfolio(page)
    P.Portfolio_click()