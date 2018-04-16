#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     xlsx_con
   Description :
   Author :       王康
   date：          2018/4/16
-------------------------------------------------
   Change Activity:
                   2018/4/16:
-------------------------------------------------
"""
from openpyxl import load_workbook
from tkinter import Frame,Button,Entry
from tkinter import filedialog

def xlsx_con(filename,string):
    filename=filename
    string=string
    data_list=string.split(" ")
    file=load_workbook(filename=filename)
    table=file.get_sheet_by_name('Sheet1')
    sheet_data_primary_key=[]
    for row in table.rows:
        sheet_data_primary_key.append(row[0].value)
    if data_list[0] not in sheet_data_primary_key:
        table.append(data_list)
    else:
        print("已经存在")
    file.save(filename=filename)



# 定义Application类表示应用/窗口，继承Frame类
class Application(Frame):
    # Application构造函数，master为窗口的父控件
    def __init__(self, master=None):
        # 初始化Application的Frame部分
        Frame.__init__(self, master)
        # 显示窗口，并用grid布局
        self.grid()
        # 创建控件
        self.createWidgets()

    # 创建控件
    def createWidgets(self):
        self.entry_filename=Button(self,text='选择文件',command=self.openfile)
        self.entry_filename.grid()
        self.entry_string = Entry(self, )
        self.entry_string.grid()
        self.quitButton = Button(self, text='提交', command=self.click)
        # 显示按钮，并使用grid布局
        self.quitButton.grid()
    def openfile(self):
        self.filename=filedialog.askopenfilename()
    def click(self):
        string=self.entry_string.get()
        xlsx_con(self.filename,string)

if __name__=='__main__':
    # 创建一个Application对象app
    app = Application()
    # 设置窗口标题为'First Tkinter'
    app.master.title = 'First Tkinter'
    app.master.geometry("300x300")
    # 主循环开始
    app.mainloop()
