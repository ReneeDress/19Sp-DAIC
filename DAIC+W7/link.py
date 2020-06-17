import requests
import re

link = []
url = 'https://sh.lianjia.com/ershoufang/songjiangdaxuecheng/'
response = requests.get(url)
list = re.findall('<a class="" href="https://sh.lianjia.com/ershoufang/(.*?).html" target="_blank"', response.text)
for j in range(0, len(list)):
    link.append(
        re.findall('<a class="" href="https://sh.lianjia.com/ershoufang/(.*?).html" target="_blank"', response.text)[j])
for i in range(2, 17):
    url = 'https://sh.lianjia.com/ershoufang/songjiangdaxuecheng/pg' + str(i) + '/'
    response = requests.get(url)
    list = re.findall('<a class="" href="https://sh.lianjia.com/ershoufang/(.*?).html" target="_blank"', response.text)
    for j in range(0, len(list)):
        link.append(
            re.findall('<a class="" href="https://sh.lianjia.com/ershoufang/(.*?).html" target="_blank"',
                       response.text)[j])

print(link)