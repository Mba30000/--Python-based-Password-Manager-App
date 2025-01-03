from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog, QFileDialog, QTreeWidgetItem, QShortcut
from pathlib import Path
from PyQt5.QtCore import QSettings
from PyQt5.QtGui import QKeySequence, QIcon
import sys

# Third party modules
from addEditPassword import Ui_Form as add_edit_password
from CreateMP import Ui_Form as createMP
from GeneratePassword import Ui_Form as generatePass
from main import Ui_MainWindow as mainpage
from AuthMP import Ui_Form as masterpassEntry
from Url_input import Ui_Form as Url_input
from ViewOld import Ui_Form as View_old_passwords
from relocate import Ui_Form as relocate_account


# User Defined modules
from passwordManager import Password_Manager
from fileloader import save, open

class MyApp(QDialog):
    def __init__(self):
        super().__init__()

        self.database = Password_Manager()
        
        self.num = 1
        self.counter = self.counter_for_new_cat()
        self.acc_num = 1
        self.acc_counter = self.counter_for_new_acc()
        self.path = False

        # setup and open mainpage
        self.mainwindow = QtWidgets.QMainWindow()
        self.main = mainpage()
        self.main.setupUi(self.mainwindow)
        self.mainwindow.show()

        #Buttons for mainpage
        self.main.actionOpen_local_File.triggered.connect(self.open_local_file)
        self.main.actionOpen_URL.triggered.connect(self.open_url)
        self.main.actionSave.triggered.connect(self.save)
        self.main.actionChange_Master_Password.triggered.connect(self.save)
        self.main.actionSave_as_Local_File.triggered.connect(self.save_as)
        self.main.actionDefault.triggered.connect(self.DefaultTheme)
        self.main.actionDark.triggered.connect(self.DarkTheme)
        self.main.addCategoryButton.clicked.connect(self.add_category)
        self.main.addPasswordButton.clicked.connect(self.add_account)
        self.main.deleteCategoryButton.clicked.connect(self.del_category)
        self.main.deletePasswordButton.clicked.connect(self.del_account)
        self.main.copyPasswordButton.clicked.connect(self.copy_password)
        self.main.editPasswordButton.clicked.connect(self.edit_password)
        self.main.accountsTreeWidget.doubleClicked.connect(self.edit_password)
        self.main.clearButton.clicked.connect(self.clear_search)
        self.main.categoriesTree.itemChanged.connect(self.check_category_name, QtCore.Qt.ConnectionType.QueuedConnection)
        self.main.categoriesTree.currentItemChanged.connect(self.check_cat_names_when_unselected)
        self.main.categoriesTree.itemSelectionChanged.connect(self.selected_category)
        self.main.accountsTreeWidget.itemSelectionChanged.connect(self.selected_account)
        self.main.searchTextEdit.textChanged.connect(self.search)
        self.main.accountsTreeWidget.hideColumn(3)
        self.main.categoriesTree.itemChanged.connect(self.change_title)


        self.selectedCat = self.main.categoriesTree.topLevelItem(0)
        self.category_title = self.selectedCat.text(0)
        self.main.categoriesTree.setCurrentItem(self.selectedCat)
        self.main.deleteCategoryButton.setEnabled(False)
        self.main.deletePasswordButton.setEnabled(False)
        self.main.editPasswordButton.setEnabled(False)
        self.main.copyPasswordButton.setEnabled(False)

        # setup account modifiction window
        self.addEditWindow = QtWidgets.QWidget()
        self.add_edit = add_edit_password()
        self.add_edit.setupUi(self.addEditWindow)

        # buttons for setting up an account
        self.add_edit.SaveCloseButton.clicked.connect(self.save_close)
        self.add_edit.generateButton.clicked.connect(self.generate)
        self.add_edit.viewOldButton.clicked.connect(self.viewOld)
        self.add_edit.showPasswordLineEdit.clicked.connect(self.showpassword)

        # setup password generation window
        self.generateWindow = QtWidgets.QWidget()
        self.gen = generatePass()
        self.gen.setupUi(self.generateWindow)

        # buttons for generation window
        self.gen.numbersCheckbox.setChecked(True)
        self.gen.lowerCaseCheckbox.setChecked(True)
        self.gen.okButton.clicked.connect(self.specify)

        # setup masterpassword (MP) creation window
        self.createMPWindow = QtWidgets.QWidget()
        self.createMP = createMP()
        self.createMP.setupUi(self.createMPWindow)

        # buttons for creating masterpassword
        self.createMP.saveButton.clicked.connect(self.confirm_password_validation)
        self.createMP.showPasswordCheckBox.clicked.connect(self.showmasterpassword_confimation)
        self.createMP.showPassword2CheckBox.clicked.connect(self.showmasterpassword_confimation)

        # setup masterpassword (MP) authentication window
        self.MPWindow = QtWidgets.QWidget()
        self.MP = masterpassEntry()
        self.MP.setupUi(self.MPWindow)

        # buttons for entering masterpassword
        self.MP.showPasswordCheckbox.clicked.connect(self.showmasterpassword)
        

        # setup url entry
        self.Url_window = QtWidgets.QLineEdit()
        self.Url_lineEdit = Url_input()
        self.Url_lineEdit.setupUi(self.Url_window)

        # button for URL
        self.Url_lineEdit.Url_button.clicked.connect(self.take_user_input_URL)

        # setup for old pass window
        self.viewOldPassWindow = QtWidgets.QWidget()
        self.view_old = View_old_passwords()
        self.view_old.setupUi(self.viewOldPassWindow)

        # button for old pass window
        self.view_old.Close_button.clicked.connect(self.return_to_account_editing)

        # setup for restore window
        self.restoreWindow = QtWidgets.QWidget()
        self.restore = relocate_account()
        self.restore.setupUi(self.restoreWindow)

        # button for Resotre window
        self.restore.cancelButton.clicked.connect(self.restoreWindow.close)
        self.restore.OKbutton.clicked.connect(self.restore_accounts)

        # shortcuts
        self.shortcut_save = QShortcut(QKeySequence('Ctrl+S'), self.mainwindow)
        self.shortcut_save_as = QShortcut(QKeySequence('Ctrl+Shift+S'), self.mainwindow)
        self.shortcut_copy_pass = QShortcut(QKeySequence('Ctrl+C'), self.mainwindow)
        self.shortcut_open_local = QShortcut(QKeySequence('Ctrl+O'), self.mainwindow)
        self.shortcut_open_url = QShortcut(QKeySequence('Ctrl+Shift+O'), self.mainwindow)
        self.shortcut_new_acc = QShortcut(QKeySequence('Ctrl+N'), self.mainwindow)

        self.shortcut_save.activated.connect(self.save)
        self.shortcut_save_as.activated.connect(self.save_as)
        self.shortcut_copy_pass.activated.connect(self.copy_password)
        self.shortcut_open_local.activated.connect(self.open_local_file)
        self.shortcut_open_url.activated.connect(self.open_url)
        self.shortcut_new_acc.activated.connect(self.add_account)

        # Previous them loader
        try:
            if self.database.check_theme_prefrences() == 1:
                self.DarkTheme()
            else:
                self.DefaultTheme()
        except:
            pass

        # CLA
        QtCore.QTimer.singleShot(4, self.open_with_cl)
#--------------------------------------------------------------------------------------------------------
# Import and Export Methods
#--------------------------------------------------------------------------------------------------------
    def open_with_cl(self):
        if len(sys.argv) < 3:
                if len(sys.argv) == 1:
                    pass
                else:
                    self.path = sys.argv[1]
                    if self.path  == '':
                        self.path = False
                        return
                    else: 
                        self.MPWindow.setWindowModality(QtCore.Qt.ApplicationModal)
                        self.MPWindow.show()     
        else:
            error_msg = QMessageBox()
            error_msg.setWindowTitle("Error")
            error_msg.setText("File is corrupted")
            error_msg.setIcon(QMessageBox.Warning)
            error_msg.setStandardButtons(QMessageBox.Ok)
            error_msg.show()
            error_msg.exec_()
            error_msg.buttonClicked.connect(lambda: error_msg.close())
            self.MPWindow.setWindowModality(QtCore.Qt.ApplicationModal)
            self.MPWindow.show()

    def showmasterpassword(self):
        if self.MP.showPasswordCheckbox.isChecked() == True:
            self.MP.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.MP.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        
    def showmasterpassword_confimation(self):
        if self.createMP.showPasswordCheckBox.isChecked() == True:
            self.createMP.createPasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.createMP.createPasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        if self.createMP.showPassword2CheckBox.isChecked() == True:
            self.createMP.confirmPasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.createMP.confirmPasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)

    def showpassword(self):
        if self.add_edit.showPasswordLineEdit.isChecked() == True:
            self.add_edit.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.add_edit.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)

    def change_title(self):
        self.category_title
        for i in range(self.main.accountsTreeWidget.topLevelItemCount()):
            cat = self.main.accountsTreeWidget.topLevelItem(i).text(3)
            if cat == self.category_title:
                self.main.accountsTreeWidget.topLevelItem(i).setText(3, self.main.categoriesTree.topLevelItem(self.category_index).text(0)) 

    def open_local_file(self):
        self.file = QFileDialog.getOpenFileName(self, "open file", filter="*.pm")
        self.path = self.file[0]
        if self.path  == '':
            self.path = False
            return
        else: 
            self.MP.passwordLineEdit.clear()
            self.MPWindow.show()
        self.MP.okButton.clicked.connect(self.return_opened_local_file)

    def return_opened_local_file(self):
        path = self.path
        masterpassword = self.MP.passwordLineEdit.text()
        try:
            self.database = self.database.Open(path, masterpassword)
            self.MPWindow.close()
            self.refrsh_ui()
        except:
            error_msg = QMessageBox()
            error_msg.setWindowTitle("Error")
            error_msg.setText("Wrong Password! Try again")
            error_msg.setIcon(QMessageBox.Warning)
            error_msg.setStandardButtons(QMessageBox.Ok)
            error_msg.show()
            error_msg.exec_()
            error_msg.buttonClicked.connect(lambda: error_msg.close())
            self.MPWindow.show()
        self.accounts_buttons_disabler()
        self.selected_account()
        self.search_show_hide()

        for i in range(self.main.accountsTreeWidget.topLevelItemCount()):
            if self.main.accountsTreeWidget.topLevelItem(i).text(3) != "General":
                self.main.accountsTreeWidget.topLevelItem(i).setHidden(True)

    def open_url(self):
        self.Url_lineEdit.Url_user_input.clear()
        self.Url_window.show()
        #https://drive.google.com/uc?export=download&id=1cG9--QdFiISlU0omzhbcQokAA8BwCSEQ
        
    def take_user_input_URL(self):
        if self.Url_lineEdit.Url_button.clicked:
            self.Url_window.close()
            self.MP.passwordLineEdit.clear()
            self.MPWindow.show()
        self.MP.okButton.clicked.connect(self.import_data)

    def import_data(self):
        Url_ = self.Url_lineEdit.Url_user_input.text()
        masterpassword = self.MP.passwordLineEdit.text()
        try:
            self.database = self.database.import_Url_file(Url_, masterpassword)
            self.MPWindow.close()
            self.refrsh_ui()

            self.main.statusbar.showMessage("Successfully imported")
            QtTest.QTest.qWait(2000)
            self.main.statusbar.showMessage("")

            self.MP.passwordLineEdit.clear()
            self.Url_lineEdit.Url_user_input.clear()
        except:
            error_msg = QMessageBox()
            error_msg.setWindowTitle("Error")
            error_msg.setText("Wrong Password! Try again")
            error_msg.setIcon(QMessageBox.Warning)
            error_msg.setStandardButtons(QMessageBox.Ok)
            error_msg.show()
            error_msg.exec_()
            error_msg.buttonClicked.connect(lambda: error_msg.close())
            self.MPWindow.show()
        self.accounts_buttons_disabler()
        self.selected_account()
        self.search_show_hide()

    def refrsh_ui(self):
        self.main.categoriesTree.clear()
        self.main.accountsTreeWidget.clear()
        for i in range(len(self.database.categories)):
            category_name = self.database.categories[i].Title
            category = QTreeWidgetItem()
            category.setText(0,category_name)
            self.main.categoriesTree.addTopLevelItem(category)
            for j in range(len(self.database.categories[i].Accounts)):
                Tag = self.database.categories[i].Accounts[j].Tag
                Username = self.database.categories[i].Accounts[j].Username
                Url = self.database.categories[i].Accounts[j].Url
                account = QTreeWidgetItem()
                
                account.setText(0,Tag)
                account.setText(1,Username)
                account.setText(2,Url)
                account.setText(3,category_name)
                self.main.accountsTreeWidget.addTopLevelItem(account)

    def save(self):
        self.createMP.createPasswordLineEdit.clear()
        self.createMP.confirmPasswordLineEdit.clear()
        if self.path == False:
            self.save_as()
        else:
            self.createMP.createPasswordLineEdit.clear()
            self.createMP.confirmPasswordLineEdit.clear()
            self.createMPWindow.setWindowModality(QtCore.Qt.ApplicationModal)
            self.createMPWindow.show()
       

    def save_as(self):
        file = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', filter = "*.pm")
        if file[0] == '':
            return
        self.path = file[0]

        self.createMP.createPasswordLineEdit.clear()
        self.createMP.confirmPasswordLineEdit.clear()
        self.createMPWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        self.createMPWindow.show()

    def confirm_password_validation(self):

        chosen_master_password = self.createMP.createPasswordLineEdit.text()
        confirmed_master_password = self.createMP.confirmPasswordLineEdit.text()

        if chosen_master_password=="" or confirmed_master_password == "":
            error_msg = QMessageBox()
            error_msg.setWindowTitle("Error")
            error_msg.setText("Missing Feilds")
            error_msg.setIcon(QMessageBox.Warning)
            error_msg.setStandardButtons(QMessageBox.Ok)
            error_msg.show()
            error_msg.exec_()
            error_msg.buttonClicked.connect(lambda: error_msg.close())
            self.createMPWindow.setWindowModality(QtCore.Qt.ApplicationModal)
            self.createMPWindow.show()
        elif chosen_master_password != confirmed_master_password:
            error_msg = QMessageBox()
            error_msg.setWindowTitle("Error")
            error_msg.setText("The two passwords you entered must match")
            error_msg.setIcon(QMessageBox.Warning)
            error_msg.setStandardButtons(QMessageBox.Ok)
            error_msg.show()
            error_msg.exec_()
            error_msg.buttonClicked.connect(lambda: error_msg.close())
            self.createMPWindow.setWindowModality(QtCore.Qt.ApplicationModal)
            self.createMPWindow.show()
        elif len(chosen_master_password) <8:
            error_msg = QMessageBox()
            error_msg.setWindowTitle("Error")
            error_msg.setText("Master Password must be at least 8 charecters long")
            error_msg.setIcon(QMessageBox.Warning)
            error_msg.setStandardButtons(QMessageBox.Ok)
            error_msg.show()
            error_msg.exec_()
            error_msg.buttonClicked.connect(lambda: error_msg.close())
            self.createMPWindow.setWindowModality(QtCore.Qt.ApplicationModal)
            self.createMPWindow.show()
        elif chosen_master_password == confirmed_master_password:
            masterpassword = confirmed_master_password
            self.database.save_as(self.path, masterpassword) 
            self.createMPWindow.close()  

            self.main.statusbar.showMessage("Successfully Saved")
            QtTest.QTest.qWait(2000)
            self.main.statusbar.showMessage("")

#------------------------------------------------------------------------------------------------------------
# Editing and Browsing Database
#-------------------------------------------------------------------------------------------------------------
    def check_category_name(self):
        try:
            self.num = 1
            current_item = self.main.categoriesTree.currentItem()
            x = self.main.categoriesTree.findItems(f"{current_item.text(0)}", QtCore.Qt.MatchFlag.MatchRegularExpression,0)
            for j in range(len(x)):
                dupli_num = j
            for i in range(self.main.categoriesTree.topLevelItemCount()):    
                if current_item == self.main.categoriesTree.topLevelItem(0) or current_item == self.main.categoriesTree.topLevelItem(1):
                    return
                elif current_item.text(0) == self.main.categoriesTree.topLevelItem(i).text(0) and current_item != self.main.categoriesTree.topLevelItem(i):
                    self.title = f"{current_item.text(0)}({j})"
                    error_msg = QMessageBox()
                    error_msg.setWindowTitle("Error")
                    error_msg.setText(f"Duplicate categories are not allowed\n The title will be changed to {current_item.text(0)}({j})")
                    error_msg.setIcon(QMessageBox.Warning)
                    error_msg.setStandardButtons(QMessageBox.Ok)
                    error_msg.setWindowModality(QtCore.Qt.ApplicationModal)
                    error_msg.show()
                    result = error_msg.exec_()
                    if result == QMessageBox.Ok:
                        z = self.duplicate_name_change(current_item)
                        current_item.setText(0,z)
                        error_msg.buttonClicked.connect(lambda: error_msg.close())

                elif current_item.text(0) == "" or current_item.text(0) == " ":
                    error_msg = QMessageBox()
                    error_msg.setWindowTitle("Error")
                    error_msg.setText("Cannot leave category name empty")
                    error_msg.setIcon(QMessageBox.Warning)
                    error_msg.setStandardButtons(QMessageBox.Ok)
                    error_msg.setWindowModality(QtCore.Qt.ApplicationModal)
                    error_msg.show()
                    error_msg.exec_()
                    error_msg.buttonClicked.connect(lambda: error_msg.close())
                    current_item.setData(0,0,"Type Here")
                    self.main.categoriesTree.editItem(current_item, 0)

                else: self.title = f"{current_item.text(0)}"
            self.database.edit_category(self.title, self.category_index)
        except:
            pass
    
    def check_cat_names_when_unselected(self):
        try:
            for i in range(self.main.categoriesTree.topLevelItemCount()):
                self.database.categories[i].Title = self.main.categoriesTree.topLevelItem(i).text(0)
        except:
            pass
    
    def duplicate_name_change(self,category_obj) -> str:
                x = self.main.categoriesTree.findItems(f"{category_obj.text(0)}", QtCore.Qt.MatchFlag.MatchRegularExpression,0)
                for j in range(len(x)):
                    dupli_name = f"{category_obj.text(0)}({j})"
                return dupli_name

    def add_category(self):

        category_name = QtWidgets.QTreeWidgetItem()
        category_name.setFlags(category_name.flags() | QtCore.Qt.ItemIsEditable)
        x = self.main.categoriesTree.findItems("New_Category", QtCore.Qt.MatchFlag.MatchRegularExpression,0)
        if x == []:
            category_name.setText(0,"New_Category")
            self.main.categoriesTree.addTopLevelItem(category_name)
        elif "New_Category" in x[0].text(0):
            for j in range(len(x)):
                category_name.setText(0,f"New_Category({j+1})")
            self.main.categoriesTree.addTopLevelItem(category_name)

        self.database.add_category(category_name.text(0))


    def del_category(self):
        self.selected_category()
        for i in range(self.main.accountsTreeWidget.topLevelItemCount()):
            print(self.main.accountsTreeWidget.topLevelItem(i).text(3), self.category_title)
            if self.main.accountsTreeWidget.topLevelItem(i).text(3) == self.category_title:
                self.main.accountsTreeWidget.topLevelItem(i).setText(3, "Recently Deleted")
        self.database.del_category(self.category_index)
        self.main.categoriesTree.takeTopLevelItem(self.category_index)

    def restore_accounts(self):
        try:
            new_dist = self.restore.CategoriesList.currentItem().text()

            self.selectedAcc.setText(3, new_dist)
            self.refresh_accounts_treewidget()

            for i in range(len(self.database.categories)):
                if new_dist == self.database.categories[i].Title:
                    index = i 
                    break

            self.database.relocate(index, self.acc_tag_name)
            self.restoreWindow.close()
        except:
            error_msg = QMessageBox()
            error_msg.setWindowTitle("Error")
            error_msg.setText("Either select a category or cancel")
            error_msg.setIcon(QMessageBox.Warning)
            error_msg.setStandardButtons(QMessageBox.Ok)
            error_msg.show()
            error_msg.exec_()
            error_msg.buttonClicked.connect(lambda: error_msg.close())
            self.restoreWindow.close()
            self.restoreWindow.setWindowModality(QtCore.Qt.ApplicationModal)
            self.restoreWindow.show()
        self.accounts_buttons_disabler()


    def del_account(self):
        
        if self.category_title == "Recently Deleted":
            self.database.del_account(1, self.acc_tag_name)
            self.main.accountsTreeWidget.takeTopLevelItem(self.acc_index) 
        else:
            self.database.del_account(self.category_index, self.acc_tag_name)
            self.main.accountsTreeWidget.topLevelItem(self.acc_index).setText(3, "Recently Deleted")
            self.refresh_accounts_treewidget()
        self.selected_account()
        self.accounts_buttons_disabler()
        

    def copy_password(self):
        try:
            acc_index = self.database.get_account_index(self.category_index, self.acc_tag_name)
            copied = self.database.categories[self.category_index].Accounts[acc_index].Password[-1]

            copy = QApplication.clipboard()
            copy.clear(mode = copy.Clipboard)
            copy.setText(copied, mode = copy.Clipboard)

            self.main.statusbar.showMessage("Copied")
            QtTest.QTest.qWait(2000)
            self.main.statusbar.showMessage("")
        except:
            print("password not found")

    def clear_search(self):
        self.main.searchTextEdit.setText("")
        x = self.main.categoriesTree.currentItem()
        self.main.categoriesTree.setCurrentItem(x)

    def search(self):
        tag_list = []
        Object = []

        for i in range(self.main.accountsTreeWidget.topLevelItemCount()):
            tag_list.append([self.main.accountsTreeWidget.topLevelItem(i).text(0).lower(), self.main.accountsTreeWidget.topLevelItem(i).text(1).lower(), self.main.accountsTreeWidget.topLevelItem(i).text(2).lower()])

        Search_key = self.main.searchTextEdit.text()
        for j in range(self.main.accountsTreeWidget.topLevelItemCount()):

            if Search_key == " " or Search_key == "":
                if self.main.actionDefault.isChecked() == True:
                    print(self.main.actionDefault.isChecked())
                    self.main.searchTextEdit.setStyleSheet("color: black;")
                elif self.main.actionDark.isChecked() == True:
                    self.main.searchTextEdit.setStyleSheet("color: rgb(200, 200, 200);")
                self.search_show_hide()

            elif Search_key.lower() not in "".join(tag_list[j]):
                self.main.searchTextEdit.setStyleSheet("color: red;")
                self.main.accountsTreeWidget.topLevelItem(j).setHidden(True)
                for k in range(self.main.accountsTreeWidget.topLevelItemCount()):
                    Object.append(self.main.accountsTreeWidget.topLevelItem(k).isHidden())
                if all(Object) == True:
                    self.main.searchTextEdit.setStyleSheet("color: red;")
                elif all(Object) != True:
                    if self.main.actionDefault.isChecked() == True:
                        self.main.searchTextEdit.setStyleSheet("color: black;")
                    elif self.main.actionDark.isChecked() == True:
                        self.main.searchTextEdit.setStyleSheet("color: rgb(200, 200, 200);")
                    
            elif Search_key.lower() in "".join(tag_list[j]):
                if self.main.actionDefault.isChecked() == True:
                        self.main.searchTextEdit.setStyleSheet("color: black;")
                elif self.main.actionDark.isChecked() == True:
                        self.main.searchTextEdit.setStyleSheet("color: rgb(200, 200, 200);") 
                self.main.accountsTreeWidget.topLevelItem(j).setHidden(False)

    def search_show_hide(self):
        for i in range(self.main.accountsTreeWidget.topLevelItemCount()):
            try:
                if self.main.accountsTreeWidget.topLevelItem(i).text(3) != self.category_title:
                    self.main.accountsTreeWidget.topLevelItem(i).setHidden(True)
                else:
                    self.main.accountsTreeWidget.topLevelItem(i).setHidden(False)
            except:
                if self.main.accountsTreeWidget.topLevelItem(i).text(3) != "General":
                    self.main.accountsTreeWidget.topLevelItem(i).setHidden(True)
                else:
                    self.main.accountsTreeWidget.topLevelItem(i).setHidden(False)

    def refresh_accounts_treewidget(self):
        for i in range(self.main.accountsTreeWidget.topLevelItemCount()):
            acc_cat = self.main.accountsTreeWidget.topLevelItem(i).text(3)
            if acc_cat == self.category_title:
                self.main.accountsTreeWidget.topLevelItem(i).setHidden(False)
            else:
                self.main.accountsTreeWidget.topLevelItem(i).setHidden(True)

    def accounts_buttons_disabler(self):
        if self.database.categories[self.category_index].Accounts == []:
            self.main.editPasswordButton.setEnabled(False)
            self.main.copyPasswordButton.setEnabled(False)
            self.main.deletePasswordButton.setEnabled(False)
        else:
            self.main.editPasswordButton.setEnabled(True)
            self.main.copyPasswordButton.setEnabled(True)
            self.main.deletePasswordButton.setEnabled(True)

    def selected_category(self):
        self.selectedCat = self.main.categoriesTree.currentItem()
        self.category_title = self.selectedCat.text(0)
        self.category_index = self.main.categoriesTree.indexOfTopLevelItem(self.selectedCat)
        
        try:
            self.main.accountsTreeWidget.setCurrentItem(self.main.accountsTreeWidget.topLevelItem(-1))
            self.accounts_buttons_disabler()
            self.selected_account()
        except:
            pass
        
        if self.category_index == 0:
            self.selectedCat.setFlags(self.selectedCat.flags() & ~QtCore.Qt.ItemIsEditable)
            self.main.editPasswordButton.setText("Edit Password")
            self.main.addPasswordButton.setEnabled(True)
            self.main.deleteCategoryButton.setEnabled(False)
        elif self.category_index == 1:
            self.main.editPasswordButton.setText("Restore Account")
            self.selectedCat.setFlags(self.selectedCat.flags() & ~QtCore.Qt.ItemIsEditable)
            self.main.addPasswordButton.setEnabled(False)
            self.main.deleteCategoryButton.setEnabled(False)
        else:
            self.main.editPasswordButton.setText("Edit Password")
            self.main.deleteCategoryButton.setEnabled(True)
            self.selectedCat.setFlags(self.selectedCat.flags() | QtCore.Qt.ItemIsEditable)
            self.main.addPasswordButton.setEnabled(True)

        self.check_category_name()
        self.refresh_accounts_treewidget()             
            
    def selected_account(self):
        try:
            self.selectedAcc = self.main.accountsTreeWidget.currentItem()
            self.acc_tag_name = self.selectedAcc.text(0)
            self.acc_index = self.main.accountsTreeWidget.indexOfTopLevelItem(self.selectedAcc)
            self.main.deletePasswordButton.setEnabled(True)
            self.main.editPasswordButton.setEnabled(True)
            self.main.copyPasswordButton.setEnabled(True)
            if self.category_index == 1:
                self.main.addPasswordButton.setEnabled(False)
            else:
                self.main.addPasswordButton.setEnabled(True)
        except:
            self.main.editPasswordButton.setEnabled(False)
            self.main.copyPasswordButton.setEnabled(False)
            self.main.deletePasswordButton.setEnabled(False)
            if self.category_index == 1:
                self.main.addPasswordButton.setEnabled(False)

        self.check_category_name 

    def add_account(self):
        self.edit = False
        self.addEditWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        self.addEditWindow.show()
        self.add_edit.tagLineEdit.clear()
        self.add_edit.usernameLineEdit.clear()
        self.add_edit.passwordLineEdit.clear()
        self.add_edit.urlLineEdit.clear()
        self.add_edit.viewOldButton.setEnabled(False)

    def edit_password(self):
        
        if self.main.editPasswordButton.text() == "Restore Account":
            self.restore.CategoriesList.clear()
            for i in range(len(self.database.categories)):
                if i == 1: continue
                self.restore.CategoriesList.addItem(self.database.categories[i].Title)
            self.restoreWindow.setWindowModality(QtCore.Qt.ApplicationModal)
            self.restoreWindow.show()

            
        else:
            self.add_edit.viewOldButton.setEnabled(True)
            self.edit = True
            self.addEditWindow.setWindowModality(QtCore.Qt.ApplicationModal)
            self.addEditWindow.show()

            acc_index = self.database.get_account_index(self.category_index, self.main.accountsTreeWidget.topLevelItem(self.acc_index).text(0))

            self.old_tag = self.database.categories[self.category_index].Accounts[acc_index].Tag
            username = self.database.categories[self.category_index].Accounts[acc_index].Username
            password = self.database.categories[self.category_index].Accounts[acc_index].Password[-1]
            URL = self.database.categories[self.category_index].Accounts[acc_index].Url
        
            self.add_edit.tagLineEdit.setText(self.old_tag)
            self.add_edit.usernameLineEdit.setText(username)
            self.add_edit.passwordLineEdit.setText(password)
            self.add_edit.urlLineEdit.setText(URL)


    def save_close(self):
        tag = self.add_edit.tagLineEdit.text()
        username = self.add_edit.usernameLineEdit.text()
        password = self.add_edit.passwordLineEdit.text()
        URL = self.add_edit.urlLineEdit.text()

        if tag == "" or username == "" or password == "" or URL == "":
            error_msg = QMessageBox()
            error_msg.setWindowTitle("Error")
            error_msg.setText("You can't leave anything empty")
            error_msg.setIcon(QMessageBox.Warning)
            error_msg.setStandardButtons(QMessageBox.Ok)
            error_msg.show()
            error_msg.exec_()
            error_msg.buttonClicked.connect(lambda: error_msg.close())
        else:
            self.add_edit.showPasswordLineEdit.setChecked(False)
            if self.edit == True:
                
                try:
                    self.database.edit_account(self.category_index, self.old_tag, tag, username, password, URL)
                    self.main.accountsTreeWidget.topLevelItem(self.acc_index).setText(0, tag)
                    self.main.accountsTreeWidget.topLevelItem(self.acc_index).setText(1, username)
                    self.main.accountsTreeWidget.topLevelItem(self.acc_index).setText(2, URL)
                    self.main.accountsTreeWidget.topLevelItem(self.acc_index).setText(3, self.category_title)
                    self.addEditWindow.close()
                except:
                    error_msg = QMessageBox()
                    error_msg.setWindowTitle("Error")
                    error_msg.setText("The tag must have a unique title")
                    error_msg.setIcon(QMessageBox.Warning)
                    error_msg.setStandardButtons(QMessageBox.Ok)
                    error_msg.show()
                    error_msg.exec_()
                    error_msg.buttonClicked.connect(lambda: error_msg.close())
            else:
                
                try:
                    self.database.add_account(self.category_index, tag, username, password, URL)
                    new_item = QtWidgets.QTreeWidgetItem()
                    new_item.setText(0, tag)
                    new_item.setText(1, username)
                    new_item.setText(2, URL)
                    new_item.setText(3, self.category_title)
                    self.main.accountsTreeWidget.addTopLevelItem(new_item)
                    self.addEditWindow.close()
                except:
                    error_msg = QMessageBox()
                    error_msg.setWindowTitle("Error")
                    error_msg.setText("The tag must have a unique title")
                    error_msg.setIcon(QMessageBox.Warning)
                    error_msg.setStandardButtons(QMessageBox.Ok)
                    error_msg.show()
                    error_msg.exec_()
                    error_msg.buttonClicked.connect(lambda: error_msg.close())
        self.accounts_buttons_disabler()
        self.selected_account()

    def viewOld(self):
        self.view_old.listWidget.clear()
        self.viewOldPassWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        self.viewOldPassWindow.show()
        account_index = self.database.get_account_index(self.category_index, self.acc_tag_name)
        for i in range(len(self.database.categories[self.category_index].Accounts[account_index].Password)-1):
            older_pass = self.database.categories[self.category_index].Accounts[account_index].Password[i]
            self.view_old.listWidget.addItem(older_pass)
        
    
    def return_to_account_editing(self):
        self.viewOldPassWindow.close()
        

    def generate(self):
        self.generateWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        self.generateWindow.show()

    def specify(self):
        include = []
        
        if self.gen.specifyCharecterNumberCheckBox.isChecked() == True:
            length = self.gen.CharecterNumberLineEdit.text()
        else:
            length = 8

        if self.gen.symbolsCheckbox.isChecked() == True:
            symbols = self.gen.symbolsLineEdit.text()
            include.append(0)
        else:
            symbols = False
            if 0 in include:
                include.pop(0)

        if self.gen.upperCaseCheckbox.isChecked() == True:
            include.append(1)
            
        if self.gen.numbersCheckbox.isChecked() == True:
            include.append(2)

        if self.gen.lowerCaseCheckbox.isChecked() == True:
            include.append(3)
        try:
            password = self.database.generate(include, length, symbols)
            self.add_edit.passwordLineEdit.setText(password)
            self.generateWindow.close()
            self.gen.numbersCheckbox.setChecked(True)
            self.gen.lowerCaseCheckbox.setChecked(True)
            self.gen.upperCaseCheckbox.setChecked(False)
            self.gen.symbolsCheckbox.setChecked(False)
            self.gen.specifyCharecterNumberCheckBox.setChecked(False)

            self.gen.CharecterNumberLineEdit.setText("")
            self.gen.symbolsLineEdit.setText("")
        except:
            error_msg = QMessageBox()
            error_msg.setWindowTitle("Error")
            error_msg.setText("You forgot to specify the number of charecters or symbols\n uncheck the box if this doesn't matter")
            error_msg.setIcon(QMessageBox.Warning)
            error_msg.setStandardButtons(QMessageBox.Ok)
            error_msg.show()
            error_msg.exec_()
            error_msg.buttonClicked.connect(lambda: error_msg.close())
            self.generateWindow.show()
            self.gen.specifyCharecterNumberCheckBox.setChecked(False)
            self.gen.symbolsCheckbox.setChecked(False)
    
    def counter_for_new_cat(self):
        while True:
            yield self.num
            self.num += 1

    def counter_for_new_acc(self):
        while True:
            yield self.acc_num
            self.acc_num += 1

#--------------------------------------------------------------------------------------------------------------
# setting themes
#--------------------------------------------------------------------------------------------------------------

    def DefaultTheme(self):
        self.main.actionDark.setChecked(False)
        self.main.actionDefault.setChecked(True)

        self.main.accountsTreeWidget.setStyleSheet("")
        self.main.categoriesTree.setStyleSheet("")
        self.main.accountsTreeWidget.setStyleSheet("")

        self.main.frame.setStyleSheet("")
        self.main.frame_2.setStyleSheet("")
        self.main.frame_3.setStyleSheet("")
        self.main.frame_4.setStyleSheet("")
        self.main.frame_5.setStyleSheet("")
        self.main.frame_7.setStyleSheet("")


        self.mainwindow.setStyleSheet("")
        self.addEditWindow.setStyleSheet("")
        self.generateWindow.setStyleSheet("")
        self.createMPWindow.setStyleSheet("")
        self.MPWindow.setStyleSheet("")
        self.Url_window.setStyleSheet("")
        self.restoreWindow.setStyleSheet("")
        self.viewOldPassWindow.setStyleSheet("")
        self.main.searchTextEdit.setStyleSheet("")

        self.main.addCategoryButton.setStyleSheet("")
        self.main.addPasswordButton.setStyleSheet("")
        self.main.editPasswordButton.setStyleSheet("")
        self.main.deleteCategoryButton.setStyleSheet("")
        self.main.deletePasswordButton.setStyleSheet("")
        self.main.clearButton.setStyleSheet("")
        self.main.copyPasswordButton.setStyleSheet("")

        self.database.theme_prefrences("DefultMode")

    def DarkTheme(self):
        self.main.actionDefault.setChecked(False)
        self.main.actionDark.setChecked(True)
        self.main.categoriesTree.setStyleSheet("QHeaderView::section { background-color: rgb(70, 70, 70);color: rgb(200, 200, 200) }")
        self.main.accountsTreeWidget.setStyleSheet("QHeaderView::section { background-color: rgb(70, 70, 70);color: rgb(200, 200, 200) }")

        self.main.frame.setStyleSheet("QTreeWidget { background-color: rgb(35, 35, 35); color: rgb(200, 200, 200);};")
        self.main.frame_2.setStyleSheet("QTreeWidget { background-color: rgb(35, 35, 35); color: rgb(200, 200, 200)};")
        self.main.frame_3.setStyleSheet("QTreeWidget { background-color: rgb(35, 35, 35); color: rgb(200, 200, 200)};")
        self.main.frame_4.setStyleSheet("QTreeWidget { background-color: rgb(35, 35, 35); color: rgb(200, 200, 200)};")
        self.main.frame_5.setStyleSheet("QTreeWidget { background-color: rgb(35, 35, 35); color: rgb(200, 200, 200)};")
        self.main.frame_7.setStyleSheet("QTreeWidget { background-color: rgb(35, 35, 35); color: rgb(200, 200, 200)};")
        
        self.mainwindow.setStyleSheet(" background-color: rgb(50, 50, 50); color: rgb(200, 200, 200) ")
        self.addEditWindow.setStyleSheet(" background-color: rgb(50, 50, 50); color: rgb(200, 200, 200) ")
        self.generateWindow.setStyleSheet(" background-color: rgb(50, 50, 50); color: rgb(200, 200, 200) ")
        self.createMPWindow.setStyleSheet(" background-color: rgb(50, 50, 50); color: rgb(200, 200, 200) ")
        self.MPWindow.setStyleSheet(" background-color: rgb(50, 50, 50); color: rgb(200, 200, 200) ")
        self.Url_window.setStyleSheet(" background-color: rgb(50, 50, 50); color: rgb(200, 200, 200) ")
        self.restoreWindow.setStyleSheet(" background-color: rgb(50, 50, 50); color: rgb(200, 200, 200) ")
        self.viewOldPassWindow.setStyleSheet(" background-color: rgb(50, 50, 50); color: rgb(200, 200, 200) ")
        

        self.main.searchTextEdit.setStyleSheet("QLineEdit {background-color: rgb(35, 35, 35); color: rgb(200, 200, 200)}")

        self.main.addCategoryButton.setStyleSheet("QPushButton::enabled { background-color: rgb(50, 50, 50);}")
        self.main.addPasswordButton.setStyleSheet("QPushButton:disabled { background-color: rgb(20, 20, 20); color: rgb(50, 50, 50)};QPushButton:enabled { background-color: rgb(50, 50, 50); border: 1px solid white}")
        self.main.editPasswordButton.setStyleSheet("QPushButton:disabled { background-color: rgb(20, 20, 20); color: rgb(50, 50, 50)};QPushButton:enabled { background-color: rgb(50, 50, 50); border: 1px solid white}")
        self.main.deleteCategoryButton.setStyleSheet("QPushButton:disabled { background-color: rgb(20, 20, 20); color: rgb(50, 50, 50)};QPushButton:enabled { background-color: rgb(50, 50, 50); border: 1px solid white}")
        self.main.deletePasswordButton.setStyleSheet("QPushButton:disabled { background-color: rgb(20, 20, 20); color: rgb(50, 50, 50)};QPushButton:enabled { background-color: rgb(50, 50, 50); border: 1px solid white}")
        self.main.copyPasswordButton.setStyleSheet("QPushButton:disabled { background-color: rgb(20, 20, 20); color: rgb(50, 50, 50)}; QPushButton:enabled { background-color: rgb(50, 50, 50); border: 1px solid white}")
        self.main.clearButton.setStyleSheet("QPushButton::enabled { background-color: rgb(50, 50, 50); min-width: 72px; min-height: 18px}")
        self.add_edit.viewOldButton.setStyleSheet("QPushButton::enabled { background-color: rgb(50, 50, 50);}")
        self.add_edit.viewOldButton.setStyleSheet("QPushButton:disabled { background-color: rgb(20, 20, 20); color: rgb(50, 50, 50)};QPushButton:enabled { background-color: rgb(50, 50, 50); border: 1px solid white}")

        self.database.theme_prefrences("DarkMode")



app = QApplication(sys.argv)
run = MyApp()
app.exec_()



