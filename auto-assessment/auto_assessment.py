
# Python Version 3.7.9
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.service import Service
from time import sleep
from os import system
import sys

#  Color
W = "\033[0m"     # white
R = '\033[31;1m'  # red
G = '\033[32;1m'  # green
B = '\033[34m'    # blue
O = '\033[93m'    # orange

logo = G + '''

 █████╗ ██╗   ██╗████████╗ ██████╗      █████╗ ███████╗███████╗███████╗███████╗███████╗███╗   ███╗███████╗███╗   ██╗████████╗
██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗    ██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝██╔════╝████╗ ████║██╔════╝████╗  ██║╚══██╔══╝
███████║██║   ██║   ██║   ██║   ██║    ███████║███████╗███████╗█████╗  ███████╗███████╗██╔████╔██║█████╗  ██╔██╗ ██║   ██║   
██╔══██║██║   ██║   ██║   ██║   ██║    ██╔══██║╚════██║╚════██║██╔══╝  ╚════██║╚════██║██║╚██╔╝██║██╔══╝  ██║╚██╗██║   ██║   
██║  ██║╚██████╔╝   ██║   ╚██████╔╝    ██║  ██║███████║███████║███████╗███████║███████║██║ ╚═╝ ██║███████╗██║ ╚████║   ██║   
╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚══════╝╚══════╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝   
                                                                                    ''' + R + '''source : https://github.com/code555man''' + O +'''

ระดับ                 ความพึงพอใจ
---------  ------------------------------------

[1]        มากที่สุด
[2]        มาก
[3]        ปานกลาง
[4]        น้อย
[5]        น้อยที่สุด

'''

def flush_text(text,color,timer_delay=0.01):
    for info in list(text):
        print(color + info, end="",flush=True)
        sleep(timer_delay)

def auto_assessment():

    try:
        system("cls")
        print(logo)
        print(f"{G}[+] โปรแกรมประเมินอาจารย์ประจำรายวิชา")
        print(f"{G}[+] ไม่เกิน 2 นาที สำหรับคนขี้เกียจ")
        print(f"{G}[+] หมายเหตุ: เมนูระดับความพึงพอใจที่เลือกจะนำไปใช้กับรายวิชาทั้งหมด\n")

        std_id = input("[?] รหัสนักศึกษา : ")
        passwd = input("[?] รหัสผ่าน : ")
        level = int(input("[?] ระดับความพึงพอใจ : "))

        # auto_assessment(std_id,passwd,level)

        service = Service(executable_path="chromedriver.exe")
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_experimental_option("detach", True)
        browser = webdriver.Chrome(service=service, options=options)

        browser.get('http://reg.sskru.ac.th/student/login.php') # url login

        browser.find_element(By.ID,"id_no").send_keys(std_id)
        sleep(1)

        browser.find_element(By.ID,"bdate").send_keys(passwd)
        sleep(1)

        browser.find_element(By.NAME,"Submit").click()
        sleep(2)

        try:
            alert = Alert(browser)
            alert.accept()
            sleep(2)

            find_subject = browser.find_elements(By.TAG_NAME,"a")
            find_std_id = browser.find_element(By.XPATH,"/html/body/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr[1]/td[2]/font/b")
            find_name = browser.find_element(By.XPATH,"/html/body/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr[1]/td[5]/font/b")
            link_subject_list = []

            for link in find_subject:
                get_att_href = link.get_attribute("href")
                if len(get_att_href) > 70:
                    link_subject_list.append(get_att_href)
                else:
                    pass

            print(f"{G}\n========== [+] รหัสนักศึกษา: {O}{find_std_id.text}{G} ชื่อ: {O}{find_name.text}{G} ===========\n")

            # list form assessment
            tag_tr_index = ["4","5","7","9","10","11","13","14","16","17","19","20","23","24","25","26","27","28","29","30","31","32"] # ลำดับข้อแบบประเมิน อ้างอิง Xpath 

            for link_subject in link_subject_list: 
                browser.get(link_subject)
                title = browser.find_element(By.XPATH,"/html/body/div/table/tbody/tr/td/form/table/tbody/tr[2]/td")
                print(f"{B}[{R}+{B}] {title.text}")
                sleep(1)
                for index in tag_tr_index:
                    browser.find_element(By.XPATH,f"/html/body/div/table/tbody/tr/td/form/table/tbody/tr[{index}]/td[3]/select").click()
                    # sleep(0.5)
                    browser.find_element(By.XPATH,f"/html/body/div/table/tbody/tr/td/form/table/tbody/tr[{index}]/td[3]/select/option[{str(level+1)}]").click()
                    # sleep(0.5)
                browser.find_element(By.NAME,"msubmit").click()
                sleep(1)
            flush_text("\n[✓] ทำแบบประเมินสำเร็จ",G)
            menu = input(f"{O}[?] เรียกใช้งานโปรแกรมอีกครั้ง (y) ออกจากโปรแกรม (ctrl + c) : ")

        except:
            find_std_id = browser.find_element(By.XPATH,"/html/body/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr[1]/td[2]/font/b")
            find_name = browser.find_element(By.XPATH,"/html/body/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr[1]/td[5]/font/b")
            print(f"{G}\n========== [+] รหัสนักศึกษา: {O}{find_std_id.text}{G} ชื่อ: {O}{find_name.text}{G} ===========\n")
            flush_text("[!] ไม่มีรายวิชาที่รอการประเมิน\n",R)
            menu = input(f"{O}[?] เรียกใช้งานโปรแกรมอีกครั้ง (y) ออกจากโปรแกรม (ctrl + c) : ")
    except:
        flush_text(f"\n[!] ล็อคอินไม่สำเร็จ ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง [{std_id}:{passwd}]\n",R)
        menu = input(f"{O}[?] เรียกใช้งานโปรแกรมอีกครั้ง (y) ออกจากโปรแกรม (ctrl + c) : ")
        
    if menu in ["Y","y"]:
        system("cls")
        auto_assessment()

if __name__ == '__main__':
    auto_assessment()
    
    
