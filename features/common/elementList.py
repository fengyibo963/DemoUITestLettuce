# -*- coding: utf-8 -*-
from lettuce import *
from selenium.webdriver.common.by import By


# 将被测系统元素写入一个元素列表,用于随时提取使用，因此被测系统的元素名称要保持独立性
@step(u'获取被测系统元素列表')
def element_list(step):
    element = {}
    element[u'浏览器私密链接_高级按钮'] = (By.ID, 'details-button')
    element[u'浏览器私密链接_继续访问按钮'] = (By.ID, 'proceed-link')
    element[u'首页_搜索输入框'] = (By.ID, 'twotabsearchtextbox')
    element[u'首页_搜索按钮'] = (By.XPATH, '//*[@id="nav-search"]/form/div[2]/div/input')
    element[u'商品列表页面_下一页按钮'] = (By.XPATH, '//*[text()="下一页"]')
    element[u'商品详情页面_加入购物车按钮'] = (By.ID, 'add-to-cart-button')
    element[u'商品详情页面_配送区域选择框'] = (By.ID, 'ddmSelectedAddressText')
    element[u'商品详情页面_配送区域(省份)选择框'] = (By.ID, 'ddmStateTriggerId')
    element[u'商品详情页面_配送区域(城市)选择框'] = (By.ID, 'ddmCityTriggerId')
    element[u'商品详情页面_配送区域(区/县)选择框'] = (By.ID, 'ddmDistrictTriggerId')
    element[u'商品详情页面_现货情况'] = (By.XPATH, '//*[@id="ddmAvailabilityMessage"]/span')
    element[u'商品加入购物车成功页面_加入结果'] = (By.ID, 'huc-v2-order-row-confirm-text')
    element[u'商品加入购物车成功页面_购物车金额'] = (By.XPATH, '//*[@id="hlb-subcart"]/div[1]/span/span[2]')
    world.element = element


# @step('我获取被测系统元素列表')
# def element_list(step):
#     element = {}
#     element['首页'] = {
#         "搜索输入框": (By.ID, 'twotabsearchtextbox'),
#         "搜索按钮": (By.XPATH, '//*[@id="nav-search"]/form/div[2]/div/input'),
#     }
#     element['商品列表页面'] = {
#         "下一页按钮": (By.XPATH, '//*[text()="下一页"]')
#     }
#     element['商品详情页面'] = {
#         "加入购物车按钮": (By.ID, 'add-to-cart-button'),
#         "配送区域选择框": (By.ID, 'ddmSelectedAddressText'),
#         "配送区域(省份)选择框": (By.ID, 'ddmStateTriggerId'),
#         "配送区域(城市)选择框": (By.ID, 'ddmCityTriggerId'),
#         "配送区域(区/县)选择框": (By.ID, 'ddmDistrictTriggerId'),
#         "现货情况": (By.XPATH, '//*[@id="ddmAvailabilityMessage"]/span')
#     }
#     element['商品加入购物车成功页面'] = {
#         "加入结果": (By.ID, 'huc-v2-order-row-confirm-text'),
#         "购物车金额": (By.XPATH, '//*[@id="hlb-subcart"]/div[1]/span/span[2]')
#     }
#     world.element = element
