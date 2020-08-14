from bs4 import BeautifulSoup
import requests

# 부모에서 자식의 값 추출
html_doc = """
            <body>
                <div class = "pr">
                    <div class = "txt">안녕</div>
                    <div class = "num">11</div>
                    <div class = "num">12</div>
                    <div class = "num">13</div>
                    <div class = "num">14</div>
                </div>
                <div class = "pr">
                    <div class = "txt">하쇼</div>
                    <div class = "num">21</div>
                    <div class = "num">22</div>
                    <div class = "num">23</div>
                    <div class = "num">24</div>
                </div>
            </body>
            """

soup = BeautifulSoup(html_doc,"html.parser")
tags = soup.select("div.pr .txt")
for i in tags:
    # print(i.text)
    if i.text == "하쇼":
        txt = i.parent.find_all(class_='num')
        for j in txt:
            print(type(int(j.text)))
            ## navigablestring to int

    
        



        
        
