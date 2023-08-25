# Python Version 3.7.9
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.service import Service
from time import sleep
from os import system

service = Service(executable_path="chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(service=service, options=options)

# url login

with open('std_id.txt',"r") as f:
    read_std_id = f.readlines()  
std_id_list = [line[:-1] for line in read_std_id]

passwd = ""

for std_id in std_id_list:

    browser.get('')
    browser.find_element(By.ID,"id_no").send_keys(std_id)

    browser.find_element(By.ID,"bdate").send_keys(passwd)

    browser.find_element(By.NAME,"Submit").click()
   

    img = browser.find_element(By.XPATH,'/html/body/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr[1]/td[5]/img')

    with open('std_mail.txt','a') as f:
        f.write(f'stu{std_id}@sskru.ac.th:{img.get_attribute("src")[36:-4]}\n')
        print(std_id)


