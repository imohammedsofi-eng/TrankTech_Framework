import pytest

from pages.Country import Country

@pytest.mark.smoke
def test_Country(page):
    C = Country(page)
    C.Country_click()