import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait

# -----Install Chromedriver on iOS----
# 1. run command 'brew install chromedriver'
# 2. run command 'which chromedriver' to get the PATH
# 3. replace the path on webdriver.Chrome('your path')

driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get('https://moto.car2db.com/')
wait(driver, 5).until(EC.frame_to_be_available_and_switch_to_it(driver.find_element_by_xpath('//*[@id="interactive"]/section/div/div[1]/iframe')))
carTypeSelect = Select(driver.find_element(By.XPATH, '//*[@id="carType"]'))
carTypeSelect.select_by_visible_text('Motorcycle')
time.sleep(3)
carMakeSelect = Select(driver.find_element(By.NAME, "carMake"))
options = carMakeSelect.options
f = open("motorcycle.txt","w+")
for index in range(1, len(options)-1):
    print(options[index].text)
    carMakeValue = options[index].get_attribute('value')
    carMakeName = options[index].text
    carMakeSelect.select_by_visible_text(carMakeName)
    time.sleep(3)
    carModelSelect = Select(driver.find_element(By.ID, 'carModel'))
    carModelOptions = carModelSelect.options
    for index in range(1, len(carModelOptions)-1):
        jsonf = '{"code":' + carModelOptions[index].get_attribute('value') + ',"name":"' + carModelOptions[index].text  + '","brand":' + carMakeValue + '}'
        f.write("%s\r\n" % jsonf)
f.close()     
driver.close()

 