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

from cityline import *

citylineMgr = CitylineMgr()
citylineMgr.requestUtsvEventList()
citylineMgr.requestEventList()
allIsSalingEvents = citylineMgr.event_list.getAllEventInSaling()
if len(allIsSalingEvents) > 0:
    print('有活动正在售卖中')
    for event in allIsSalingEvents:
        print('正在售卖中 : ', event.eventId(), event.siteType(), event.saleStartTime())
    citylineMgr.requestRealPurchaseUrl(allIsSalingEvents[0])
else:
    print('没有活动正在售卖中')
exit(0)


_0x23707d = [
    "multilingual",
    "Completed",
    "/url/",
    "Mins",
    "4OMgaGj",
    "countDownHeaderLabel",
    "href",
    "系統忙碌中，請稍候再試。\nServer is busy, please try again later.",
    "dataLayer",
    "16alHqTm",
    "purchaseLabel",
    "data",
    "log",
    "trim",
    "close",
    "other",
    "presalesuat",
    "563556Qsdtlu",
    "UA-111662758-1",
    "data-soldOut",
    "</span>",
    "#dayText",
    "status",
    "effectiveTo",
    "fail",
    "enableServices",
    "toBeAnnouncedLabel",
    ".json?v=",
    "html",
    "includes",
    "div-gpt-ad-1491149715899-0",
    "onSaleEnd",
    "cookie",
    "engagement",
    "toUTCString",
    "onload",
    "now",
    ".cityline.com",
    "config",
    "cmd",
    "forEach",
    "eventYear",
    "survey error:",
    "pb_survey_time_",
    "<br>",
    "isAgree",
    ".surveyBtn",
    "surveyUrl",
    "GET",
    "appendChild",
    "733117KYGJZI",
    "#minuteText",
    "<button id=\"buyTicketBtn\" class=\"load-button surveyBtn\" onclick=\"getReady();\"><span>",
    "createElement",
    "effectiveFrom",
    "endLabel",
    "presales",
    "onSaleTime",
    "#hour",
    "https://www.googletagmanager.com/gtag/js?id=UA-111662758-1",
    "get",
    "attr",
    "async",
    "toBeAnnounced",
    "replaceAll",
    "css",
    "</div>",
    "floor",
    "replace",
    "loginRequire",
    "40nVJFeh",
    "</br>",
    "length",
    "286289IbevCe",
    "getTime",
    "加入候补名单",
    "Days",
    "user profile error",
    "3057660USiVur",
    "pubads",
    "split",
    "ajax",
    "substring",
    "/240512512/cityline_web_homepage_right_ATF_300x250",
    "to go",
    "margin-top",
    "text",
    "434trAQEc",
    "url",
    "#timeText",
    "parse",
    "searchParams",
    "<span>",
    "replace url error:",
    "type",
    "getTimezoneOffset",
    "load-button",
    ".buyTicketBox",
    "content",
    "<button id=\"buyTicketBtn\" class=\"load-button\" onclick=\"openWaitListPage();\"><span>",
    "height",
    "language",
    "querySelector",
    "464810aFXhGd",
    "src",
    "script",
    "endsWith",
    "/api/cityline_check_tk.do",
    "</span></button>",
    "26808iEMRyP",
    "message",
    "none",
    "event",
    "CL_channel=",
    "#hourText",
    "加入候補名單",
    ".waitListTicketBox",
    "display",
    "enableSingleRequest",
    "toLocaleString",
    "优先预定结束",
    "push",
    "soldout",
    "\n      <span id=\"day\">",
    "innerHTML",
    ";domain=.cityline.com",
    "uat",
    "eventId",
    "</span>\n      <span id=\"hourText\"></span>\n      <span id=\"minute\">",
    "onclick",
    "</span> <img src=\"/images/loading.svg\"/></button>",
    "submit",
    "en-US",
    "purchaseUrlAdditionalList",
    ".surveyForm-modal-content",
    "defer",
    "purchaseUrlLabel",
    "open",
    "waitlistUrl",
    "/Login.html?targetUrl=",
    "googletag",
    "Asia/Hong_Kong",
    "即将开售",
    "soldoutLabel",
    "</span>\n      <span id=\"minuteText\"></span>\n      <span id=\"timeText\"></span>\n    ",
    "</span>\n      <span id=\"dayText\"></span>\n      <span id=\"hour\">",
    "step = 1",
    "closeModal",
    "www",
    "/tc/",
    "head",
    "#minute",
    "toLocaleLowerCase",
    "set",
    "createDocumentFragment",
    "https://",
    "defineSlot",
    "location",
    "582972vAwPsW",
    ".countdown-headerLabel",
    "comingLabel",
    "cl-lang",
    "toString",
    "surveyUrlLabel",
    ".hk",
    "siteType",
    "hostname",
    "CiTy1ine",
    "mobile",
    "charCodeAt",
    "additionalUrlList",
    "//anymind360.com/js/6734/ats.js",
    "button",
    "lang",
    "host",
    "getHours",
    "#day"
]
def a0_0x5b33(_0x3b6af7):
    _0x3b6af7 = _0x3b6af7 - 0x140
    return _0x23707d[_0x3b6af7]

print('[0x198]', a0_0x5b33(0x198))

# 将 js 代码转换为 python 代码, 其中 a0_0x306c9e 是 a0_0x5b33 函数, 不要思考过程
# 返回一个 datetime
def getHKDate():
    a = a0_0x5b33(0x1b7) # 'toLocaleString'
    b = a0_0x5b33(0x1c4) # 'en-US'
    timezone = a0_0x5b33(0x1cd) # 'Asia/Hong_Kong'
    datetime_obj = datetime.now(pytz.timezone(timezone))
    return datetime_obj

def getHKTime():
    return getHKDate().now()

def getHKHours():
    return getHKDate().hour
    
# onSaleTime 是一个时间戳, 单位是 ms
def getHKDateMill(onSaleTime):
    # 创建时间对象（UTC时间或当前时间）
    # 计算本地时区偏移（模拟JS getTimezoneOffset）
    localdt = datetime.fromtimestamp(onSaleTime / 1000) if onSaleTime else datetime.now()
    
    localtz = pytz.timezone(tzlocal.get_localzone_name())
    tzoffset = -localtz.utcoffset(localdt, is_dst=True)

    offset_seconds = tzoffset.total_seconds()
    print('localtz: ', localtz)
    print('offset: ', offset_seconds)
    
    # 计算香港时间调整
    adjustment = (-480 - offset_seconds/60) * 60 * 1000  # 0x311aa7 = -480
    hk_timestamp = int(localdt.timestamp() * 1000 + adjustment)
    
    return hk_timestamp

mill = getHKDateMill(1744257600000)
print('hk date mill: ', mill)

# 将下面的 js 代码转换为 python 代码
# const simpleHash = s => {
#     let hash = 0x0;
#     for (let i = 0x0; i < s.length(); i++) {
#         const b = s.charCodeAt(i);
#         hash = (hash << 0x5) - hash + b,
#         hash &= hash;
#     }
#     return new Uint32Array([hash])[0x0].toString(0x24);
# }
def simpleHash(s):
    hash = 0
    for c in s:
        code = ord(c)
        hash = (hash << 5) - hash + code  # 等价 hash = hash * 31 + code
        hash &= 0xFFFFFFFF  # 强制转换为32位无符号整数
    
    # 处理0的特殊情况
    if hash == 0:
        return '0'
    
    # 转换为36进制字符串（小写字母）
    chars = '0123456789abcdefghijklmnopqrstuvwxyz'
    result = []
    num = hash
    while num > 0:
        num, rem = divmod(num, 36)
        result.append(chars[rem])
    return ''.join(reversed(result))

hash = simpleHash('2023-09-25 10:00:00')
print('hash: ', hash)

def getPurchaseUrl(event):
    saleTime = event.get('onSaleTime')


# 定义一个类来表示活动

    
    
# https://shows.cityline.com/data/event-list.json?v=1744475707000
def getEventList():
    timestamp = str(int(time.time() * 1000))
    url = 'https://shows.cityline.com/data/event-list.json?v=' + timestamp
    result = requests.get(url)
    

# https://www.cityline.com/data/utsvEventList.json?_t=1744456311879
# 从这个链接获取所有的活动
def getUTSVEventList():
    timestamp = str(int(time.time() * 1000))
    result = requests.get('https://www.cityline.com/data/utsvEventList.json?_t=' + timestamp)
    #print(result.text)

    utsvEventList = json.loads(result.text)
    # 遍历所有的活动
    for event in utsvEventList.get('utsvEventList'):
        if event.get('config').get('soldOut') == False:
            print('event: ', event)
                
getEventList()                                          
exit(0)

# edgePath = '/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge'
chromePath = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
coption = ChromiumOptions().set_browser_path(chromePath)
coption.save()
Settings.set_language('zh_cn')

chromium = Chromium(addr_or_opts=coption)
# 启动或接管浏览器，并获取标签页对象
tab = chromium.latest_tab
# 跳转到登录页面
tab.get('https://www.cityline.com/zh_CN/Events.html')

# 获取屏幕的宽度和高度
screen_width, screen_height = pyautogui.size()
# 打印屏幕的宽度和高度
print(f"屏幕宽度: {screen_width}, 屏幕高度: {screen_height}")

def passCloudFlare():
    # 这里会出现 Context Change error
    # 所以这里需要catch错误，并做循环处理
    # 找到 cloudFlare 的最外层 iframe
    checkbox = None
    while (checkbox is None):
        try:
            clCtWidget = tab.ele('#cl-ct-widget')
            # 在 ShadowRoot 中找到 iframe 元素
            cloudFlareFrame = clCtWidget.ele('tag:div').sr('t:iframe')
            #print('cff pos: ', cloudFlareFrame.rect.screen_midpoint, cloudFlareFrame.rect.screen_location)
            # print('cloudFlareFrame: ', cloudFlareFrame.html)
            # 这是最外层的 iframe, 找到他的 body
            cloudFlareBody = cloudFlareFrame.ele('tag:body')
            # print('cloudFlareBody: ', cloudFlareBody.html)
            # body 中有一个 class=cb-lb 的元素
            cloudFlareEle = cloudFlareBody.sr('.cb-lb')
            # print('cloudFlareEle: ', cloudFlareEle.html)
            # 他有一个子元素 <input type=checkbox>，我们需要点击它
            checkbox = cloudFlareEle.ele('tag:input')
            # print('checkbox: ', checkbox.html)
        except Exception as e:
            print('Error: ', e)
            # 等待 1 秒
            time.sleep(1)

    if checkbox is None:
        raise ValueError('没有找到 cloudFlare 的 checkbox')
    # 不知道为什么在我的 mac 上屏幕坐标都乘了 2
    px, py = checkbox.rect.screen_midpoint
    px = px / 2
    py = py / 2
    print('pos: ', px, py)
    # 移动鼠标
    pyautogui.moveTo(px, py, duration=0.5 )
    time.sleep(1)
    # 点击右键
    pyautogui.click()
    pyautogui.click()


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

if tab.ele('.memberName purplelink'):
    print('已经登录')
else:
    print('没有登录, 点击登录按钮')
    clickLoginBtn()
    passCloudFlare()
    
    
