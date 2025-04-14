import json
from DrissionPage import Chromium
from DrissionPage import ChromiumOptions
from DrissionPage.common import Settings
import pyautogui
import time
import requests
from datetime import datetime, timezone, timedelta
import pytz
import tzlocal
import cv2
import numpy as np
from cnocr import CnOcr
from cityline import *

# purchaseUrl = 'https://event.cityline.com/utsvInternet/internet/eventDetail?event=53742'

# edgePath = '/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge'
chromePath = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
coption = ChromiumOptions().set_browser_path(chromePath)
coption.save()
Settings.set_language('zh_cn')

chromium = Chromium(addr_or_opts=coption)
# 启动或接管浏览器，并获取标签页对象
tab = chromium.latest_tab

# tab.ele('.modal-footer').ele('.btn-login').click()
# exit(0)



citylineMgr = CitylineMgr()
citylineMgr.requestUtsvEventList()
citylineMgr.requestEventList()
allIsSalingEvents = citylineMgr.event_list.getAllEventInSaling()
if len(allIsSalingEvents) == 0:
    print('没有活动正在售卖中')
    exit(0)

print('有活动正在售卖中')
for event in allIsSalingEvents:
    print('正在售卖中 : ', event.eventId(), event.siteType(), event.saleStartTime())

purchaseUrl = citylineMgr.requestRealPurchaseUrl(allIsSalingEvents[1])

# 跳转到登录页面
tab.get(purchaseUrl)

# 获取屏幕的宽度和高度
screen_width, screen_height = pyautogui.size()
# 打印屏幕的宽度和高度
print(f"屏幕宽度: {screen_width}, 屏幕高度: {screen_height}")


def clickLoginBtn():
    eleNavBar = tab.ele('.navbar')
    if eleNavBar:
        loginBtns = eleNavBar.eles('登入')
        for loginBtn in loginBtns:
            print('loginBtn: ', loginBtn.html)
            try:
                loginBtn.click()
            except Exception as e:
                print('Error: ', e)
    else:
        raise ValueError('没有找到 navbar 元素')
    
    #passCloudFlare()

# if tab.ele('.memberName purplelink'):
#     print('已经登录')
# else:
#     print('没有登录, 点击登录按钮')
#     clickLoginBtn()
#     passCloudFlare()

tab.scroll.to_see('.btn btn-outline-primary purchase-btn')
purchaseBtn = tab.ele('.btn btn-outline-primary purchase-btn')
time.sleep(1)
purchaseBtn.click()

# 这个函数是用来找到 cloudFlare 的根 div 的位置
def waitCloudFlareRootDiv(venueTab, locator, timeoutS=10):
    start_time = time.time()
    div = venueTab.ele(locator)
    while True:
        if (time.time() - start_time) > timeoutS:
            print('超时了')
            return None
        try:
            if not div:
                div = venueTab.ele(locator)
            a = div.rect.screen_location
            break
        except Exception as e:
            print('Error: ', e)
            # 等待 0.1 秒
            time.sleep(0.1)
            continue
        
    return div

# 等待登录按钮可用
# 点了 cloudflare 的 checkbox 之后，登录按钮才会可用
# 这个函数是用来等待登录按钮可用的
def waitLoginBtnEnable(venueTab, locator, timeoutS=10):
    btn = venueTab.ele(locator)
    start_time = time.time()
    while True:
        if (time.time() - start_time) > timeoutS:
            print('超时了')
            return None
        try:
            if not btn:
                btn = venueTab.ele(locator)
            # 如果按钮是可用的，就返回这个按钮
            if btn.states.is_enabled():
                break
        except Exception as e:
            print('Error: ', e)
        # 等待 0.1 秒
        time.sleep(0.1)
        
    return btn

# 在我的电脑上，屏幕坐标都是乘了 2
# 所以这里需要除以 2，其他电脑可能是 1
CONFIG_SCREEN_SCALE = 2
def element_screen_rect(element):
    # 获取元素的屏幕坐标
    px, py = element.rect.screen_location
    # 获取元素的大小
    width, height = element.rect.size
    # 返回一个元组 (x, y, width, height)
    return (px/CONFIG_SCREEN_SCALE, py/CONFIG_SCREEN_SCALE, width, height)

# 两种截图方式
# 1. 使用 pyautogui 截图, 优点：截图的是真实屏幕图像不会对网页有任何影响，缺点：速度慢，且需要依赖元素的位置，且会被其他窗口遮挡
# 2. 使用 DrissionPage 截图，优点：速度快，且可以直接获取元素的截图，缺点：截图的图像是网页渲染后的图像，会有闪屏，可能会对网页有影响并检测到
# 返回值是一个 numpy 数组
def element_screenshot(element, use_pyautogui=False):
    if use_pyautogui:
        # 使用 pyautogui 截图
        px, py, width, height = element_screen_rect(element)
        img = pyautogui.screenshot(region=(int(px), int(py), int(width), int(height)))
        img = np.array(img)
    else:
        # 使用 DrissionPage 截图
        img = element.get_screenshot(as_bytes='jpg')
        img = cv2.imdecode(np.frombuffer(img, np.uint8), cv2.IMREAD_UNCHANGED)
    return img

# 这个函数是用来找到 cloudFlare 的 checkbox 的位置
def find_cloud_flare_checkbox_position(element, timeoutS=-1):
    # 注意 ocr 第一次执行会比较慢，因为要加载模型，所以最好先执行一次 ocr
    ocr = CnOcr()
    
    start_time = time.time()
    # 文字左侧中点的坐标
    text_pos = None
    cloudflare_logo_width = 0
    # 循环截图，一直找到 确认您是真人 这几个字的位置，然后它左边一点的位置就是 checkbox 的位置
    while True:
        # 截图
        img = element_screenshot(element, use_pyautogui=False)
        # 使用 OCR 识别文本
        result = ocr.ocr(img)
        if len(result) > 0:
            for item in result:
                # item[0] 是文本，item[1] 是位置
                text = item.get('text', '')
                pos = item.get('position', None)
                print('识别到的文本: ', text)
                print('识别到的文本位置: ', pos)
                # 如果识别到的文本中有 确认您是真人，就返回这个位置
                if (('确认您是真人' in text) or 'you are human' in text or '您是人類' in text) and pos is not None:
                    text_pos = ( pos[0][0], (pos[0][1]+pos[3][1]) / 2)
                    print('找到 checkbox 的位置: ', text_pos)
                    
                if ('CLOUDFLARE' in text or 'cloudflare' in text):
                    # 计算 logo 的宽度
                    cloudflare_logo_width = pos[1][0] - pos[0][0]
                    print('找到 cloudflare 的 logo 的位置: ', pos)
                    
        # 如果找到了，就退出循环
        if text_pos is not None:
            break
        # 如果超时了，就退出循环
        # 这里的 timeout_ms 是毫秒，所以要除以 1000
        if (timeoutS > 0) and (time.time() - start_time > timeoutS):
            print('超时了')
            break
        # 等待 0.1 秒，避免过于频繁的截图
        time.sleep(0.1)
    if text_pos is None:
        return None
    
    px, py, width, height = element_screen_rect(element)
    px = px + text_pos[0]/CONFIG_SCREEN_SCALE
    py = py + text_pos[1]/CONFIG_SCREEN_SCALE
    offset_x = cloudflare_logo_width / CONFIG_SCREEN_SCALE / 4
    px = px - offset_x 
    return (px, py)

cloudFlareRootDiv = waitCloudFlareRootDiv(tab, '.modal-content h-100')
print('cloudFlareRootDiv rect: ', cloudFlareRootDiv.rect.screen_midpoint, cloudFlareRootDiv.rect.screen_location)

checkbox_pos = find_cloud_flare_checkbox_position(cloudFlareRootDiv)

if checkbox_pos is not None:
    print('找到 checkbox 的位置: ', checkbox_pos)
    # 移动鼠标到 checkbox 的位置
    pyautogui.moveTo(checkbox_pos[0], checkbox_pos[1], duration=0.1)
    pyautogui.click()
    pyautogui.click()
    
    btnDiv = tab.ele('.modal-footer')
    print('btndiv: ', btnDiv.html)
    loginBtn = btnDiv.ele('.btn-login')
    print('loginBtn: ', loginBtn.html)
    while ('disabled="disabled"' in loginBtn.html):
        print('登录按钮不可用，等待 1 秒')
        time.sleep(0.1)
        loginBtn = btnDiv.ele('.btn-login')
        print('loginBtn: ', loginBtn.html)
    # loginBtn = waitLoginBtnEnable(btnDiv, '.btn-login')
    loginBtn.click()
else:
    print('没有找到 checkbox 的位置')
