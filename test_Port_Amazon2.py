#TWO OPTIONS FOR SEARCH & Stars filtering

from utilities.BaseClass import BaseClass

#Search
class TestSearch(BaseClass):
    def test_Search01(self):
        driver=self.driver

        searchKey="hatchimals colleggtibles eggs"
        driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']").send_keys(searchKey)
        driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']").send_keys(u'\ue007')  #ENTER
        #Stars
        driver.find_element_by_xpath("//body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/span[1]/div[1]/span[1]/div[1]/div[1]/div[2]/ul[1]/li[1]/span[1]/a[1]/section[1]/i[1]").click()

    def test_Search02(self):
        driver=self.driver
        driver.implicitly_wait(20)

        searchKey="hatchimals colleggtibles eggs"
        driver.find_element_by_xpath("//input[@id='nav-search-submit-button']").click()
        #Stars
        driver.find_element_by_xpath("//body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/span[1]/div[1]/span[1]/div[1]/div[1]/div[2]/ul[1]/li[1]/span[1]/a[1]/section[1]/i[1]").click()
#assertion
        driver.implicitly_wait(20)
        items = driver.find_elements_by_xpath("//div[@class='a-section a-spacing-medium']/div/div[1]")
        for i in items:
            #print(i.text, "\n")
            assert "Hatchimals" or "Sponsored" in i.text