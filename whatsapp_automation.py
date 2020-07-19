from os import system

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

system('pip install Selenium -q -q -q')
system('pip install webdriver-manager --user -q -q -q')

contact = input("\n\nEnter a saved contact name to send a message to:\n")
text = input("\n\nWhat's the message ?\n")

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.delete_all_cookies()
driver.maximize_window()
# Navigating to WhatsApp Web
driver.get("https://web.whatsapp.com")

# Scanning QR Code
# Logged In

# input contact name
inp_css_search = "._3FRCZ.copyable-text.selectable-text"
input_box_search = WebDriverWait(driver, 50).until(
    lambda chrome_driver: driver.find_element_by_css_selector(inp_css_search))
input_box_search.click()
input_box_search.send_keys(contact)

# click on contact
selected_contact = WebDriverWait(driver, 50).until(
    lambda chrome_driver: driver.find_element_by_xpath("//span[@title='" + contact + "']"))
selected_contact.click()

# enter message and send
inp_css = "body.web:nth-child(2) div._347-w._2UMYL.app-wrapper-web.os-win div.h70RQ.two:nth-child(6) " \
          "div._1-iDe.Wu52Z:nth-child(4) div._2WG1s footer._2vJ01:nth-child(7) div._3ee1T._1LkpH.copyable-area " \
          "div._3uMse:nth-child(2) div._2FVVk._2UL8j > div._3FRCZ.copyable-text.selectable-text "
input_box = WebDriverWait(driver, 50).until(lambda driver: driver.find_element_by_css_selector(inp_css))
input_box.send_keys(text + Keys.ENTER)
time.sleep(1)

# open WhatsApp menu
menu_xpath = "//header[@class='_1QUKR']//div[3]//div[1]"
menu = driver.find_element_by_xpath(menu_xpath)
menu.click()
time.sleep(1)

# logout from WhatsApp
logout_css = "body.web:nth-child(2) div._347-w._2UMYL.app-wrapper-web.os-win div.h70RQ.two:nth-child(6) " \
             "div._1-iDe._1xXdX:nth-child(3) div._1KyAW header._1QUKR div._3euVJ div._3All_._3NrAe " \
             "div.PVMjB._4QpsN:nth-child(3) span:nth-child(2) div._2s_eZ._1bC39 ul.I4jbF > " \
             "li._1N-3y.eP_pD._36Osw:nth-child(6) "
logout = driver.find_element_by_css_selector(logout_css)
logout.click()

# close all windows opened by selenium
driver.quit()
