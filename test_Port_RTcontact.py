
import time
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from utilities.BaseClass import BaseClass


class Test_RT(BaseClass):
    def test_mapPage(self):
        #variables
        driver=self.driver
        wait=WebDriverWait(driver,30)
        act=ActionChains(driver)

        driver.find_element_by_link_text("צור קשר").click()
        childWindow=driver.window_handles[-1]
        driver.switch_to.window(childWindow)
        driver.execute_script("window.scrollTo(0,500)")
        driver.find_element_by_xpath("//span[contains(text(),'תל אביב')]").click()
        driver.execute_script("window.scrollTo(0,300)")


        title_ta=driver.find_element_by_xpath("//div[@class='su-tabs-pane su-u-clearfix su-u-trim Stab su-tabs-pane-open']/h2")
        adress_ta = driver.find_element_by_xpath("//body/div[@id='top']/div[1]/article[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/p[1]")
        telephon_number_ta = driver.find_element_by_xpath("//body/div[@id='top']/div[1]/article[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/p[2]/a[1]")
        #assertion
        assert title_ta.is_displayed()
        assert title_ta.text == "סניף תל אביב:"

        assert adress_ta.is_displayed()
        assert  adress_ta.text =="יגאל אלון 123, תל אביב"
        assert  "077-7067057"  in telephon_number_ta.text

    def test_contact(self):
        #variables
        driver=self.driver

        name_box=driver.find_element_by_xpath("//input[@name='myName']")
        name_box.send_keys("סבטלנה")
        name_box_value=name_box.get_attribute("value")


        sendButton=driver.find_element(By.XPATH, "//input[@class='wpcf7-form-control wpcf7-submit btn btn-primary btn-lg']")
        driver.execute_script("arguments[0].click();", sendButton)
        driver.execute_script("window.scrollTo(0,300)")



        email_box=driver.find_element_by_xpath("//span[@class='wpcf7-form-control-wrap email']/input[@type='email']")
        email_box_value01=email_box.get_attribute("value")
        #email_box_value02 =driver.execute_script("return document.getElementById('email').value")  #practice of JS

        alert=driver.find_element_by_xpath("//span[@class='wpcf7-form-control-wrap email']/span[@class='wpcf7-not-valid-tip']")

        email_box_color= email_box.value_of_css_property("box-shadow")

#Assert Name value
        #assert name_box.text=="סבטלנה" #do not work
        assert name_box_value =="סבטלנה"


#Assert Email value
        assert email_box_value01 == ""
        #assert email_box_value02 == ""

#Assert Alert
        assert alert.is_displayed()

#Assert color
        assert email_box_color == "rgb(229, 35, 35) 1px 1px 5px 0px"
