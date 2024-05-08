import requests
from bs4 import BeautifulSoup
import pandas as pd

data = []

for i in range(1, 5) :
  response = requests.get(f'https://startcoding.pythonanywhere.com/basic?page={i}')
  html = response.text
  soup = BeautifulSoup(html, 'html.parser')
  items = soup.select('.product')
  for item in items :
    category = item.select_one('.product-category').text
    name = item.select_one('.product-name').text
    link = item.select_one('.product-name > a').attrs['href']
    price = item.select_one('.product-price').text.split('원')[0].replace(',', '')
    print(category, name, link, price)
    data.append([category, name, link, price])
# pandas 데이터 프레임 만들기
df = pd.DataFrame(data, columns=['카테고리', '상품명', '링크', '가격'])

# 엑셀 저장
df.to_excel('result.xlsx', index=False)