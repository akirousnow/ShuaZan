# -*- coding: cp936 -*-
import requests,re,execjs,json,js2py
proxies = { 
           }
url = 'http://ds.slu8.cn/'
res = requests.get(url,proxies=proxies)
sec_defend = re.findall("\'sec_defend\',(.*?)\);", res.text)[0]
sec_defend = js2py.eval_js( 'function $(name) {return eval(name)}' )(sec_defend)
header = {'Cookie':'sec_defend='+sec_defend,'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'}
req = requests.get(url,headers=header,proxies=proxies)
hashsalt =re.findall('var hashsalt=(.*);', req.text)[0]
hashsalt = js2py.eval_js( 'function $(name) {return eval(name)}' )(hashsalt)
cookie=dict(req.cookies)
header={
'Cookie':'PHPSESSID='+cookie['PHPSESSID']+';mysid='+cookie['mysid']+';sec_defend='+sec_defend
    }
print "输入你的qq号:"
SBQQ = raw_input();
data={'tid':655,
'inputvalue':str(SBQQ),
'num':1,
'hashsalt':hashsalt
      }
rea = requests.post('http://ds.slu8.cn/ajax.php?act=pay',data=data,headers=header,proxies=proxies)
print rea.text
orderid= json.loads(rea.text)['trade_no']

rea = requests.get('http://ds.slu8.cn/other/submit.php?type=qqpay&orderid='+str(orderid),proxies=proxies)
print rea.text
