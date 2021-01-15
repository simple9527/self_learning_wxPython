#!/bin/bash
# -*- coding: utf-8 -*-
"""
https://github.com/necan/wxPython-tutorial/blob/master/2.%E7%AC%AC%E4%B8%80%E6%AD%A5.md
@Project ：wxPython_learning 
@File    ：01_1移动窗体到指定位置.py
@IDE     ：PyCharm 
@Author  ：yang.liu5@flex.com
@Date    ：2021/1/15 下午6:50 
"""


import wx


class Example(wx.Frame):
    """
    构造一个wx.Frame类
    """
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title,
            size=(300, 200))
        # self.Move((800, 250)) # 移动到800 250像素位置
        self.Center()   # 居中


def main():
    """
    控制流程
    :return:
    """
    app = wx.App()
    ex = Example(None, title='Moving')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()