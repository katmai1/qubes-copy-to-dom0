# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/q/dev/qubes-copy-to-dom0/ui/main.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainwin(object):
    def setupUi(self, mainwin):
        mainwin.setObjectName("mainwin")
        mainwin.resize(364, 418)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainwin.sizePolicy().hasHeightForWidth())
        mainwin.setSizePolicy(sizePolicy)
        self.centralWidget = QtWidgets.QWidget(mainwin)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.list_vms = QtWidgets.QListWidget(self.centralWidget)
        self.list_vms.setObjectName("list_vms")
        self.verticalLayout.addWidget(self.list_vms)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_help = QtWidgets.QPushButton(self.centralWidget)
        self.btn_help.setObjectName("btn_help")
        self.horizontalLayout.addWidget(self.btn_help)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_copy = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_copy.sizePolicy().hasHeightForWidth())
        self.btn_copy.setSizePolicy(sizePolicy)
        self.btn_copy.setObjectName("btn_copy")
        self.horizontalLayout.addWidget(self.btn_copy)
        self.verticalLayout.addLayout(self.horizontalLayout)
        mainwin.setCentralWidget(self.centralWidget)

        self.retranslateUi(mainwin)
        QtCore.QMetaObject.connectSlotsByName(mainwin)

    def retranslateUi(self, mainwin):
        _translate = QtCore.QCoreApplication.translate
        mainwin.setWindowTitle(_translate("mainwin", "Copy To Dom0"))
        self.label.setText(_translate("mainwin", "Select Source VM"))
        self.btn_help.setText(_translate("mainwin", "Help"))
        self.btn_copy.setText(_translate("mainwin", "Copy to Dom0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainwin = QtWidgets.QMainWindow()
    ui = Ui_mainwin()
    ui.setupUi(mainwin)
    mainwin.show()
    sys.exit(app.exec_())

