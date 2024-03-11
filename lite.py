from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QGraphicsScene,QDesktopWidget
from PyQt5.QtWidgets import QGraphicsDropShadowEffect,QListWidgetItem,QHeaderView
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton, QProgressBar
from PyQt5.QtGui import QPixmap, QImage ,QColor
from PyQt5.QtCore import Qt, QThread, pyqtSignal

import ui
import os
import sys
import time 
import json

import pandas as pd
import math

class setting_windows(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("Form")
        self.resize(427, 221)
        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 431, 231))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridlayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridlayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridlayout.setContentsMargins(20, 20, 20, 20)
        self.gridlayout.setVerticalSpacing(7)
        self.gridlayout.setObjectName("gridlayout")
        self.spinBox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.spinBox.setFont(font)
        self.spinBox.setRange(-100,100)
        self.spinBox.setObjectName("spinBox")
        self.gridlayout.addWidget(self.spinBox, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridlayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_2.sizePolicy().hasHeightForWidth())
        self.radioButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridlayout.addWidget(self.radioButton_2, 3, 1, 1, 1)
        self.fontComboBox = QtWidgets.QFontComboBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.fontComboBox.setFont(font)
        self.fontComboBox.setObjectName("fontComboBox")
        self.gridlayout.addWidget(self.fontComboBox, 1, 1, 1, 1)
        self.radioButton_1 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_1.sizePolicy().hasHeightForWidth())
        self.radioButton_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.radioButton_1.setFont(font)
        self.radioButton_1.setObjectName("radioButton_1")
        self.gridlayout.addWidget(self.radioButton_1, 2, 1, 1, 1)
        self.radioButton_3 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_3.sizePolicy().hasHeightForWidth())
        self.radioButton_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridlayout.addWidget(self.radioButton_3, 4, 1, 1, 1)
        self.label_1 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.gridlayout.addWidget(self.label_1, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridlayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.gridlayout.addWidget(self.buttonBox, 5, 1, 1, 1)
        self.gridlayout.setRowMinimumHeight(0, 20)
        self.gridlayout.setRowMinimumHeight(1, 20)
        self.gridlayout.setRowMinimumHeight(2, 20)
        self.gridlayout.setRowMinimumHeight(3, 20)
        self.gridlayout.setRowMinimumHeight(4, 20)
        self.gridlayout.setRowMinimumHeight(5, 20)
        self.gridlayout.setColumnStretch(0, 2)
        self.gridlayout.setColumnStretch(1, 3)
        self.gridlayout.setRowStretch(0, 1)
        self.gridlayout.setRowStretch(1, 1)
        self.gridlayout.setRowStretch(2, 1)
        self.gridlayout.setRowStretch(3, 5)
        self.gridlayout.setRowStretch(4, 5)
        self.gridlayout.setRowStretch(5, 5)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "设置"))
        self.label_3.setText(_translate("Form", "爬虫方式："))
        self.radioButton_2.setText(_translate("Form", "Firefox"))
        self.fontComboBox.setCurrentText(_translate("Form", "霞鹜新晰黑"))
        self.radioButton_1.setText(_translate("Form", "Edge"))
        self.radioButton_3.setText(_translate("Form", "Request"))
        self.label_1.setText(_translate("Form", "行高修正："))
        self.label_2.setText(_translate("Form", "字体："))

# 只有查看功能 删除所有爬虫功能
# 主窗口
class mainWindow(QMainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        try:
            cscd=pd.read_csv('cscd中文库.csv',encoding = 'gbk')
        except:
            cscd=pd.DataFrame({'序号':[0],'期刊名称':['农专校报'],'ISSN':['不晓得'],'库标识':['核心库']})
        #print(cscd.head())
        
        try:
            with open(r'setting.json','r+') as f:
                self.setdata=json.load(f)
            self.font=self.setdata['font']
            self.additon=self.setdata['additon']
            self.choose=self.setdata['file']
            self.size=self.setdata['size']
        except:
            with open(r'setting.json','w') as f:
                json.dump({'font':"霞鹜新晰黑",'additon':0,'file':'A_Sample.tsv','size':0.7},f)
            with open(r'setting.json','r+') as f:
                self.setdata=json.load(f)
            self.font=self.setdata['font']
            self.additon=self.setdata['additon']
            self.choose=self.setdata['file']
            self.size=self.setdata['size']


        

        self.cscd=cscd

        self.ui = ui.Ui_Form()        
        self.ui.setupUi(self)

        #self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
        #self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        #设置表头
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(230, 230, 230))
        brush = QtGui.QBrush(QtGui.QColor(95, 117, 140))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        #self.ui.tableWidget.setHorizontalHeaderItem(4, item)
        self.ui.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(230, 230, 230))
        brush = QtGui.QBrush(QtGui.QColor(95, 117, 140))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.ui.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(230, 230, 230))
        brush = QtGui.QBrush(QtGui.QColor(95, 117, 140))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.ui.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(230, 230, 230))
        brush = QtGui.QBrush(QtGui.QColor(95, 117, 140))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.ui.tableWidget.setHorizontalHeaderItem(3, item)

        item = self.ui.tableWidget.horizontalHeaderItem(0)
        item.setText(("类型"))
        item = self.ui.tableWidget.horizontalHeaderItem(1)
        item.setText(("日期"))
        item = self.ui.tableWidget.horizontalHeaderItem(2)
        item.setText(("标题"))
        item = self.ui.tableWidget.horizontalHeaderItem(3)
        item.setText(("来源"))
     
        #self.size=0.7
        
        if self.size>=0.6:
            add=self.size
        else:
            add=5*(self.size-0.6)
        


        #int(50*12/fsize)
        self.ui.tableWidget.verticalHeader().setDefaultSectionSize(int(50+5*add))
        self.ui.tableWidget.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Custom)
        #self.ui.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        
        self.ui.tableWidget.verticalScrollBar().setStyleSheet("QScrollBar{background:transparent; width: 10px;}QScrollBar::sub-line{background:transparent;}QScrollBar::handle{background:rgb(80, 100, 140); border:2px solid transparent; border-radius:4px;}")
        #"QTableWidget::section::checked{background:rgb(95, 117, 140);}"self.ui.tableWidget.horizontalHeader().setStyleSheet("::section::checked{background:rgb(95, 117, 140);}")
        self.ui.tableWidget.verticalHeader().setStyleSheet("::section::checked{background:rgb(95, 117, 140);background-color:transparent;color:gray;border:2px solid rgb(95, 117, 140);border-radius:2px}")
        # 定义菜单open打开图片
        self.ui.tableWidget.setStyleSheet("QTableWidget::item{padding:2px;border:0px;}QTableWidget::item::selected{background:rgb(95, 117, 140);}")
        self.ui.tableWidget.itemSelectionChanged.connect(self.on_selection_changed)
        
        

        self.ui.textEdit.horizontalScrollBar().hide()
        self.ui.textEdit.verticalScrollBar().hide()
        self.ui.textEdit.setStyleSheet("QScrollBar{background:transparent; width: 0px;}QScrollBar::sub-line{background:transparent;}QScrollBar::handle{background:rgb(80, 100, 140); border:0px solid transparent; border-radius:0px;}")
        #self.ui.listWidget.addItem(QListWidgetItem('Pear'))

        font = QtGui.QTextCharFormat()
        font.setFontPointSize(10)
        font.setFontFamily("霞鹜新晰黑")
        font.setFontWeight(1)
        self.ui.textEdit.setCurrentCharFormat(font)

        self.ui.textBrowser.setOpenExternalLinks(True)
        self.ui.textBrowser.setReadOnly(True)
        self.ui.textBrowser.document().setDefaultStyleSheet("a{text-decoration:none;color:rgb(95, 117, 140);background-color:white;}")
        #self.ui.textBrowser.setStyleSheet("{border:0px;border-color:rgb(95, 117, 140)}")

        self.scalenum=1

        # 设置无边框圆角带阴影窗口
        #self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 无边框
        # ===============透明阴影====================
        self.ui.textBrowser.setAutoFillBackground(True) #一定要加上
        self.ui.textEdit.setAutoFillBackground(True)
        #self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 窗口透明
        shadow=QGraphicsDropShadowEffect()  # 创建阴影
        shadow.setBlurRadius(20)  # 设置阴影大小为9px
        shadow.setColor(QColor("#444444"))  # 设置颜色透明度为100的（0,0,0）黑色
        shadow.setOffset(0,0)  # 阴影偏移距离为0px
        self.ui.textBrowser.setGraphicsEffect(shadow)  # 添加阴影
        
        #self.ui.textEdit.setGraphicsEffect(shadow)  # 添加阴影
        #self.ui.listWidget.setGraphicsEffect(shadow)  # 添加阴影
        
        self.del_shadow(self.ui.listWidget)
        self.del_shadow(self.ui.textEdit)
        self.del_shadow(self.ui.textBrowser)
        self.ui.listWidget.itemClicked.connect(self.on_item_clicked)
        self.ui.pushButton_2.clicked.connect(self.set)
       
        #self.auto_resize()
        #self.auto_resize(0.9)
        #self.auto_resize(0.6)
        
        #self.showFullScreen()
        #print(self.windowState())


        #获取组件初始位置和大小
        self.window_width = self.width()
        self.window_height = self.height()
        rect=[]
        for widget in self.findChildren(QWidget):
            rect.append(widget.geometry())
        self.default_rect=rect
        
        #self.fsize=10
        self.auto_resize(self.size)
        self.new_tab(self.choose)

    def keyPressEvent(self,event):
        #print("按下：" + str(event.key()))
        if event.key() == 16777249 and self.size<1:
            #按下：16777248:
            #print("按下了ctrl键")
            self.size+=0.1
            
            
        if event.key() == 16777248 and self.size>0.3:
            #按下：16777248:
            #print("按下了shift键")
            self.size-=0.1
        #if event.key() == 16777252:
            #self.additon += 1
        self.size = round(self.size,1)
        self.auto_resize(self.size)
        #self.new_tab(self.choose)
        #self.on_selection_changed()
        self.fresh()
        print(f'size_now: {self.size}')
        

    def auto_resize(self,size=0.6):
        
        size=self.size
        self.setdata['size']=self.size
        with open(r'setting.json','w') as f:
            json.dump(self.setdata,f)

        # 获取窗口原来大小
        # default = 1088 x 612
        #default_width=1088
        #default_height=612
        
        #把获取当前改成以初始状态为基准就ok了
        window_width = self.window_width
        window_height = self.window_height

        # 获取屏幕大小
        screen = QDesktopWidget().availableGeometry()
        #print(window_width,window_height,screen.width(),screen.height())
        screen_width = screen.width()
        screen_height = screen.height()
        # 自定义新窗口大小
        new_window_width = int(screen_width * size)
        resize_rate = new_window_width / window_width  # 确定放大比例
        new_window_height = int(window_height * resize_rate)  # 确定新窗口高度
        # 重新调整窗口大小并移动到屏幕中心
        self.resize(new_window_width, new_window_height)
        #self.move((screen_width - new_window_width) // 2, (screen_height - new_window_height) // 3)
        # 重新调整子控件位置大小
        #fsize=int(-23.33*(size**2)+28.996*size)
        if size> 0.6:
            fsize=int(10*size)+3
        elif size== 0.6:
            fsize=10
        else:
            fsize=int(9*size/0.6)+1
              
        for widget,rect in zip(self.findChildren(QWidget),self.default_rect):
            #rect = widget.geometry()
            widget.setGeometry(QtCore.QRect(
                int(rect.x() * resize_rate),
                int(rect.y() * resize_rate),
                int(rect.width() * resize_rate),
                int(rect.height() * resize_rate),))
            if widget in [self.ui.label,self.ui.label_2,self.ui.pushButton]:
                #print(widget)
                font = QtGui.QFont()                
                font.setPointSize(fsize)
                font.setFamily('Microsoft YaHei')
                #font.setFamily("Microsoft YaHei")
                #font.setBold(True)
                #font.setWeight(75)
                widget.setFont(font)
            if widget == self.ui.tableWidget:
                pass
                #会导致无法更新？不知道为什么
                #点击行后（on_selection_changed）之后列宽会失效保持之前的列宽
                '''
                item = QtWidgets.QTableWidgetItem()
                font = QtGui.QFont()
                font.setFamily("Microsoft YaHei")
                font.setBold(True)
                font.setWeight(fsize)
                item.setFont(font)
                item.setBackground(QtGui.QColor(230, 230, 230))
                brush = QtGui.QBrush(QtGui.QColor(95, 117, 140))
                brush.setStyle(QtCore.Qt.SolidPattern)
                item.setForeground(brush)
                item.setText(("类型"))
                widget.setHorizontalHeaderItem(0, item)

                
                item = widget.horizontalHeaderItem(0)
                item.setText(("类型"))
                item = widget.horizontalHeaderItem(1)
                item.setText(("日期"))
                item = widget.horizontalHeaderItem(2)
                item.setText(("标题"))
                item = widget.horizontalHeaderItem(3)
                item.setText(("来源"))
                '''
                #更新行高
                if self.size>=0.6:
                    add=self.size
                else:
                    add=5*(self.size-0.6)
                row_height = 50+10*add+self.additon
                #print(f'更新行高 {row_height}')
                #int(50*12/fsize)
                widget.verticalHeader().setDefaultSectionSize(int(row_height))
                widget.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Custom)
                
            if widget == self.ui.listWidget:
                f = QtGui.QFont()
                f.setFamily("Microsoft YaHei")
                f.setPointSize(fsize)
                #f.setBold(True)
                #f.setWeight(75)
                widget.setFont(f)
            if widget == self.ui.textBrowser:
                f = QtGui.QFont()
                f.setFamily("Microsoft YaHei")
                f.setBold(True)
                f.setPointSize(fsize)
                widget.setFont(f)
            if widget ==self.ui.textEdit:
                f = QtGui.QTextCharFormat()
                # 10
                f.setFontPointSize(int(fsize/9*10))
                f.setFontFamily(self.font)
                f.setFontWeight(1)
                widget.setCurrentCharFormat(f)
            [self.ui.tableWidget,self.ui.textEdit]
        self.fsize=fsize
        #print(f'当前字号： {fsize}')
    

    def fresh(self):
        #self.label.setText('Thread finished.')
        print('更新数据',end=' ')
        self.new_tab(self.choose)
        try:
            #更新摘要文字和链接
            self.ui.textBrowser.clear()
            self.ui.textEdit.clear()
            self.ui.textEdit.setPlainText('      '+self.abstr_cache)
            self.ui.textBrowser.append(self.net_cache)
        except:
            pass

    def del_shadow(self,button):#删除阴影
        self.effect_shadow = QGraphicsDropShadowEffect(self)
        self.effect_shadow.setOffset(0,0)  # 偏移
        self.effect_shadow.setBlurRadius(2)  # 阴影半径
        self.effect_shadow.setColor(QColor("#444444"))  # 阴影颜色
        button.setGraphicsEffect(self.effect_shadow)  # 将设置套用到button窗口中
    
    def on_item_clicked(self, item):
        #切换tsv
        self.choose=item.text()
        self.setdata['file']=self.choose
        with open(r'setting.json','w') as f:
            json.dump(self.setdata,f)
        print(f"选择文件： {self.choose}", end='\t')
        self.new_tab(self.choose)
        try:
            self.ui.textBrowser.clear()
            self.ui.textBrowser.append(self.net)
        except:
            pass
    def on_selection_changed(self):
        #选择文献
        self.ui.textBrowser.clear()
        self.ui.textEdit.clear()
        selected_cells = self.ui.tableWidget.selectedItems()
        # autosize后选择会丢失，压根不执行if后面的
        if selected_cells:
            self.cell=selected_cells[0]
            #print(f"序号：{self.cell.row()+1}")
            #self.ui.textEdit.setPlainText('摘要：\n      '+self.abstr.loc[self.cell.row(),'摘要'])
            self.ui.textEdit.setPlainText('      '+self.abstr.loc[self.cell.row(),'摘要'])
            adress=self.abstr.loc[self.cell.row(),'链接']
            #print(adress)
            self.net="<a href=\""+adress+"\">&emsp;CNKI链接跳转</a>"
            self.ui.textBrowser.append(self.net)
            self.abstr_cache=str(self.abstr.loc[self.cell.row(),'摘要'])
            self.net_cache=str(self.net)
    def set(self):
        self.setting=setting_windows()
        self.setting.show()
        ff=QtGui.QFont()
        ff.setFamily(self.font)
        self.setting.fontComboBox.setCurrentFont(ff)
        self.setting.spinBox.setValue(self.additon)

        self.setting.buttonBox.clicked.connect(self.save)
        self.setting.buttonBox.rejected.connect(self.cancel)
    def save(self):
        self.additon=self.setting.spinBox.value()
        self.font=self.setting.fontComboBox.currentFont().family()
        self.auto_resize(self.size)
        self.fresh()
        self.setdata['font']=self.font
        self.setdata['additon']=self.additon
        with open(r'setting.json','w') as f:
            json.dump(self.setdata,f)
        
    def cancel(self):
        self.setting.close()
    def new_tab(self,file='A_Sample.tsv'):
        self.ui.tableWidget.clearContents()
        self.ui.tableWidget.setRowCount(0)

        self.ui.listWidget.clear()

        self.choose=file
        file=file
        try:
            df=pd.read_csv(file, sep='\t',encoding = 'gbk')
        except Exception as e:
            print(e)
            df=pd.DataFrame({'序号':['0','1'],'日期':['2020/9/28','2019/2/5'],'来源':['上海米哈游','美国艺电EA'],
                             '标题':['原神启动','《Apex英雄》评测:3A品质的FPS游戏'],'类型':['硕士','期刊'],
                             '摘要':['你说的对，但是《原神》是由米哈游自主研发的一款全新开放世界冒险游戏。游戏发生在一个被称作‘提瓦特’的幻想世界，在这里，被神选中的人将被授予‘神之眼’，导引元素之力。你将扮演一位名为‘旅行者’的神秘角色，在自由的旅行中邂逅性格各异、能力独特的同伴们，和他们一起击败强敌，找回失散的亲人——同时，逐步发掘‘原神’的真相。',
                                    '“准星，有的枪可能是三角形的，你可以把他对到人身上，你就可以打到人了知道吧。方形的也可以，你只要把他框住就好了，更简单，你是不是连框都没有框住呢，就是移过去，然后你点开枪就可以了，没有别的事情需要你担心的，就你不需要做心算，不需要做算数题什么的，也不需要充钱，你直接开枪就可以了，没有那么多别的事情需要你担心的，你知道吗，有没有可能是你框的不够准呢，就如果你看到人的时候再开枪，不要说是人不在你的框里面就开枪，可以吗？可以这样吗？额…有明白吗？需要我单独做一个噼哩噼哩教程吗？上传一下子需要吗？就是做一个文图版本的，就是告诉你怎么把这个准星移到别人身上的这个事情，需要知道吗？我教你啊这游戏能走路可以按WASD能走路你知道吧，把路走明白可以吗？”'],
                             '链接':['https://ys.mihoyo.com/','https://www.ea.com/games/apex-legends?isLocalized=true']})
            df.to_csv('A_Sample.tsv', sep='\t',index=False,encoding='gbk')
            
        riqi=df.loc[:,'日期']
        theriqi=[]
        #我也不知道-哪来的
        for i in range(len(df)):
            word=riqi.loc[i]
            #print(word)
            try:
                num=word.split('/')
            except:
                continue
            if len(num)<2:
                num=word.split('-')
            #print(num)
            if len(num[1])==1:
                num[1]='0'+num[1]
            if len(num[2])==1:
                num[2]='0'+num[2]
            word=num[0]+'-'+num[1]+'-'+num[2]
            theriqi.append(word)
        theriqi=pd.DataFrame(theriqi,columns=['日期'])
        df.loc[:,'日期']=theriqi
        # 创建一个映射函数
        map_function = lambda key: 3 if key == '期刊' else (2 if key == '硕士' else (1 if key == '博士' else None))
        # 添加一个排序用的辅助列
        df['类型排序列'] = df['类型'].map(map_function)
        #print(df.loc[:,'日期'])
        df.sort_values(by=['类型排序列','日期'],inplace=True,ascending=False) 
        #内容变了，索引没变，重置索引
        df.reset_index(drop=True,inplace=True)
        #print(df.loc[:,'日期'])
        self.abstr=df.loc[:,['摘要','链接']]
        df=df.loc[:,['类型','日期','标题','来源']]
        #print(list(df.loc[0]))
        #print('共{}篇文献'.format(len(df)))

        items=df
        
        #items = [['燕十三','21','Male','武林大侠'],['萧十一郎','21','Male','武功好']]
        
        font = QtGui.QFont()
        font.setPointSize(self.fsize)
        font.setFamily("霞鹜新晰黑")
        font.setBold(True)
        font.setWeight(12)

        #cs=cscd.loc[cscd['库标识']=='核心库']
        css=list(self.cscd.loc[:,'期刊名称'])
        for i in range(len(items)):
            item = items.loc[i]
            row = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row)
            #self.ui.tableWidget.setRowsWidth(i, 20)
            for j in range(len(item)):
                item = QtWidgets.QTableWidgetItem(str(items.loc[i][j]))
                self.ui.tableWidget.setItem(row,j,item)
                item.setFont(font)
                #item.setTextAlignment(QtCore.Qt.AlignTop | QtCore.Qt.TextWordWrap)
                if j == 3 and str(items.loc[i][j]) in css:
                    #print(items.loc[i][j]) #核心期刊名
                    item.setForeground(QColor(192, 0, 0))
                if j != 2:
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        length = self.ui.tableWidget.fontMetrics().averageCharWidth()
        #length = self.fsize
        #print('字符长度：{}'.format(length))
        bili=self.fsize/9

        self.ui.tableWidget.setColumnWidth(0, int(6*length*bili))
        self.ui.tableWidget.setColumnWidth(1, int(14*length*bili))
        #似乎是下面这行的问题
        #self.ui.tableWidget.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        #self.ui.tableWidget.setColumnWidth(3, 12*length)
        #self.ui.tableWidget.setColumnWidth(2, 300)

        #表index的位数
        s=int(math.log10(len(df)))
        if self.size <= 0.5:
            g = int(3*length*bili)
        else:
            g = 0        
        title_length = self.ui.tableWidget.width()-int(18*length*bili)-self.ui.tableWidget.columnWidth(0)-self.ui.tableWidget.columnWidth(1)-int(s*22)+g
        self.ui.tableWidget.setColumnWidth(2, title_length)
        #print(f'title_length: {title_length}',end='\t')
        #print(f'{[self.ui.tableWidget.width(),int(18*length*bili),self.ui.tableWidget.columnWidth(0),self.ui.tableWidget.columnWidth(1)]}',end='\t')
        #莫名其妙，其实完全没必要考虑滚动条长度，不知道哪抄的
        #self.ui.tableWidget.verticalScrollBar().width(), horizontalScrollBar
        
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(3,QHeaderView.Stretch)

        #os.walk疑似内部有文件夹才能生效
        path=os.getcwd()
        files = [os.path.join(file) for file in os.listdir(path)]
        # 遍历文件列表，输出文件名
            
        for i in files:
            if 'tsv' in i:
                #print(i)
                self.ui.listWidget.addItem(QListWidgetItem(i))
        

        

'''
def netsearch(theme,numbers):#网络搜索
    #global theme,number
    try:
        number=int(numbers)
    except:
        print('请输入数字')
    print('文献主题：{}\n查找数量：{}\n'.format(theme,number))
    search(theme,number)
'''    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = mainWindow()
    theui = main.ui
    #new_tab(theui)
    main.show()
    sys.exit(app.exec_())   

