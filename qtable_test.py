import sys
import pandas as pd
from PyQt5.QtCore import Qt, QAbstractTableModel, QModelIndex, QEvent
from PyQt5.QtWidgets import (QApplication, QTableView, QStyleOptionViewItem, 
                             QStyledItemDelegate, QStyle, QHeaderView, 
                             QLineEdit, QLabel, QVBoxLayout, QWidget)
from PyQt5.QtGui import QColor, QPalette, QBrush, QKeySequence

class HighlightSelectionDelegate(QStyledItemDelegate):
    """自定义委托用于改变选中行的背景色"""
    def initStyleOption(self, option, index):
        super().initStyleOption(option, index)
        
        # 获取视图
        view = option.widget
        if not view:
            return
            
        # 检查整行是否被选中
        if view.selectionModel().isRowSelected(index.row(), QModelIndex()):
            # 设置选中行的背景色
            option.backgroundBrush = QBrush(QColor("#e6f7ff"))  # 浅蓝色
            option.palette.setBrush(QPalette.Highlight, QBrush(QColor("#1890ff")))  # 深蓝色边框
            option.palette.setBrush(QPalette.HighlightedText, QBrush(Qt.white))  # 白色文字
    
    def createEditor(self, parent, option, index):
        """创建编辑器时设置初始文本并全选"""
        editor = QLineEdit(parent)
        editor.setText(index.data())  # 设置当前文本
        editor.selectAll()  # 全选文本以便复制
        return editor

class PandasTableModel(QAbstractTableModel):
    """支持复制的Pandas数据模型"""
    def __init__(self, df):
        super().__init__()
        self._df = df.copy()

    def rowCount(self, parent=None):
        return self._df.shape[0]

    def columnCount(self, parent=None):
        return self._df.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
            
        row = index.row()
        col = index.column()
        
        if role == Qt.DisplayRole or role == Qt.EditRole:
            return str(self._df.iloc[row, col])
            
        return None

    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole:
            return None
            
        if orientation == Qt.Horizontal:
            return str(self._df.columns[section])
        return str(self._df.index[section])

    def flags(self, index):
        """启用选择标志和文本复制功能"""
        flags = super().flags(index)
        flags |= Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemNeverHasChildren
        flags |= Qt.ItemIsEditable  # 允许编辑以便选择文本
        return flags

class DataFrameTableView(QTableView):
    """增强功能的表格视图"""
    def __init__(self, df, parent=None):
        super().__init__(parent)
        
        # 设置模型
        self.model = PandasTableModel(df)
        self.setModel(self.model)
        
        # 设置选择行为
        self.setSelectionBehavior(QTableView.SelectRows)  # 点击单元格时选择整行
        self.setSelectionMode(QTableView.SingleSelection)  # 单行选择
        
        # 设置自定义委托
        self.delegate = HighlightSelectionDelegate()
        self.setItemDelegate(self.delegate)
        
        # 优化表格显示
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        self.verticalHeader().setVisible(False)
        self.setAlternatingRowColors(True)
        self.setStyleSheet("""
            QTableView {
                gridline-color: #e0e0e0;
                alternate-background-color: #f9f9f9;
                selection-background-color: #1890ff;
                selection-color: white;
            }
            QTableView::item {
                padding: 4px;
            }
        """)
        
        # 启用文本选择
        self.setTextElideMode(Qt.ElideRight)
        self.setWordWrap(False)
        
        # 设置双击选择文本 - 使用自定义处理
        self.setEditTriggers(QTableView.SelectedClicked | QTableView.DoubleClicked)
        
        # 添加键盘快捷键支持
        self.setupKeyboardShortcuts()
        
        # 连接双击信号
        self.doubleClicked.connect(self.handleDoubleClick)
    
    def setupKeyboardShortcuts(self):
        """设置复制快捷键"""
        from PyQt5.QtWidgets import QShortcut
        # Ctrl+C 复制
        QShortcut(QKeySequence.Copy, self, self.copySelection)
    
    def copySelection(self):
        """复制选中内容到剪贴板"""
        selection = self.selectedIndexes()
        if not selection:
            return
            
        # 获取选中的行和列
        rows = set(index.row() for index in selection)
        cols = set(index.column() for index in selection)
        
        # 按行和列排序
        rows_sorted = sorted(rows)
        cols_sorted = sorted(cols)
        
        # 构建复制的文本
        text = ""
        for row in rows_sorted:
            row_data = []
            for col in cols_sorted:
                index = self.model.index(row, col)
                row_data.append(self.model.data(index, Qt.DisplayRole))
            text += "\t".join(row_data) + "\n"
        
        # 复制到剪贴板
        QApplication.clipboard().setText(text.strip())
    
    def handleDoubleClick(self, index):
        """处理双击事件 - 显示编辑器但不进入编辑状态"""
        if index.isValid():
            # 打开编辑器并立即关闭，以便选择文本
            self.openPersistentEditor(index)
            self.closePersistentEditor(index)
            
            # 手动选择单元格文本
            item_text = self.model.data(index, Qt.DisplayRole)
            if item_text:
                # 模拟文本选择
                self.edit(index)
                editor = self.findChild(QLineEdit)
                if editor:
                    editor.setText(item_text)
                    editor.selectAll()
    
    def event(self, event):
        """拦截事件以处理文本选择"""
        # 处理鼠标释放事件以保持文本选择
        if event.type() == QEvent.MouseButtonRelease:
            index = self.indexAt(event.pos())
            if index.isValid():
                self.selectionModel().select(index, self.selectionModel().Rows)
        return super().event(event)

# 示例用法
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    file=r'CNKI_浮游植物.tsv'
    df=pd.read_csv(file, sep='\t',encoding = 'gbk')
    
    # 创建表格视图
    view = DataFrameTableView(df)
    view.setWindowTitle("增强型数据表格视图")
    view.resize(800, 500)
    
    # 自动调整列宽
    view.resizeColumnsToContents()
    
    # 添加说明标签
    widget = QWidget()
    layout = QVBoxLayout()
    info_label = QLabel("🖱️ 单击单元格选择整行 | 🖱️🖱️ 双击单元格选择文本 | Ctrl+C 复制选中内容")
    info_label.setStyleSheet("font-weight: bold; padding: 8px; background: #f0f8ff;")
    layout.addWidget(info_label)
    layout.addWidget(view)
    widget.setLayout(layout)
    
    widget.show()
    sys.exit(app.exec_())