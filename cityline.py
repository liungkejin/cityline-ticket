
from datetime import datetime
import pytz, time, requests, tzlocal, json

from cloudflare_bypasser import CloudFlareBypasser
    
################ 下面的 js 代码转换为 python 代码

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

# print('[0x198]', a0_0x5b33(0x198))

# 将 js 代码转换为 python 代码, 其中 a0_0x306c9e 是 a0_0x5b33 函数, 不要思考过程
# 返回一个 datetime
def getHKDate():
    #a = a0_0x5b33(0x1b7) # 'toLocaleString'
    #b = a0_0x5b33(0x1c4) # 'en-US'
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
    # print('localtz: ', localtz)
    # print('offset: ', offset_seconds)
    
    # 计算香港时间调整
    adjustment = (-480 - offset_seconds/60) * 60 * 1000  # 0x311aa7 = -480
    hk_timestamp = int(localdt.timestamp() * 1000 + adjustment)
    
    return hk_timestamp

# mill = getHKDateMill(1744257600000)
# print('hk date mill: ', mill)

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

# hash = simpleHash('2023-09-25 10:00:00')
# print('hash: ', hash)

# UTSV Event data
#  {
#     "id": 25768,
#     "utsvId": -1,
#     "likeCount": 0,
#     "synonym": "TA25MD",
#     "nameEng": "MAYDAY #5525 LIVE TOUR IN HONG KONG",
#     "nameTc": "五月天 [ #5525 回到那一天 ] 25週年巡迴演唱會香港站 · 展新啟航版",
#     "nameSc": "五月天 [ #5525 回到那一天 ] 25周年巡回演唱会香港站 · 展新启航版",
#     "venueKey": 921,
#     "categoryKey": 181,
#     "subCategoryKeys": [],
#     "redirectUrl": "https://shows.cityline.com/{pbLang}/2025/5525mayday.html",
#     "onSaleTime": 1744257600000,
#     "firstSalesDate": 1742476980000,
#     "accessEndTime": 1747134000000,
#     "status": 1,
#     "fromUTSV": false,
#     "linkMode": "LIVE",
#     "displayDate": null,
#     "currency": "HKD",
#     "marketCurrency": null,
#     "salesStatus": null,
#     "venue": {
#         "id": 921,
#         "code": "$$ONLIVE",
#         "nameEng": "On-Live",
#         "nameTc": "線上直播",
#         "nameSc": "线上直播",
#         "addressEng": "-",
#         "addressTc": "-",
#         "addressSc": "-",
#         "region": "OTHERS",
#         "telephone": "-",
#         "latitude": 22.319304,
#         "longitude": 114.169361,
#         "status": 1,
#         "isPartner": -1
#     },
#     "presenter": {
#         "presenterId": null,
#         "nameEng": null,
#         "nameTc": null,
#         "nameSc": null
#     },
#     "performingDates": [],
#     "availiablePerfDates": [],
#     "displaySeq": 1,
#     "enHashTags": [
#         "Mayday",
#         "KTSP",
#         "HongKong",
#         "concert",
#         "shows"
#     ],
#     "tcHashTags": [
#         "五月天",
#         "啟德體育園",
#         "香港",
#         "演唱會",
#         "節目"
#     ],
#     "scHashTags": [
#         "五月天",
#         "启德体育园",
#         "香港",
#         "演唱会",
#         "节目"
#     ],
#     "performances": [],
#     "eventType": "NORMAL_UTSV_EVENT",
#     "trailerUrl": null,
#     "free": false,
#     "vote": false,
#     "hiddenBeforeOnSaleTime": false,
#     "config": {
#         "priorityBookingKey": 8938,
#         "updates": false,
#         "natureTc": null,
#         "natureSc": null,
#         "natureEn": null,
#         "soldOutOnBackground": true,
#         "soldOutOnBackgroundTime": "2025-04-10 12:36",
#         "soldOut": false,
#         "soldOutTime": null,
#         "showAdded": true,
#         "tixAdded": false,
#         "hideInCityline": false,
#         "autoTcToSc": true,
#         "targetUrlTc": "https://shows.cityline.com/{pbLang}/2025/5525mayday.html",
#         "targetUrlSc": "https://shows.cityline.com/{pbLang}/2025/5525mayday.html",
#         "targetUrlEn": "https://shows.cityline.com/{pbLang}/2025/5525mayday.html",
#         "videoPath": null,
#         "videoUrl": null,
#         "imagePathTc": "priority-booking/images/2025/202504101042553.jpg",
#         "imagePathSc": "priority-booking/images/2025/202504101042459.jpg",
#         "imagePathEn": "priority-booking/images/2025/202504101042339.jpg",
#         "imageUrlTc": "https://shows.cityline.com/images/2025/202504101042553.jpg?format=auto&width=300",
#         "imageUrlSc": "https://shows.cityline.com/images/2025/202504101042459.jpg?format=auto&width=300",
#         "imageUrlEn": "https://shows.cityline.com/images/2025/202504101042339.jpg?format=auto&width=300",
#         "videoPathTc": null,
#         "videoPathSc": null,
#         "videoPathEn": null,
#         "videoUrlTc": null,
#         "videoUrlSc": null,
#         "videoUrlEn": null,
#         "banner": {
#             "name": null,
#             "displayInterval": null,
#             "displayType": "image",
#             "imagePath": null,
#             "imageUrl": null,
#             "videoPath": null,
#             "videoUrl": null,
#             "imagePathTc": "priority-booking/images/2025/202504080000845.jpg",
#             "imagePathSc": "priority-booking/images/2025/202504080000835.jpg",
#             "imagePathEn": "priority-booking/images/2025/202504080000657.jpg",
#             "imageUrlTc": null,
#             "imageUrlSc": null,
#             "imageUrlEn": null,
#             "videoPathTc": null,
#             "videoPathSc": null,
#             "videoPathEn": null,
#             "videoUrlTc": null,
#             "videoUrlSc": null,
#             "videoUrlEn": null,
#             "enable": false,
#             "effectiveFrom": null,
#             "effectiveTo": null
#         },
#         "kiosk": {
#             "groups": [],
#             "displayInterval": null,
#             "showInBanner": false,
#             "showImageInSaver": false,
#             "showVideoInSaver": false,
#             "bannerEffectiveFrom": null,
#             "bannerEffectiveTo": null
#         },
#         "categoryList": [
#             "shows"
#         ],
#         "showDateFromUtsv": false,
#         "showDateList": [],
#         "onSaleEnd": "2025-05-13 19:00"
#     },
#     "purchasible": true,
#     "todaySale": false,
#     "normalButton": false,
#     "livebutton": true,
#     "detailsButton": false
# },

class CitylineUtsvEvent:
    def __init__(self, event_data):
        self.event_data = event_data
        
    def id(self):
        return self.event_data.get('id', 0)
    
    def utsvId(self):
        return self.event_data.get('utsvId', -1)
    
    def nameEng(self):
        return self.event_data.get('nameEng', '')
    
    def nameTc(self):
        return self.event_data.get('nameTc', '')
    
    def nameSc(self):
        return self.event_data.get('nameSc', '')
    
class CitylineUtsvEventList:
    def __init__(self, event_data_list):
        self.event_data_list = event_data_list
        self.event_items = [CitylineUtsvEvent(event_data) for event_data in event_data_list]
        
    def getEventById(self, id):
        for item in self.event_items:
            if item.id() == id:
                return item
        return None
    
    def getEventByUtsvId(self, utsvId):
        for item in self.event_items:
            if item.utsvId() == utsvId:
                return item
        return None
        
    def getAllEventNameMatch(self, name):
        return [
            item for item in self.event_items if name in item.nameEng() or name in item.nameTc() or name in item.nameSc()
        ]
    
# Cityline Event Data
# {
#     "content": {
#         "autoTcToSc": true,
#         "bannerUrlEn": "/images/2025/202504011529463.jpg?format=auto&width=600",
#         "bannerUrlSc": "/images/2025/202504011529463.jpg?format=auto&width=600",
#         "bannerUrlTc": "/images/2025/202504011529463.jpg?format=auto&width=600",
#         "comingLabelEn": "Coming Soon",
#         "comingLabelSc": "即将开售",
#         "comingLabelTc": "即將發售",
#         "countDownHeaderLabelSc": "",
#         "currency": "HKD",
#         "effectiveFrom": "2025-04-01 15:28",
#         "effectiveTo": "2025-05-27 15:00",
#         "endLabelEn": "Priority Booking Ends",
#         "endLabelSc": "优先预订已结束",
#         "endLabelTc": "優先預訂已完結",
#         "eventScale": "S10",
#         "hiddenBeforeOnSaleTime": false,
#         "hiddenInLandingPage": false,
#         "hideInPastEvent": false,
#         "imagePathTc": "priority-booking/images/2025/202504101319477.jpg",
#         "imageUrlTc": "/images/2025/202504101319477.jpg",
#         "loginRequire": false,
#         "multilingual": true,
#         "onSaleEnd": "2025-05-27 15:00",
#         "onSaleTime": "2025-04-16 11:00",
#         "perfDateEn": "6,15,22,27 May 2025 3pm",
#         "perfDateSc": "2025年5月6,15,22,27 日 下午3时",
#         "perfDateTc": "2025年5月6,15,22,27 日 下午3時",
#         "purchaseLabelEn": "On Sale",
#         "purchaseLabelSc": "热卖中",
#         "purchaseLabelTc": "熱賣中",
#         "purchaseUrlAdditionalList": [],
#         "purchaseUrlLabelEn": "Go to purchase",
#         "purchaseUrlLabelSc": "前　往　购　票",
#         "purchaseUrlLabelTc": "前　往　購　票",
#         "seoDescSc": "",
#         "seoKeyWordSc": "",
#         "seoTitleSc": "",
#         "showAdded": false,
#         "soldOutOnBackground": false,
#         "soldout": false,
#         "soldoutLabelEn": "Sold Out",
#         "soldoutLabelSc": "售罄",
#         "soldoutLabelTc": "售罄",
#         "surveyUrlLabelSc": "",
#         "synonym": "TA25BM05",
#         "titleEn": "Bethanie Museum (May 2025)",
#         "titleSc": "伯大尼博物馆 (2025年5月)",
#         "titleTc": "伯大尼博物館 (2025年5月)",
#         "tixAdded": false,
#         "toBeAnnounced": false,
#         "updates": false,
#         "utsvEventKey": 25770,
#         "venueEn": "HKAPA Bethanie Landmark Heritage Campus",
#         "venueSc": "香港演艺学院伯大尼古迹校园",
#         "venueTc": "香港演藝學院伯大尼古蹟校園"
#     },
#     "createdOn": "2025-04-01 15:38",
#     "disable": false,
#     "eventId": "bethaniemuseummay2025",
#     "eventYear": 2025,
#     "id": 8977,
#     "publishedOn": "2025-04-10 13:22",
#     "siteType": "cultural",
#     "siteTypeList": [
#         "cultural"
#     ],
#     "updatedOn": "2025-04-10 13:22",
#     "url": "/tc/2025/bethaniemuseummay2025.html"
# }

class CitylineEvent:
    def __init__(self, event_data):
        self.event_data = event_data
        
    def eventId(self):
        return self.event_data.get('eventId', '')
    
    def eventYear(self):
        return self.event_data.get('eventYear', 0)
        
    def content(self):
        return self.event_data.get('content', {})
    
    def titleEn(self):
        return self.content().get('titleEn', '')
    
    def titleSc(self):
        return self.content().get('titleSc', '')
    
    def titleTc(self):
        return self.content().get('titleTc', '')
    
    def isEnabled(self):
        return self.event_data.get('disable', False) == False
        
    def isNotSoldOut(self):
        return self.content().get('soldout', False) == False
    
    def isSaling(self):
        return self.getSalingType() == 0
    
    def saleStartTime(self):
        on_sale_time = self.content().get('onSaleTime', '')
        if on_sale_time == '':
            return None
        on_sale_time = datetime.strptime(on_sale_time, '%Y-%m-%d %H:%M')
        return datetime.fromtimestamp(on_sale_time.timestamp(), tz=pytz.timezone('Asia/Hong_Kong'))
        
    def saleEndTime(self):
        on_sale_end = self.content().get('onSaleEnd', '')
        if on_sale_end == '':
            return None
        on_sale_end = datetime.strptime(on_sale_end, '%Y-%m-%d %H:%M')
        return datetime.fromtimestamp(on_sale_end.timestamp(), tz=pytz.timezone('Asia/Hong_Kong'))
    
    def getSalingType(self):
        # 即将开票 返回 -1
        # 在售 返回 0
        # 已结束 返回 1
        # 判断是否正在售票
        on_sale_time = self.saleStartTime()
        if on_sale_time is None:
            return 1
        on_sale_end = self.saleEndTime()
        if on_sale_end is None:
            return 1
        # 获取当前时间
        current_time = getHKDate()
        if current_time < on_sale_time:
            return -1
        elif current_time > on_sale_end:
            return 1
        return 0
    
    def siteType(self):
        return self.event_data.get('siteType', '')
    
    def isType(self, type):
        return type in self.siteType()
    
    def utsvEventKey(self):
        return self.content().get('utsvEventKey', 0)
    
class CitylineEventList:
    def __init__(self, event_data_list):
        self.event_data_list = event_data_list
        self.event_items = [CitylineEvent(event_data) for event_data in event_data_list]
        
    def getNotSoldOutEvents(self):
        return [
            item for item in self.event_items if item.isNotSoldOut()
        ]
        
    def getAllSoldOutEvents(self):
        return [
            item for item in self.event_items if not item.isNotSoldOut()
        ]
    
    def getAllEventTypeOf(self, type):
        return [
            item for item in self.event_items if item.isType(type)
        ]
        
    def getAllEventInSaling(self, type = None):
        return [
            item for item in self.event_items if item.isSaling() and (type is None or item.isType(type))
        ]
        
    def getAllEventComingSoon(self, type = None):
        return [
            item for item in self.event_items if item.getSalingType() == -1 and (type is None or item.isType(type))
        ]
        
    def findEventMatchTitle(self, name):
        # 查找所有包含 name 的活动
        for item in self.event_items:
            if name in item.titleEn() or name in item.titleSc() or name in item.titleTc():
                return item
        return None
        

class CitylineMgr:
    def __init__(self, screenScale = 1.0):
        self.event_list = CitylineEventList([])
        self.utsv_event_list = CitylineUtsvEventList([])
        self.price_zone_list = CitylinePriceZoneList(None)
        self.screen_scale = screenScale
        
    def requestEventList(self):
        url = 'https://shows.cityline.com/data/event-list.json?v=' + str(int(time.time() * 1000))
        result = requests.get(url)
        if result.status_code == 200:
            print('requestEventList success')
            eventList = json.loads(result.text)
            self.event_list = CitylineEventList(eventList)
            return self.event_list
        print('requestEventList error: ', result.status_code)
        return None
    
    def requestUtsvEventList(self):
        url = 'https://www.cityline.com/data/utsvEventList.json?v=' + str(int(time.time() * 1000))
        print('requestUtsvEventList url: ', url)
        result = requests.get(url)
        if result.status_code == 200:
            print('requestUtsvEventList success')
            eventList = json.loads(result.text)
            self.utsv_event_list = CitylineUtsvEventList(eventList.get('utsvEventList', {}))
            return self.utsv_event_list
        print('requestUtsvEventList error: ', result.status_code)
        return None
    
    def requestAllEvent(self):
        self.requestUtsvEventList()
        self.requestEventList()

    # {
    #     "additionalUrlList": [],
    #     "url": "https://event.cityline.com/utsvInternet/5225MAYDAYHK25/home"
    # }
    def requestRealPurchaseUrl(self, event: CitylineEvent):
        # 构造出一个 url
        eventId = event.eventId()
        saleTime = str(getHKDateMill(event.saleStartTime().timestamp() * 1000))
        hour = str(getHKDate().hour)
        eventYear = str(event.eventYear())
        url = a0_0x5b33(0x142) + eventYear + '/' + eventId + '.' + saleTime + '.' + simpleHash(eventId + saleTime + a0_0x5b33(0x1e7)) + a0_0x5b33(0x15b) + hour
        url = 'https://shows.cityline.com' + url
        print('goPurchase url: ', url)
        
        result = requests.get(url)
        if result.status_code == 200:
            # 解析出 url
            print('getRealPurchaseUrl result: ', result.text)
            result = json.loads(result.text)
            url = result.get('url', '')
            # 给 url 带上一个 lang=CN 参数
            if url and not url.endswith('.html'):
                if '?' in url:
                    url += '&lang=CN'
                else:
                    url += '?lang=CN'
            return url
        print('getRealPurchaseUrl error: ', result.status_code)
        return None
            
    # 监听活动，直到开卖
    def monitorEvent(self, eventTitle):
        self.requestAllEvent()
        findEvent = self.event_list.findEventMatchTitle(eventTitle)
        if findEvent is None:
            print('没找到 匹配 ', eventTitle, ' 的活动')
            return (None, None)
        print('找到活动: ', findEvent.event_data)
        
        salingType = findEvent.getSalingType()
        if salingType == -1:
            print('活动还没有开售')
        elif salingType == 0:
            print('活动正在售票中')
        elif salingType == 1:
            print('活动已经结束')
        
        saleStartTime = findEvent.saleStartTime().timestamp()
        # 一直循环直到 开售
        while True:
            currentTime = getHKDate().timestamp()
            # 在开售前 30s 开始不断拉取真实的购买链接
            if currentTime < saleStartTime - 300:
                deltaTime = saleStartTime - currentTime
                print('距离开售还有 %ds, 等待中...' % deltaTime)
                time.sleep(1)
                continue
            # 开售了，拉取真实的购买链接
            realPurchaseUrl = self.requestRealPurchaseUrl(findEvent)
            if realPurchaseUrl is None and realPurchaseUrl != '':
                if salingType == 1:
                    return (findEvent, None)
                print('没有获取到真实购买链接，继续拉取')
                continue
            print('获取到真实购买链接: ', realPurchaseUrl)
            return (findEvent, realPurchaseUrl)
        
    # 点击购买按钮，会有几种情况
    # 1. 弹出 cloudflare 验证码框，验证过了之后，直接打开了选座页面
    # 2. 如果之前有购买，就会直接跳转到选座页面
    # 返回验证码框的div，如果不需要验证码就返回 None
    def clickFirstPurchaseBtn(self, tab):
        #name='.btn btn-outline-primary purchase-btn required'
        print('点击第一个购买按钮')
        # 必须要等到这个控件
        ticketCard = False
        retryCount = 0
        while True:
            try:
                btnRetry = tab.ele('#btn-retry-en-1', timeout = 0)
                if (btnRetry):
                    btnRetry.wait.enabled(timeout = 0.5)
                    print('找到 btnRetry, 点击')
                    btnRetry.click()
            except Exception as e:
                btnRetry = False # ignore
                
            try:
                ticketCard = tab.ele('.ticketCard', timeout = 1)
            except Exception as e:
                print('没有找到 ticketCard: ', e, ' retryCount: ', retryCount)
                ticketCard = False
                
            if ticketCard:
                break
            retryCount += 1
            
        tab.scroll.to_see('.ticketCard')
        purchaseBtn = ticketCard.ele('tag:button')
        purchaseBtn.wait.clickable()
        prev_url = tab.url
        print('点击第一个购买按钮, url: ', prev_url)
        purchaseBtn.click()
        
        start_time = time.time()
        # 判断是否 tab 的 url 发生了变化，还是弹出了 cloudflare 验证码框
        while True:
            if tab.url != prev_url:
                print('url 发生变化，应该不需要验证码: ', tab.url)
                return None
            try:
                cloud_flare_div = tab.ele('.modal fade show', timeout=0.3)
                if cloud_flare_div:
                    print('找到验证码框布局显示，需要进行验证')
                    return cloud_flare_div
            except Exception as e:
                ignore = ''
                
            if time.time() - start_time > 5:
                print('超时了，既没有页面改变又没有发现验证码框，返回 None')
                return None
        return None
        
    def clickPurchaseBtnAfterCloudFlare(self, tab):
        btnDiv = tab.ele('.modal-footer')
        loginBtn = btnDiv.ele('.btn-login')
        loginBtn.wait.enabled()
        loginBtn.click()
        
        
    def processFirstPurchasePage(self, tab):
        print('processFirstPurchasePage')
        tab.listen.start("/pricezones")
        
        cloud_flare_div = self.clickFirstPurchaseBtn(tab)

        if cloud_flare_div is not None:
            cloud_flare_dialog_root = cloud_flare_div.ele('.modal-content h-100')
            if not cloud_flare_dialog_root:
                print('没有找到 cloudFlare 的 div')
                return False
            # 验证 cloudFlare
            clbypasser = CloudFlareBypasser(self.screen_scale)
            if not clbypasser.bypass(tab, cloud_flare_dialog_root):
                print('CloudFlare 验证失败')
                return False
            else:
                print('CloudFlare 验证成功')
            
            # 验证成功之后，点击购买按钮
            # 这里面有两种情况
            # 1. 点击购买按钮，直接进入到选座页面
            # 2. 点击购买按钮，进入到排队页面
            self.clickPurchaseBtnAfterCloudFlare(tab)
        
        return True

    # expectNum 是期望的票数
    # priceZone 是票价区间信息
    def selectTicketTypeAndNum(self, tab, priceZone, expectNum):
        print('选择票价 和 张数')
        ticketType = priceZone.aviableTicketType()
        if ticketType is None:
            print('没有找到可用的票')
            return False
        
        priceBox1 = tab.ele('.price-box1')
        priceDiv = priceBox1.ele('.price')
        
        # 这里不处理没有选中的情况，因为系统有一个默认选中的票价
        exvalue = 'value="' + str(priceZone.id()) + '"'
        for div in priceDiv.children():
            radio = div.ele('.ticket-price-btn')
            if exvalue in radio.html:
                print('选择票的类型: ', radio.html)
                radio.click()
                break
        discountDegree = tab.ele('.discount-degree')
        selectForm = discountDegree.child().ele('tag:select')
        # print('selectForm = ', selectForm.html)
        # 第一个选项是当前选中的票价，不是真的的选项
        optionCount = len(selectForm.select.options)-1
        num = min(optionCount, expectNum)
        print('optionCount = ', optionCount, ', selectNum = ', num)
        
        selectForm.select.by_index(num+1)
        return True
        
    def clickSecondPagePurchaseBtn(self, tab):
        expressPurchaseBtn = tab.ele('#expressPurchaseBtn')
        print('expressPurchaseBtn = ', expressPurchaseBtn.html)
        expressPurchaseBtn.click()
        
    # 处理第二个购买页面, 选座和选票
    def processSecondPurchasePage(self, tab, expectTicketNum):
        print('processSecondPurchasePage')
        packet = tab.listen.wait(timeout=5)
        if not packet or packet is None or packet.response is None or packet.response.status != 200:
            print('没有获取到 pricezones 信息')
            return False
        self.price_zone_list = CitylinePriceZoneList(packet.response.body)
        avPriceZone = self.price_zone_list.getAavaiableMaxPriceZone()
        if avPriceZone is None:
            print('没有找到可用的票价区间')
            return False
        print('找到可用的价格区间: ', avPriceZone.id(), '-', avPriceZone.code(), '-', avPriceZone.price())

        print('正在跳转到选座页面, 等待页面加载完成')
        # 正在跳转到选座页面, 等待页面加载完成
        tab.wait.doc_loaded(timeout=10)
        
        if not self.selectTicketTypeAndNum(tab, avPriceZone, expectTicketNum):
            print('选择票价和张数失败')
            return False
        self.clickSecondPagePurchaseBtn(tab)
        return True
            
def clickLoginBtn(tab):
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
    
# https://venue.cityline.com/utsvInternet/internet/api/event/53743/performance/83614/pricezones?_=1745657524461
#{
#    "pricezones": [
#        {
#            "pricezoneId": 324,
#            "code": "A",
#            "color": "#FF3333",
#            "nameEn": "A",
#            "nameTc": "A",
#            "nameSc": "A",
#            "price": 780.0,
#            "status": "AVAILABLE",
#            "ticketTypes": [
#                {
#                    "tickettypeId": 100,
#                    "tickettypeCode": "STAN",
#                    "descriptionEn": "STANDARD",
#                    "descriptionTc": "正價票",
#                    "descriptionSc": "正价票",
#                    "tickettypeNameEn": "STANDARD",
#                    "tickettypeNameTc": "正價票",
#                    "tickettypeNameSc": "正价票",
#                    "quantity": 10,
#                    "price": 780.0,
#                    "boundType": null,
#                    "boundQuantity": null,
#                    "prerequisiteTicketTypeId": null
#                }
#            ],
#            "additionalMessages": []
#        },
#        {
#            "pricezoneId": 325,
#            "code": "B",
#            "color": "#0066FF",
#            "nameEn": "B",
#            "nameTc": "B",
#            "nameSc": "B",
#            "price": 680.0,
#            "status": "AVAILABLE",
#            "ticketTypes": [
#                {
#                    "tickettypeId": 100,
#                    "tickettypeCode": "STAN",
#                    "descriptionEn": "STANDARD",
#                    "descriptionTc": "正價票",
#                    "descriptionSc": "正价票",
#                    "tickettypeNameEn": "STANDARD",
#                    "tickettypeNameTc": "正價票",
#                    "tickettypeNameSc": "正价票",
#                    "quantity": 10,
#                    "price": 680.0,
#                    "boundType": null,
#                    "boundQuantity": null,
#                    "prerequisiteTicketTypeId": null
#                }
#            ],
#            "additionalMessages": []
#        }
#    ]
#}

class CitylineTicketType:
    def __init__(self, tickettype_data):
        self.tickettype_data = tickettype_data
        
    def id(self):
        return self.tickettype_data.get('tickettypeId', 0)
    
    def code(self):
        return self.tickettype_data.get('tickettypeCode', '')
    
    # 是否是正价票
    def isStandard(self):
        return self.tickettype_data.get('tickettypeCode', '') == 'STAN'
    
    def quantity(self):
        return self.tickettype_data.get('quantity', 0)
    
    def price(self):
        return self.tickettype_data.get('price', 0)
    
    def available(self):
        return self.quantity() > 0

class CitylinePriceZoneItem:
    def __init__(self, pricezone_data):
        self.pricezone_data = pricezone_data
        
    def id(self):
        return self.pricezone_data.get('pricezoneId', 0)
    
    def code(self):
        return self.pricezone_data.get('code', '')
    
    def price(self):
        return self.pricezone_data.get('price', 0)
    
    def allTicketTypes(self):
        ticket_types = self.pricezone_data.get('ticketTypes', [])
        return [CitylineTicketType(ticket_type) for ticket_type in ticket_types]

    def aviableTicketType(self, code = 'STAN'):
        ticket_types = self.allTicketTypes()
        for ticket_type in ticket_types:
            if ticket_type.available() and (code is None or ticket_type.code() == code):
                return ticket_type
        return None
    
    def available(self, code = 'STAN'):
        return self.aviableTicketType(code) is not None
    
class CitylinePriceZoneList:
    def __init__(self, pricezone_data):
        self.pricezone_data_list = []
        if pricezone_data is not None:
            self.pricezone_data_list = pricezone_data.get('pricezones', [])
        self.pricezone_items = [CitylinePriceZoneItem(pricezone_data) for pricezone_data in self.pricezone_data_list]
        
    def getPriceZoneById(self, id):
        for item in self.pricezone_items:
            if item.id() == id:
                return item
        return None
    
    # 找到正价票的数量 > 0 的价格最高的票
    def getAavaiableMaxPriceZone(self):
        max_price = 0
        max_price_zone = None
        for item in self.pricezone_items:
            if item.price() > max_price and item.available():
                max_price = item.price()
                max_price_zone = item
        return max_price_zone