import requests, pprint, json
from bs4 import BeautifulSoup

url = "" # url target

with requests.session() as session:

    data = {
            'idno' : "6412732113",
            'idpass' : "1348600003933",
            'page': 1,
            'Submit' : '++%E0%B9%80%E0%B8%82%E0%B9%89%E0%B8%B2%E0%B8%AA%E0%B8%B9%E0%B9%88%E0%B8%A3%E0%B8%B0%E0%B8%9A%E0%B8%9A++'
        }
    
    
    response = session.post(url,data=data)



    # assessment

    if response:

        url2 = "http://reg.sskru.ac.th/student/accsskru/assessment_t.php?term=2/2565&subjcode=Z2dmZWdnbF"

        data2 = {
            'ACQ1' : '5',
            'ACQ2' : '5',
            'ACQ3' : '5',
            'ACQ4' : '5',
            'ACQ5' : '5',
            'ACQ6' : '5',
            'ACQ7' : '5',
            'ACQ8' : '5', 
            'ACQ9' : '5',
            'ACQ10' : '5',
            'ACQ12' : '5',
            'ACQ13' : '5',
            'ACQ14' : '5',
            'ACQ15' : '5',
            'ACQ16' : '5',
            'ACQ17' : '5',
            'ACQ18' : '5',
            'ACQ19' : '5',
            'ACQ20' : '5',
            'ACQ21' : '5',
            'ACQ22' : '5',
            'ACMT2': '',
            'idno' : "6412732113",
            'term' : '2%2F2565',
            'subjcode' : '1521102',
            'msubmit' : '%E0%B8%9A%E0%B8%B1%E0%B8%99%E0%B8%97%E0%B8%B6%E0%B8%81%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%A1%E0%B8%B9%E0%B8%A5'
        }

        asm = session.post(url2,headers=headers,data=data2)

        with open('index.html','w') as f:

            f.write(asm.text)