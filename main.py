# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 538)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 300))
        MainWindow.setInputMethodHints(QtCore.Qt.ImhNone)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(600, 300))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_7 = QtWidgets.QFrame(self.frame)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.searchTextEdit = QtWidgets.QLineEdit(self.frame_7)
        self.searchTextEdit.setMinimumSize(QtCore.QSize(0, 20))
        self.searchTextEdit.setObjectName("searchTextEdit")
        self.horizontalLayout_3.addWidget(self.searchTextEdit)
        self.clearButton = QtWidgets.QPushButton(self.frame_7)
        self.clearButton.setObjectName("clearButton")
        self.horizontalLayout_3.addWidget(self.clearButton)
        self.verticalLayout.addWidget(self.frame_7)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setMinimumSize(QtCore.QSize(300, 0))
        self.frame_3.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.categoriesTree = QtWidgets.QTreeWidget(self.frame_3)
        self.categoriesTree.setMinimumSize(QtCore.QSize(130, 0))
        self.categoriesTree.setStyleSheet("")
        self.categoriesTree.setColumnCount(1)
        self.categoriesTree.setObjectName("categoriesTree")
        item_0 = QtWidgets.QTreeWidgetItem(self.categoriesTree)
        item_0 = QtWidgets.QTreeWidgetItem(self.categoriesTree)
        self.categoriesTree.header().setCascadingSectionResizes(False)
        self.categoriesTree.header().setDefaultSectionSize(75)
        self.verticalLayout_2.addWidget(self.categoriesTree)
        self.addCategoryButton = QtWidgets.QPushButton(self.frame_3)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addCategoryButton.setIcon(icon)
        self.addCategoryButton.setIconSize(QtCore.QSize(14, 14))
        self.addCategoryButton.setObjectName("addCategoryButton")
        self.verticalLayout_2.addWidget(self.addCategoryButton)
        self.deleteCategoryButton = QtWidgets.QPushButton(self.frame_3)
        self.deleteCategoryButton.setObjectName("deleteCategoryButton")
        self.verticalLayout_2.addWidget(self.deleteCategoryButton)
        self.horizontalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setMaximumSize(QtCore.QSize(1500, 16777215))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.accountsTreeWidget = QtWidgets.QTreeWidget(self.frame_4)
        self.accountsTreeWidget.setObjectName("accountsTreeWidget")
        self.verticalLayout_3.addWidget(self.accountsTreeWidget)
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.editPasswordButton = QtWidgets.QPushButton(self.frame_5)
        self.editPasswordButton.setMinimumSize(QtCore.QSize(0, 25))
        self.editPasswordButton.setMaximumSize(QtCore.QSize(200, 100))
        self.editPasswordButton.setObjectName("editPasswordButton")
        self.horizontalLayout_4.addWidget(self.editPasswordButton)
        self.copyPasswordButton = QtWidgets.QPushButton(self.frame_5)
        self.copyPasswordButton.setMinimumSize(QtCore.QSize(0, 25))
        self.copyPasswordButton.setMaximumSize(QtCore.QSize(200, 100))
        self.copyPasswordButton.setObjectName("copyPasswordButton")
        self.horizontalLayout_4.addWidget(self.copyPasswordButton)
        self.addPasswordButton = QtWidgets.QPushButton(self.frame_5)
        self.addPasswordButton.setMinimumSize(QtCore.QSize(0, 25))
        self.addPasswordButton.setMaximumSize(QtCore.QSize(200, 100))
        self.addPasswordButton.setIcon(icon)
        self.addPasswordButton.setIconSize(QtCore.QSize(14, 14))
        self.addPasswordButton.setObjectName("addPasswordButton")
        self.horizontalLayout_4.addWidget(self.addPasswordButton)
        self.deletePasswordButton = QtWidgets.QPushButton(self.frame_5)
        self.deletePasswordButton.setMaximumSize(QtCore.QSize(200, 100))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.deletePasswordButton.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.deletePasswordButton.setFont(font)
        self.deletePasswordButton.setFlat(False)
        self.deletePasswordButton.setObjectName("deletePasswordButton")
        self.horizontalLayout_4.addWidget(self.deletePasswordButton)
        self.verticalLayout_3.addWidget(self.frame_5)
        self.horizontalLayout.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.frame_2)
        self.horizontalLayout_2.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 18))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuTheme = QtWidgets.QMenu(self.menuSettings)
        self.menuTheme.setObjectName("menuTheme")
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen_local_File = QtWidgets.QAction(MainWindow)
        self.actionOpen_local_File.setObjectName("actionOpen_local_File")
        self.actionOpen_URL = QtWidgets.QAction(MainWindow)
        self.actionOpen_URL.setObjectName("actionOpen_URL")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as_Local_File = QtWidgets.QAction(MainWindow)
        self.actionSave_as_Local_File.setObjectName("actionSave_as_Local_File")
        self.actionAdd_Cat = QtWidgets.QAction(MainWindow)
        self.actionAdd_Cat.setObjectName("actionAdd_Cat")
        self.actionDelete_Cat = QtWidgets.QAction(MainWindow)
        self.actionDelete_Cat.setObjectName("actionDelete_Cat")
        self.actionChange_Master_Password = QtWidgets.QAction(MainWindow)
        self.actionChange_Master_Password.setObjectName("actionChange_Master_Password")
        self.actionAutoSave = QtWidgets.QAction(MainWindow)
        self.actionAutoSave.setCheckable(True)
        self.actionAutoSave.setChecked(False)
        self.actionAutoSave.setObjectName("actionAutoSave")
        self.actionDark = QtWidgets.QAction(MainWindow)
        self.actionDark.setCheckable(True)
        self.actionDark.setObjectName("actionDark")
        self.actionNeon = QtWidgets.QAction(MainWindow)
        self.actionNeon.setObjectName("actionNeon")
        self.actionCottonCandy = QtWidgets.QAction(MainWindow)
        self.actionCottonCandy.setObjectName("actionCottonCandy")
        self.actionKau = QtWidgets.QAction(MainWindow)
        self.actionKau.setObjectName("actionKau")
        self.actionDefault = QtWidgets.QAction(MainWindow)
        self.actionDefault.setCheckable(True)
        self.actionDefault.setChecked(True)
        self.actionDefault.setObjectName("actionDefault")
        self.actionDataStream = QtWidgets.QAction(MainWindow)
        self.actionDataStream.setObjectName("actionDataStream")
        self.menuFile.addAction(self.actionOpen_local_File)
        self.menuFile.addAction(self.actionOpen_URL)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as_Local_File)
        self.menuTheme.addAction(self.actionDefault)
        self.menuTheme.addAction(self.actionDark)
        self.menuSettings.addAction(self.menuTheme.menuAction())
        self.menuSettings.addAction(self.actionChange_Master_Password)
        self.menuSettings.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.searchTextEdit.setPlaceholderText(_translate("MainWindow", "search..."))
        self.clearButton.setText(_translate("MainWindow", "Clear"))
        self.categoriesTree.headerItem().setText(0, _translate("MainWindow", "Categories"))
        __sortingEnabled = self.categoriesTree.isSortingEnabled()
        self.categoriesTree.setSortingEnabled(False)
        self.categoriesTree.topLevelItem(0).setText(0, _translate("MainWindow", "General"))
        self.categoriesTree.topLevelItem(1).setText(0, _translate("MainWindow", "Recently Deleted"))
        self.categoriesTree.setSortingEnabled(__sortingEnabled)
        self.addCategoryButton.setText(_translate("MainWindow", "Add Category"))
        self.deleteCategoryButton.setText(_translate("MainWindow", "Delete Category"))
        self.accountsTreeWidget.headerItem().setText(0, _translate("MainWindow", "TAG/Label"))
        self.accountsTreeWidget.headerItem().setText(1, _translate("MainWindow", "Username"))
        self.accountsTreeWidget.headerItem().setText(2, _translate("MainWindow", "URL"))
        self.accountsTreeWidget.headerItem().setText(3, _translate("MainWindow", "Cat"))
        self.editPasswordButton.setText(_translate("MainWindow", "Edit Password"))
        self.copyPasswordButton.setText(_translate("MainWindow", "Copy Password"))
        self.addPasswordButton.setText(_translate("MainWindow", "Add Password"))
        self.deletePasswordButton.setText(_translate("MainWindow", "Delete Password"))
        self.menuFile.setTitle(_translate("MainWindow", "File "))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuTheme.setTitle(_translate("MainWindow", "Theme"))
        self.actionOpen_local_File.setText(_translate("MainWindow", "Open local File"))
        self.actionOpen_URL.setText(_translate("MainWindow", "Open URL "))
        self.actionSave.setText(_translate("MainWindow", "Save "))
        self.actionSave_as_Local_File.setText(_translate("MainWindow", "Save as Local File"))
        self.actionAdd_Cat.setText(_translate("MainWindow", "Edit Category"))
        self.actionDelete_Cat.setText(_translate("MainWindow", "Delete Category"))
        self.actionChange_Master_Password.setText(_translate("MainWindow", "Change Master Password"))
        self.actionAutoSave.setText(_translate("MainWindow", "AutoSave"))
        self.actionDark.setText(_translate("MainWindow", "Dark"))
        self.actionNeon.setText(_translate("MainWindow", "Neon"))
        self.actionCottonCandy.setText(_translate("MainWindow", "CottonCandy"))
        self.actionKau.setText(_translate("MainWindow", "Kau"))
        self.actionDefault.setText(_translate("MainWindow", "Default"))
        self.actionDataStream.setText(_translate("MainWindow", "Futuristic"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
