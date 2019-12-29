import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.com/Sony-Mirrorless-Digital-Camera-28-70mm/dp/B00PX8CNCM/ref=sxin_0_ac_d_pm?ac_md=6-0-VW5kZXIgJDEsMjAw-ac_d_pm&keywords=sony+a7&pd_rd_i=B00PX8CNCM&pd_rd_r=2bd66d1f-23b8-4414-b8d1-15a3858ddda8&pd_rd_w=xF7aq&pd_rd_wg=CPWQa&pf_rd_p=709d2064-e546-4799-9e66-b352ea89951f&pf_rd_r=RKNSDW8VNMKPVH6QAQ2Y&psc=1&qid=1577606451'

headers = { "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0'}
page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')
newSoup = BeautifulSoup(soup.prettify(), 'html.parser')

title = newSoup.find(id="productTitle").get_text()
price = newSoup.find(id="priceblock_saleprice").get_text()
print(price)