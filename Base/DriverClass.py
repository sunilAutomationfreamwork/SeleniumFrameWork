from selenium import webdriver
import Utilities.CustomLogger as cl
class webDriverclass:
    log=cl.customLogger()
    def get_WebDriver(self,browserName):
        driver=None
        if browserName=="chrome":
            driver=webdriver.Chrome()
            self.log.info("Chrome browser launched")
        elif browserName == "edge":
            driver = webdriver.Edge()
            self.log.info("edge browser launched")
        elif browserName == "firefox":
            driver = webdriver.Firefox()
            self.log.info("firefox browser launched")
        return driver
