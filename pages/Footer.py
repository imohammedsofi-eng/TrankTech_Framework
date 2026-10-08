class Footer:
    def __init__(self,page):
        self.page = page

    #Web Development

        # self.Web_Development = page.locator("(//a[@href='https://www.tranktechnologies.com/web-development-company'])[2]")
        self.Web_Development = page.locator('//a[text()="Web Development"]')
        self.CMS_Website_Development = page.locator('//a[@href="https://www.tranktechnologies.com/cms-website-development-company"]')
        self.eCommerce_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[7]')
        self.Arrow_head_One = page.locator('(//i[@aria-hidden="true"])[3]')
        self.Website_Development = page.locator('//a[@href="https://www.tranktechnologies.com/website-development-company"]') 
        self.Custom_Web_Portal_Development = page.locator('//a[@href="https://www.tranktechnologies.com/custom-web-portal-development-company"]')
        self.Web_Development_List = [self.Web_Development, self.CMS_Website_Development, self.Custom_Web_Portal_Development]
        self.Web_Development_Sub_List = [self.Website_Development]

#App Development 
        self.App_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/app-development-company"])[1]')
        self.iOS_App_Development = page.locator('//a[@href="https://www.tranktechnologies.com/ios-mobile-app-development-company"]')
        self.Android_App_Development = page.locator('//a[@href="https://www.tranktechnologies.com/app-development-company"]')
        self.Arrow_head_Two = page.locator('(//i[@aria-hidden="true"])[4]')
        self.Android_App_Development_Sub = page.locator('//a[@href="https://www.tranktechnologies.com/android-app-development-company"]')
        self.App_Development_Sub = page.locator('(//a[@href="https://www.tranktechnologies.com/app-development-company"])[2]')
        self.Hybrid_Mobile_App_Development = page.locator('//a[@href="https://www.tranktechnologies.com/hybrid-mobile-app-development-company"]')
        self.Cross_Platform_App_Development = page.locator('//a[@href="https://www.tranktechnologies.com/cross-platform-mobile-app-development-company"]')
        self.Progressive_Web_App_Development = page.locator('//a[@href="https://www.tranktechnologies.com/progressive-web-app-development-company"]')
        self.App_Development_List = [self.App_Development, self.iOS_App_Development, self.Hybrid_Mobile_App_Development, self.Cross_Platform_App_Development, self.Progressive_Web_App_Development]
        self.App_Development_Sub_list = [self.Android_App_Development_Sub, self.App_Development_Sub]

#Graphic Design
        self.Graphic_Design = page.locator('//a[@href="https://www.tranktechnologies.com/graphic-design-company"]')
        self.Logo_Design = page.locator('//a[@href="https://www.tranktechnologies.com/logo-design-company"]')
        self.Banner_Design = page.locator('//a[@href="https://www.tranktechnologies.com/banner-design-company"]')
        self.Packaging_Design = page.locator('//a[@href="https://www.tranktechnologies.com/packaging-design-company"]')
        self.Business_Cards_Design = page.locator('//a[@href="https://www.tranktechnologies.com/business-cards-design-company"]')
        self.Graphic_Design_List = [self.Graphic_Design, self.Logo_Design, self.Banner_Design, self.Packaging_Design, self.Business_Cards_Design]

#UI UX Design

        # self.UI_UX_Design = page.locator('//a[@href="https://www.tranktechnologies.com/ui-ux-design-company"]') self.UI_UX_Design,
        self.UI_UX_Design = page.locator('//a[text()="UI UX Design"]')
        self.Mobile_App_Design = page.locator('//a[@href="https://www.tranktechnologies.com/mobile-app-design-company"]')
        self.Responsive_Web_Design = page.locator('//a[@href="https://www.tranktechnologies.com/responsive-web-design-company"]')
        self.Brand_Idendity_Design = page.locator('//a[@href="https://www.tranktechnologies.com/brand-identity-design-services-company"]')
        self.UI_UX_Design_List = [self.Mobile_App_Design, self.Responsive_Web_Design, self.Brand_Idendity_Design]

    def Graphic_design_click(self):
        # self.Contact_Us.click()
        # self.page.wait_for_load_state("load")
        for i in self.Graphic_Design_List:
            i.click()
            self.page.wait_for_load_state("load")
            self.page.wait_for_timeout(1000)
            self.page.go_back()

    def UI_UX_click(self):
        # self.Contact_Us.click()
        # self.page.wait_for_load_state("load")
        # self.page.wait_for_timeout(5000)
        for i in self.UI_UX_Design_List:
            # self.UI_UX_Design.scroll_into_view_if_needed()
            # self.page.wait_for_timeout(1000)
            i.click()
            self.page.wait_for_load_state("load")
            self.page.wait_for_timeout(1000)
            self.page.go_back()

    def Web_Dev_click(self):
        # self.Contact_Us.click()
        # self.page.wait_for_load_state("load")
        for i in self.Web_Development_List:
            i.click()
            self.page.wait_for_load_state("load")
            self.page.wait_for_timeout(1000)
            self.page.go_back()

    def Web_Dev_Sub_click(self):
        # self.Contact_Us.click()
        # self.page.wait_for_load_state("load")
        self.Arrow_head_One.click()
        for i in self.Web_Development_Sub_List:
            with self.page.context.expect_page() as new_page_info:
                i.click()
                new_tab = new_page_info.value
                new_tab.wait_for_load_state("load")
                new_tab.wait_for_timeout(1000)
                new_tab.close()


    def App_Dev_click(self):
        # self.Contact_Us.click()
        # self.page.wait_for_load_state("load")
        for i in self.App_Development_List:
            i.click()
            self.page.wait_for_load_state("load")
            self.page.wait_for_timeout(1000)
            self.page.go_back()

    def App_Dev_Sub_click(self):
        # self.Contact_Us.click()
        # self.page.wait_for_load_state("load")
        self.Arrow_head_Two.click()
        for i in self.App_Development_Sub_list:
            with self.page.context.expect_page() as new_page_info:
                i.click()
                new_tab = new_page_info.value
                new_tab.wait_for_load_state("load")
                new_tab.wait_for_timeout(1000)
                new_tab.close()

