# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(757, 434)
        self.login = QtWidgets.QPushButton(Dialog)
        self.login.setGeometry(QtCore.QRect(90, 170, 113, 32))
        self.login.setObjectName("login")
        self.id = QtWidgets.QLineEdit(Dialog)
        self.id.setGeometry(QtCore.QRect(150, 50, 113, 21))
        self.id.setObjectName("id")
        self.password = QtWidgets.QLineEdit(Dialog)
        self.password.setGeometry(QtCore.QRect(150, 80, 113, 21))
        self.password.setObjectName("password")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 50, 60, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 80, 60, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 115, 82, 18))
        self.label_3.setObjectName("label_3")
        self.file_open = QtWidgets.QPushButton(Dialog)
        self.file_open.setGeometry(QtCore.QRect(150, 110, 113, 32))
        self.file_open.setObjectName("file_open")
        self.file_name = QtWidgets.QLabel(Dialog)
        self.file_name.setGeometry(QtCore.QRect(20, 150, 711, 16))
        self.file_name.setText("")
        self.file_name.setObjectName("file_name")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(80, 10, 131, 16))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.login.setText(_translate("Dialog", "로그인"))
        self.label.setText(_translate("Dialog", "아이디"))
        self.label_2.setText(_translate("Dialog", "비밀번호"))
        self.label_3.setText(_translate("Dialog", "크롬 드라이버"))
        self.file_open.setText(_translate("Dialog", "파일 찾기"))
        self.label_4.setText(_translate("Dialog", "쿠팡 장바구니 매크로"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
