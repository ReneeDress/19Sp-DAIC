import requests
import re
import pandas as pd

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
# 户型-房间	户型-厅	户型-厨房	户型-卫生	建筑面积	朝向	装修	电梯	总楼层	所处层数	建筑类型	建筑结构	小区	经度	纬度	地址	建筑时间	价格（万）
xlsx = pd.ExcelFile('housePrice.xlsx')
df = pd.read_excel(xlsx, 'Sheet1', index_col=0)
writer = pd.ExcelWriter('housePrice.xlsx')
print(df)
a = 1
for number in link:
    print(a, number)
    # number = '107101038917'
    url = "https://sh.lianjia.com/ershoufang/" + number + '.html'
    response = requests.get(url)
    if response:
        house = re.findall('<span class="label">房屋户型</span>(.*?)</li>', response.text)
        bed = re.findall('(.*?)室', house[0])[0]
        living = re.findall('室(.*?)厅', house[0])[0]
        kitchen = re.findall('厅(.*?)厨', house[0])[0]
        bath = re.findall('厨(.*?)卫', house[0])[0]
        space = re.findall('<span class="label">建筑面积</span>(.*?)㎡</li>', response.text)[0]
        direction = re.findall('<span class="label">房屋朝向</span>(.*?)</li>', response.text)[0]
        decoration = re.findall('<span class="label">装修情况</span>(.*?)</li>', response.text)[0]
        if re.findall('<span class="label">配备电梯</span>(.*?)</li>', response.text) != []:
            lift = re.findall('<span class="label">配备电梯</span>(.*?)</li>', response.text)[0]
        else:
            continue
        height = re.findall('<span class="label">所在楼层</span>(.*?)</li>', response.text)[0]
        whole = re.findall('(.*?)楼层', height)[0]
        level = re.findall('共(.*?)层', height)[0]
        type = re.findall('<span class="label">建筑类型</span>(.*?)</li>', response.text)[0]
        rate = re.findall('<span class="label">梯户比例</span>(.*?)</li>', response.text)[0]
        estatewhole = re.findall('<a href="(.*?)" target="_blank" class="info ">(.*?)</a><a href="#around" class="map">地图</a>', response.text)[0]
        estatehref = 'https://sh.lianjia.com' + estatewhole[0]
        estate = estatewhole[1]
        position = re.findall('resblockPosition:\'(.*?)\'', response.text)
        position = re.split(',', position[0])
        longitude = position[0]
        latitude  = position[1]
        price = re.findall('<span class="total">(.*?)</span>', response.text)[0]
        response = requests.get(estatehref)
        if re.findall('<div class="detailDesc">\(松江松江大学城\)(.*?)</div></div>', response.text) != []:
            address = re.findall('<div class="detailDesc">\(松江松江大学城\)(.*?)</div></div>', response.text)[0]
        else:
            continue
        if re.findall('<div class="xiaoquInfoItem"><span class="xiaoquInfoLabel">建筑年代</span><span class="xiaoquInfoContent">(.*?)年建成 </span></div>', response.text) != []:
            time = re.findall('<div class="xiaoquInfoItem"><span class="xiaoquInfoLabel">建筑年代</span><span class="xiaoquInfoContent">(.*?)年建成 </span></div>', response.text)[0]
        else:
            continue
        # print(bed, living, kitchen, bath, space, direction, decoration, lift, whole, level, type, rate, estate, longitude, latitude, address, time, price)
        # df2 = pd.DataFrame([bed, living, kitchen, bath, space, direction, decoration, lift, whole, level, type, rate, estate, longitude, latitude, address, time, price], columns=list('AB'))
        row = [bed, living, kitchen, bath, space, direction, decoration, lift, level, whole, type, rate, estate, longitude, latitude, address, time, price]
        # df = df.append(row, ignore_index=True)
        df.loc[a+1] = row
        print(df)
        df.to_excel(writer, sheet_name='Sheet1', startcol=0, index=True)
        df.to_csv('Result.csv')
        a += 1

print(df)
writer = pd.ExcelWriter('housePrice.xlsx')
df.to_excel(writer, sheet_name='Sheet1', startcol=0, index=True)