"""xpath实战案例之爬取58同城二手房房源信息标题"""
"""2023.8 58采用了http2传输，本代码仍需修改"""
from lxml import etree
import requests

# import httpx

url = 'https://nn.58.com/ershoufang/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0'
}
page_text = requests.get(url=url, headers=headers).text
# client=httpx.Client(http2=True)
# page_text=httpx.get(url=url,headers=headers).text

# 数据解析
tree = etree.HTML(page_text)
div_list = tree.xpath('//section[@class="list"]/div')
with open('./58.txt', 'w', encoding='utf-8') as f:
    for div in div_list:
        title = div.xpath('.//div[@class="property-content-title"]/h3/text()')
        print(title)
        f.write(title + '\n')

# li_list=tree.xpath('//div[@class=property-content-title]/h3/text()')
