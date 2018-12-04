#main.py

import urllib.request
import urllib.parse
import urllib.error


#urlopen(url,data,timeout...)
#Request(url,data,headers,method...)
url="http://python.org"
headers={
    "User-Agent":""
}
req=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(req)
print(response.status)
