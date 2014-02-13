#
# Importproject (c) Barry Rowlingson 2011
#
#    This file is part of "importlayers"
#
#    Importlayers is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Rasterlang is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Rasterlang.  If not, see <http://www.gnu.org/licenses/>.

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *

from LayerDialog import LayerDialog

import resources
import doAbout

class MainPlugin(object):
  def __init__(self, iface):
    # Save a reference to the QGIS iface
    self.iface = iface

  def initGui(self):
    # Create action
    self.action = QAction(QIcon(":/icons/importlayers.png"),"Import Layers from Project",self.iface.mainWindow())
    self.action.setWhatsThis("Import Layers from a .qgs project file")
    QObject.connect(self.action,SIGNAL("triggered()"),self.run)
    self.iface.addToolBarIcon(self.action)
    self.iface.addPluginToMenu("&ImportProject",self.action)
    self.about = QAction("About ImportProject",self.iface.mainWindow())
    QObject.connect(self.about,SIGNAL("triggered()"),self.clickAbout)
    self.iface.addPluginToMenu("&ImportProject",self.about)


  def unload(self):
    # Remove the plugin
    self.iface.removePluginMenu("&ImportProject",self.action)
    self.iface.removePluginMenu("&ImportProject",self.about)
    self.iface.removeToolBarIcon(self.action)
    

  def run(self):
    """ do the whole thing """
    # choose a file
    # fire up the main dialog
    # import layers
    filePath = QFileDialog.getOpenFileName(self.iface.mainWindow(),"Choose project file" ,
                                                 "",
                                                 "QGis projects (*.qgs)")
    if filePath == "":
      return
    self.iface.mapCanvas().freeze(1)
    window = LayerDialog()
    window.populateTable(filePath)
    window.show()
    status = window.exec_()
    self.iface.mapCanvas().freeze(0)
    self.iface.mapCanvas().refresh()

  def clickAbout(self):
    d = doAbout.Dialog()
    d.exec_()

