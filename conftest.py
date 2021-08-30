import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")

#------------------------------Options for differentr URL-------------------------------------------------
    #driver.get("https://www.amazon.com/ref=nav_logo")  #FOR Amazon

    # testedURL="https://www.amazon.com/ref=nav_logo"     #FOR Amazon1
    # driver.get(testedURL)

    # testedURL="https://il.shein.com/"                     #FOR Shein
    # driver.get(testedURL)

    # driver.get("https://rt-ed.co.il/")                   #FOT RT_contact

    driver.get("https://rt-ed.co.il/")                   #FOT RTcourses

    # driver.get("https://www.iwantoneofthose.com/")          #FOR IWOOT

    #-----------------------------------------------------------------------------------------------------------
    driver.maximize_window()
    request.cls.driver = driver
    yield
    #driver.close()
    # driver.quit()
