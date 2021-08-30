import re
import time
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.BaseClass import BaseClass


class TestCoupon(BaseClass):
    def test_Login(self):

#variables:
          driver=self.driver
          wait=WebDriverWait(driver,30)
          act=ActionChains(driver)

          username ="example@gmail.com"
          passw="password"

          #HANDLE POPUP
          driver.switch_to.window(driver.window_handles[-1])
          wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class='emailReengagement_close_button']")))
          driver.find_element(By.XPATH,"//button[@class='emailReengagement_close_button']").click()

          #lOGIN
          accountT=driver.find_element(By.XPATH,"//div[@class='responsiveAccountHeader_openAccountPanel']/a")
          loginI=driver.find_element(By.XPATH,"//ul[@class='responsiveAccountHeader_accountGroup']/li[@class='responsiveAccountHeader_accountListItem responsiveAccountHeader_accountListButtonItem responsiveAccountHeader_accountListButtonItem-first']")
          act.move_to_element(accountT).move_to_element(loginI).click().perform()
          #switch to login application page


          driver.implicitly_wait(20)
          handles=driver.window_handles
          for h in handles:
               driver.switch_to.window(h)


          #login with valid password
          wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='sc-dNLxif oHMZQ']/div/div[@class='sc-dNLxif sc-jqCOkK sc-dqBHgY iYUGBX']/div[@class='sc-dNLxif sc-jqCOkK sc-uJMKN HEgXz']/input[@class='sc-bbmXgH pPbSM']")))
          username_textbox=driver.find_element(By.XPATH,"//div[@class='sc-dNLxif oHMZQ']/div/div[@class='sc-dNLxif sc-jqCOkK sc-dqBHgY iYUGBX']/div[@class='sc-dNLxif sc-jqCOkK sc-uJMKN HEgXz']/input[@class='sc-bbmXgH pPbSM']")
          username_textbox.send_keys(username)

          wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='sc-dNLxif bdzkfc']/div/div[@class='sc-dNLxif sc-jqCOkK sc-dqBHgY iYUGBX']/div[@class='sc-dNLxif sc-jqCOkK sc-uJMKN HEgXz']/input[@class='sc-bbmXgH pPbSM']")))
          pass_textbox=driver.find_element(By.XPATH,"//div[@class='sc-dNLxif bdzkfc']/div/div[@class='sc-dNLxif sc-jqCOkK sc-dqBHgY iYUGBX']/div[@class='sc-dNLxif sc-jqCOkK sc-uJMKN HEgXz']/input[@class='sc-bbmXgH pPbSM']")
          pass_textbox.send_keys(passw)

          driver.find_element(By.XPATH,"//div[@class='sc-jDwBTQ izTyOD']/button").submit() #enter

          #link to login main page
          time.sleep(5)
          handles=driver.window_handles
          for h in handles:
               driver.switch_to.window(h)


          #seach box
          driver.find_element(By.XPATH,"//input[@id='header-search-input']").send_keys("lego")
          driver.switch_to.window(driver.window_handles[-1])
          driver.implicitly_wait(5)
          results=driver.find_elements(By.XPATH,"//ul[@class='headerSearch_resultsList']/li")

          for r in results:
               if r.text == 'lego storage':
                    r.click()
                    break
          #quick buy
          driver.find_element(By.XPATH, "//body/div[2]/div[4]/div[1]/div[1]/div[1]/div[1]/main[1]/div[3]/ul[1]/li[1]/div[1]/div[2]/div[1]/button[1]").click()
          driver.switch_to.window(driver.window_handles[-1])
          wait.until(EC.element_to_be_clickable((By.XPATH, "//body/div[2]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[8]/div[2]/a[1]")))
          driver.find_element(By.XPATH, "//body/div[2]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[8]/div[2]/a[1]").click()

          #switch to basket page
          time.sleep(5)
          handles=driver.window_handles
          for h in handles:
               driver.switch_to.window(h)


          #coupon not applied
          wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='responsiveBasket_bodyItem responsiveBasket_bodyItem-subTotal']")))
          totalBeforeCoupon=driver.find_element(By.XPATH,"//div[@class='responsiveBasket_bodyItem responsiveBasket_bodyItem-subTotal']").text

          #manual applain coupon
          coupon="LEGO10"
          driver.find_element(By.XPATH, "//input[@id='discountcode']").send_keys(coupon)
          driver.find_element(By.XPATH, "//button[@id='add-discount-code']").click()



          totalAfterCoupon=driver.find_element(By.XPATH,"//div[@class='responsiveBasket_totalValue']").text
          # print(totalBeforeCoupon , "," , type(totalBeforeCoupon))
          # print(totalAfterCoupon , "," , type(totalAfterCoupon))

          tbc=re.split('(\d+)',  totalBeforeCoupon)
          tac=re.split('(\d+)',  totalAfterCoupon)
          # print(tbc+ tac)

          Ftbc=float(tbc[1]+"."+tbc[3])
          roundFtbc=('%0.2f' % Ftbc)
          Ftac=float(tac[1]+"."+tac[3])
          roundFtac=('%0.2f' % Ftac)

          # print(Ftbc)
          # print(Ftac)

          # #validate coupon message
          message=driver.find_element(By.XPATH,"//div[@class='responsiveBasket_discountLabel']/p").text
          # print(message)

          # # total amount
          total=driver.find_element(By.XPATH,"//div[@class='responsiveBasket_totalValue']").text
          tfinal=re.split('(\d+)',total)
          tf=float(tfinal[1]+"."+tfinal[3])
          roundTf=float('%0.2f' % tf)
          print("TofalFinal:",roundTf,type(roundTf))

            #discount function
          def percent(num1, num2):
              num1 = float(num1)
              num2 = float(num2)
              percentage = '{0:.2f}'.format((num1 * (num2/100)))
              return float(percentage)

          discount=percent(roundFtbc,10)
          roundDiscount=('%0.1f' % discount)
          print ("discount by function:",roundDiscount,type(discount))

          # #discount by substraction
          discountBySubsrtaction=(Ftbc-Ftac)
          roundDiscountBySubsrtactio=('%0.1f' % discountBySubsrtaction)
          print("discount by subtraction",roundDiscountBySubsrtactio)

          assert Ftac< Ftbc
          assert  message == "10% Off Lego Storage Accessories & Gifts"
          assert  roundDiscount == roundDiscountBySubsrtactio
          assert Ftbc-discount == tf


#COUPON EXPIRED
    def test_expiredCoupon(self):
        driver = self.driver
        driver.get("https://www.iwantoneofthose.com/my.basket")

        coupon_old = "LEGO20"
        driver.find_element(By.XPATH, "//input[@id='discountcode']").send_keys(coupon_old)
        driver.find_element(By.XPATH, "//button[@id='add-discount-code']").click()

        message=driver.find_element(By.XPATH,"//div[@class='responsiveBasket_errorAlert ']")
        print(message.text)
        assert "Discount Code expired on: 26 Jul 2021 12:00 GMT" in message.text





