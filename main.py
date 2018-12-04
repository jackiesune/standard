#main.py
import re
import urllib.request
import urllib.parse
import urllib.error
import json

#urlopen(url,data,timeout...)
#Request(url,data,headers,method...)
#url="http://python.org"
url="https://movie.douban.com/chart"
headers={
    "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0",
    "Host":"movie.douban.com"
}
def get_page():
    req=urllib.request.Request(url=url,headers=headers)
    response=urllib.request.urlopen(req)
#print(response.status)
    html=response.read().decode('utf8')
#print(html)
    return html
def parse_page(html):
    choose='''<table.*?item.*?valign.*?<div.*?>.*?<a.*?>(.*?)</a>.*?<p.*?pl.*?>(.*?)</p>.*?<span.*?rating_nums.*?>(.*?)</span>'''
    pattern=re.compile(choose,re.S)
    results=re.findall(pattern,html)
    patternp=re.compile('<span.*?>|</span>')
    patterna=re.compile('<a.*?>(.*?)<span>(.*?)</span></a>')

    for result in results:
        temp1=re.sub(' |\n','',result[0])
        fina=re.sub(patternp,'',temp1)
#        print(result)
        yield{
            'title':fina,
            'actors':result[1],
            'rating':result[2]
        }


def write_tofile(content):
    with open('热门.txt','a',encoding='utf-8') as f:
#        print(type(json.dumps(content)))
        f.write(json.dumps(content,ensure_ascii=False)+'\n')

def main ():
    html=get_page()
    for item in parse_page(html):
        print(item)
        write_tofile(item)

main()



