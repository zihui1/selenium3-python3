# encoding = utf-8
import win32clipboard as w
import win32con

class Clipboard(object):
    '''
    模拟windows设置剪切板
    '''

    # 读取剪切板
    @staticmethod
    def getText():
        # 打开剪切板
        w.OpenClipboard()
        d = w.GetClipboardData(win32con.CF_TEXT)
        # 关闭剪切板
        w.CloseClipboard()
        return d

    # 设置剪切板内容
    @staticmethod
    def setText(aString):
        # 打开剪切板
        w.OpenClipboard()
        # 清空剪切板
        w.EmptyClipboard()
        # 将数据aString写入到剪贴板
        w.SetClipboardData(win32con.CF_UNICODETEXT,aString)
        # 关闭剪贴板
        w.CloseClipboard()