#main.py
#import http.cookiejar
#from urllib.request import HTTPCookieProcessor,build_opener
#import urllib.request
import http.cookiejar,urllib.request
from urllib.request import HTTPCookieProcessor,build_opener


url="http://www.baidu.com"
def not_file():
    cookie=http.cookiejar.CookieJar()
    handler=urllib.request.HTTPCookieProcessor(cookie)
    opener=urllib.request.build_opener(handler)
    response=opener.open(url)
    for item in cookie:
        print(item.name+':'+item.value)


def mozilla_cookie():
    filename='cookieMozilla'
    cookie=http.cookiejar.MozillaCookieJar(filename)
    handler=HTTPCookieProcessor(cookie)
    opener=build_opener(handler)
    response=opener.open(url)
    cookie.save(ignore_discard=True,ignore_expires=True)


def LWP_cookie():
    filename='cookieLWP'
    cookie=http.cookiejar.LWPCookieJar(filename)
    handler=HTTPCookieProcessor(cookie)
    opener=build_opener(handler)
    response=opener.open(url)
    cookie.save(ignore_discard=True,ignore_expires=True)



def load_LWP_cookie():
    filename='cookieLWP'
    cookie=http.cookiejar.CookieJar()
    cookie.load(filename,ignore_discard=True,ignore_expires=True)
    handler=HTTPCookieProcessor(cookie)
    opener=build_opener(handler)
    response=opener.open(url)
    print(response.read().decode('utf8'))



          
          
          
def main():


    order=input("which would you want to run:not_file(n),mozilla(m),LWP_cookie(l),load(o)")
    if order=='n':not_file()
    if order=='m':mozilla_cookie()
    if order=='l':LWP_cookie()
    if order=='o':load_LWP_cookie()
        


main()

