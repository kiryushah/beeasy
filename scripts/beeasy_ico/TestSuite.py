# -*- coding: utf-8 -*-
import Login, kyc, ChangePassword, click_to_all, InvestBTC, InvestETH, SignUp
import unittest
import sys
import HTMLTestRunner
from datetime import date
import os.path

IcoTestSuite = unittest.TestSuite()
IcoTestSuite.addTest(unittest.makeSuite(Login.LogIn))
IcoTestSuite.addTest(unittest.makeSuite(ChangePassword.ChangePassword))
IcoTestSuite.addTest(unittest.makeSuite(click_to_all.ClcikToAll))
IcoTestSuite.addTest(unittest.makeSuite(InvestBTC.InvestBTC))
IcoTestSuite.addTest(unittest.makeSuite(InvestETH.InvestEth))
IcoTestSuite.addTest(unittest.makeSuite(SignUp.SignUp))
IcoTestSuite.addTest(unittest.makeSuite(kyc.Kyc))


now = date.today()

filename = str(now)+"-" +"Report.html"

outfile = open(os.path.join('/home/kiryushah/PycharmProjects/crypto/reports',filename), "w")
runner = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='Test Report',
                description='This demonstrates the report output.'
                )


runner.run(IcoTestSuite)


