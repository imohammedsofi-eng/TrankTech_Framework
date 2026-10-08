class Technologies :
    def __init__(self,page):
        self.page = page
        #Technologies 
        self.Technologies = page.locator('(//a[@href="#"])[5]')

        self.eCommerce_Development = page.locator('//strong[text()="eCommerce Development"]')
        self.Magneto_Dev = page.locator('(//a[@href="https://www.tranktechnologies.com/magento-development"])[1]')
        self.Codeigniter_Dev = page.locator('(//a[@href="https://www.tranktechnologies.com/codeigniter-development"])[1]')
        self.Big_Commerce = page.locator('(//a[@href="https://www.tranktechnologies.com/big-commerce"])[1]')
        self.CS_Cart_Dev = page.locator('(//a[@href="https://www.tranktechnologies.com/cs-cart-development"])[1]')
        self.Nop_Commerce = page.locator('(//a[@href="https://www.tranktechnologies.com/nopcommerce-design-and-development-company"])[1]')
        self.Laravel_Dev = page.locator('(//a[@href="https://www.tranktechnologies.com/laravel-development"])[1]')
        self.Opencart_Dev = page.locator('(//a[@href="https://www.tranktechnologies.com/opencart-development"])[1]')
        self.WordPress_Dev = page.locator('(//a[@href="https://www.tranktechnologies.com/wordpress-development"])[1]')
        self.Shopify_Dev = page.locator('(//a[@href="https://www.tranktechnologies.com/shopify-development"])[1]')
        self.NodeJS_Dev = page.locator('(//a[@href="https://www.tranktechnologies.com/node-js-development"])[1]')
        self.Woo_Commerce = page.locator('(//a[@href="https://www.tranktechnologies.com/woocommerce-development"])[1]')
        self.Prestashop_Dev = page.locator('(//a[@href="https://www.tranktechnologies.com/prestashop-development"])[1]')
        self.eCommerce_Development_List = [self.Magneto_Dev, self.Codeigniter_Dev, self.Big_Commerce, self.CS_Cart_Dev, self.Nop_Commerce, self.Laravel_Dev, self.Opencart_Dev, self.WordPress_Dev, self.Shopify_Dev, self.NodeJS_Dev, self.Woo_Commerce, self.Prestashop_Dev]
    
        self.Mobile_App_Development = page.locator('//strong[text()="Mobile App Development"]')
        self.React_Native_Mobile_App_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/react-native-mobile-app-development"])[1]')
        self.Enterprise_Mobile_App_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/enterprise-mobile-app-development"])[1]')
        self.Xamarin_Mobile_App_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]')
        self.Kotlin_Mobile_App_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]')
        self.Flutter_Mobile_App_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/flutter-mobile-app-development"])[1]')
        self.Ionic_App_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/ionic-mobile-app-development"])[1]')
        self.Swift_App_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/swift-mobile-app-development"])[1]')
        self.Appointment_Booking_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/appointment-booking-development"])[1]')
        self.Mobile_App_Development_List = [self.React_Native_Mobile_App_Development, self.Enterprise_Mobile_App_Development, self.Xamarin_Mobile_App_Development, self.Kotlin_Mobile_App_Development, self.Flutter_Mobile_App_Development, self.Ionic_App_Development, self.Swift_App_Development, self.Appointment_Booking_Development]
	    
        self.Artificial_Intelligence = page.locator('//strong[text()="Artificial Intelligence"]')
        self.AI_list =[self.Artificial_Intelligence]


    def Ecom_dev_click(self):
        for i in self.eCommerce_Development_List:
            self.Technologies.hover()
            self.eCommerce_Development.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def Mobile_App_click(self):
        for i in self.Mobile_App_Development_List:
            self.Technologies.hover()
            self.Mobile_App_Development.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def AI_Options_Click(self):
        for i in self.AI_list:
            self.Technologies.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()
