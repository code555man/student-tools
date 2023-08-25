# Python Version 3.7.9
# selenium 4.10.0
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
service = Service(executable_path="chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(service=service, options=options)
browser.get('http://reg.sskru.ac.th/informservice/prn_group1.php') 
find_study_group = browser.find_elements(By.TAG_NAME,"a")
link_study_group_list = []
for tag_a in find_study_group:
    s = tag_a.text
    if s.startswith("60",0,2):
        link_study_group_list.append(tag_a.get_attribute("href"))
    else:
        pass
for link_std in link_study_group_list:
    browser.get(link_std)
    find_std_id = browser.find_elements(By.XPATH,"/html/body/center/table/tbody/tr[4]/td/table[1]/tbody/tr")
    time.sleep(1)
    list_student = []
    for i in find_std_id:
        list_student.append(i.text)    
    with open("std_id.txt","a") as f:
        for std in list_student:
            if "รหัสประจำตัว" in std:
                pass
            else:
                f.write(std.split(" ")[1])
                f.write("\n")
            print(std)
