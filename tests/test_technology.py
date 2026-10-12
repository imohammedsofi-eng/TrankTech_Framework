
import pytest

from pages.technology import Technology


@pytest.mark.smoke
def test_eCommerce_development(page):
    tg=Technology(page)
    tg.eCommerce_development_click()
    
@pytest.mark.smoke
def test_mobileappdevelopment(page):
    tg=Technology(page)
    tg.mobile_app_dev_click()

@pytest.mark.smoke
def test_AI(page):
    ai=Technology(page)
    ai.AI_click()



    