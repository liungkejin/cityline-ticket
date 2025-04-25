##
## 使用 截图 + OCR + pyautogui 方式
##

import cv2
import numpy as np
from cnocr import CnOcr
import pyautogui, time

# 在我的电脑上，屏幕坐标都是乘了 2
# 所以这里需要除以 2，其他电脑可能是 1
def element_screen_rect(element, screenScale=2):
    # 获取元素的屏幕坐标
    px, py = element.rect.screen_location
    # 获取元素的大小
    width, height = element.rect.size
    # 返回一个元组 (x, y, width, height)
    return (px/screenScale, py/screenScale, width, height)

# 两种截图方式
# 1. 使用 pyautogui 截图, 优点：截图的是真实屏幕图像不会对网页有任何影响，缺点：速度慢，且需要依赖元素的位置，且会被其他窗口遮挡
# 2. 使用 DrissionPage 截图，优点：速度快，且可以直接获取元素的截图，缺点：截图的图像是网页渲染后的图像，会有闪屏，可能会对网页有影响并检测到
# 返回值是一个 numpy 数组
def element_screenshot(element, use_pyautogui=False):
    try:
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
    except Exception as e:
        #print('Error: ', e)
        return None

class CloudFlareBypasser:
    def __init__(self, screen_scale=2):
        # 屏幕坐标缩放比例, 在我的电脑上，屏幕坐标都是乘了 2
        self.screen_scale = screen_scale
        self.ocr = CnOcr()
        
    # 这个函数是用来找到 cloudFlare 的 checkbox 的位置
    # 也可以判断是否成功了
    # 返回值是一个元组 (status, x, y), None 表示没有找到
    # status = 0: 找到 checkbox 的位置
    # status = 1: 成功了
    def find_cloud_flare_checkbox_position(self, element, timeoutS=-1):
        # 注意 ocr 第一次执行会比较慢，因为要加载模型，所以最好先执行一次 ocr
        
        start_time = time.time()
        # 文字左侧中点的坐标
        text_pos = None
        cloudflare_logo_width = 0
        # 循环截图，一直找到 确认您是真人 这几个字的位置，然后它左边一点的位置就是 checkbox 的位置
        while True:
            # 截图
            img = element_screenshot(element, use_pyautogui=False)
            if img is not None:
                # 使用 OCR 识别文本
                result = self.ocr.ocr(img)
                if len(result) > 0:
                    for item in result:
                        # item[0] 是文本，item[1] 是位置
                        text = item.get('text', '')
                        pos = item.get('position', None)
                        print('识别到的文本: ', text, pos)
                        # 如果识别到的文本中有 确认您是真人，就返回这个位置
                        if (('确认您是真人' in text) or 'you are human' in text or '您是人類' in text) and pos is not None:
                            text_pos = ( pos[0][0], (pos[0][1]+pos[3][1]) / 2)
                            print('找到 checkbox 的位置: ', text_pos)
                            
                        if ('CLOUDFLARE' in text or 'cloudflare' in text):
                            # 计算 logo 的宽度
                            cloudflare_logo_width = pos[1][0] - pos[0][0]
                            print('找到 cloudflare 的 logo 的位置: ', pos)
                            
                        if ('Success' in text or '成功' in text):
                            # 直接成功了，返回 None
                            print('直接成功了')
                            return (1, 0, 0, 0, 0)
                            
                # 如果找到了，就退出循环
                if text_pos is not None:
                    break
            # 如果超时了，就退出循环
            # 这里的 timeout_ms 是毫秒，所以要除以 1000
            if (timeoutS > 0) and (time.time() - start_time > timeoutS):
                print('超时了')
                break
            # 等待 0.1 秒，避免过于频繁的截图
            # time.sleep(0.1)
        if text_pos is None:
            return None
        
        px, py, width, height = element_screen_rect(element)
        px = px + text_pos[0]/self.screen_scale
        py = py + text_pos[1]/self.screen_scale
        offset_x = cloudflare_logo_width / self.screen_scale / 4
        px = px - offset_x 
        
        rx = text_pos[0]/self.screen_scale - offset_x
        ry = text_pos[1]/self.screen_scale
        return (0, px, py, rx, ry)
    
    def waiting_success(self, element, timeoutS=10):
        start_time = time.time()
        # 循环截图，一直找到 成功 这几个字的位置
        while True:
            # 截图
            img = element_screenshot(element, use_pyautogui=False)
            if img is not None:
                # 使用 OCR 识别文本
                result = self.ocr.ocr(img)
                if len(result) > 0:
                    for item in result:
                        # item[0] 是文本，item[1] 是位置
                        text = item.get('text', '')
                        pos = item.get('position', None)

                        if ('Success' in text or '成功' in text):
                            # 直接成功了，返回 None
                            print('成功了')
                            return True
                        if ('Error' in text or '失敗' in text or '失败' in text):
                            # 直接失败了，返回 None
                            print('失败了')
                            return False

            # 如果超时了，就退出循环
            # 这里的 timeout_ms 是毫秒，所以要除以 1000
            if (timeoutS > 0) and (time.time() - start_time > timeoutS):
                print('超时了')
                break
            
        return False
    
    # 这个函数是用来找到 cloudFlare 的根 div 的位置
    def waitCloudFlareRootDiv(self, venueTab, locator, timeoutS=10):
        start_time = time.time()
        div = venueTab.ele(locator)
        while not div:
            if (time.time() - start_time) > timeoutS:
                print('waitCloudFlareRootDiv: 超时了')
                return None
            try:
                div = venueTab.ele(locator)
            except Exception as e:
                print('Error: ', e)
                # 等待 0.1 秒
                time.sleep(0.1)
                continue
            
        return div
    
    def bypass(self, tab, cloudFlareRootDivLocator):
        cloudFlareRootDiv = self.waitCloudFlareRootDiv(tab, cloudFlareRootDivLocator)
        checkbox_pos = self.find_cloud_flare_checkbox_position(cloudFlareRootDiv)

        if checkbox_pos is not None:
            if checkbox_pos[0] == 1:
                return True
            
            print('找到 checkbox 的位置: ', checkbox_pos)
            sx = checkbox_pos[1]  # 屏幕绝对位置
            sy = checkbox_pos[2]
            rx = checkbox_pos[3]  # 元素相对位置
            ry = checkbox_pos[4]
            
            if False:
                tab.actions.move_to(cloudFlareRootDiv, rx, ry, 0)
                tab.actions.click()
            else:
                # 这里是使用 pyautogui 来移动鼠标
                # 移动鼠标到 checkbox 的位置
                pyautogui.moveTo(sx, sy, duration=0)
                pyautogui.click()
                pyautogui.click()
            time.sleep(0.1)
            print('点击了 checkbox 的位置: ', (sx, sy, rx, ry), ', 等待完成')
            # 等待成功
            result = self.waiting_success(cloudFlareRootDiv, timeoutS=5)
            print('bypass result: ', result)
            
            return result
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
            return False

