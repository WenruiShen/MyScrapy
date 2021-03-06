#!/usr/bin/python3
#coding=utf-8

##############################################
#
# Author:       Shen Wenrui
# Date:         20180518
# Description:
#
##############################################


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import time

from .AppleIdRegisterXpath import appleIdRegisterXpath

import logging
logger = logging.getLogger("appleIdRegister")

class appleIdEmailAuthOpt():
    def __init__(self, appleIdRegisterBrowser):
        self.__xpath = appleIdRegisterXpath()
        self.__appleIdRegisterBrowser = appleIdRegisterBrowser

    def __submitEmailAuthCode(self):
        return True

    def __inputOneNumber(self, index, num):
        try:
            emailAuthCodeXpathInput = self.__xpath.getEmailAuthCodeXpathInput(index)
            authCodeInputElement = self.__appleIdRegisterBrowser.find_element_by_xpath(emailAuthCodeXpathInput)
            authCodeInputElement.clear()
            authCodeInputElement.send_keys(num)
        except Exception as err:
            logger.error("__inputOneNumber Failed: " + repr(err))
            return None

    def __inputCode(self, emailAuthCode):
        index = 0
        for num in list(emailAuthCode):
            index = index + 1
            self.__inputOneNumber(index, num)

    def __submitAuthCode(self):
        try:
            submitEmailAuthCodeXpathButtonOk = self.__xpath.getSubmitEmailAuthCodeXpathButtonOk()
            self.__appleIdRegisterBrowser.find_element_by_xpath(submitEmailAuthCodeXpathButtonOk).click()

            # Explicitly wait.
            WebDriverWait(self.__appleIdRegisterBrowser, 10, 0.5).until(
                EC.presence_of_element_located((By.XPATH, self.__xpath.getTempEmailAddrXpath()))
            )
            return True
        except Exception as err:
            logger.error("__submitAuthCode Failed: " + repr(err))
            return False

    def inputEmailAuthCode(self, emailAuthCode = "123456"):
        try:
            self.__inputCode(emailAuthCode)
            time.sleep(2)
            return self.__submitAuthCode()
        except Exception as err:
            logger.error("InputEmailAuthCode Failed: " + repr(err))
            return False

    def emailAuthCodeListener(self, emailAuthCodeQueue):
        try:
            # 阻塞等待2min
            emailAuthCode = emailAuthCodeQueue.get(timeout=120.0)
            logger.info("Queue receive emailAuthCode: " + emailAuthCode)
            # 正则校验
            if not re.match(r'\d{3,6}', emailAuthCode):
                return None
            return emailAuthCode
        except Exception as err:
            logger.error("emailAuthCodeListener Failed: " + repr(err))
            return None