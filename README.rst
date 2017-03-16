``libvirtaio`` Libvirt event loop implementation using asyncio
==============================================================

Simple usage
------------

Register the implementation of default loop:

.. code-block:: python

    import libvirtaio
    impl = libvirtaio.LibvirtAsyncIOEventImpl()
    impl.register()

Almost simple usage
-------------------

Register the implementation on specific loop:

.. code-block:: python

    import asyncio
    import libvirtaio
    impl = libvirtaio.LibvirtAsyncIOEventImpl(loop=asyncio.get_event_loop())
    impl.register()

Advanced usage
--------------

This module also contains an ``execute_ff_callback(opaque)`` function to be
used from other implementation, which parses the opaque object and executes the
``ff`` callback.

.. seealso::
    https://libvirt.org/html/libvirt-libvirt-event.html
