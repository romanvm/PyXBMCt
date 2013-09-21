pyxt is a mini-framework which simplifies UI creation for XBMC addons. It works much like PyQt GUI framework (hence the name) and provides a main window and a number of controls (widgets).

The main windows serves as a parent widget for the controls much like QtGui.QWidget class and provides a grid layout manager to place the controls.

Simply add \pyxt directory to your addon directory and use

from pyxt.addonwindow import *

to acces framework classes and variables.
