import pytest

from pages.blog import Blog


@pytest.mark.smoke
def test_blog(page):
    blg=Blog(page)
    blg.blog_click()