from urllib.request  import HTTPPasswordMgrWithDefaultRealm,HTTPBasicAuthHandler,build_opener
from urllib.request import ProxyHandler
import urllib.error



#user="username"
#password="password"
#url="http://localhost:5000"

#p=HTTPPasswordMgrWithDefaultRealm()
#p.add_password(None,url,user,password)
#handler=HTTPBasicAuthHandler(p)
#opener=bulid_opener(handler)

proxy_handler=ProxyHandler({
    'http':'http:127.0.0.1:9999',
    'https':'https://127.0.0.1:9999'
})
opener=build_opener(proxy_handler)
try:
    response=opener.open(url)
    print(response.read().decode('utf8')
except urllib.error.URLError as e:
          print(e.reason)





