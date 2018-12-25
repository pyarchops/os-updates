.. highlight:: shell

============
Installation
============

Stable release
--------------

The ArchOps software should be installed through the main repository,
.. _pyArchOps : https://github.com/pyarchops/archops.git

.. code-block:: console

    $ pip install archops


Latest OS updates release
---------------------------

To install ArchOps OS updates, run this command in your terminal:

.. code-block:: console

    $ pip install archops_os_updates

This is the preferred method to install pyArchOps OS updates, as it will always install the most recent stable release.

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/


From sources
------------

The sources for ArchOps OS updates can be downloaded from the `Github repo`_.

You can either clone the public repository:

.. code-block:: console

    $ git clone git://github.com/pyarchops/os_updates

Or download the `tarball`_:

.. code-block:: console

    $ curl  -OL https://github.com/pyarchops/os_updates/tarball/master

Once you have a copy of the source, you can install it with:

.. code-block:: console

    $ python setup.py install


.. _Github repo: https://github.com/pyarchops/os_updates
.. _tarball: https://github.com/pyarchops/os_updates/tarball/master
