# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'masterpasswordcreation.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(248, 204)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout.addWidget(self.frame_3, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)
        self.frame_5 = QtWidgets.QFrame(Form)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout.addWidget(self.frame_5, 10, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 1, 1, 1)
        self.confirmPasswordLineEdit = QtWidgets.QLineEdit(Form)
        self.confirmPasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmPasswordLineEdit.setObjectName("confirmPasswordLineEdit")
        self.gridLayout.addWidget(self.confirmPasswordLineEdit, 6, 1, 1, 1)
        self.frame_4 = QtWidgets.QFrame(Form)
        self.frame_4.setMaximumSize(QtCore.QSize(100, 16777215))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout.addWidget(self.frame_4, 3, 2, 1, 1)
        self.showPasswordCheckBox = QtWidgets.QCheckBox(Form)
        self.showPasswordCheckBox.setObjectName("showPasswordCheckBox")
        self.gridLayout.addWidget(self.showPasswordCheckBox, 4, 1, 1, 1)
        self.createPasswordLineEdit = QtWidgets.QLineEdit(Form)
        self.createPasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.createPasswordLineEdit.setObjectName("createPasswordLineEdit")
        self.gridLayout.addWidget(self.createPasswordLineEdit, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        self.saveButton = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.saveButton.setFont(font)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout.addWidget(self.saveButton, 8, 1, 1, 1)
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout.addWidget(self.frame_2, 3, 0, 1, 1)
        self.showPassword2CheckBox = QtWidgets.QCheckBox(Form)
        self.showPassword2CheckBox.setObjectName("showPassword2CheckBox")
        self.gridLayout.addWidget(self.showPassword2CheckBox, 7, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Confirm your master password below"))
        self.confirmPasswordLineEdit.setPlaceholderText(_translate("Form", "password..."))
        self.showPasswordCheckBox.setText(_translate("Form", "Show Password"))
        self.createPasswordLineEdit.setPlaceholderText(_translate("Form", "password..."))
        self.label.setText(_translate("Form", "PASSWORD MANAGER"))
        self.label_2.setText(_translate("Form", "Create your master password below"))
        self.saveButton.setText(_translate("Form", "Save"))
        self.showPassword2CheckBox.setText(_translate("Form", "Show Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())