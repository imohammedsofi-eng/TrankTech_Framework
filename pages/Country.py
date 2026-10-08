class Country:
    def __init__(self,page):
        self.page = page


    def Country_click(self): 
        Countries = ["India", "USA", "UAE"]
        for i in Countries:
            self.page.locator('//select[@id="countrySelector"]').select_option (i)
            self.page.wait_for_timeout(5000)