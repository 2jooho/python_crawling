
import pandas as pd
import requests
import openpyxl
from bs4 import BeautifulSoup
wb = openpyxl.Workbook()
sheet1 = wb.active
sheet1.title = '수집 데이터'
for page in range(3):
    resp = requests.get('https://search.naver.com/search.naver?where=post&sm=tab_jum&query=%EA%B3%A0%ED%98%88%EC%95%95%EC%97%90+%EB%82%98%EC%81%9C+%EC%9D%8C%EC%8B%9D&start='+ str(page * 10 + 1), headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(resp.text, 'html.parser')
    titles = soup.select('.type01 > li')  # 타이틀(제목)을 가지고 있는 클래스 명

    for title in titles:
        results=title.select_one('.sh_blog_passage').text
        print(results)
        sheet1.append([results])

wb.save('test2.xlsx')
