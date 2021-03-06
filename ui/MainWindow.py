# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1019, 644)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/wafer_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setMaximumSize(QtCore.QSize(250, 16777215))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.treeWidget = QtWidgets.QTreeWidget(self.splitter)
        self.treeWidget.setMaximumSize(QtCore.QSize(270, 16777215))
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.frame = QtWidgets.QFrame(self.splitter)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.graphicsView = QtWidgets.QGraphicsView(self.splitter_2)
        self.graphicsView.setMinimumSize(QtCore.QSize(0, 0))
        self.graphicsView.setObjectName("graphicsView")
        self.tabWidget = QtWidgets.QTabWidget(self.splitter_2)
        self.tabWidget.setMaximumSize(QtCore.QSize(300, 16777215))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.comboBox_selected_lot = QtWidgets.QComboBox(self.tab)
        self.comboBox_selected_lot.setObjectName("comboBox_selected_lot")
        self.gridLayout_2.addWidget(self.comboBox_selected_lot, 0, 0, 1, 1)
        self.comboBox_selected_wafer = QtWidgets.QComboBox(self.tab)
        self.comboBox_selected_wafer.setObjectName("comboBox_selected_wafer")
        self.gridLayout_2.addWidget(self.comboBox_selected_wafer, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.toolButton_back = QtWidgets.QToolButton(self.tab)
        self.toolButton_back.setMinimumSize(QtCore.QSize(0, 0))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/Sign-left.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_back.setIcon(icon1)
        self.toolButton_back.setIconSize(QtCore.QSize(35, 35))
        self.toolButton_back.setObjectName("toolButton_back")
        self.horizontalLayout.addWidget(self.toolButton_back)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.toolButton_forward = QtWidgets.QToolButton(self.tab)
        self.toolButton_forward.setMinimumSize(QtCore.QSize(0, 0))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/Sign-right.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_forward.setIcon(icon2)
        self.toolButton_forward.setIconSize(QtCore.QSize(35, 35))
        self.toolButton_forward.setObjectName("toolButton_forward")
        self.horizontalLayout.addWidget(self.toolButton_forward)
        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.pushButton_next = QtWidgets.QPushButton(self.tab)
        self.pushButton_next.setObjectName("pushButton_next")
        self.gridLayout_2.addWidget(self.pushButton_next, 3, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_Reset = QtWidgets.QPushButton(self.tab)
        self.pushButton_Reset.setObjectName("pushButton_Reset")
        self.verticalLayout.addWidget(self.pushButton_Reset)
        self.pushButton_read_csv = QtWidgets.QPushButton(self.tab)
        self.pushButton_read_csv.setObjectName("pushButton_read_csv")
        self.verticalLayout.addWidget(self.pushButton_read_csv)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 188, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout.addWidget(self.splitter_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1019, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WaferMap"))
        self.toolButton_back.setText(_translate("MainWindow", "..."))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.toolButton_forward.setText(_translate("MainWindow", "..."))
        self.pushButton_next.setText(_translate("MainWindow", "Next Wafer"))
        self.pushButton_Reset.setText(_translate("MainWindow", "Reset"))
        self.pushButton_read_csv.setText(_translate("MainWindow", "Read .csv"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Selection"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Setting"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Data"))

from ui import source_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
