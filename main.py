import os
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

hub = os.getenv("SELENIUM_HUB")
def check_browser(browser):
  driver = webdriver.Remote(
    command_executor=f"http://{hub}:4444/wd/hub",
    desired_capabilities=getattr(DesiredCapabilities, browser)
  )
  driver.get("http://google.com")
  assert "google" in driver.page_source
  print("asserting .....")
  time.sleep(15)
  driver.quit()
  print("Browser %s checks out!" % browser)


#check_browser("FIREFOX")
check_browser("CHROME")
