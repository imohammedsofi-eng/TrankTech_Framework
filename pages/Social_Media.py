class Social_Media:
    def __init__(self,page):
        self.page = page

        self.SocialMedia = self.page.locator('(//a[@href="https://www.tranktechnologies.com/contact-us"])[1]')
        self.Facebook = page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/facebook.png"]')
        self.LinkedIn = page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/linkedin.png"]')
        self.Instagram = page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/Insta.png"]')
        self.Pinterest = page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/pinterest.png"]')
        self.Twitter = page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/twitter.png"]')
        self.YouTube = page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/youtube.png"]')
        self.Quora = page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/quora.png"]')
        self.SocialMedia_Pages = [self.Facebook, self.LinkedIn, self.Instagram, self.Pinterest, self.Twitter, self.YouTube, self.Quora]

    # def Social_Media_click(self):
    #     for i in self.SocialMedia_Pages:
    #         i.click()
    #         self.page.wait_for_load_state("load")
    #         self.page.locator('(//a[@href="https://www.tranktechnologies.com/contact-us"])[1]').click()
    #         self.page.wait_for_load_state("load")


    def Social_Media_click(self):
        self.SocialMedia.click()
        self.page.wait_for_load_state("load")

        for i in self.SocialMedia_Pages:
            with self.page.context.expect_page() as new_page_info:
                i.click()
            new_tab = new_page_info.value
            new_tab.wait_for_load_state("load")
            new_tab.close()