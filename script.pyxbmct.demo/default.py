# -*- coding: utf-8 -*-
# Licence: GPL v.3 http://www.gnu.org/licenses/gpl.html
# This is an XBMC addon for demonstrating the capabilities
# and usage of PyXBMCt framework.

import sys, os
import xbmc, xbmcaddon, xbmcgui
from pyxbmct.addonwindow import *

_addon = xbmcaddon.Addon()
_addon_path = _addon.getAddonInfo('path').decode(sys.getfilesystemencoding())


class MyAddon(AddonDialogWindow):

    def __init__(self, title=''):
        super(MyAddon, self).__init__(title)
        self.setGeometry(400, 675)
        self.setGrid(15, 2)
        self.set_controls()
        self.set_navigation()
        # Connect an action (Backspace) to close the window.
        self.connect(ACTION_NAV_BACK, self.close)

    def set_controls(self):
        # Demo for PyXBMCt UI controls.
        no_int_label = Label('Interactive Controls', alignment=ALIGN_CENTER)
        self.placeControl(no_int_label, 0, 0, 1, 2)
        #
        button_label = Label('Button')
        self.placeControl(button_label, 1, 0)
        # Button
        self.button = Button('Close')
        self.placeControl(self.button, 1, 1)
        # Connect control to close the window.
        self.connect(self.button, self.close)
        #
        radiobutton_label = Label('RadioButton')
        self.placeControl(radiobutton_label, 2, 0)
        # RadioButton
        self.radiobutton = RadioButton('Switch on/off')
        self.placeControl(self.radiobutton, 2, 1)
        #
        edit_label = Label('Edit')
        self.placeControl(edit_label, 3, 0)
        # Edit
        self.edit = Edit('Edit')
        self.placeControl(self.edit, 3, 1)
        # Additional properties must be changed after (!) displaying a control.
        self.edit.setText('Enter text here')
        #
        list_label = Label('List')
        self.placeControl(list_label, 4, 0)
        # List
        self.list = List()
        self.placeControl(self.list, 4, 1, 3, 1)
        self.list.addItems(['Item 1', 'Item 2', 'Item 3'])
        # Connect list to a function to display which list item is selected.
        self.connect(self.list, lambda: xbmc.executebuiltin('Notification(Note!,%s selected.)' %
                                            self.list.getListItem(self.list.getSelectedPosition()).getLabel()))
        #
        slider_label = Label('Slider')
        self.placeControl(slider_label, 7, 0)
        # Slider
        self.slider = Slider()
        self.placeControl(self.slider, 7, 1, pad_y=10)
        self.slider.setPercent(25)
        #
        no_int_label = Label('Information output', alignment=ALIGN_CENTER)
        self.placeControl(no_int_label, 8, 0, 1, 2)
        #
        label_label = Label('Label')
        self.placeControl(label_label, 9, 0)
        # Label
        self.label = Label('Simple label')
        self.placeControl(self.label, 9, 1)
        #
        fadelabel_label = Label('FadeLabel')
        self.placeControl(fadelabel_label, 10, 0)
        # FadeLabel
        self.fade_label = FadeLabel()
        self.placeControl(self.fade_label, 10, 1)
        self.fade_label.addLabel('Very long string can be here.')
        #
        textbox_label = Label('TextBox')
        self.placeControl(textbox_label, 11, 0)
        # TextBox
        self.textbox = TextBox()
        self.placeControl(self.textbox, 11, 1, 2, 1)
        self.textbox.setText('Text box.\nIt can contain several lines.')
        #
        image_label = Label('Image')
        self.placeControl(image_label, 13, 0)
        # Image
        self.image = Image(os.path.join(_addon_path, 'xbmc-logo.png'))
        self.placeControl(self.image, 13, 1, 2, 1)

    def set_navigation(self):
        # Set navigation between controls
        self.button.controlUp(self.slider)
        self.button.controlDown(self.radiobutton)
        self.radiobutton.controlUp(self.button)
        self.radiobutton.controlDown(self.edit)
        self.edit.controlUp(self.radiobutton)
        self.edit.controlDown(self.list)
        self.list.controlUp(self.edit)
        self.list.controlDown(self.slider)
        self.slider.controlUp(self.list)
        self.slider.controlDown(self.button)
        # Set initial focus
        self.setFocus(self.button)


def main():
    window = MyAddon('PyXBMCt Demo')
    window.doModal()

if __name__ == '__main__':
    main()
