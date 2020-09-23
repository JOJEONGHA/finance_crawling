from bs4 import BeautifulSoup
from selenium import webdriver
import requests



# https://navercomp.wisereport.co.kr/v2/company/c1010001.aspx?cmp_cd=006090&cn=
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(chrome_options=options)

browser.get("https://navercomp.wisereport.co.kr/v2/company/c1010001.aspx?cmp_cd=006090&cn=")
ybtn = browser.find_element_by_css_selector('#cns_Tab21') # 연간
qbtn = browser.find_element_by_css_selector('#cns_Tab22') # 분기

qbtn.click()
        



        
        
