class Verticals :
    def __init__(self,page):
        self.page = page
        #Verticals 
        self.Verticals = page.locator('(//a[@href="#"])[2]')

        self.Trading = page.locator("//strong[text()='Trading']")
        self.Stock_Trading = page.locator("(//a[text()='Stock Trading'])[1]")
        self.Paper_Trading = page.locator('(//a[@href="https://www.tranktechnologies.com/paper-trading-app-development-company"])[1]')
        self.Cfd_Trading = page.locator('(//a[@href="https://www.tranktechnologies.com/cfd-trading-app-development-company"])[1]')
        self.Stock_Trading_Mass = page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')
        self.Algo_Trading = page.locator('(//a[@href="https://www.tranktechnologies.com/algo-trading-app-development-company"])[1]')
        self.Custom_Trading = page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
        self.Web_Portal_Trading = page.locator('(//a[@href="https://www.tranktechnologies.com/webportal-trading-development"])[1]')
        self.Trading_List = [self.Stock_Trading, self.Paper_Trading, self.Cfd_Trading, self.Stock_Trading_Mass, self.Algo_Trading, self.Custom_Trading, self.Web_Portal_Trading]

        self.Retail_Ecommerce = page.locator('//strong[text()="Retail and Ecommerce"]')
        self.eCommerce_Website_Development = page.locator("(//a[@href='https://www.tranktechnologies.com/ecommerce-web-development-company'])[1]")
        # self.eCommerce_Website_Development = page.locator('(//a[text()="eCommerce Website Development"])[1]')
        self.eCommerce_App_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-app-development"])[1]')
        self.Retail_Ecom_List = [self.eCommerce_Website_Development, self.eCommerce_App_Development]

        self.Healthcare = page.locator('//strong[text()="Healthcare"]')
        self.Diet_Nutritions = page.locator('(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]')
        self.Health_tracking_App = page.locator('(//a[@href="https://www.tranktechnologies.com/health-tracking-app"])[1]')
        self.Healthcare_List = [self.Diet_Nutritions, self.Health_tracking_App]

        self.Fintech = page.locator('//strong[text()="Fintech"]')
        self.Pos_Software = page.locator('(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]')
        self.Crypto = page.locator('(//a[@href="https://www.tranktechnologies.com/cryptocurrency-mobile-app-development-company"])[1]')
        # self.Pos_Software = page.locator('(//a[text()="Pos Software Development"])[1]')
        # self.Crypto = page.locator('(//a[text()="Crypto"])[1]')
        self.Fintech_List = [self.Pos_Software, self.Crypto]

        self.Custom_App = page.locator('//strong[text()="Custom App"]')
        self.Desktop_App = page.locator('(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]')
        self.HRM_Dev = page.locator('(//a[@href="https://www.tranktechnologies.com/hrm-application-development-company"])[1]')
        self.Travel = page.locator('(//a[@href="https://www.tranktechnologies.com/travel-mobile-app-development-company"])[1]')
        self.Dating_app_Dev = page.locator('(//a[@href="https://www.tranktechnologies.com/dating-app-development-company"])[1]')
        self.CRM_Dev_USA = page.locator('(//a[@href="https://www.tranktechnologies.com/usa/custom-crm-development-company-usa"])[1]') 
        self.CRM_Dev = page.locator('(//a[@href="https://www.tranktechnologies.com/custom-crm-development-company"])[1]')
        self.ERP_App_Dev = page.locator('(//a[@href="https://www.tranktechnologies.com/erp-app-development-company"])[1]')
        self.E_Learn = page.locator('(//a[@href="https://www.tranktechnologies.com/e-learning-mobile-app-development-company"])[1]')
        self.Real_Estate = page.locator('(//a[@href="https://www.tranktechnologies.com/real-estate-mobile-app-development-company"])[1]')
        # self.Desktop_App = page.locator('(//a[text()="Desktop App Development"])[1]')
        # self.Travel = page.locator('(//a[text()="Travel"])[1]')
        # self.CRM_Dev_USA = page.locator('(//a[text()="CRM Development USA"])[1]')
        # self.E_Learn = page.locator('(//a[text()="E-Learning"])[1]')
        # self.Real_Estate = page.locator('(//a[text()="Real Estate"])[1]')
        self.Custom_App_List = [self.Desktop_App, self.HRM_Dev, self.Travel, self.Dating_app_Dev, self.CRM_Dev_USA, self.CRM_Dev, self.ERP_App_Dev, self.E_Learn, self.Real_Estate]

    def Trading_options_click(self):
        for i in self.Trading_List:
            self.Verticals.hover()
            self.Trading.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def Retail_Ecom_click(self):
        for i in self.Retail_Ecom_List:
            self.Verticals.hover()
            self.Retail_Ecommerce.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def Healthcare_click(self):
        for i in self.Healthcare_List:
            self.Verticals.hover()
            self.Healthcare.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def Fintech_click(self):
        for i in self.Fintech_List:
            self.Verticals.hover()
            self.Fintech.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def Custom_App_click(self):
        for i in self.Custom_App_List:
            self.Verticals.hover()
            self.Custom_App.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()
