class Contact_Us:
    def __init__(self,page):
        self.page = page

        #Contact_US
        self.Contact_Us = self.page.locator('(//a[@href="https://www.tranktechnologies.com/contact-us"])[1]')
        # self.Contact_Us.click()
        # self.page.wait_for_load_state("load")
        # self.page.locator('(//input[@placeholder="Your Name"])[2]').fill("Iqbal")
        # self.page.locator('(//input[@placeholder="Your Mail"])[2]').fill("i.mohammed.sofi@gmail.com")
        # self.page.once("dialog", lambda dialog: dialog.accept())
        # self.page.locator('(//button[@type="button"])[2]').click()
        # self.page.locator('(//input[@placeholder="Enter OTP"])[2]').fill("1234")
        # self.page.locator('(//input[@placeholder="Your Company"])[2]').fill("STC")
        # self.page.locator('(//select[@name="service"])[2]').select_option("Web Development")
        # self.page.locator('(//input[@placeholder="Your Phone"])[2]').fill("+919398649944")
        # self.page.locator('(//textarea[@placeholder="Message"])[2]').fill("This is a Message Box")
        # self.page.wait_for_timeout(1000)


    def Contact_us_click(self):
        self.Contact_Us.click()
        self.page.wait_for_load_state("load")
        self.page.locator('(//input[@placeholder="Your Name"])[2]').fill("Iqbal")
        self.page.locator('(//input[@placeholder="Your Mail"])[2]').fill("i.mohammed.sofi@gmail.com")
        self.page.once("dialog", lambda dialog: dialog.accept())
        self.page.locator('(//button[@type="button"])[2]').click()
        self.page.locator('(//input[@placeholder="Enter OTP"])[2]').fill("1234")
        self.page.locator('(//input[@placeholder="Your Company"])[2]').fill("STC")
        self.page.locator('(//select[@name="service"])[2]').select_option("Web Development")
        self.page.locator('(//input[@placeholder="Your Phone"])[2]').fill("+919398649944")
        self.page.locator('(//textarea[@placeholder="Message"])[2]').fill("This is a Message Box")
        self.page.wait_for_timeout(1000)    



