class Technology:
    def __init__(self,page):
        self.page= page
        #Technology
        self.Technology= page.locator("(//a[text()='Technologies'])[1]")
        self.eCommerce_Development= page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"]/strong)[2]')
        self.Magento_Development= page.locator('(//a[@href="https://www.tranktechnologies.com/magento-development"])[1]')
        self.Codeigniter_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/codeigniter-development"])[1]')
        self.Big_Commerce = page.locator('(//a[@href="https://www.tranktechnologies.com/big-commerce"])[1]')
        self.CS_Cart_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/cs-cart-development"])[1]')
        self.Nop_Commerce= page.locator('(//a[@href="https://www.tranktechnologies.com/nopcommerce-design-and-development-company"])[1]')
        self.Opencart_Development= page.locator('(//a[@href="https://www.tranktechnologies.com/opencart-development"])[1]')
        self.WordPress_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/wordpress-development"])[1]')
        self.Shopify_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/shopify-development"])[1]')
        self.Node_JS_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/node-js-development"])[1]')
        self.Woo_Commerce = page.locator('(//a[@href="https://www.tranktechnologies.com/woocommerce-development"])[1]')
        self.Laravel_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/laravel-development"])[1]')
        self.Prestashop_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/prestashop-development"])[1]')
        self.Drupal_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/drupal-development"])[1]')
        self.Wix_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/wix-development"])[1]')
        self.Joomla_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/joomla-development"])[1]')
        self.React_JS_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/react-js-development"])[1]')
        self.Express_JS_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/express-js-development"])[1]')
        self.Technologylist=[self.Magento_Development,self.Big_Commerce,self.CS_Cart_Development,self.Nop_Commerce,self.Opencart_Development,self.WordPress_Development,self.Shopify_Development,self.Node_JS_Development,self.Woo_Commerce,self.Laravel_Development,self.Prestashop_Development,self.Drupal_Development,self.Wix_Development,self.Joomla_Development,self.React_JS_Development,self.Express_JS_Development]
        
        #Mobile App Development
        self.Mobile_App_Development= page.locator('//a[@href="https://www.tranktechnologies.com/mobile-app-development-company"]/strong')
        self.React_Native_Mobile_App= page.locator('(//a[@href="https://www.tranktechnologies.com/react-native-mobile-app-development"])[1]')
        self.Enterprise_Mobile_App= page.locator('(//a[@href="https://www.tranktechnologies.com/enterprise-mobile-app-development"])[1]')
        self.Xamarin_Mobile_App = page.locator('(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]')
        self.Kotlin_Mobile_App=  page.locator('(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]')                                       
        self.Flutter_Mobile_App = page.locator('(//a[@href="https://www.tranktechnologies.com/flutter-mobile-app-development"])[1]')
        self.Ionic_app=  page.locator('(//a[@href="https://www.tranktechnologies.com/ionic-mobile-app-development"])[1]')                                       
        self.Swift_App =page.locator('(//a[@href="https://www.tranktechnologies.com/swift-mobile-app-development"])[1]')
        self.Appointment_booking = page.locator('(//a[@href="https://www.tranktechnologies.com/appointment-booking-development"])[1]')
        self.Mobile_App_DevelopmentList=[self.React_Native_Mobile_App,self.Enterprise_Mobile_App,self.Xamarin_Mobile_App,self.Kotlin_Mobile_App,self.Flutter_Mobile_App,self.Ionic_app,self.Swift_App,self.Appointment_booking]

        #AI
        self.AI= page.locator('//a[@href="https://www.tranktechnologies.com/artificial-intelligence-development-services-company-india"]/strong')

    def eCommerce_development_click(self):
        for k in self.Technologylist:
            self.Technology.hover()
            self.eCommerce_Development.hover()
            k.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()
    def mobile_app_dev_click(self):
        for l in self.Mobile_App_DevelopmentList:
            self.Technology.hover()
            self.Mobile_App_Development.hover()
            l.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()
    def AI_click(self):
        self.Technology.hover()
        self.AI.click()
        self.page.wait_for_load_state("load")
        self.page.go_back()


        


