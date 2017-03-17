# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'W:\GitHub\ImportLayersFromProject\importLayersFromProject\LayerChooser.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

class Ui_Layers(object):
    def setupUi(self, Layers):
        Layers.setObjectName("Layers")
        Layers.resize(543, 613)
        Layers.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Layers)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.layerBox = QtWidgets.QGroupBox(Layers)
        self.layerBox.setMinimumSize(QtCore.QSize(0, 180))
        self.layerBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.layerBox.setObjectName("layerBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layerBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.layerBox)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setText("Name")
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("Type")
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("Geometry")
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("Provider")
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("Source")
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.tableWidget)
        self.verticalLayout_2.addWidget(self.layerBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(Layers)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(Layers)
        self.buttonBox.accepted.connect(Layers.accept)
        self.buttonBox.rejected.connect(Layers.close)
        QtCore.QMetaObject.connectSlotsByName(Layers)

    def retranslateUi(self, Layers):
        _translate = QtCore.QCoreApplication.translate
        Layers.setWindowTitle(_translate("Layers", "Layer Chooser"))
        self.layerBox.setTitle(_translate("Layers", "Select Layers to Import"))
        self.tableWidget.setSortingEnabled(True)

