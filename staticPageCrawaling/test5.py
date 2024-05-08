import os
os.system('pip install --upgrade selenium')

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import random

options = Options()

options.add_experimental_option("excludeSwitches", ["enable-automation"])

options.add_argument('--start-maximized')
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)
random_sec = random.uniform(3, 5)

url = 'https://www.naver.com'

driver.get(url)
time.sleep(random_sec)
# 1
# query = driver.find_element(By.ID, 'query')
# query.send_keys('인공지능')
# time.sleep(2)

# search_btn = driver.find_element(By.CSS_SELECTOR, '#search-btn')
# search_btn.click()
# time.sleep(2)
# 2
query = driver.find_element(By.ID, 'query')
query.send_keys('인공지능')
time.sleep(random_sec)

query.send_keys(Keys.ENTER)
time.sleep(random_sec)

driver.save_screenshot('naver_인공지능.png')

driver.quit()



