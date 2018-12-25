=====================
pyArchOps/OS updates
=====================


.. image:: https://img.shields.io/pypi/v/pypyarchops_os_updates.svg
        :target: https://pypi.python.org/pypi/pypyarchops_os_updates

.. image:: https://img.shields.io/travis/pypyarchops/pypyarchops_os_updates.svg
        :target: https://travis-ci.org/pypyarchops/pypyarchops_os_updates

.. image:: https://readthedocs.org/projects/pypyarchops-os_updates/badge/?version=latest
        :target: https://pypyarchops-os_updates.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/pypyarchops/os-updates/shield.svg
     :target: https://pyup.io/repos/github/pypyarchops/os-updates/
          :alt: Updates


Install All OS updates


* Free software: MIT license
* Documentation: https://pypyarchops-os_updates.readthedocs.io.


Features
--------

* Applies the latest packages on the OS.

Usage
--------

.. code-block:: python

    import os
    import pyarchops_os_updates

    api = Api(
        '127.0.0.1:22',
        connection='smart',
        remote_user='ubuntu',
        private_key_file=os.getenv('HOME') + '/.ssh/id_rsa',
        become=True,
        become_user='root',
        sudo=True,
        ssh_extra_args='-o StrictHostKeyChecking=no'
    )
    result = pyarchops_os_updates.apply(api)
    print(result)

Development
-----------

Install requirements:

.. code-block:: console

    $ sudo pacman -S tmux python-virtualenv python-pip libjpeg-turbo gcc make
    vim git tk tcl

Git clone this repository

.. code-block:: console

    git clone https://github.com/pypyarchops/os-updates.git pypyarchops.os-updates
    cd pypyarchops.os-updates


2. See the `Makefile`, to get started simply execute:

.. code-block:: console

    $ make up


Credits
-------

* TODO

