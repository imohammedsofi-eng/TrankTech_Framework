class Contact_Us:
    def __init__(self,page):
        self.page=page 
        self.contact_us= page.locator("(//a[text()='Contact us'])[1]").click()
        self.your_name = page.locator('(//input[@placeholder="Your Name"])[2]').fill("Santanu")
        self.your_mail = page.locator('(//input[@placeholder="Your Mail"])[2]').fill('santanu@gmail.com')
        self.send_otp = page.locator("(//button[text()='Send OTP'])[2]").click()
        self.enter_otp = page.locator('(//input[@placeholder="Enter OTP"])[2]').fill("123456")
        self.your_company = page.locator('(//input[@placeholder="Your Company"])[2]').fill('ABC')
        self.your_service = page.locator('(//select[@name="service"])[2]').click()
        self.page.locator('(//select[@name="service"])[2]').select_option(value='Web Development')
        self.your_phone= page.locator('(//input[@placeholder="Your Phone"])[2]').fill('8908415977')
        self.message_text = 'I am Santanu, from West Bengal. I am looking for a good testing job'
        self.message = page.locator('(//textarea[@placeholder="Message"])[2]').fill(self.message_text)
        self.page.wait_for_timeout(5000)


