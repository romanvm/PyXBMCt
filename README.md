PyXBMCt
=======

PyXBMCt is a mini-framework which simplifies UI creation for XBMC addons. It works much like PyQt GUI framework (hence the name) and provides a main window and a number of controls (widgets). The main windows serves as a parent widget for the controls much like QtGui.QWidget class and provides a grid layout manager to place the controls.

Simply install the framework as an XBMC addon and use
from pyxbmct.addonwindow import *
to acces framework classes and variables.
The framework uses image textures from XBMC Confluence skin.

Licence: GPL v.3 http://www.gnu.org/licenses/gpl.html
