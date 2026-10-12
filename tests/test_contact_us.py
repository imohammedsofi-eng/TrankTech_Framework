import pytest

from pages.contact_us import Contact_Us


@pytest.mark.smoke
def test_contact_us(page):
    Contact_Us(page)
    