class Blog:
    def __init__(self,page):
        self.page= page   # we just create a variable name as self.page and then call the page method which is under conftest.py

        #BLOG
        self.blog=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/"])[1]')
        self.app_development = page.locator("(//a[text()='App Development'])[3]")
        self.artificial_intelligence = page.locator("(//a[starts-with(text(),'Artificial')])[3]")
        self.content_marketing= page.locator("//a[text()='Content Marketing']")
        self.crm_development = page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/crm-development/"]')
        self.digital_marketing = page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/digital-marketing/"]')
        self.ecommerce_development= page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/ecommerce-development/"])[5]')
        self.email_marketing = page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/email-marketing/"]')
        self.graphic_design = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/graphic-design/"])[3]')
        self.software_it_company= page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/software-it-company/"]')
        self.software_development = page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/software-development/"]')
        self.ui_ux_design = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/ui-ux-design/"])[5]')
        self.web_development = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/web-development/"])[5]')
        self.all_blog = [self.app_development,self.artificial_intelligence,self.content_marketing,self.crm_development,self.digital_marketing,self.ecommerce_development,self.email_marketing,self.graphic_design,self.software_it_company,self.software_development,self.ui_ux_design,self.web_development]

    def blog_click(self):
        for i in self.all_blog:
            self.blog.click()
            i.click()
            self.page.wait_for_load_state('load')
            self.page.go_back()


