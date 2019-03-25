# encoding = utf-8
from selenium.webdriver.support.ui import WebDriverWait


# 获取单个元素
def getElement(driver,locationType,locatorExpression):
    try:
        element = WebDriverWait(driver,30).until(\
            lambda x:x.find_element(by=locationType,value=locatorExpression))
        return element
    except Exception as e:
        raise e

# 获取多个相同类型的元素对象已List返回
def getElements(driver,locationType,locatorExpression):
    try:
        element = WebDriverWait(driver,30).until(\
            lambda x:x.find_elements(by=locationType,value=locatorExpression))
        return element
    except Exception as e:
        raise e
