Connection Manager
==================

Connection manager is similar to the signal-slot connection mechanism of Qt framework.
It allows you to connect an event — a control or a key action code — to a function or a method to be activated
when the respective control is activated or when a key is pressed, thus invoking the key action bound to it.
The connection manager is implemented through :meth:`connect<pyxbmct.addonwindow.AbstractWindow.connect>`
method of a base PyXBMCt class.

You can only connect the following controls: :class:`Button<pyxbmct.addonwindow.Button>`,
:class:`RadioButton<pyxbmct.addonwindow.RadioButton>` and :class:`List<pyxbmct.addonwindow.List>`.
Other controls do not generate any UI events, so connecting them won’t have any effect.

.. warning::
    For connection you must provide a function object without brackets ``()``, not a function call!

Similarly to PyQt’s signal-slot connection, ``lambda`` can be used to connect a function/method with arguments
known at runtime. The key code ``ACTION_PREVIOUS_MENU`` or ``10`` (bound to ``ESC`` key by default) is already connected
to the method that closes a current addon window (``close``), so you cannot connect it to any function/method.
Or technically you can, but such connection won’t work. It guarantees that you always have a way
to close an active addon window.
