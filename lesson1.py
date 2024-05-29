"""通用爬虫-requests简单使用"""
# 指定url
# 发起请求
# 获取响应数据
# （存储本地）


#爬取百度首页html源代码
import requests
#1.指定url
url="https://www.baidu.com/"
#2.发起请求
response=requests.get(url=url)
#3.获取响应，text返回的是字符串形式的响应数据
page_text=response.text
print(page_text)

#存储数据
with open('./baudu.html','w',encoding='utf-8') as f:
    f.write(page_text)

print("爬取完成！")