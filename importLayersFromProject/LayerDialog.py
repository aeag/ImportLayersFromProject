# -*- coding: utf-8 -*-

from PyQt5.QtCore import (QUuid, QFile, QIODevice, Qt, QDir, QFileInfo)
from PyQt5.QtWidgets import (QTableWidgetItem, QDialog, QApplication, QFileDialog)
from qgis.PyQt import QtXml

from qgis.core import QgsProject, QgsMessageLog

from .LayerChooser import Ui_Layers


class LayerDialog(QDialog, Ui_Layers):

    def __init__(self):
        QDialog.__init__(self)

        # Set up the user interface from Designer.
        self.setupUi(self)
        self.domdoc = None

    def populateTable(self, filePath):
        self.filePath = filePath[0]
        ui = self
        table = ui.tableWidget
        table.setRowCount(0)

        self.domdoc = QtXml.QDomDocument()
        xml = QFile(self.filePath)
        if (xml.open(QIODevice.ReadOnly | QIODevice.Text)):
            self.domdoc.setContent(xml)

        layers = self.domdoc.elementsByTagName("legendlayer")
        self.layers = layers

        for i in range(layers.length()):
            table.setRowCount(table.rowCount()+1)
            info = self.getLayerInfo(layers.item(i))
            if info:
                nameItem = QTableWidgetItem(info['name'])
                nameItem.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                nameItem.setCheckState(Qt.Unchecked)
                nameItem.setData(Qt.UserRole, info['id'])
                nameItem.setData(Qt.ToolTipRole, info['doc'])
                table.setItem(i, 0, nameItem)
                table.setItem(i, 1, FixedWidgetItem(info['mtype']))
                table.setItem(i, 2, FixedWidgetItem(info['geom']))
                table.setItem(i, 3, FixedWidgetItem(info['provider']))
                ds = FixedWidgetItem(info['ds'])
                ds.setData(Qt.ToolTipRole, info['ds'])
                table.setItem(i, 4, ds)

    def accept(self):
        """ do this for selected layers
        QgsProject.instance().readLayer(layers.item(3))
        """
        here = QDir.currentPath()
        QDir.setCurrent(str(QFileInfo(self.filePath).absoluteDir().canonicalPath()))

        for row in range(self.tableWidget.rowCount()):
            if self.tableWidget.item(row, 0).checkState():
                # index = self.tableWidget.item(row,0).data(QtCore.Qt.UserRole).toInt()[0]
                layerId = self.tableWidget.item(row, 0).data(Qt.UserRole)

                # noeud xml
                layerNode = self.getLayerNode(layerId)

                if layerNode:
                    # recherche id
                    idNode = layerNode.namedItem("id")
                    if idNode is not None:
                        newLayerId = QUuid.createUuid().toString()
                        idNode.firstChild().toText().setData(newLayerId)

                    QgsProject.instance().readLayer(layerNode)

        QDir.setCurrent(here)
        super(LayerDialog, self).accept()

    def getLayerNode(self, layerId):
        maplayers = self.domdoc.elementsByTagName("maplayer")
        for ml in (maplayers.item(i) for i in range(maplayers.size())):
            idelt = ml.namedItem("id")
            id = ""

            if idelt:
                id = idelt.firstChild().toText().data()

            attrEmbedded = ml.toElement().attribute("embedded", "0")
            if (attrEmbedded == "1"):
                id = ml.toElement().attribute("id", "")

            if (id == layerId):
                return ml

        return None

    def getLayerInfo(self, legendNode):
        legendlayerfileElt = legendNode.firstChild().firstChildElement("legendlayerfile")
        layerId = legendlayerfileElt.attribute("layerid")

        layerNode = self.getLayerNode(layerId)
        if layerNode is not None:
            title = layerNode.namedItem("title").firstChild().toText().data()
            name = layerNode.namedItem("layername").firstChild().toText().data()
            ds = layerNode.namedItem("datasource").firstChild().toText().data()
            provider = layerNode.namedItem("provider").firstChild().toText().data()
            mtype = layerNode.attributes().namedItem("type").firstChild().toText().data()
            abstract = layerNode.namedItem("abstract").firstChild().toText().data()

            doc = name
            if (abstract != "") and (title == ""):
                doc = "<p>%s</p>" % ("<br/>".join(abstract.split("\n")))
            else:
                if (abstract != "" or title != ""):
                    doc = "<b>%s</b><br/>%s" % (title, "<br/>".join(abstract.split("\n")))

            if mtype == "vector":
                geom = layerNode.attributes().namedItem("geometry").firstChild().toText().data()
            elif mtype == "raster":
                geom = layerNode.namedItem("rasterproperties")\
                    .namedItem("mDrawingStyle").firstChild().toText().data()
                if provider == "":
                    provider = "gdal ?"
            else:
                QgsMessageLog.logMessage("Unknown mtype: %s " % mtype, 'Extensions')

            return {'id': layerId, 'name': name, 'doc': doc, 'ds': ds, 'mtype': mtype,
                    'geom': geom, 'provider': provider}

        return None


class FixedWidgetItem(QTableWidgetItem):

    def __init__(self, label):
        super(FixedWidgetItem, self).__init__(label)
        self.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    filePath = QFileDialog.getOpenFileName(None, "Choose project file",
                                           "",
                                           "QGis projects (*.qgs)")
    window = LayerDialog()
    window.populateTable(filePath)
    window.show()
    app.exec_()
