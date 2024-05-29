#requests实战之简易网页采集器
import requests
#UA（User-Agent）伪装
headers={
    'User-Agent':'浏览器标识，f12查看'
}
url='https://www.baidu.com/web'

#处理url携带的参数，存在字典中
kw=input('请输入：')
param={
    'query':kw
}
#发送请求
response=requests.get(url=url,params=param,headers=headers)

page_text=response.text
filterName=kw+'.html'
with open(filterName,'w',encoding='utf=8') as f:
    f.write(page_text)

print(filterName,'保存成功！')

