from selenium import webdriver

from bs4 import BeautifulSoup

chrome_driver = webdriver.Chrome()

import requests

url = "http://www.9966dy.com"
chrome_driver.get(url)

# 找到对应按钮

button_obj = chrome_driver.find_element_by_xpath('//*[@id="nav_menu"]/div/ul/a[4]')

# 点击对应按钮
button_obj.click()

# 创建soup对象

soup = BeautifulSoup(chrome_driver.page_source,"lxml")

# 找到ul标签

ul = soup.find("ul",attrs={"class":"list_tab_img","id":"vod_list"})

# 找所有的img标签

img = ul.find_all("img",attrs={"class":"loading"})

for i in img:
    # 获取图片链接
    img_url = url+i["xsrc"]

    # 请求图片地址
    res = requests.get(img_url)

    # 判断图片地址是否正常连通
    if res.status_code==200:
        # 保存图片
        with open("./save_img/"+i["alt"]+".jpg","wb") as file:
            file.write(res.content)

