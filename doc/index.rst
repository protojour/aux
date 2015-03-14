.. Auxiliary documentation master file, created by
   sphinx-quickstart on Tue Apr 29 23:51:27 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Auxiliary's documentation!
=====================================


Contents:

.. toctree::
   :maxdepth: 2

License
=======
.. include:: ../LICENSE
   :literal:


Using Aux for Testing
=====================



Working with devices
====================
Create a python egg module named aux_device_<device_name>

When installed the device can be called through aux.device.<device_name>

<device_name>sspapi.py
<device_name>wsdlapi.py

Aux API
=======
External API
------------
The aux.api is a high level access to feature in Aux.

* aux.api.http
* aux.api.ssh

Internal API
------------
* aux.protocol.http
* aux.protocol.soap
* aux.protocol.ssh

Development
===========




.. automodule:: aux

.. autoclass:: aux.protocols.http.http.SimpleHTTPClient
    :members:


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

