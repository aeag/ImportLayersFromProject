#!/usr/bin/python

from PyQt4 import QtGui,QtCore, QtXml
from PyQt4.QtGui import QTableWidgetItem

from PyQt4.QtCore import QUuid

from qgis.core import *
from qgis.gui import *
from LayerChooser import Ui_Layers

class LayerDialog(QtGui.QDialog, Ui_Layers):
    def __init__(self):
        QtGui.QDialog.__init__(self)

        # Set up the user interface from Designer.
        self.setupUi(self)

    def populateTable(self,filePath):
        self.filePath = filePath
        ui = self
        table = ui.tableWidget
#        table.clear()
        table.setRowCount(0)
        xml = file(filePath).read()
        d = QtXml.QDomDocument()
        d.setContent(xml)
        maps = d.elementsByTagName("maplayer")
        self.maps=maps

        for i in range(maps.length()):
            table.setRowCount(table.rowCount()+1)
            info = getMapInfo(maps.item(i))
            nameItem = QTableWidgetItem(info['name'])
            nameItem.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
            nameItem.setCheckState(QtCore.Qt.Unchecked)
            nameItem.setData(QtCore.Qt.UserRole,str(i))
            table.setItem(i,0,nameItem)
            table.setItem(i,1,FixedWidgetItem(info['mtype']))
            table.setItem(i,2,FixedWidgetItem(info['geom']))
            table.setItem(i,3,FixedWidgetItem(info['provider']))
            ds = FixedWidgetItem(info['ds'])
            ds.setData(QtCore.Qt.ToolTipRole,info['ds'])
            table.setItem(i,4,ds)

    def accept(self):
        """ do this for selected layers 
        QgsProject.instance().read(maps.item(3))
        """
        here = QtCore.QDir.currentPath()
        QtCore.QDir.setCurrent(QtCore.QFileInfo(self.filePath).absoluteDir().canonicalPath())
        print 'importproject debug. layerdialog.py line 50 tablewidget range: ' + str(range(self.tableWidget.rowCount()))
       
        for row in range(self.tableWidget.rowCount()):
            print str(self.tableWidget.item(row,0).data(QtCore.Qt.UserRole))
             
            if self.tableWidget.item(row,0).checkState():
                # index = self.tableWidget.item(row,0).data(QtCore.Qt.UserRole).toInt()[0]
                index = self.tableWidget.item(row,0).data(QtCore.Qt.UserRole)[0]
                index = int(index)
                
                print 'importproject debug. layerdialog.py line 50 index of checked layers: ' +str(index)
                
                # noeud xml
                layerNode = self.maps.item(index)
                
                # recherche id
                idNode = layerNode.namedItem("id")
                if idNode != None:
                    id = idNode.firstChild().toText().data()
                    # give it a new id (for multiple import)
                    #import uuid
                    newLayerId = QUuid.createUuid().toString()
                    idNode.firstChild().toText().setData(newLayerId)
                
                QgsProject.instance().read(layerNode)
       
        QtCore.QDir.setCurrent(here)
        super(LayerDialog,self).accept()
        pass

class FixedWidgetItem(QTableWidgetItem):
    def __init__(self,label):
        super(FixedWidgetItem,self).__init__(label)
        self.setFlags(QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsSelectable)

def getMapInfo(mapDom):
    name = mapDom.namedItem("layername").firstChild().toText().data()
    ds = mapDom.namedItem("datasource").firstChild().toText().data()
    provider = mapDom.namedItem("provider").firstChild().toText().data()
    mtype = mapDom.attributes().namedItem("type").firstChild().toText().data()
    if mtype == "vector":
        geom = mapDom.attributes().namedItem("geometry").firstChild().toText().data()
    elif mtype == "raster":
        geom = mapDom.namedItem("rasterproperties").namedItem("mDrawingStyle").firstChild().toText().data()
        if provider == "":
            provider = "gdal?"
    else:
        print "Unknown mtype: %s " % mtype
    return {'name':name,'ds':ds,'mtype':mtype,'geom':geom,'provider':provider}

if __name__=="__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    filePath = QtGui.QFileDialog.getOpenFileName(None,"Choose project file" ,
                                                 "",
                                                 "QGis projects (*.qgs *.xpm *.jpg)")
    window = LayerDialog()
    window.populateTable(filePath)
    window.show()
    app.exec_()
