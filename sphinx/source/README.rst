===========
selenium_py
===========

:Info: See `github <https://github.com/gavinln/selenium_py.git>`_ for the latest source.
:Author: Gavin Noronha <gavinln@hotmail.com>

About
=====

This project demonstrates the following technologies.
    #. Vagrant vm
    #. Puppet to install all software
    #. Virtualenv
    #. Python
    #. IPython
    #. Web based notebook for IPython
    #. Using selenium to drive Firefox on a headless server and take screenshots


Using
-----

The web notebooks are available at `<http://localhost:8888/>`_ are are used to
run Selenium to control a Firefox web browser and capture screenshots.

Running
=======

#. To start the virtual machine(VM) type::

    vagrant up

#. Connect to the VM::

    REM on windows
    vm\ssh_vagrant.bat

    # on unix
    vagrant ssh

#. Start the web notebook::

    /vagrant/vm/ipython_notebook.sh

#. Open the notebook in the browser at `<http://localhost:8888/>`_

The notebooks are stored in ``/vagrant/notebooks``

Requirements
------------

- `Oracle VM VirtualBox <https://www.virtualbox.org/>`_
- `Vagrant <http://vagrantup.com/>`_

Testing
-------
Need to create testing scripts.

Credits
=======

Thanks to (in no particular order):

- Glen Noronha
