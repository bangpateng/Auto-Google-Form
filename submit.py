import pandas as pd
from selenium import webdriver
import time

def fill_form():
    data = pd.read_csv('data.csv')
    recycle = data.shape[0]
    for i in range(recycle):
        print(i)
        driver = webdriver.Chrome(executable_path='TEMPAT_WEBDRIVER_YANG_KALIAN_SIMPAN')
        driver.get('LINK_GOOGLE_FORM')
        time.sleep(1)

        name = data.iloc[i]['name']
        inputName = driver.find_element("xpath",'MASUKAN_DATA_XPATH')
        for j in name:
            inputName.send_keys(j)
            time.sleep(0.05)

        email = data.iloc[i]['email']
        inputEmail = driver.find_element("xpath",'MASUKAN_DATA_XPATH')
        for j in email:
            inputEmail.send_keys(j)
            time.sleep(0.05)

        address = data.iloc[i]['address']
        inputAddress = driver.find_element("xpath",'MASUKAN_DATA_XPATH'))
        for j in address:
            inputAddress.send_keys(j)
            time.sleep(0.05)

        submit = driver.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
        submit.click()
        time.sleep(0.5)

        backForm = driver.find_element("xpath",'/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        backForm.click()
        time.sleep(1)

fill_form()
time.sleep(1)
