=====================
pyArchOps OS updates
=====================


.. image:: https://img.shields.io/pypi/v/pyarchops_os_updates.svg
        :target: https://pypi.python.org/pypi/pyarchops_os_updates

.. image:: https://img.shields.io/travis/pyarchops/pyarchops_os_updates.svg
        :target: https://travis-ci.org/pyarchops/pyarchops_os_updates

.. image:: https://readthedocs.org/projects/pyarchops-os_updates/badge/?version=latest
        :target: https://pyarchops-os_updates.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/pyarchops/os-updates/shield.svg
     :target: https://pyup.io/repos/github/pyarchops/os-updates/
          :alt: Updates


Install All OS updates


* Free software: MIT license
* Documentation: https://pyarchops-os_updates.readthedocs.io.


Features
--------

* Applies the latest packages on the OS.

Usage
--------

.. code-block:: python

    import os
    import archops_os_updates

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
    result = archops_os_updates.apply(api)
    print(result)

Development
-----------

1. Install `tmux`

2. Install python requirements: `python3-virtualenv python3-pip`

3. Install `make`


See the `Makefile`, to get started simply execute:

.. code-block:: console

    $ make up


Credits
-------

* TODO

