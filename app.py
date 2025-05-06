import json
from DrissionPage import Chromium
from DrissionPage import ChromiumOptions
from DrissionPage.common import Settings
from cityline import *
from cloudflare_bypasser import *

browserPath = 'c:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe'
#chromePath = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
coption = ChromiumOptions().set_browser_path(browserPath)
coption.save()
Settings.set_language('zh_cn')

# 要抢的张数, 默认强最贵的
config_ticket_num = 5
# TODO 监控的活动名称
config_monitor_name = 'G-DRAGON'

chromium = Chromium(addr_or_opts=coption)
# 启动或接管浏览器，并获取标签页对象
# tab = chromium.latest_tab

sw, sh = pyautogui.size()
print(f'屏幕分辨率: {sw}x{sh}')

# modalContent = tab.ele('.modal-content h-100')
# print('rect.size: ', modalContent.rect.size)
# print('rect.location: ', modalContent.rect.location)
# print('rect.screen_location: ', modalContent.rect.screen_location)
# print('rect.screen_midpoint: ', modalContent.rect.screen_midpoint)

# pyautogui.moveTo(modalContent.rect.screen_location[0], modalContent.rect.screen_location[1], duration=2)
# exit(0)

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