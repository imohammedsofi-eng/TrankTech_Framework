# import pytest

# from pages.Social_Media import Social_Media
    
# @pytest.mark.smoke
# def test_Social_Media(page):
#     SM = Social_Media(page)
#     SM.Social_Media_click()

import pytest

from pages.Footer import Footer

@pytest.mark.smoke
def test_Graphic_Design(page):
    GD = Footer(page)
    GD.Graphic_design_click()

@pytest.mark.smoke
def test_UI_UX(page):
    GD = Footer(page)
    GD.UI_UX_click()

@pytest.mark.smoke
def test_Web_Dev(page):
    GD = Footer(page)
    GD.Web_Dev_click()

@pytest.mark.smoke
def test_Web_Dev_Sub(page):
    GD = Footer(page)
    GD.Web_Dev_Sub_click()

@pytest.mark.smoke
def test_App_Dev(page):
    GD = Footer(page)
    GD.App_Dev_click()

@pytest.mark.smoke
def test_App_Dev_Sub(page):
    GD = Footer(page)
    GD.App_Dev_Sub_click()