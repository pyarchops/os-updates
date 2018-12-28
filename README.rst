=====================
pyArchOps/OS updates
=====================


.. image:: https://img.shields.io/pypi/v/pyarchops_os_updates.svg
        :target: https://pypi.python.org/pypi/pyarchops_os_updates

.. image:: https://img.shields.io/gitlab/pipeline/gitlab-org/gitlab-ce/master.svg
        :target: https://gitlab.com/pyarchops/os-updates/pipelines

.. image:: https://readthedocs.org/projects/os-updates/badge/?version=latest
        :target: https://os-updates.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/pyarchops/os-updates/shield.svg
     :target: https://pyup.io/repos/github/pyarchops/os-updates/
          :alt: Updates


Install All OS updates


* Free software: MIT license
* Documentation: https://pyarchops-os-updates.readthedocs.io.


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
        remote_user='root',
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

    $ sudo pacman -S tmux python-virtualenv python-pip libjpeg-turbo gcc make vim git tk tcl

Git clone this repository

.. code-block:: console

    $ git clone https://github.com/pyarchops/os-updates.git pyarchops.os-updates
    $ cd pyarchops.os-updates


2. See the `Makefile`, to get started simply execute:

.. code-block:: console

    $ make up


Credits
-------

* TODO

