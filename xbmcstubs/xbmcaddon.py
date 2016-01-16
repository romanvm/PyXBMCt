# coding: utf-8
"""
A class to access addon properties
"""

__author__ = 'Team Kodi <http://kodi.tv>'
__credits__ = 'Team Kodi'
__date__ = 'Fri May 01 16:22:07 BST 2015'
__platform__ = 'ALL'
__version__ = '2.20.0'


class Addon(object):
    """
    Addon(id=None)

    Creates a new Addon class.

    :param id: string - id of the addon (autodetected in XBMC Eden)

    Example::

        self.Addon = xbmcaddon.Addon(id='script.recentlyadded')
    """
    def __init__(self, id=None):
        """Creates a new Addon class.

        :param id: string - id of the addon (autodetected in XBMC Eden)

        Example::

            self.Addon = xbmcaddon.Addon(id='script.recentlyadded')
        """
        pass

    def getLocalizedString(self, id):
        """Returns an addon's localized 'unicode string'.

        :param id: integer - id# for string you want to localize.

        Example::

            locstr = self.Addon.getLocalizedString(id=6)
        """
        return unicode()

    def getSetting(self, id):
        """Returns the value of a setting as a unicode string.

        :param id: string - id of the setting that the module needs to access.

        Example::

            apikey = self.Addon.getSetting('apikey')
        """
        return unicode()

    def setSetting(self, id, value):
        """Sets a script setting.

        :param id: string - id of the setting that the module needs to access.
        :param value: string or unicode - value of the setting.

        Example::

            self.Settings.setSetting(id='username', value='teamxbmc')
        """
        pass

    def openSettings(self):
        """Opens this scripts settings dialog."""
        pass

    def getAddonInfo(self, id):
        """Returns the value of an addon property as a string.

        :param id: string - id of the property that the module needs to access.

        .. note::
            Choices are (author, changelog, description, disclaimer, fanart, icon, id, name, path
            profile, stars, summary, type, version)

        Example::

            version = self.Addon.getAddonInfo('version')
        """
        return str()
