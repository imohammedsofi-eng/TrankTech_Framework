class All_below_link():
    def __init__(self,page):
        self.page=page
        #Web Development
        self.cms_website_development= page.locator('//a[@href="https://www.tranktechnologies.com/cms-website-development-company"]')
        self.ecommerce_web_dev_dropdown= page.locator("//a[text()='eCommerce Development']/parent::span/parent::div/span[2]")
        self.web_development= page.locator("//a[text()='Website Development']")
        self.custom_web_portal_development= page.locator("//a[text()='Custom Web Portal Development']")
        self.web_dev= [self.cms_website_development,self.custom_web_portal_development,self.ecommerce_web_dev_dropdown,self.web_development]

        #App Development
        self.app_dev_androidappdev_dropdown= page.locator("//a[text()='iOS App Development']//parent::li//parent::ul/li[3]/div/div/div/span[2]/i") 
        self.app_dev_iosappdev= page.locator('//a[@href="https://www.tranktechnologies.com/ios-mobile-app-development-company"]')
        self.app_dev_aad= page.locator("(//a[text()='Android App Development'])[2]")
        self.app_dev_ad= page.locator("(//a[text()='App Development'])[2]")
        self.app_dev_hmad = page.locator("//a[text()='Hybrid Mobile App Development']")
        self.app_dev_cpmad= page.locator("//a[text()='Cross-Platform App Development']")
        self.app_dev_pwad= page.locator("//a[text()='Progressive Web App Development']")
        self.appdev= [self.app_dev_iosappdev,self.app_dev_hmad,self.app_dev_cpmad,self.app_dev_pwad,self.app_dev_androidappdev_dropdown,self.app_dev_aad,self.app_dev_ad]

    def all_link_click_web_dev(self):
        for i in self.web_dev:
            i.click()
            self.page.wait_for_load_state('load')
            self.page.go_back()
    def all_link_click_app_dev(self):
        for j in self.appdev:
            j.click()
            self.page.wait_for_load_state('load')
            self.page.go_back()

    
    