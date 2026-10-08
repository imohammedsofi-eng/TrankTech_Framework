import pytest

from pages.Contact_us import Contact_Us

@pytest.mark.smoke
def test_Contact_us(page):
    GD = Contact_Us(page)
    GD.Contact_us_click()

