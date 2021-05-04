import urllib.request
import urllib.parse
import json
from io import BytesIO
import gzip

url = "https://www.google-analytics.com/collect?v=1&_v=j90&aip=1&a=777777723&t=pageview&_s=10&dl=https%3A%2F%2Fwww.virustotal.com%2Fgui%2F&dp=%2Fgui%2Fsearch%2Fhttps%25253A%25252F%25252Fwww.onlinedown.net%25252Fnew%25252F&ul=zh-cn&de=UTF-8&dt=VirusTotal&sd=24-bit&sr=1536x864&vp=1519x724&je=0&_u=aADAAEABAAAAAC~&jid=&gjid=&cid=1790469519.1616678334&tid=UA-27433547-2&_gid=1198063172.1620099012&cd1=free&z=1183760587"
data = {}
data['v'] = 1
data['_v'] = 'j90'
data['aip'] = 1
data['a'] = 777777723
data['t'] = 'pageview'
data['_s'] = 10
data['dl'] = 'https://www.virustotal.com/gui/'
data['dp'] = '/gui/search/https%253A%252F%252Fwww.onlinedown.net%252Fnew%252F'
data['ul'] = 'zh-cn'
data['de'] = 'UTF-8'
data['dt'] = 'VirusTotal'
data['sd'] = '24-bit'
data['sr'] = '1536x864'
data['vp'] = '1519x724'
data['je'] = 0
data['_u'] = 'aADAAEABAAAAAC~'
data['jid'] = 692299083
data['gjid'] = 344990479
data['cid'] = '1790469519.1616678334'
data['tid'] = 'UA-27433547-2'
data['_gid'] = '1198063172.1620099012'
data['_r'] = 1
data['cd1'] = 'free'
data['z'] = '1183760587'

head = {}
head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.2261 SLBChan/30'

data = urllib.parse.urlencode(data).encode('utf8')

req = urllib.request.Request(url,data,head)
response = urllib.request.urlopen(req)
html = response.read()
buff = BytesIO(html)
f = gzip.GzipFile(fileobj=buff)
html = f.read().decode('utf-8')
print(html)
"""a = json.loads(html)
print(a)"""
"""result = a['content']['out']
print(result)"""