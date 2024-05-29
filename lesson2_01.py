"""正则实战案例"""
# 爬取糗图百科中的图片
import requests
import re
import os

# 先普通爬虫，将整个网页爬取下来
url = ''
headers = {
    'User-Agent': ''
}
page_text = requests.get(url=url, headers=headers).text
# 再用聚焦爬虫爬取图片
ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'  # 正则 ()中是想要的
img_list = re.findall(ex, page_text, re.S)  # 表示正则作用于page_text中

if not os.path.exists('./qiutulibs'):
    os.mkdir('./qiutulibs')  # 创建文件夹，方便存储图片

for src in img_list:
    src = 'https://' + src  # 拼接出完整的url

    img_data = requests.get(url=src, headers=headers).content  # 保存二进制数据用.content
    img_name = src.split('/')[-1]  # 用/切割图片路径名，以最后一块作为图片的文件名
    imgPath = './qiutulibs' + img_name  # 图片路径
    with open(imgPath, 'wb') as f:
        f.write(img_data)
        print("下载成功")
print("over!!!")
