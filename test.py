# -*- coding: utf-8 -*-
from appium import webdriver
from time import sleep
import unittest
from test import *
from test import withDraw,deposit,Bet


acc = 'wade01'
pwd = 'pppppppp'
fpwd = 'aaaassss'
money = '100'


class TryTry(unittest.TestCase):

    def setUp(self):
        desired_caps = {'deviceName' : '127.0.0.1:62001',
                    'platformName' : 'android',
                    'appPackage' :'tw.com.ark.football_dev_test',
                    'appActivity' : 'tw.com.ark.football.login.LoginActivity',
                    'noReset' : 'true'}
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(8)


    def test_deposit(self):
        Login(self.driver).login(acc,pwd)
        deposit.deposit(self.driver).deposit_one_hundred_dollars(money)

    def test_withdrawl(self):
        Login(self.driver).login(acc, pwd)
        withDraw.withDraw(self.driver).withdraw(fpwd,money)


    def test_bet(self):
        Login(self.driver).login(acc, pwd)
        Bet.bet(self.driver).bet()



    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main()
