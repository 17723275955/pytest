# # frequency_code={'QD':'1',"BID":"2","TID":'3','QOD':'4','BIW':'5','Q6H':'6','Q4H':'7','QW':'8','ST':'9','PRN':'10','Q8H':'11','Q12H':'12','QN':'13','QID':'17'}
# # import random
# # # re=['QD',"BID","TID",'QOD','BIW','Q6H','Q4H','QW','ST','PRN','Q8H','Q12H','QN','QID']
# # # s=random.choice(re)
# # # print(s,frequency_code[f'{s}'])
# #
# #
# # supply_name={'口服':'1',"静滴":'2','静推':'3','肌注':'4','外用':'5','雾化':'6','直肠给药':'8','微泵':'10','皮下注射':'11','滴眼':'12','皮内注射':'14','腹腔滴注':'16','吸入':'17','喷入':'18',
# #              '局封':'28','治疗':'32','冲管用':'42','灌肠':'49','局部浸润':'56','覆膜透析':'61'
# #                                                                                                                                                      }
# #
# # rs=['口服',"静滴",'静推','肌注','外用','雾化','直肠给药','微泵','皮下注射','滴眼','皮内注射','腹腔滴注','吸入','喷入','局封','治疗','冲管用','灌肠','局部浸润','覆膜透析']
# # s1=random.choice(rs)
# # print(s1,supply_name[f'{s1}'])
#
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# import time
# import   win32gui,win32con
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# class login():
#     def __init__(self):
#         self.dr=webdriver.Chrome()
#         self.dr.maximize_window()
#         self.dr.implicitly_wait(1)
#     def logi(self):
#         url="http://192.168.1.125:8874/login"
#         self.dr.get(url)
#         self.dr.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div/form/div/div[1]/div[1]/div/div[1]/input').send_keys('huangyu-护理部')
#         self.dr.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div/form/div/div[1]/div[2]/div/div/input').send_keys('123456')
#         self.dr.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div/form/div/div[2]/div/button').click()
#         self.dr.find_element_by_xpath('//*[@id="app"]/div/div[3]/section/div/div[1]/div[1]/div[2]/div/div[2]/div[1]/div[2]').click()
#         self.dr.find_element_by_xpath('//*[@id="app"]/div/div[3]/section/div/div[3]/div/div/section/div[2]/div[1]').click()
#         self.dr.find_element_by_xpath('//*[@id="navMenu"]/li[4]').click()
#         self.dr.find_element_by_xpath('//*[@id="app"]/div/div[3]/section/div/div[1]/form/div[3]/div/button[3]/span').click()
#
#
#         # self.dr.find_element_by_xpath('//*[@id="app"]/div/div[3]/section/div/div[2]/div[3]/div[2]/div/div[2]/div/div[2]/form/div[1]/div/div/input').send_keys('110')
#         # self.dr.find_element_by_xpath('//*[@id="app"]/div/div[3]/section/div/div[2]/div[3]/div[2]/div/div[2]/div/div[2]/form/div[2]/div/div/input').send_keys('黄宇')
#         # self.dr.find_element_by_xpath('//*[@id="app"]/div/div[3]/section/div/div[2]/div[3]/div[2]/div/div[2]/div/div[2]/form/div[3]/div/div/div[1]/input').click()
#         # self.dr.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[1]').click()
#         # # Select(se).select_by_index(1)
#         # self.dr.find_element_by_xpath('//*[@id="app"]/div/div[3]/section/div/div[2]/div[3]/div[2]/div/div[2]/div/div[2]/form/div[4]/div/div/div/input').click()  #选择职称
#         # se=self.dr.find_element_by_css_selector('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(4)').click()
#         # self.dr.find_element_by_xpath('//*[@id="app"]/div/div[3]/section/div/div[2]/div[3]/div[2]/div/div[2]/div/div[2]/form/div[5]/div/div/div[1]/input').click()
#         # self.dr.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[3]').click()
#         # self.dr.find_element_by_xpath('//*[@id="app"]/div/div[3]/section/div/div[2]/div[3]/div[2]/div/div[2]/div/div[2]/form/div[6]/div/div/div/input').click()
#         # self.dr.find_element_by_xpath('/html/body/div[5]/div[1]/div[1]/ul/li[1]').click()
#         # self.dr.find_element_by_xpath('//*[@id="app"]/div/div[3]/section/div/div[2]/div[3]/div[2]/div/div[2]/div/div[2]/form/div[8]/div/div/div/div[1]/input').click()
#         # self.dr.find_element_by_xpath('/html/body/div[6]/div[1]/div[1]/ul/li[1]/span').click()
#         # self.dr.find_element_by_xpath('//*[@id="app"]/div/div[3]/section/div/div[2]/div[3]/div[2]/div/div[2]/div/div[2]/form/div[9]/div/div/textarea').send_keys('你好')
#         #
#         self.dr.find_element_by_xpath('//*[@id="app"]/div/div[3]/section/div/div[2]/div[3]/div[2]/div/div[2]/div/div[1]/div[2]/div/div/button').click()
#         # self.dr.find_element_by_xpath('//*[@id="app"]/div/div[3]/section/div/div[2]/div[3]/div[2]/div/div[3]/div/button[2]/span').click()
#         # http://192.168.1.125:9010/minio-ward-test/202305/5d04d056-8d23-4b88-ae38-1c88e91bc7f611a9174e1e632b3aa08499806a358b1.jpg
#
#         self.dr.find_element_by_xpath('//*[@id="app"]/div/div[3]/section/div/div[2]/div[3]/div[2]/div/div[3]/div/button[2]/span').send_keys(Keys.CONTROL,'V')
#         self.dr.find_element_by_xpath('//*[@id="app"]/div/div[3]/section/div/div[2]/div[3]/div[2]/div/div[3]/div/button[2]/span').send_keys(Keys.ENTER)
#
#         time.sleep(3)
#
#
#         self.dr.quit()
#
#
# login().logi()

# import random
#
# order_class1={'a':"西药,中成药",'b':"暂无",'c':"检查",'d':"检验",'e':"治疗",'f':'手术','i':'膳食'}
# order_class = ['a', 'b', 'c', 'd', 'e', 'f', 'i']
# s2=random.choice(order_class)
# print(s2,order_class1[f'{s2}'])

from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
#
api = NinjaAPI()


@api.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]

