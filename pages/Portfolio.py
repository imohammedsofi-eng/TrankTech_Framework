class Portfolio:
    def __init__(self,page):
        self.page = page

        self.Portfolio = page.locator('//a[@href="https://www.tranktechnologies.com/portfolio"]')
        self.page.wait_for_load_state("load")
        self.ICS_Homework = page.locator('//a[@href="https://www.icshomework.in/"]')
        self.Wings_Pharma = page.locator('//a[@href="https://www.wingspharma.com/"]')
        self.Arena_Animation = page.locator('//a[@href="https://arenasonipat.com/"]')
        self.Home_360 = page.locator('//a[@href="https://home360stores.com/"]')
        self.Club_Meeting = page.locator('(//a[text()="View More"])[5]') 
        self.Cords_Cables = page.locator('//a[@href="https://cordscable.tranktechnologies.com/"]')

        self.Portfolio_list = [self.ICS_Homework, self.Wings_Pharma , self.Arena_Animation, self.Home_360,  self.Club_Meeting, self.Cords_Cables]


    def Portfolio_click(self):
        self.Portfolio.click()
        self.page.wait_for_load_state("load")

        for i in self.Portfolio_list:
            if i == self.Club_Meeting:
                self.Club_Meeting.click()
            else:
                with self.page.context.expect_page() as new_page_info:
                    i.click()
                new_tab = new_page_info.value
                new_tab.wait_for_load_state("load")
                new_tab.close()
            # self.page.wait_for_load_state("load")
            # self.page.go_back()
            # self.page.locator('//a[@href="https://www.tranktechnologies.com/portfolio"]').click()
            # self.page.wait_for_load_state("load")