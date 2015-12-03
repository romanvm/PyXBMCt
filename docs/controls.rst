Controls
========

PyXBMCt provides 9 ready-to-use UI controls that are based on the respective ``xbmcgui`` controls
with the following differences:

* You don’t need to specify coordinates and size for the controls explicitly. The Grid layout manager takes care of control placement.

* All controls that require textures are provided with default textures (borrowed from Confluence skin resources). You can specify your own textures for PyXBMCt controls, but you need to do this through keyword arguments (important!).

* Button caption is center-aligned by default. You can change button caption alignment by providing a necessary alignment parameter through a keyword argument (PyXBMCt already includes symbolic constants for control text alignment). Since PyXBMCt controls are sub-classed from ``xbmcgui`` controls, you can use all their methods to work with the controls.

Since all PyXBMCt Controls are subclassed from ``xbmcgui.Control*`` classes, you can use all parent ``xbmcgui``
classes' methods to set Control properties.

Below is the list of PyXBMCt controls with brief descriptions:

Label
-----

Simple text label much like ``Tkinter.Label`` or ``QLabel``.

FadeLabel
---------

It is similar to ``Label``, but a very long text string is auto-scrolled.

TextBox
-------

``TextBox`` can contain multiline text. It can autoscroll very long text.

Image
-----

This control displays images from files (``.jpg``, ``.png``, ``.gif``).
For ``.gif`` and ``.png`` images animation and transparency are supported.

Button
------

A clickable button. It generates a control event on click.

RadioButton
-----------

A 2-state switch. It generates a control event on click.

Edit
----

Text entry field, similar to ``Tkinter.Entry`` or ``QLineEdit``.
When activated, it opens an on-screen keyboard to enter text.

List
----

A list of items. The list scrolls when it cannot display all its items within available space.
It generates a control event when an item is selected.

Slider
------

A control for stepless adjusting some value (e.g. volume level).


API Reference
-------------

.. autosummary::

    pyxbmct.addonwindow.Label
    pyxbmct.addonwindow.FadeLabel
    pyxbmct.addonwindow.TextBox
    pyxbmct.addonwindow.Image
    pyxbmct.addonwindow.Button
    pyxbmct.addonwindow.RadioButton
    pyxbmct.addonwindow.Edit
    pyxbmct.addonwindow.List
    pyxbmct.addonwindow.Slider
