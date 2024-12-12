import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://github.com/')
time.sleep(3)
driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/header/div/div[2]/div/div/div/a').click()
driver.find_element(By.XPATH, '//*[@id="login_field"]').send_keys('')
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('')
driver.find_element(By.XPATH, '//*[@id="login"]/div[4]/form/div/input[13]').click()
time.sleep(3)

driver.find_element(By.XPATH, '//*[@id="global-create-menu-anchor"]/span').click()
driver.find_element(By.XPATH, '//*[@id=":r7:--label"]').click()


time.sleep(3)


driver.execute_script("window.scrollBy(0, 600)")
time.sleep(5)
driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/main/react-app/div/form/div[5]/button/span').click()
time.sleep(3)

