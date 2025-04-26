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
config_monitor_name = 'G-DRAGON'

chromium = Chromium(addr_or_opts=coption)
# 启动或接管浏览器，并获取标签页对象
# tab = chromium.latest_tab

citylineMgr = CitylineMgr()
citylineMgr.requestAllEvent()
allIsSalingEvents = citylineMgr.event_list.getAllEventInSaling('shows')
if len(allIsSalingEvents) == 0:
    print('没有活动正在售卖中')
    exit(0)

print('有活动正在售卖中')
for event in allIsSalingEvents:
    print('正在售卖中 : ', event.event_data)

purchaseUrl = citylineMgr.requestRealPurchaseUrl(allIsSalingEvents[0])
if purchaseUrl is None:
    print('没有获取到购买页链接')
    exit(-1)

print('open purchaseUrl = ', purchaseUrl)
# 跳转到第一个购买页面
# 可能出现以下几种情况
# 1. 正常情况，直接打开了购买页面
# 2. 弹出登录框，登录账号（这种情况不考虑，因为我们需要先登录账号，保证浏览器有登录的 session 在）
# 3. 出现排队的情况，这种情况我们还没有处理，不知道是等待排队完成，还是不断刷新，不过排队完成后会自动进入到购买页面
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