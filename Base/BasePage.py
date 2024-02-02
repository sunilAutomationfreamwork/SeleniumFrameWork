from traceback import print_stack

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


import Utilities.CustomLogger as cl

class BaseClass:
    log = cl.customLogger()
    def __init__(self,driver):
        self.driver= driver

    def launchwebpage(self,url,title):
        try:
            self.driver.get(url)
            assert title in self.driver.title
            self.log.info("web page launched with url:"+ url)
        except:
            self.log.info("web page not launched with url:" + url)
            print_stack()
    def getlocatorType(self,locatorType):
        locatorType=locatorType.lower()
        if locatorType=="id":
            return By.ID
        elif locatorType=="name":
            return By.NAME
        elif locatorType=="class":
            return By.CLASS_NAME
        elif locatorType=="xpath":
            return By.XPATH
        elif locatorType=="css":
            return By.CSS_SELECTOR
        elif locatorType=="link":
            return By.LINK_TEXT
        elif locatorType=="plink":
            return By.PARTIAL_LINK_TEXT
        else:
            self.log.error("locator type"+locatorType+"entered not found")

        return False
    def getWebElement(self,locatorValue,locatorType="id"):
        webElement=None
        try:
            locatorType=locatorType.lower()
            locatorByType=self.getlocatorType(locatorType)
            webElement=self.driver.find_element(locatorByType,locatorValue)
            self.log.info("webElement found with locator value"+locatorValue+"using loactorType"+locatorType)
        except:
            self.log.error("webElement not found with locator value"+locatorValue+"using loactorType"+locatorType)
            print_stack()
        return webElement
    def waitForElement(self,locatorValue,locatorType="id"):
        webElement=None
        try:
            locatorType=locatorType.lower()
            locatorByType=self.getlocatorType(locatorType)
            wait=WebDriverWait(self.driver,25)
            webElement=wait.until(ec.presence_of_element_located((locatorByType,locatorValue)))
            self.log.info("webElement found with locator value"+locatorValue+"using loactorType"+locatorType)
        except:
            self.log.error("webElement not found with locator value"+locatorValue+"using loactorType"+locatorType)
            print_stack()
        return webElement

    def clickElement(self,locatorValue,locatorType="id"):
        webElement=None
        try:
            locatorType=locatorType.lower()
            webElement=self.waitForElement(locatorValue,locatorType)
            webElement.click()
            self.log.info("clicked on webElement with loactor value"+locatorValue+"using locatortype"+locatorType)
        except:
            self.log.error("clicked on webElement with loactor value"+locatorValue+"using locatortype"+locatorType)
            print_stack()

    def sendKeys(self,txt,locatorValue,locatorType="id"):
        webElement=None
        try:
            locatorType=locatorType.lower()
            webElement=self.waitForElement(locatorValue,locatorType)
            webElement.send_keys(txt)
            self.log.info("entered txt ")
        except:
            self.log.error("text not entered")
            print_stack()
    def getText(self,locatorValue,locatorType="id"):
        elementText=None
        try:
            locatorType=locatorType.lower()
            webElement=self.waitForElement(locatorValue,locatorType)
            elementText=webElement.text
            self.log.info("Got the text")
        except:
            self.log.error("Unable to get text")
            print_stack()
        return elementText
    def isElementDisplayed(self,locatorValue,locatorType="id"):
        elementDisplayed=None
        try:
            locatorType=locatorType.lower()
            webElement=self.waitForElement(locatorValue,locatorType)
            elementDisplayed=webElement.is_displayed()
            self.log.info("element displayed")
        except:
            self.log.error("Element not displayed")
            print_stack()
        return elementDisplayed

    def scrollTo(self,locatorValue,locatorType="id"):
        actions=ActionChains(self.driver)
        try:
            locatorType=locatorType.lower()
            webElement=self.waitForElement(locatorValue,locatorType)
            actions.move_to_element(webElement).perform()
            self.log.info("scrolled to webelement")
        except:
            self.log.error("Unable to scroll")
            print_stack()



