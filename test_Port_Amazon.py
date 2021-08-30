#!!!!Class must start with "Test"
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from utilities.BaseClass import BaseClass


class TestSearch(BaseClass): #!!!!Class must start with "Test"
    def test_search(self):
        # searching
        self.driver.find_element(By.ID, "twotabsearchtextbox").send_keys("science kit")
        self.driver.find_element(By.ID, "twotabsearchtextbox").send_keys(Keys.ENTER)
        # checkBox
        checkboxesNames = self.driver.find_elements(By.XPATH,
                                                    "//div[@class='a-checkbox a-checkbox-fancy s-navigation-checkbox aok-float-left']/parent::a/span")
        for name in checkboxesNames:
            if name.text == "NATIONAL GEOGRAPHIC":
                print(name.text)
                name.click()
                break
        # assertion
        items = self.driver.find_elements(By.XPATH,
                                          "//h2[@class='a-size-mini a-spacing-none a-color-base s-line-clamp-4']")
        print(len(items))
        for i in items:
            # print(i.text , "\n")
            assert "NATIONAL GEOGRAPHIC" or "National Geographic" in i.text
