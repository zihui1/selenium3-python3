#encoding = utf-8
from action.PageAction import *
from util.ParseExcel import ParseExcel
from config.VarConfig import *
from util.Log import Log
import time
import traceback

# 创建解析Excel对象
excelObj = ParseExcel()
# 将Excel数据文件加载到内存
excelObj.loadWorkBook(dataFilePath)
log = Log()
