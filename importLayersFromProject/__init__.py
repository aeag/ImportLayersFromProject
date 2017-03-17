# (c) Barry Rowlingson 2008

def classFactory(iface):
  from .main import MainPlugin
  return MainPlugin(iface)

