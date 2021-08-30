import sys

from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException

from utilities.BaseClass import BaseClass


class TestRTCourses(BaseClass):
    def test_RtCourses(self):
        driver=self.driver

        driver.find_element_by_xpath("//*[@id='MenuLeft']/a").click()

        secondwind = driver.window_handles[1]
        driver.switch_to.window(secondwind)
        driver.implicitly_wait(5)
        driver.find_element_by_xpath("//*[@id='mat-input-0']").send_keys("examplr@gmail.com")
        driver.find_element_by_xpath("//*[@id='mat-input-1']").send_keys("password")
        driver.find_element_by_xpath("//span[contains(text(),'Login')]").click()
        driver.maximize_window()

        driver.find_element_by_xpath("//button[@class='btn']").click()  # Close pop up Tav Yarok

        #var
        courseField=driver.find_elements_by_xpath("//div[@class='table-responsive']/table/tbody/tr")
        countAll=len(courseField)
        countClicable=0

        list_All=[]
        list_Clickable=[]
        list_notClickable=[]

        #All Courses
        for f in courseField:

                driver.execute_script('arguments[0].scrollIntoView(true);', f)
                list_All.append(f.find_element_by_xpath("td").text)

        #Clickable  Courses
        for num in range(1, countAll + 1): #without +1 will not print last course
            try:
                courseName =driver.find_element_by_xpath("//div[@class='table-responsive']/table/tbody/tr[" + str(num) + "]/td[1]/a")  #this locator only valid for active element

                driver.execute_script('arguments[0].scrollIntoView(true);', courseName)
                countClicable +=1
                list_Clickable.append(courseName.text)
                courseName.click()

                driver.execute_script("window.history.go(-1)")
                driver.find_element_by_xpath("//button[@class='btn']").click()  # Close pop up Tav Yarok

            except NoSuchElementException:
                pass
            except ElementNotInteractableException:
                # print("Error:", sys.exc_info()[0])
                pass

        #not clickable courses
        for cours in list_All:
            if cours not in list_Clickable:
                list_notClickable.append(cours)

        countNotClickable=len(list_notClickable)

        print("Count of All Courses:", countAll)
        print("Count of Clickable Courses:",countClicable,"\n","List:\n",list_Clickable)
        print("Count of Not Clickable Courses:",countNotClickable,"\n","List:\n", list_notClickable)


