class vertical:
    def __init__(self,page):
        self.page= page
        #Verticals
        self.Verticals=page.locator("(//a[text()='Verticals'])[1]")
        self.Trading= page.locator("//strong[text()='Trading']") 
        self.Stock_Trading= page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-mobile-app-development-company"])[1]')
        self.Paper_Trading= page.locator("(//a[text()='Paper Trading'])[1]")
        self.CFD_Trading = page.locator("(//a[text()='CFD Trading'])[1]")
        self.Trading_Development = page.locator("(//a[contains(text(),'Development in Massachusetts')])[1]")
        self.Algo_Trading = page.locator("(//a[text()='Algo Trading'])[1]")
        self.Custom_Trading =page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
        self.Web_Portal_Trading= page.locator('(//a[text()="Web Portal Trading"])[1]')
        self.Trading_list = [self.Stock_Trading,self.Paper_Trading,self.CFD_Trading,self.Trading_Development,self.Algo_Trading,self.Custom_Trading,self.Web_Portal_Trading]
        #Retail and Ecommerce
        self.Retail_and_Ecommerce= page.locator('//*[text()="Retail and Ecommerce"]')
        self.eCommerce_Website_Development= page.locator('(//*[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[2]')
        self.eCommerce_App_Development= page.locator("//a[text()='eCommerce App Development']")
        self.Retail_Ecommerce_list = [self.eCommerce_Website_Development,self.eCommerce_App_Development]

    def Trading_options_click(self):
        for i in self.Trading_list:
            self.Verticals.hover()
            self.Trading.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()
    def Retail_Ecommerce_click(self):
        for j in self.Retail_Ecommerce_list:
            self.Verticals.hover()
            self.Retail_and_Ecommerce.hover()
            j.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()




    # #Healthcare
    # Healthcare= page.locator("(//*[text()='Healthcare'])[1]")
    # Diet_Nutritions= page.locator('(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]')
    # health_tracking_app=page.locator('(//a[text()="Health tracking App"])[1]')
    # Healthcare_list = [Diet_Nutritions,health_tracking_app]

    # #Fintech
    # Fintech= page.locator("(//*[text()='Fintech'])[1]")
    # Pos_Software_Development = page.locator("(//a[starts-with(text(),'Pos Software')])[1]")
    # Crypto= page.locator("(//a[text()='Crypto'])[1]")
    # Fintechlist = [Pos_Software_Development,Crypto]

    # #Custom App
    # Custom_App= page.locator('//li[@data-id="customApp"]/a/strong')
    # Desktop_App_Development= page.locator('(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]')
    # HRM_Development= page.locator('(//a[@href="https://www.tranktechnologies.com/hrm-application-development-company"])[1]')
    # Travel = page.locator("(//a[text()='Travel'])[1]")
    # Dating_App_Development= page.locator("(//a[text()='Dating App Development'])[1]")
    # CRM_Development_USA = page.locator("(//a[text()='CRM Development USA'])[1]")
    # CRM_Development= page.locator("(//a[starts-with(text(),'CRM')])[1]")
    # ERP_App_Development= page.locator("(//a[starts-with(text(),'ERP App')])[1]")
    # E_Learning= page.locator("(//a[text()='E-Learning'])[1]")
    # Real_Estate= page.locator("(//a[text()='Real Estate'])[1]")
    # Custom_App_list = [Desktop_App_Development,HRM_Development,Travel,Dating_App_Development,CRM_Development_USA,CRM_Development,ERP_App_Development,E_Learning,Real_Estate]

