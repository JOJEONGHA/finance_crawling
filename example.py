from bs4 import BeautifulSoup
import requests

url = "https://finance.naver.com/"
html_doc = requests.get(url)
html_doc = html_doc.text
soup = BeautifulSoup(html_doc,"html.parser")

tags = soup.select(".aside_area.aside_stock .tbl_home tbody th > a")
for i in range(len(tags)):
    print(i)
    print("\n")
    print(tags[i].text)

