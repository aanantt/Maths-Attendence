import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
import platform

print("-----------❤️ HAR HAR MAHADEV ❤----------️")
time.sleep(2)
# DOWNLOAD GECKODRIVER FROM HERE https://github.com/mozilla/geckodriver/releases
driver = webdriver.Firefox(executable_path="GECKODRIVER_PATH")
driver.get('http://gmail.com')
emailElem = driver.find_element_by_id('identifierId')
emailElem.send_keys('YOUR_EMAIL_ADDRESS')
nextButton = driver.find_element_by_id('identifierNext')
nextButton.click()
time.sleep(10)
passwordElem = driver.find_element_by_xpath(
    '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
passwordElem.send_keys('YOUR_EMAIL_PASSWORD')
signinButton = driver.find_element_by_id('passwordNext')
signinButton.click()
wait = WebDriverWait(driver, 600)
wait.until(EC.presence_of_element_located(
    (By.XPATH, "/html/body/div[7]/div[3]/div/div[1]/div[3]/header/div[2]/div[1]/div[4]/div/a/img")))
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get("GOOGLE_FORM_LINK")
while 1:
    try:
        nextButton = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        nextButton.click()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div').click()
        break

    except:
        time.sleep(20)
        driver.refresh()
time.sleep(5)
driver.close()
if platform.system() == 'Linux':
    shutdown_str = 'shutdown -t 1'
else:
    shutdown_str = 'shutdown -s -t 1'
os.system(shutdown_str)
