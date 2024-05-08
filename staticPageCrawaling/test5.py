from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

options = Options()

options.add_argument('--start-maximized')
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)

url = 'https://www.naver.com'

driver.get(url)
time.sleep(3)
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
time.sleep(2)

query.send_keys(Keys.ENTER)
time.sleep(2)

driver.save_screenshot('naver_인공지능.png')

driver.quit()



