import pytest
from pages.page_down_all_link import All_below_link

@pytest.mark.smoke
def test_page_down_all_link_web_dev(page):
    web_link= All_below_link(page)
    web_link.all_link_click_web_dev()

@pytest.mark.smoke
def test_page_down_all_link_app_dev(page):
    app_link=All_below_link(page)
    app_link.all_link_click_app_dev()



