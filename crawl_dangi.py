from bs4 import BeautifulSoup
from selenium import webdriver
import requests

# Pull number of full page
url = "https://finance.naver.com/sise/theme.nhn?&page=1"
html_doc = requests.get(url)
html_doc = html_doc.text
soup = BeautifulSoup(html_doc,"html.parser")
tags = soup.select("table.Nnavi a")
page_num = len(tags) - 1 # number of pages

# url by pages
for i in range(page_num):
    link = "https://finance.naver.com/sise/theme.nhn?&page=" + str(i+1)

    # url by atag in a page
    html_doc = requests.get(link)
    html_doc = html_doc.text
    soup = BeautifulSoup(html_doc,"html.parser")
    tags = soup.select("table.theme td.col_type1 a")
    for j in tags:
        link = "https://finance.naver.com/" + j.attrs['href']

        #url by atag in a thema
        html_doc = requests.get(link)
        html_doc = html_doc.text
        soup = BeautifulSoup(html_doc,"html.parser")
        tags = soup.select("table.type_5 .name_area a")
        for k in tags:
            # k tag has company name >>>>>>>>>>>>>
            link = k.attrs['href']

            # 재무재표 url
            code = link.split("=")[1]
            link = "https://navercomp.wisereport.co.kr/v2/company/c1030001.aspx?cmp_cd=" + code + "&cn="
            

            # 당기순이익 +- 정보 추출
            html_doc = requests.get(link)
            # html_doc = html_doc.text
            # soup = BeautifulSoup(html_doc,"html.parser")
            # tbs = soup.select(".clear")

            browser = webdriver.Chrome('./webdriver_84/chromedriver')
            browser.get(link)
            soup = BeautifulSoup(browser.page_source, "html.parser")
            tbs = soup.select("table .txt")
            print(tbs)
            # print(tbs)
            # for n in tbs:
                # if n.text == '당기순이익':
                # print(type(n.title()))
                # if  == "당기순이익":
                #     tbs.parent.
                #     break    
            ## .lvl1 .txt 의 title == '당기순이익'
            
        
        
