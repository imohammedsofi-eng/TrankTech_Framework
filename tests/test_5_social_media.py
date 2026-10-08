import pytest

from pages.Social_Media import Social_Media
    
@pytest.mark.smoke
def test_Social_Media(page):
    SM = Social_Media(page)
    SM.Social_Media_click()