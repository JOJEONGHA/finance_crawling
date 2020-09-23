from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time

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
        print("< " + j.text + " >") # 테마명 출력
        link = "https://finance.naver.com/" + j.attrs['href']

        #url by atag in a thema
        html_doc = requests.get(link)
        html_doc = html_doc.text
        soup = BeautifulSoup(html_doc,"html.parser")
        tags = soup.select("table.type_5 .name_area a")

        # One event >>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        for k in tags:
            # k tag has company name >>>>>>>>>>>>>
            link = k.attrs['href']
            # 재무재표 url
            code = link.split("=")[1]
            link = "https://navercomp.wisereport.co.kr/v2/company/c1030001.aspx?cmp_cd=" + code + "&cn="
            link_test = "https://navercomp.wisereport.co.kr/v2/company/c1010001.aspx?cmp_cd=" + code + "&cn="

            # 당기순이익 +- 정보 추출
            browser = webdriver.Chrome('./webdriver_84/chromedriver')
            browser.get(link_test)
            ybtn = browser.find_element_by_css_selector('#cns_Tab21') # 연간
            qbtn = browser.find_element_by_css_selector('#cns_Tab22') # 분기
            qbtn.click()

            # #TDdCYnFkT0 .gHead01 tbody tr
            soup = BeautifulSoup(browser.page_source, "html.parser")
            ni = soup.select("#TDdCYnFkT0 .gHead01 tbody tr")
            # print(">>>>>>>>>>>>>>")
            print(type(ni))
            print(ni)
            for n in ni:
                # print(">>>>>>>>>>>>>>")
                # print(type(n))
                tag = n.select(".txt")
                # print(type(tag))
                # print(tag)
                # if tag[0].text == "당기순이익":
                #     tag = n.select(".num")
                #     nums = ""
                #     for m in range(5):
                #         num = tag[m].text
                #         num = num.replace(",","")
                #         if float(num) < 0:
                #             break
                #         nums = nums + " " + num
                #         # break 되지않고 마지막 항목을 통과한다면 단기순이익은 모두 양수라는 뜻이다.
                #         if m == 4: 
                #             print("종목이름 : " + k.text) # 종목이름
                #             print("당기순이익 : " + nums) # 당기순이익 5년치
                #     break



            # browser.get(link)
            # soup = BeautifulSoup(browser.page_source, "html.parser")
            # ni = soup.select(".lvl1")
            # for n in ni:
            #     tag = n.select(".txt")
            #     if tag[0].attrs['title'] == "당기순이익":
            #         tag = n.select(".num")
            #         nums = ""
            #         for m in range(5):
            #             num = tag[m].text
            #             num = num.replace(",","")
            #             if float(num) < 0:
            #                 break
            #             nums = nums + " " + num
            #             # break 되지않고 마지막 항목을 통과한다면 단기순이익은 모두 양수라는 뜻이다.
            #             if m == 4: 
            #                 print("종목이름 : " + k.text) # 종목이름
            #                 print("당기순이익 : " + nums) # 당기순이익 5년치
            #         break

# 1년치 분기별 당기순이익 흑적자 유무에 따라 출력
# CB,BW 유무에 따라 출력
# 시가총액 출력

# print가 아닌 메모장 파일로 저장
          
            
        
        
