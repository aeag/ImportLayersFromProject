# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LayerChooser.ui'
#
# Created: Tue Jun  7 18:03:50 2011
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Layers(object):
    def setupUi(self, Layers):
        Layers.setObjectName("Layers")
        Layers.resize(543, 613)
        Layers.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Layers)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.layerBox = QtGui.QGroupBox(Layers)
        self.layerBox.setMinimumSize(QtCore.QSize(0, 180))
        self.layerBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.layerBox.setObjectName("layerBox")
        self.verticalLayout = QtGui.QVBoxLayout(self.layerBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtGui.QTableWidget(self.layerBox)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.horizontalHeaderItem(0).setText("Name")
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeaderItem(1).setText("Type")
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeaderItem(2).setText("Geometry")
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeaderItem(3).setText("Provider")
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeaderItem(4).setText("Source")
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.tableWidget)
        self.verticalLayout_2.addWidget(self.layerBox)
        self.buttonBox = QtGui.QDialogButtonBox(Layers)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(Layers)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Layers.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Layers.close)
        QtCore.QMetaObject.connectSlotsByName(Layers)

    def retranslateUi(self, Layers):
        Layers.setWindowTitle(QtGui.QApplication.translate("Layers", "Layer Chooser", None, QtGui.QApplication.UnicodeUTF8))
        self.layerBox.setTitle(QtGui.QApplication.translate("Layers", "Select Layers to Import", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.setSortingEnabled(True)

