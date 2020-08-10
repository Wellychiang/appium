# -*- coding: utf-8 -*-
class withDraw():
    def __init__(self, driver):
        self.driver = driver

    def withdrawPage(self,fpwd,money):
        self.driver.find_element_by_id('tw.com.ark.football_dev_test:id/tab_person_info').click()
        self.driver.find_element_by_xpath("//*[contains(@text,'提现')]").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'4138')]").click()

        obalance = self.driver.find_element_by_xpath("//*[contains(@resource-id,'balance')]").text
        olimit = self.driver.find_element_by_xpath("//*[contains(@resource-id,'limit')]").text
        oavailable = self.driver.find_element_by_xpath("//*[contains(@resource-id,'available')]").text

        self.driver.find_element_by_xpath("//*[contains(@resource-id,'text_amount')]").send_keys(money)
        self.driver.find_element_by_xpath("//*[contains(@resource-id,'text_pw')]").send_keys(fpwd)
        self.driver.find_element_by_xpath("//*[contains(@resource-id,'withdraw_btn')]").click()

        print('舊當前餘額: %s'%obalance, '舊提款限額: %s'%olimit, '舊可提資金: %s'%oavailable)



    def withdrawlSucces(self):

        try:
            succes = self.driver.find_element_by_xpath("//*[contains(@text,'提现申请成功!')]").text
            prompt = self.driver.find_element_by_xpath("//*[contains(@resource-id,'message_text')]").text
            self.driver.find_element_by_xpath("//*[contains(@text,'确认')]").click()
            print(succes,prompt)


        except Exception as e:
            print(u'錯誤by提現驗證:(withdrawEr) %s'%e)
            self.driver.get_screenshot_as_file('withdrawEr.png')

        finally:
            self.driver.find_element_by_xpath("//*[contains(@text,'提现')]").click()
            self.driver.find_element_by_xpath("//*[contains(@text,'4138')]").click()
            balance = self.driver.find_element_by_xpath("//*[contains(@resource-id,'balance')]").text
            limit = self.driver.find_element_by_xpath("//*[contains(@resource-id,'limit')]").text
            available = self.driver.find_element_by_xpath("//*[contains(@resource-id,'available')]").text
            print('balance: %s' % balance, 'limit: %s' % limit, 'available: %s' % available)

    def withdraw(self,fpwd,money):
        try:
            self.withdrawPage(fpwd,money)
            result=self.withdrawlSucces()
            if result == True:
                print('ya')


        except Exception as e:
            print(u'提現錯誤: %s'%e)
            self.driver.get_screenshot_as_file('fail.png')