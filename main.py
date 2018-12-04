from urllib.request  import HTTPPasswordMgrWithDefaultRealm,HTTPBasicAuthHandler,build_opener
import urllib.error



user="username"
password="password"
url="http://localhost:5000"

p=HTTPPasswordMgrWithDefaultRealm()
p.add_password(None,url,user,password)
handler=HTTPBasicAuthHandler(p)
opener=bulid_opener(handler)

try:
    response=opener.open(url)
    print(response.read().decode('utf8')
except urllib.error.URLError as e:
          print(e.reason)





