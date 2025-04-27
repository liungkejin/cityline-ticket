import json
from DrissionPage import Chromium
from DrissionPage import ChromiumOptions
from DrissionPage.common import Settings
from cityline import *
from cloudflare_bypasser import *

# edgePath = '/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge'
chromePath = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
coption = ChromiumOptions().set_browser_path(chromePath)
coption.save()
Settings.set_language('zh_cn')

# 要抢的张数, 默认强最贵的
config_ticket_num = 2
# TODO 监控的活动名称
config_monitor_name = '天色2025'# 'G-DRAGON'

chromium = Chromium(addr_or_opts=coption)
# 启动或接管浏览器，并获取标签页对象
# tab = chromium.latest_tab

citylineMgr = CitylineMgr()
citylineMgr.requestAllEvent()

(findEvent, purchaseUrl) = citylineMgr.monitorEvent(config_monitor_name)
if purchaseUrl is None:
    print('没有获取到购买页链接')
    exit(-1)

tab = chromium.new_tab(purchaseUrl)
## todo 判断当前是否正在排队，如果在排队就不断地刷新页面，直到排队完成

if citylineMgr.processFirstPurchasePage(tab):
    print('第一个页面处理成功')
else:
    print('第一个页面处理失败')
    exit(-1)
    
if citylineMgr.processSecondPurchasePage(tab, config_ticket_num):
    print('第二个页面处理成功')
else:
    print('第二个页面处理失败')
    exit(-1)

print('============= 抢票成功 =============')