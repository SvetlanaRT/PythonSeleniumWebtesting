from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class TestSearch(BaseClass):
    def test_Search(self):
        driver = self.driver
        driver.implicitly_wait(20)
        searchKey = "classic dress"
        actionChains = ActionChains(driver)

        # close popup
        driver.switch_to.window(driver.window_handles[-1])
        driver.find_element_by_xpath( "//body/div[1]/div[5]/div[1]/div[1]/div[1]/i[1]").click()
        # close popup
        driver.implicitly_wait(50)
        driver.switch_to.window(driver.window_handles[-1])
        print(driver.title)
        driver.find_element_by_xpath("//div[@class='quickg-outside']").click()

        driver.switch_to.window(driver.window_handles[0])
        driver.implicitly_wait(20)
        # print(driver.title)
        # searching
        driver.find_element_by_xpath( "//input[@type='search']").send_keys(searchKey)
        driver.find_element_by_xpath("//div[@class='search-btn she-btn-black j-search-btn']").click()
        driver.execute_script("window.scrollTo(0,300)")

        # add to cart
        driver.implicitly_wait(5)
        item = driver.find_element_by_xpath( "//body/div[1]/div[1]/div[2]/div[2]/section[1]/div[1]/section[1]/div[1]/a[1]/img[2]")
        addButton =driver.find_element_by_xpath('//body/div[1]/div[1]/div[2]/div[2]/section[1]/div[1]/section[1]/div[1]/section[1]/div[1]/div[1]/div[1]/button[1]') #normalize-space() do not work

        actionChains.move_to_element(item).perform()  #must!!! be separated
        actionChains.pause(10).click(addButton).perform() #must!!! be separated

        select_please=driver.find_element_by_xpath("//h6[contains(text(),'Please select')]")
        actionChains.move_to_element(select_please)

        optionSize = driver.find_elements_by_xpath("//span[@class='S-radio__input-preset keMdPD']")
        # print(type(optionSize))
        # print(len(optionSize))
        for o in optionSize:
            if o.text == 'M':
               o.click()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("//button[contains(text(),'submit')]").click()
