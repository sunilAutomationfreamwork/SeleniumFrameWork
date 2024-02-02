from Base.DriverClass import webDriverclass
from selenium import webdriver
import time
import Utilities.CustomLogger as cl
from Base.BasePage import BaseClass
wd=webDriverclass()
driver=wd.get_WebDriver('chrome')
bp=BaseClass(driver)
bp.launchwebpage("http://dummypoint.com/seleniumtemplate.html","Selenium Template — DummyPoint")
bp.scrollTo("//input[@id='submitbutton']","xpath")
time.sleep(5)
driver.quit


