#! /usr/bin/python3
# -*- coding: utf-8 -*-

import wx
"""
一个简单的GUI应用程序显示Hello World消息使用以下构建步骤 −
导入 wx 模块

定义应用程序类的一个对象


创建一个顶层窗口的 wx.Frame 类的对象。 给出构造标题和尺寸参数。

虽然其他控件可以在Frame对象加入，但它们的布局无法管理。因此，把一个Panel对象到框架。

添加一个静态文本对象，以显示hello world’在窗口内的任意位置。

通过show()方法激活框架窗口。

输入应用程序对象的主事件循环//原文出自【易百教程】，商业转载请联系作者获得授权，非商业请保留原文链接：https://www.yiibai.com/wxpython/wxpython_hello_world.html

"""

app = wx.App()
window = wx.Frame(None, title="title", size=(400, 300))
panel = wx.Panel(window)
label = wx.StaticText(panel, label="hello world", pos=(100, 100))
window.Show(True)
app.MainLoop()

