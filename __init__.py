# -*- coding: utf-8 -*-
from appium import webdriver



class Login():
    def __init__(self,driver):
        self.driver=driver

    def loginPage(self,acc,pwd):
        try:
                self.driver.find_element_by_xpath("//*[@text='稍后再说']").click()
                self.driver.find_element_by_id('tw.com.ark.football_dev_test:id/fragment_login_account_edit').send_keys(acc)
                self.driver.find_element_by_id('tw.com.ark.football_dev_test:id/fragment_login_account_pw').send_keys(pwd)
                self.driver.find_element_by_xpath("//*[@text='登录']").click()






        except Exception as e:
            print('loginPage: %s'%e)
            self.driver.get_screenshot_as_file('www.png')


    def loginSucces(self):
        try:
            text=self.driver.find_element_by_xpath("//*[contains(@resource-id,'d9')]").text
            print(u'登入驗證成功,帳號為: %s'%text)


        except Exception as error:
            print(u"登入驗證錯誤: %s"%error)
            self.driver.get_screenshot_as_file('wrongAns.png')


    def login(self,acc,pwd):
        '''登入'''
        try:
            self.loginPage(acc,pwd)
            result=self.loginSucces()
            print(result)


        except Exception as e:
            print(u'登入錯誤: %s'%e)

class base():
    def __init__(self,driver):
        self.driver=driver

    def xpath(self,xpath):
        return self.driver.find_element_by_xpath(xpath)
    def id(self,id):
        return self.driver.find_element_by_id(id)
    def screenshot(self,name):
        return self.drvier.get_screenshot_as_file(name)
























