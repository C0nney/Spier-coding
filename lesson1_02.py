#requests.post() 百度翻译页面中的翻译栏 - 设计动态获取 ajax
import requests
import json
post_url='https://fanyi.baidu.com/'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0'
}

#post请求参数处理与get一致
word=input('请输入：')
data={
    'kw':word
}
response=requests.post(url=post_url,data=data,headers=headers)
#获取响应数据，json()方法返回的是obj（确认响应数据是json类型才用该方法）
dic_obj=response.json()

filterName=word+'.json'
with open(filterName,'w',encoding='utf-8') as f:
    json.dump(dic_obj,fp=f,ensure_ascii=False)

print('保存成功！')

