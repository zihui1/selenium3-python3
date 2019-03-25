# encoding = utf-8
import os


# 各浏览器wendriver地址
ieDriverFilePath = "c:\\"
chromeDriverFilePath = "c:\\"
firefoxDriverFilePath = "c:\\"

# 获取当前父级绝对路径
parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LogPath = parentDirPath+u"\\Log\\"

# 异常截图存放目录绝对路径
screePicturesDir = parentDirPath + u'\\exceptionpictures\\'

# 存放数据文件存放绝对路径
dataFilePath = parentDirPath+u'\\testData\\163邮箱创建联系人并发邮件.xlsx'

# 测试数据文件中，测试用例表中部分列对应的数字序号
testCase_testCaseName =2
testCase_frameWorkName = 4
testCase_testStepSheetName =5
testCase_dataSourceSheetName = 6
testCase_isExecute =7
testCase_runTime =8
testCase_testResult = 9

# 用例步骤表中，部分列对应的数字序号
testStep_testStepDescribe = 2
testStep_keyWords = 3
testStep_locationType = 4
testStep_locatorExpression = 5
testStep_operatValue = 6
testStep_runTime = 7
testStep_testResult = 8
testStep_errorInfo = 9
testStep_errorPic = 10


# 数据源表中，是否执行列对应的数字编号
dataSource_isExecute = 7
dataSource_email = 3
dataSource_runTime = 8
dataSource_result = 9




if __name__ == "__main__":
    print(screePicturesDir)