# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'py_manage.ui',
# licensing of 'py_manage.ui' applies.
#
# Created: Sat Dec  7 18:20:13 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(702, 578)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.py_box = QtWidgets.QComboBox(Form)
        self.py_box.setObjectName("py_box")
        self.horizontalLayout_3.addWidget(self.py_box)
        self.py_setting_btn = QtWidgets.QToolButton(Form)
        self.py_setting_btn.setObjectName("py_setting_btn")
        self.horizontalLayout_3.addWidget(self.py_setting_btn)
        self.horizontalLayout_3.setStretch(1, 9)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.path = QtWidgets.QLabel(Form)
        self.path.setText("")
        self.path.setObjectName("path")
        self.verticalLayout.addWidget(self.path)
        self.pip_list = QtWidgets.QListWidget(Form)
        self.pip_list.setObjectName("pip_list")
        self.verticalLayout.addWidget(self.pip_list)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Python路径", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "Python解释器", None, -1))
        self.py_setting_btn.setText(QtWidgets.QApplication.translate("Form", "⚙", None, -1))
