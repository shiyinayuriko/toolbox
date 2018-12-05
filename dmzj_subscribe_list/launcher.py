import requests
from bs4 import BeautifulSoup


session = requests.Session()

payload = {"nickname": "*", "password": "*", "token": "*", "type": 0}
session.post("https://i.dmzj.com/doLogin", data=payload, verify=False)


with open('./out.txt', "w", encoding="utf8") as f:

    page = 1
    while page < 8:
        payload = {'page': page, "type_id": 4, "letter_id": 0, "read_id": 1}
        r = session.post("https://i.dmzj.com/ajax/my/subscribe", data=payload, verify=False)

        soup = BeautifulSoup(r.text)
        for div in soup.findAll("div", "dy_content_li"):
            # print(div.img.attrs["src"], div.h3.a.get_text(), div.h3.a.attrs["href"], sep='\t')
            # print(div.img.attrs["src"])
            # print(div.h3.a.get_text())
            # print(div.h3.a.attrs["href"])
            line = '\t'.join([div.img.attrs["src"], div.h3.a.get_text(), div.h3.a.attrs["href"]])
            # print(line)
            f.write(line + '\n')
            
        page += 1
