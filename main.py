#main.py

import urllib.request
import urllib.parse
import urllib.error


#urlopen(url,data,timeout...)
#Request(url,data,headers,method...)
#url="http://python.org"
url="https://movie.douban.com/"
headers={
    "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0",
    "Host":"movie.douban.com"
}
req=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(req)
print(response.status)
html=response.read().decode('utf8')
#print(html)
choose='''<body>.*?<.*?wrapper.*?>.*?content.*?>.*?<.*?list-wp.*?>.*?<.*?slider-wrapper.*?>.*?slide-page.*?data-index="(/d)">.*?<p>(.*?).*?<strong>(.*?)</strong>'''
pattern=re.compile(choose)
results=re.findall(pattern,html)
for result in results:
    print(result)







