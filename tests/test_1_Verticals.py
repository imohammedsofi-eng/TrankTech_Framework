import pytest

from pages.verticals_page import Verticals
# from pages.1_verticals import vertivals


@pytest.mark.smoke
def test_trading(page):
    tr = Verticals(page)
    tr.Trading_options_click()

@pytest.mark.smoke
def test_retail(page):
    rt = Verticals(page)
    rt.Retail_Ecom_click()

@pytest.mark.smoke
def test_healthcare(page):
    Hr = Verticals(page)
    Hr.Healthcare_click()

@pytest.mark.smoke
def test_Fintech(page):
    FT = Verticals(page)
    FT.Fintech_click()

@pytest.mark.smoke
def test_Custom_App(page):
    CA = Verticals(page)
    CA.Custom_App_click()

