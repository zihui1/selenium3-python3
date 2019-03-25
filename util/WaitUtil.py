# encoding = utf-8
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
class WaitUtil(object):
    def __init__(self,driver):
        self.locationTypeDict = {
            "xpath":By.XPATH,
            "id":By.ID,
            "name":By.NAME,
            "class_name":By.CLASS_NAME,
            "tag_name":By.TAG_NAME,
            "like_text":By.LINK_TEXT,
            "partial_link_text":By.PARTIAL_LINK_TEXT
        }
        self.driver = driver
        self.wait = WebDriverWait(self.driver,30)

    def presenceOfElementLocated(self,locationType,locatorExpression,*args):
        '''显示等待页面元素出现在Dom中，但并不一定可见，存在则返回该页面元素对象'''
        try:
            if locationType.lower() in self.locationTypeDict:
                element = self.wait.until(EC.presence_of_element_located((self.locationTypeDict[\
                                                                    locationType.lower()],locatorExpression)))
                return element
            else:
                raise TypeError(u"未找到定位方式，请确认定位方法是否写正确")
        except Exception as e:
            raise e



    def frameToBeAvailaBleSwitchToIt(self,locationType,locatorExpression,*args):
        '''
        检查Frame是否存在，存在则切换斤Frame控件中
        '''
        try:
            self.wait.until(EC.frame_to_be_available_and_switch_to_it((self.locationTypeDict[\
                                                                          locationType.lower()],locatorExpression)))
        except Exception as e:
            raise e

    def visibilityOfElementLocated(self,locationType,locatorExpression,*args):
        '''显示等待页面元素出现'''
        try:
            element = self.wait.until(EC.visibility_of_element_located((\
                self.locationTypeDict[locationType.lower()],locatorExpression)))
            return element
        except Exception as e:
            raise e


if __name__ == "__main__":
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get("http://mail.163.com")
    wu = WaitUtil(driver)

    wu.frameToBeAvailaBleSwitchToIt("xpath","//iframe[starts-with(@id, 'x-URS-iframe')]")
    ps = wu.visibilityOfElementLocated("name","email")
    wc = wu.presenceOfElementLocated("name","email")
    # wc = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME, 'email')))
    wc.send_keys("1111")
    ps.send_keys("11111")
    time.sleep(5)

    driver.quit()