# -*- coding: utf-8 -*-
class deposit():
    def __init__(self,driver):
        self.driver=driver

    def deposit_one_hundred_dollars(self, money):

        self.driver.find_element_by_id('tw.com.ark.football_dev_test:id/tab_person_info').click()
        self.driver.find_element_by_xpath("//*[contains(@text,'充值')]").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'支付宝转账')]").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'支付宝一键支付')]").click()
        self.driver.find_element_by_xpath("//*[contains(@class,'Edit')]").send_keys(money)
        self.driver.find_element_by_xpath("//*[contains(@text,'下一步')]").click()

        try:
            text = self.driver.find_element_by_xpath("//*[contains(@text,'支付成功!')]").text
            print(u'充值成功訊息: %s' % text)

        except Exception as e:
            print(u'充值錯誤(Fail.png): %s' % e)
            self.driver.get_screenshot_as_file('Fail.png')