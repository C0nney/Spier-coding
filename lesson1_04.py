#爬取药监局化妆品企业信息
import requests
import json
#经过分析发现，列表页和详情页都经过ajax动态传输。列表页可以获取不同公司的id，得到id后获取详情数据

"""先获取列表页"""
url=''
#还需要完成具体细节和分页操作（循环）
data={

}
headers={
    'User-Agent':''
}
data_list=requests.post(url=url,data=data,headers=headers).json()
#分析列表页json发现，字典内嵌列表，列表内嵌多个字典（公司）
#通过for循环取出字典中的id，另存在列表id_list中，方便后面使用
id_list=[]
for id in data_list['']:
    id_list.append(dic[''])

"""获取详情页"""
all_datail=[]
post_url=''
for id in id_list:
    data={
        'id':id
    }
    datail=requests.post(url=post_url,data=data,headers=headers).json()
    all_datail.append(detail)

#存储到本地
with open('./allData.json','w',encoding='utf-8') as f:
    json.dump(all_datail,fp=f,ensure_ascii=False)

print('over!')