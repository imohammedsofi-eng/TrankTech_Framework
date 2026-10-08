import pytest

from pages.technologies_page import Technologies
@pytest.mark.smoke
def test_eCommerce_Development(page):
    ECom_Dev = Technologies(page)
    ECom_Dev.Ecom_dev_click()

@pytest.mark.smoke
def test_Mobile_App(page):
    Mob_App = Technologies(page)
    Mob_App.Mobile_App_click()

@pytest.mark.smoke
def test_AI(page):
    AI = Technologies(page)
    AI.AI_Options_Click()