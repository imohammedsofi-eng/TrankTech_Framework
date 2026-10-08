
import pytest
from pages.blog_page import Blog

@pytest.mark.smoke
def test_Blog(page):
    Blog_page = Blog(page)
    Blog_page.Blog_click()