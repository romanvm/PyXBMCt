## @package xbmcvfs
#  Classes and functions to work with files and folders.
#
"""
Classes and functions to work with files and folders
"""

__author__ = 'Team Kodi <http://kodi.tv>'
__credits__ = 'Team Kodi'
__date__ = 'Fri May 01 16:22:23 BST 2015'
__platform__ = 'ALL'
__version__ = '2.20.0'


class File(object):
    def __init__(self, filepath, mode=None):
        """
        'w' - (opt) open for write
        example:
         f = xbmcvfs.File(file, ['w'])
        """
        pass

    def close(self):
        """
        example:
         f = xbmcvfs.File(file)
         f.close()
        """
        pass

    def read(self, numBytes=0):
        """
        read(numBytes)

        numBytes : how many bytes to read [opt]- if not set it will read the whole file
        example:
        f = xbmcvfs.File(file)
        b = f.read()
        f.close()
        """
        return str

    def readBytes(self, numBytes=0):
        """
        readBytes(numBytes)

        numBytes : how many bytes to read [opt]- if not set it will read the whole file

        returns: bytearray

        example:
        f = xbmcvfs.File(file)
        b = f.read()
        f.close()
        """
        return bytearray

    def seek(self, seekBytes, iWhence):
        """
        seek()

        seekBytes : position in the file
        iWhence : where in a file to seek from[0 begining, 1 current , 2 end possition]
        example:
         f = xbmcvfs.File(file)
         result = f.seek(8129, 0)
         f.close()
        """
        return long

    def size(self):
        """
        size()

        example:
         f = xbmcvfs.File(file)
         s = f.size()
         f.close()
        """
        return long

    def write(self, buffer):
        """
        write(buffer)

        buffer : buffer to write to file
        example:
         f = xbmcvfs.File(file, 'w', True)
         result = f.write(buffer)
         f.close()
        """
        return bool


def copy(strSource, strDestnation):
    """Copy file to destination, returns true/false.

    source: string - file to copy.
    destination: string - destination file

    Example:
        success = xbmcvfs.copy(source, destination)"""
    return bool


def delete(file):
    """Deletes a file.

    file: string - file to delete

    Example:
        xbmcvfs.delete(file)"""
    pass


def rename(file, newFile):
    """Renames a file, returns true/false.

    file: string - file to rename
    newFile: string - new filename, including the full path

    Example:
        success = xbmcvfs.rename(file,newFileName)"""
    return bool


def mkdir(path):
    """Create a folder.

    path: folder

    Example:
        success = xbmcfvs.mkdir(path)
    """
    return bool


def mkdirs(path):
    """
    mkdirs(path)--Create folder(s) - it will create all folders in the path.

    path : folder

    example:

    - success = xbmcvfs.mkdirs(path)
    """
    return bool


def rmdir(path, force=False):
    """Remove a folder.

    path: folder

    Example:
        success = xbmcfvs.rmdir(path)
    """
    return bool


def exists(path):
    """Checks for a file or folder existance, mimics Pythons os.path.exists()

    path: string - file or folder

    Example:
        success = xbmcvfs.exists(path)"""
    return bool

def listdir(path):
    """
    listdir(path) -- lists content of a folder.

    path        : folder

    example:
     - dirs, files = xbmcvfs.listdir(path)
    """
    return tuple


class Stat(object):
    def __init__(self, path):
        """
        Stat(path) -- get file or file system status.

        path        : file or folder

        example:
        - print xbmcvfs.Stat(path).st_mtime()
        """

    def st_mode(self):
        return long

    def st_ino(self):
        return long

    def st_nlink(self):
        return long

    def st_uid(self):
        return long

    def st_gid(self):
        return long

    def st_size(self):
        return long

    def st_atime(self):
        return long

    def st_mtime(self):
        return long

    def st_ctime(self):
        return long
