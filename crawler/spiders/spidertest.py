# import urllib.request
# response=urllib.request.urlopen('http://www.zhihu.com')
# html=response.read().decode('utf8')
# print(html)




# import requests
# import chardet
# url='https://detail.tmall.com/item.htm?spm=a230r.1.14.6.73c66ec54n4BOO&id=558300490641&cm_id=140105335569ed55e27b&abbucket=1'
# s=requests.session()
# r=s.get(url)
# # r.encoding=chardet.detect(r.content)
# r.encoding='GBK'
# print(r.text)
# print(r.headers)

from selenium import webdriver
from bs4 import BeautifulSoup
service_args=[]
service_args.append('--load-images=no')  ##关闭图片加载
service_args.append('--disk-cache=no')  ##不开启缓存
service_args.append('--ignore-ssl-errors=true') ##忽略https错误

driver = webdriver.PhantomJS(service_args=service_args)
driver.get('https://detail.tmall.com/item.htm?spm=a230r.1.14.6.73c66ec54n4BOO&id=558300490641&cm_id=140105335569ed55e27b&abbucket=1')

print(driver.find_element_by_xpath('/html').text)
driver.get('https://detail.tmall.com/item.htm?id=561209556535&spm=a220o.1000855.0.0.1068f0b0z0e9Ts&spm=a220o.1000855.0.0.1068f0b0z0e9Ts&sku_properties=20509:28383')
print(driver.find_element_by_xpath('/html').text)
driver.get('https://detail.tmall.com/item.htm?spm=a230r.1.14.3.5d47c708fewb0S&id=562003579553&cm_id=140105335569ed55e27b&abbucket=1&sku_properties=10004:653780895;5919063:6536025')
print(driver.find_element_by_xpath('/html').text)
driver.get('https://detail.tmall.com/item.htm?spm=a230r.1.14.28.5d47c708fewb0S&id=561902568813&ns=1&abbucket=1&sku_properties=10004:385316259;5919063:6536025')
print(driver.find_element_by_xpath('/html').text)
driver.get('https://item.taobao.com/item.htm?spm=a230r.1.14.63.5d47c708fewb0S&id=561507585385&ns=1&abbucket=1')
print(driver.find_element_by_xpath('/html').text)
driver.get('https://item.taobao.com/item.htm?spm=a230r.1.14.72.5d47c708fewb0S&id=561561158582&ns=1&abbucket=1')
print(driver.find_element_by_xpath('/html').text)
driver.get('https://item.taobao.com/item.htm?spm=a230r.1.14.109.5d47c708fewb0S&id=561983924158&ns=1&abbucket=1')
print(driver.find_element_by_xpath('/html').text)
driver.get('https://detail.tmall.com/item.htm?spm=a230r.1.14.157.5d47c708fewb0S&id=562011589689&ns=1&abbucket=1&sku_properties=10004:827902415;5919063:6536025')
print(driver.find_element_by_xpath('/html').text)
driver.get('https://item.taobao.com/item.htm?spm=a230r.1.14.212.5d47c708fewb0S&id=545771582035&ns=1&abbucket=1')
print(driver.find_element_by_xpath('/html').text)
driver.get('https://item.taobao.com/item.htm?spm=a230r.1.14.270.5d47c708fewb0S&id=561644727208&ns=1&abbucket=1')
print(driver.find_element_by_xpath('/html').text)
print('finish')