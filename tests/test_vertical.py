
import pytest
from pages.verticals import vertical

@pytest.mark.smoke
def test_trading(page):
    tr= vertical(page)
    tr.Trading_options_click()

@pytest.mark.smoke
def test_retailandecommerce(page):
    rtl=vertical(page)
    rtl.Retail_Ecommerce_click()



