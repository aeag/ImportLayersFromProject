# (c) Barry Rowlingson 2008

import ConfigParser
import os.path
p = ConfigParser.ConfigParser()
here = os.path.join(os.path.dirname(__file__),"config.ini")
p.read(here)

def name():
  return p.get('general','name')

def description():
  return p.get('general','description')

def version():
  return p.get('general','version')

def qgisMinimumVersion():
  return p.get("general","qgisMinimumVersion")


def classFactory(iface):
  from main import MainPlugin
  return MainPlugin(iface)

