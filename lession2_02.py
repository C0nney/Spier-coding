import requests
from lxml import etree

url = 'http://m.ranwen.com.cn/html/47/47200/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0'
}

page_text = requests.get(url=url, headers=headers).text

tree = etree.HTML(page_text)
dd_list = tree.xpath('//div[@class="books"]/div[5]/dl/dd')

with open('./books.txt', 'w', encoding='utf-8') as f:
    for dd in dd_list:
        src = 'http://m.zzxsw.com' + dd.xpath('./a/@href')[0]
        # print(src)
        # break
        title = dd.xpath('./a/text()')[0]
        detail_text = requests.get(url=src, headers=headers).text
        newtree = etree.HTML(detail_text)
        chapter = newtree.xpath('//div[@id="chaptercontent"]//text()')
        if chapter:
            chapter_text = '\n'.join([text.strip() for text in chapter if text.strip()])
        f.write(title + ':' + chapter_text + '\n')
        print(chapter_text)
        # break
print('爬取成功！')

# http: // m.zzxsw.com / html / 47 / 47200 / 27796687.html
