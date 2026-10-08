class Blog :
    def __init__(self,page):
        self.page = page
        
        #Blog 
        self.Blog = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/"])[1]')

        self.App_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/app-development/"])[1]')
        self.Artificial_Intelligence = page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/artificial-intelligence/"]')
        self.Content_Marketing = page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/content-marketing/"]')
        self.CRM_Development = page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/crm-development/"]')
        self.Digital_Marketing = page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/digital-marketing/"]')
        self.ECommerce_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/ecommerce-development/"])[5]')
        self.Email_Marketing = page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/email-marketing/"]')
        self.Graphic_Design = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/graphic-design/"])[3]')
        self.Software_IT_Company = page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/software-it-company/"]')
        self.Software_Development = page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/software-development/"]')
        self.UI_UX_Design = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/ui-ux-design/"])[5]')
        self.Web_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/web-development/"])[5]')
        self.Categories = [self.App_Development, self.Artificial_Intelligence, self.Content_Marketing, self.CRM_Development, self.Digital_Marketing, self.ECommerce_Development, self.Email_Marketing, self.Graphic_Design, self.Software_IT_Company, self.Software_Development, self.UI_UX_Design, self.Web_Development]

    def Blog_click(self): 
        for i in self.Categories:
            self.Blog.click()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()