#爬取豆瓣电影榜单（不翻页）
import requests
import  json

url='https://movie.douban.com/j/chart/top_list'
param={
    'type':'24',
    'interval_id':'100:90',
    'start':'1', #从库中第几部电影开始取
    'limit':'20' #一次取出几部

}
headers={
    'User-Agent':''
}

response=requests.get(url=url,params=param,headers=headers)

list_data=response.json()

f=open('./douban.com','w',encoding='utf=8')
json.dump(list_data,fp=f,ensure_ascii=False)
print('over')