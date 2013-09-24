# -*- coding: utf-8 -*-
#
# A mini-framework for creating XBMC Python addons with arbitrary UI
# made of controls - decendants of xbmcgui.Control class.
# The framework uses image textures from XBMC Confluence skin.
#
# Licence: GPL v.3 http://www.gnu.org/licenses/gpl.html

import sys, os
import xbmcgui, xbmcaddon

_ADDON_NAME = 'script.module.pyxbmct'
_addon = xbmcaddon.Addon(id=_ADDON_NAME)
_addon_path = _addon.getAddonInfo('path').decode(sys.getfilesystemencoding())
_images = os.path.join(_addon_path, 'lib', 'pyxbmct', 'textures', 'default')


# Text alighnment constants. Mixed variants are obtained by bit OR (|)
ALIGN_LEFT = 0
ALIGN_RIGHT = 1
ALIGN_CENTER_X = 2
ALIGN_CENTER_Y = 4
ALIGN_CENTER = 6
ALIGN_TRUNCATED = 8
ALIGN_JUSTIFY = 10

# XBMC key action codes.
# More codes at https://github.com/xbmc/xbmc/blob/master/xbmc/guilib/Key.h
ACTION_PREVIOUS_MENU = 10 # ESC
ACTION_NAV_BACK = 92 # Backspace
ACTION_MOVE_LEFT = 1
ACTION_MOVE_RIGHT = 2
ACTION_MOVE_UP = 3
ACTION_MOVE_DOWN = 4


def _set_textures(textures={}, kwargs={}):
    """Set texture arguments for controls."""
    for texture in textures.keys():
        try:
            kwargs[texture]
        except KeyError:
            kwargs[texture] = textures[texture]


class AddonWindowError(Exception):
    """Custom exception."""
    pass


class Label(xbmcgui.ControlLabel):
    """ControlLabel class.

    Parameters:
    label: string or unicode - text string.
    font: string - font used for label text. (e.g. 'font13')
    textColor: hexstring - color of enabled label's label. (e.g. '0xFFFFFFFF')
    disabledColor: hexstring - color of disabled label's label. (e.g. '0xFFFF3300')
    alignment: integer - alignment of label - *Note, see xbfont.h
    hasPath: bool - True=stores a path / False=no path.
    angle: integer - angle of control. (+ rotates CCW, - rotates CW)"

    Note:
        After you create the control, you need to add it to the window with placeControl().

    Example:
        self.label = Label('Status', angle=45)
    """
    def __new__(cls, *args, **kwargs):
        return super(Label, cls).__new__(cls, -10, -10, 1, 1, *args, **kwargs)


class FadeLabel(xbmcgui.ControlFadeLabel):
    """Control that scrolls label text.

    Parameters:
    font: string - font used for label text. (e.g. 'font13')
    textColor: hexstring - color of fadelabel's labels. (e.g. '0xFFFFFFFF')
    alignment: integer - alignment of label - *Note, see xbfont.h

    Note:
        After you create the control, you need to add it to the window with placeControl().

    Example:
        self.fadelabel = FadeLabel(textColor='0xFFFFFFFF')
    """
    def __new__(cls, *args, **kwargs):
        return super(FadeLabel, cls).__new__(cls, -10, -10, 1, 1, *args, **kwargs)


class TextBox(xbmcgui.ControlTextBox):
    """ControlTextBox class.

    Parameters:
    font: string - font used for text. (e.g. 'font13')
    textColor: hexstring - color of textbox's text. (e.g. '0xFFFFFFFF')

    Note:
        After you create the control, you need to add it to the window with placeControl().

    Example:
        self.textbox = TextBox(textColor='0xFFFFFFFF')
    """
    def __new__(cls, *args, **kwargs):
        return super(TextBox, cls).__new__(cls, -10, -10, 1, 1, *args, **kwargs)


class Image(xbmcgui.ControlImage):
    """ControlImage class.

    Parameters:
    filename: string - image filename.
    colorKey: hexString - (example, '0xFFFF3300')
    aspectRatio: integer - (values 0 = stretch (default), 1 = scale up (crops), 2 = scale down (black bars)
    colorDiffuse: hexString - (example, '0xC0FF0000' (red tint)).

    Note:
        After you create the control, you need to add it to the window with placeControl().

    Example:
        self.image = Image('d:\images\picture.jpg', aspectRatio=2)
    """
    def __new__(cls, *args, **kwargs):
        return super(Image, cls).__new__(cls, -10, -10, 1, 1, *args, **kwargs)


class Button(xbmcgui.ControlButton):
    """ControlButton class.

    Parameters:
    label: string or unicode - text string.
    focusTexture: string - filename for focus texture.
    noFocusTexture: string - filename for no focus texture.
    textOffsetX: integer - x offset of label.
    textOffsetY: integer - y offset of label.
    alignment: integer - alignment of label - *Note, see xbfont.h
    font: string - font used for label text. (e.g. 'font13')
    textColor: hexstring - color of enabled button's label. (e.g. '0xFFFFFFFF')
    disabledColor: hexstring - color of disabled button's label. (e.g. '0xFFFF3300')
    angle: integer - angle of control. (+ rotates CCW, - rotates CW)
    shadowColor: hexstring - color of button's label's shadow. (e.g. '0xFF000000')
    focusedColor: hexstring - color of focused button's label. (e.g. '0xFF00FFFF')

    Note:
        After you create the control, you need to add it to the window with placeControl().

    Example:
        self.button = Button('Status', font='font14')
    """
    def __new__(cls, *args, **kwargs):
        textures = {'focusTexture': os.path.join(_images, 'Button', 'KeyboardKey.png'),
                    'noFocusTexture': os.path.join(_images, 'Button', 'KeyboardKeyNF.png')}
        _set_textures(textures, kwargs)
        try:
            kwargs['alignment']
        except KeyError:
            kwargs['alignment'] = ALIGN_CENTER
        return super(Button, cls).__new__(cls, -10, -10, 1, 1, *args, **kwargs)


class RadioButton(xbmcgui.ControlRadioButton):
    """ControlRadioButton class.

    Parameters:
    label: string or unicode - text string.
    focusTexture: string - filename for focus texture.
    noFocusTexture: string - filename for no focus texture.
    textOffsetX: integer - x offset of label.
    textOffsetY: integer - y offset of label.
    _alignment: integer - alignment of label - *Note, see xbfont.h
    font: string - font used for label text. (e.g. 'font13')
    textColor: hexstring - color of enabled radio button's label. (e.g. '0xFFFFFFFF')
    disabledColor: hexstring - color of disabled radio button's label. (e.g. '0xFFFF3300')
    angle: integer - angle of control. (+ rotates CCW, - rotates CW)
    shadowColor: hexstring - color of radio button's label's shadow. (e.g. '0xFF000000')
    focusedColor: hexstring - color of focused radio button's label. (e.g. '0xFF00FFFF')
    TextureRadioFocus: string - filename for radio focus texture.
    TextureRadioNoFocus: string - filename for radio no focus texture.

    Note:
        After you create the control, you need to add it to the window with placeControl().

    Example:
        self.radiobutton = RadioButton('Status', font='font14')
    """
    def __new__(cls, *args, **kwargs):
        textures = {'focusTexture': os.path.join(_images, 'RadioButton', 'MenuItemFO.png'),
                    'noFocusTexture': os.path.join(_images, 'RadioButton', 'MenuItemNF.png'),
                    'TextureRadioFocus': os.path.join(_images, 'RadioButton', 'radiobutton-focus.png'),
                    'TextureRadioNoFocus': os.path.join(_images, 'RadioButton', 'radiobutton-nofocus.png')}
        _set_textures(textures, kwargs)
        return super(RadioButton, cls).__new__(cls, -10, -10, 1, 1, *args, **kwargs)


class Edit(xbmcgui.ControlEdit):
    """
   	ControlEdit class.

    Edit(label[, font, textColor, disabledColor, alignment, focusTexture, noFocusTexture])

    Parameters:
    label          : string or unicode - text string.
    font           : [opt] string - font used for label text. (e.g. 'font13')
    textColor      : [opt] hexstring - color of enabled label's label. (e.g. '0xFFFFFFFF')
    disabledColor  : [opt] hexstring - color of disabled label's label. (e.g. '0xFFFF3300')
    _alignment      : [opt] integer - alignment of label - *Note, see xbfont.h
    focusTexture   : [opt] string - filename for focus texture.
    noFocusTexture : [opt] string - filename for no focus texture.
    isPassword     : [opt] bool - if true, mask text value.

    *Note, You can use the above as keywords for arguments and skip certain optional arguments.
    Once you use a keyword, all following arguments require the keyword.
    After you create the control, you need to add it to the window with palceControl().

    example:
    - self.edit = Edit('Status')
    """
    def __new__(cls, *args, **kwargs):
        textures = {'focusTexture': os.path.join(_images, 'Edit', 'button-focus.png'),
                    'noFocusTexture': os.path.join(_images, 'Edit', 'black-back2.png')}
        _set_textures(textures, kwargs)
        return super(Edit, cls).__new__(cls, -10, -10, 1, 1, *args, **kwargs)


class List(xbmcgui.ControlList):
    """ControlList class.

    Parameters:
    font: string - font used for items label. (e.g. 'font13')
    textColor: hexstring - color of items label. (e.g. '0xFFFFFFFF')
    buttonTexture: string - filename for no focus texture.
    buttonFocusTexture: string - filename for focus texture.
    selectedColor: integer - x offset of label.
    _imageWidth: integer - width of items icon or thumbnail.
    _imageHeight: integer - height of items icon or thumbnail.
    _itemTextXOffset: integer - x offset of items label.
    _itemTextYOffset: integer - y offset of items label.
    _itemHeight: integer - height of items.
    _space: integer - space between items.
    _alignmentY: integer - Y-axis alignment of items label - *Note, see xbfont.h

    Note:
        After you create the control, you need to add it to the window with placeControl().

    Example:
        self.cList = List('font14', space=5)
    """
    def __new__(cls, *args, **kwargs):
        textures = {'buttonTexture': os.path.join(_images, 'List', 'MenuItemNF.png'),
                    'buttonFocusTexture': os.path.join(_images, 'List', 'MenuItemFO.png')}
        _set_textures(textures, kwargs)
        return super(List, cls).__new__(cls, -10, -10, 1, 1, *args, **kwargs)


class Slider(xbmcgui.ControlSlider):
    """ControlSlider class.

    Parameters:
    textureback: string - image filename.
    texture: string - image filename.
    texturefocus: string - image filename.

    Note:
        After you create the control, you need to add it to the window with placeControl().

    Example:
        self.slider = Slider()
    """
    def __new__(cls, *args, **kwargs):
        textures = {'textureback': os.path.join(_images, 'Slider', 'osd_slider_bg.png'),
                    'texture': os.path.join(_images, 'Slider', 'osd_slider_nibNF.png'),
                    'texturefocus': os.path.join(_images, 'Slider', 'osd_slider_nib.png')}
        _set_textures(textures, kwargs)
        return super(Slider, cls).__new__(cls, -10, -10, 1, 1, *args, **kwargs)


class _AbstractWindow(object):

    """
    Top-level control window.

    The control windows serves as a parent widget for other XBMC UI controls
    much like Tkinter.Tk or PyQt QWidget class.
    This is an abstract class which is not supposed to be instantiated directly
    and will raise exeptions. It is designed to be implemented in a grand-child class
    with the second inheritance from xbmcgui.Window or xbmcgui.WindowDialog
    in a direct child class.

    This is a basic "skeleton" for a control window.
    """

    def __init__(self):
        """
        Constructor method.

        Creates a new control window with default width and height.
        """
        self.actions_connected = []
        self.controls_connected = []

    def setGeometry(self, width_, height_, pos_x=-1, pos_y=-1):
        """
        Set control window width, height and coordinates (optional).

        pos_x, pos_y - coordinates of the top left corner of the window.
        if pos_x=0, pos_y=0, the window will be placed at the center of the screen.
        Example:
            self.setGeometry(500, 500)
        """
        self.width = width_
        self.height = height_
        if pos_x > 0 and pos_y > 0:
            self.x = pos_x
            self.y = pos_y
        else:
            self.x = 640 - self.width/2
            self.y = 360 - self.height/2

    def setGrid(self, rows_, columns_):
        """
        Set window grid layout of rows * columns.

        Example:
            self.setGrid(5, 4)
        """
        self.rows = rows_
        self.columns = columns_
        try:
            self.grid_x = self.x
            self.grid_y = self.y
            self.tile_width = self.width/self.columns
            self.tile_height = self.height/self.rows
        except AttributeError:
            raise AddonWindowError('Window geometry is not defined! Call setGeometry(width, height) first.')

    def placeControl(self, control, row, column, rowspan=1, columnspan=1, pad_x=5, pad_y=5):
        """
        Place a control within the window grid layout.

        pad_x, pad_y: horisontal and vertical padding for control's
        size and aspect adjustments. Negative values can be used
        to make a control overlap with grid cells next to it, if necessary.
        Raises AddonWindowError if a grid has not yet been set.
        Example:
            self.placeControl(self.label, 0, 1)
        """
        try:
            control_x = (self.grid_x + self.tile_width * column) + pad_x
            control_y = (self.grid_y + self.tile_height * row) + pad_y
            control_width = self.tile_width * columnspan - 2 * pad_x
            control_height = self.tile_height * rowspan - 2 * pad_y
        except AttributeError:
            raise AddonWindowError('Window grid is not set! Call setGrid(rows#, columns#) first.')
        control.setPosition(control_x, control_y)
        control.setWidth(control_width)
        control.setHeight(control_height)
        self.addControl(control)

    def getX(self):
        """Get X coordinate of the top-left corner of the window."""
        try:
            return self.x
        except AttributeError:
            raise AddonWindowError('Window geometry is not defined! Call setGeometry(width, height) first.')

    def getY(self):
        """Get Y coordinate of the top-left corner of the window."""
        try:
            return self.y
        except AttributeError:
            raise AddonWindowError('Window geometry is not defined! Call setGeometry(width, height) first.')

    def getWindowWidth(self):
        """Get window width."""
        try:
            return self.width
        except AttributeError:
            raise AddonWindowError('Window geometry is not defined! Call setGeometry(width, height) first.')

    def getWindowHeight(self):
        """Get window height."""
        try:
            return self.height
        except AttributeError:
            raise AddonWindowError('Window geometry is not defined! Call setGeometry(width, height) first.')

    def getRows(self):
        """
        Get grid rows count.
        Raises AddonWindowError if a grid has not yet been set.
        """
        try:
            return self.rows
        except AttributeError:
            raise AddonWindowError('AddonWindow grid is not set! Call setGrid(rows#, columns#) first.')

    def getColumns(self):
        """
        Get grid columns count.
        Raises AddonWindowError if a grid has not yet been set.
        """
        try:
            return self.columns
        except AttributeError:
            raise AddonWindowError('AddonWindow grid is not set! Call setGrid(rows#, columns#) first.')

    def connect(self, event, function, connected_list):
        """
        Connect an event to a function.
        This is a helper method not to be called directly.
        """
        try:
            self.disconnect(event, connected_list)
        except AddonWindowError:
            pass
        connected_list.append([event, function])

    def connectAction(self, action, function):
        """
        Connect a key action to a function or a method to be executed
        when the respective key pressed. lambda can be used to call the function
        with parameters.
        More action codes can be found at https://github.com/xbmc/xbmc/blob/master/xbmc/guilib/Key.h
        """
        self.connect(action, function, self.actions_connected)

    def connectControl(self, control, function):
        """
        Connect a control to a function or a method to be executed
        when the control activated. lambda can be used to call the function
        with parameters.
        """
        self.connect(control, function, self.controls_connected)

    def executeConnected(self, event, connected_list):
        """
        Execute a connected event (an action or a control).
        This is a helper method not to be called directly.
        """
        for item in connected_list:
            if event == item[0]:
                item[1]()
                break

    def disconnect(self, event, connected_list):
        """
        Disconnect an event which is coneected to a function.
        This is a helper method not to be called directly.
        Raises AddonWindowError if an event is not connected to any function.
        """
        for index in range(len(connected_list)):
            if event == connected_list[index][0]:
                connected_list.pop(index)
                break
        else:
            raise AddonWindowError('The action or control is not connected!')

    def disconnectAction(self, action):
        """
        Disconnect an action which is coneected to a function.
        Raises AddonWindowError if an action is not connected to any function.
        """
        self.disconnect(action, self.actions_connected)

    def disconnectControl(self, control):
        """
        Disconnect a control which is coneected to a function.
        Raises AddonWindowError if a control is not connected to any function.
        """
        self.disconnect(control, self.controls_connected)


class _AddonWindow(_AbstractWindow):

    """
    Top-level control window.

    The control windows serves as a parent widget for other XBMC UI controls
    much like Tkinter.Tk or PyQt QWidget class.
    This is an abstract class which is not supposed to be instantiated directly
    and will raise exeptions. It is designed to be implemented in a grand-child class
    with the second inheritance from xbmcgui.Window or xbmcgui.WindowDialog
    in a direct child class.

    This class provides a control window with a background and a header
    similar to top-level widgets of desktop UI frameworks.
    """

    def __init__(self, title=''):
        """
        Constructor method.

        Creates a new control window with default width and height.
        """
        super(AddonWindow, self).__init__()
        self.setFrame(title)

    def setFrame(self, title):
        """
        Define paths to images for window background and title background textures,
        and set control position adjustment constants used in setGrid.
        """
        # Window background image
        self.background_img = os.path.join(_images, 'AddonWindow', 'ContentPanel.png')
        print self.background_img
        # Background for a window header
        self.title_background_img = os.path.join(_images, 'AddonWindow', 'dialogheader.png')
        # Horisontal adjustment for a header background if the main background has transparent edges.
        self.X_MARGIN = 5
        # Vertical adjustment for a header background if the main background has transparent edges
        self.Y_MARGIN = 5
        # Header position adjustment if the main backround has visible borders.
        self.Y_SHIFT = 4
        # The height of a window header (for the title background and the title label).
        self.HEADER_HEIGHT = 35
        self.background = xbmcgui.ControlImage(-10, -10, 1, 1, self.background_img)
        self.addControl(self.background)
        self.title_background = xbmcgui.ControlImage(-10, -10, 1, 1, self.title_background_img)
        self.addControl(self.title_background)
        self.title_bar = xbmcgui.ControlLabel(-10, -10, 1, 1, title, alignment=ALIGN_CENTER, textColor='0xFFFFA500')
        self.addControl(self.title_bar)

    def setGeometry(self, width_, height_, pos_x=-1, pos_y=-1):
        """
        Set control window width, height and coordinates (optional).

        pos_x, pos_y - coordinates of the top left corner of the window.
        if pos_x=0, pos_y=0, the window will be placed at the center of the screen.
        Example:
            self.setGeometry(500, 500)
        """
        super(AddonWindow, self).setGeometry(width_, height_, pos_x, pos_y)
        self.background.setPosition(self.x, self.y)
        self.background.setWidth(self.width)
        self.background.setHeight(self.height)
        self.title_background.setPosition(self.x + self.X_MARGIN, self.y + self.Y_MARGIN + self.Y_SHIFT)
        self.title_background.setWidth(self.width - 2 * self.X_MARGIN)
        self.title_background.setHeight(self.HEADER_HEIGHT)
        self.title_bar.setPosition(self.x + self.X_MARGIN, self.y + self.Y_MARGIN + self.Y_SHIFT)
        self.title_bar.setWidth(self.width - 2 * self.X_MARGIN)
        self.title_bar.setHeight(self.HEADER_HEIGHT)

    def setGrid(self, rows_, columns_, padding=5):
        """
        Set window grid layout of rows * columns.

        Example:
        self.setGrid(5, 4)
        """
        self.rows = rows_
        self.columns = columns_
        try:
            self.grid_x = self.x + self.X_MARGIN + padding
            self.grid_y = self.y + self.Y_MARGIN + self.Y_SHIFT + self.HEADER_HEIGHT + padding
            self.tile_width = (self.width - 2 * (self.X_MARGIN + padding))/self.columns
            self.tile_height = (
                        self.height - self.HEADER_HEIGHT - self.Y_SHIFT - 2 * (self.Y_MARGIN + padding))/self.rows
        except AttributeError:
            raise AddonWindowError('Window geometry is not defined! Call setGeometry(width, height) first.')

    def setTitle(self, title=''):
        """
        Set window title.

        This method must be called AFTER (!!!) setGeometry(),
        otherwise there is some werid bug with all skin text labels set to the 'title' text.
        Example:
        self.setTitle('My Cool Addon')
        """
        self.title_bar.setLabel(title)

    def getTitle(self):
        """Get windos title."""
        return self.title_bar.getLabel()


class BlankFullWindow(xbmcgui.Window, _AbstractWindow):

    """
    Addon UI container with a solid background.

    This is a blank window with a black background and without any elements whatsoever.
    The decoration and layout are completely up to an addon developer.
    The window controls can hide under video or music visualization.

    Minimal example:

    class MyAddon(BlankFullWindow):
        def __init__(self)
            super(MyAddon, self).__init__()
            self.setGeometry(400, 300)
            self.setGrid(4, 3)

    addon = MyAddon()
    addon.doModal
    del addon
    """

    def onAction(self, action):
        """
        Catch button actions.

        Note that, despite being compared to an integer,
        action is an instance of xbmcgui.Action class.
        """
        if action == ACTION_PREVIOUS_MENU:
            self.close()
        else:
            self.executeConnected(action, self.actions_connected)

    def onControl(self, control):
        """
        Catch activated controls.

        Control is an instance of xbmcgui.Control class.
        """
        self.executeConnected(control, self.controls_connected)


class BlankDialogWindow(xbmcgui.WindowDialog, _AbstractWindow):

    """
    Addon UI container with a transparent background.

    This is a blank window with a transparent background and without any elements whatsoever.
    The decoration and layout are completely up to an addon developer.
    The window controls are always displayed over video or music visualization.

    Minimal example:

    class MyAddon(BlankDialogWindow):
        def __init__(self)
            super(MyAddon, self).__init__()
            self.setGeometry(400, 300)
            self.setGrid(4, 3)

    addon = MyAddon()
    addon.doModal
    del addon
    """

    def onAction(self, action):
        """
        Catch button actions.

        Note that, despite being compared to an integer,
        action is an instance of xbmcgui.Action class.
        """
        if action == ACTION_PREVIOUS_MENU:
            self.close()
        else:
            self.executeConnected(action, self.actions_connected)

    def onControl(self, control):
        """
        Catch activated controls.

        Control is an instance of xbmcgui.Control class.
        """
        self.executeConnected(control, self.controls_connected)


class AddonFullWindow(xbmcgui.Window, _AddonWindow):

    """
    Addon UI container with a solid background.

    Control window is displayed on top of the main background image - self.main_bg.
    Video and music visualization are displayed unhindered.
    Window ID can be passed as the 2nd positional agrument.
    Minimal example:

    class MyAddon(AddonFullWindow):
        def __init__(self, title='')
            super(MyAddon, self).__init__(title)
            self.setGeometry(400, 300)
            self.setGrid(4, 3)

    addon = MyAddon('My Cool Addon')
    addon.doModal
    del addon
    """

    def __new__(cls, title='', *args, **kwargs):
        return super(AddonFullWindow, cls).__new__(cls, *args, **kwargs)

    def __init__(self, title=''):
        super(AddonFullWindow, self).__init__(title)

    def setFrame(self):
        """
        Set the image for for the fullscreen background.
        """
        # Image for the fullscreen background.
        self.main_bg_img = os.path.join(_images, 'AddonWindow', 'SKINDEFAULT.jpg')
        # Fullscreen background image control.
        self.main_bg = xbmcgui.ControlImage(1, 1, 1280, 720, self.main_bg_img)
        self.addControl(self.main_bg)
        super(AddonFullWindow, self).setFrame()

    def setBackground(self, image=''):
        """
        Set the main bacground to an image file.
        image: path to an image file as str.
        Example:
            self.setBackground('d:\images\bacground.png')
        """
        self.main_bg.setImage(image)

    def onAction(self, action):
        """
        Catch button actions.

        Note that, despite being compared to an integer,
        action is an instance of xbmcgui.Action class.
        """
        if action == ACTION_PREVIOUS_MENU:
            self.close()
        else:
            self.executeConnected(action, self.actions_connected)

    def onControl(self, control):
        """
        Catch activated controls.

        Control is an instance of xbmcgui.Control class.
        """
        self.executeConnected(control, self.controls_connected)


class AddonDialogWindow(xbmcgui.WindowDialog, _AddonWindow):

    """
    Addon UI container with a transparent background.

    Control window is displayed on top of XBMC UI,
    including video an music visualization!
    Minimal example:

    class MyAddon(AddonDialogWindow):
        def __init__(self, title='')
            super(MyAddon, self).__init__(title)
            self.setGeometry(400, 300)
            self.setGrid(4, 3)

    addon = MyAddon('My Cool Addon')
    addon.doModal
    del addon
    """

    def __new__(cls, title='', *args, **kwargs):
        return super(AddonDialogWindow, cls).__new__(cls, *args, **kwargs)

    def __init__(self, title=''):
        super(AddonDialogWindow, self).__init__(title)

    def onAction(self, action):
        """
        Catch button actions.
        Note that, despite being compared to an integer,
        action is an instance of xbmcgui.Action class.
        """
        if action == ACTION_PREVIOUS_MENU:
            self.close()
        else:
            self.executeConnected(action, self.actions_connected)

    def onControl(self, control):
        """
        Catch activated controls.
        Control is an instance of xbmcgui.Control class.
        """
        self.executeConnected(control, self.controls_connected)


def main():
    pass

if __name__ == '__main__':
    main()
