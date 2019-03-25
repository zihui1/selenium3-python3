# encoding = utf-8
from selenium import webdriver
from util.ObjectMap import getElement
from util.WaitUtil import WaitUtil
from util.KeyBoardUtil import KeyboardKeys
from util.ClipboardUtil import Clipboard
from util.DirAndTime import *
from config.VarConfig import ieDriverFilePath,chromeDriverFilePath,firefoxDriverFilePath
import time

# 定义全局driver变量
driver = None
# 全局的等待类实例对象
waitUtil = None

def open_browser(browserName,*args):
    global driver,waitUtil
    try:
        if browserName.lower() =="ie":
            driver = webdriver.Ie(executable_path=ieDriverFilePath)
        elif  browserName.lower() =="chrome":
            driver = webdriver.Chrome()
        elif browserName.lower() =="firefox":
            driver = webdriver.Firefox(executable_path=firefoxDriverFilePath)
        waitUtil = WaitUtil(driver)
    except Exception as e:
        raise e

def visit_url(url,*args):
    # 访问某个网址
    global driver
    try:
        driver.get(url)
    except Exception as e:
        raise e

def close_browser(*args):
    # 关闭浏览器
    global driver
    try:
        driver.quit()
    except Exception as e:
        raise e

def sleep(sleepSeconds,*args):
    # 强制等待
    try:
        time.sleep(int(sleepSeconds))
    except Exception as e:
        raise e

def clear(locationType,locatorExpression,*args):
    # 清楚输入框默认内容
    global driver
    try:
        getElement(driver,locationType,locatorExpression).clear()
    except Exception as e:
        raise e

def input_string(locationType,locatorExpression,inputContent):
    # 在输入框中输入内容
    global driver
    try:
        getElement(driver,locationType,locatorExpression).send_keys(inputContent)
    except Exception as e:
        raise e

def click(LocationType,locatorExpression,*args):
    # 单击页面元素
    global driver
    try:
        getElement(driver,LocationType,locatorExpression).click()
    except Exception as e:
        raise e

def assert_string_in_pagesource(assertString,*args):
    # 断言页面源码是否存在关键字或关键字符串
    global driver
    try:
        assert assertString in driver.page_source,\
        u'%s ：源码中找不到该关键字!'%(assertString)
    except AssertionError as e:
        raise AssertionError(e)
    except Exception as e:
        raise e

def assert_title(titleStr,*args):
    # 断言页面标题是否存在给定的关键字符串
    global driver
    try:
        assert titleStr in driver.title,\
        u"%s ：title找不到！" %(titleStr)
    except AssertionError as e:
        raise AssertionError(e)
    except Exception as e:
        raise e

def getTitle(*args):
    # 获取页面标题
    global driver
    try:
        return driver.title
    except Exception as e:
        raise e

def getPageSource(*args):
    # 获取页面源码
    global driver
    try:
        return driver.page_source
    except Exception as e:
        raise e

def switch_to_js(locationType,*args):
    #使用js对页面进行操作
    global driver
    try:
        return driver.execute_script(locationType)
    except Exception as e:
        raise e


def switch_to_frame(locationType,frameLocatorExpression,*args):
    # 切换进入frame
    global driver
    try:
        driver.switch.to.frame(getElement(driver,locationType,frameLocatorExpression))
    except Exception as e:
        print("frame异常")
        raise e

def switch_to_default_content(*args):
    # 切出frame
    global driver
    try:
        driver.switch_to.default_content()
    except Exception as e:
        raise e

def paste_string(pasteString,*args):
    # 模拟键盘复制
    try:
        Clipboard.setText(pasteString)
        time.sleep(2)
        KeyboardKeys.twoKeys('ctrl','v')
    except Exception as e:
        raise e

def press_tab_key(*args):
    # 模拟键盘tab
    try:
        KeyboardKeys.oneKey('tab')
    except Exception as e:
        raise e

def press_enter_key(*args):
    # 模拟键盘Enter
    try:
        KeyboardKeys.oneKey("enter")
    except Exception as e:
        raise e

def maximize_browser():
    # 窗口最大化
    global driver
    try:
        driver.maximize_window()
    except Exception as e:
        raise e

def capture_screen(*args):
    # 截取屏幕图片
    global driver
    currTime = getCurrentTime()
    picNameAndPath= str(createCurrentDateDir())+"\\"+str(currTime)+".png"
    try:
        driver.get_screenshot_as_file(picNameAndPath.replace('\\',r'\\'))
    except Exception as e:
        raise e
    else:
        return picNameAndPath


def waitPresenceOfElementLocated(locationType,locatorExpression,*args):
    '''显示等待页面元素出现在Dom中，但并不一定可见，存在则返回该页面元素对象'''
    global waitUtil
    try:
        waitUtil.presenceOfElementLocated(locationType,locatorExpression)
    except Exception as e:
        raise e

def waitFrameToBeAvailableAndSwitchToIt(locationType,locatorExpression,*args):
    '''检查frame是否存在，存在则切换进frame控件中'''
    global waitUtil
    try:
        waitUtil.frameToBeAvailaBleSwitchToIt(locationType,locatorExpression)
    except Exception as e:
        raise e

def waitVisibilityOfElementLocated(locationType,locatorExpression,*args):
    '''显示等待页面元素出现在DOM中，并且可见，存在返回该页面元素对象'''
    global waitUtil
    try:
        waitUtil.visibilityOfElementLocated(locationType,locatorExpression,*args)
    except Exception as e:
        raise e