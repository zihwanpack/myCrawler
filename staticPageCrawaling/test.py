import requests
from bs4 import BeautifulSoup

response = requests.get('https://startcoding.pythonanywhere.com/basic')

# 문자열 형태라 원하는 정보를 추출하기 힘들다.
# 따라서 beautifulsoup의 도움을 받아야함

html = response.text
soup = BeautifulSoup(html, 'html.parser')
# 원하는 태그에 class나 id가 없을 때 부모태그에서 접근하기 attrs로 속성 접근
# dictionary 형태라 아래처럼 접근하면 href값 찾기 가능하다.
# print(soup.select_one('.product-name > a').attrs['href'])

print(soup.select_one('.product-price').text.strip().replace(',', '').replace('원', ''))