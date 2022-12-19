Installation
============

This document describes the steps for installing the HOP Command Line
Tool. The main usage of the tool is bootstrapping new HOP-based web
applications[#]_.

.. [#] It also provides utilities for managing already deployed
   HOP-based applications. All the available utilities are
   described in the :doc:`/reference/hop-cli/main` page.

At the end of this tutorial you will be ready to bootstrap your first
HOP-based web application.

Prerequisites
-------------

Two third-party programs are required to run the HOP Command Line
Tool:

* `Babashka <https://github.com/babashka/babashka>`_, that provides a
  fast-starting, native Clojure interpreter. It is used to interpret
  (run) the Command Line Tool.
* `OpenSSL <https://www.openssl.org/>`_, that provides cryptographical
  capabilities to the HOP Command Line Tool. In HOP it is used to
  store credentials securely, and to run other crypto operations like
  creating self-signed SSL certificates.

Install Babashka
++++++++++++++++

There are multiple installation options available depending on your
Operating System and package manager of choice. You can find them
described in the `official documentation
<https://github.com/babashka/babashka#installation>`_.

Once you are done with the installation, you can check that the
installation was succesfull by running the following command from a
terminal:

.. code-block:: console

   $: bb version
   Babashka v0.10.163

As of this writing, the HOP Command Line Tool does not require a
specific version of Babashka. Using the latest available version is
generally recommended.

Install OpenSSL
++++++++++++++++

OpenSSL is a widely used tool, so you might already have it installed
on your system. You can check that by running the following command
from a terminal:

.. code-block:: console

   $: openssl version
   bash: openssl: command not found

If a version number is returned, you already have it installed and no
further steps are needed. No specific version of OpenSSL is required,
but using the latest available version is recommended.

If not, you will have to install the program.

For Debian/Ubuntu you can run the following command:

.. code-block:: console

   $: sudo apt install openssl

For MacOs you can run the following command (assuming you already have
``brew`` installed):

.. code-block:: console

   $: brew install openssl

We do not provide installation steps for other Operating Systems. But,
as it is a very common tool, it should be straightfordward to find the
steps on the web.

You can check that OpenSSL has been succesfully installed by running
the version command again:

.. code-block:: console

   $: openssl version
   OpenSSL 1.1.1n  15 Mar 2022

Download the HOP Command Line Tool
------------------------------------

The HOP Command Line Tool is distributed as a Babashka Uberjar. All
the required Clojure dependencies and resources are packed in a single
JAR file that can be run from the command line using Babashka.

The mentioned file can be downloaded from the `Github Releases
section`_. Download the ``hop-cli.jar`` file for the latest available
release.

.. _Github Releases section: https://github.com/gethop-dev/hop-cli/releases

Run the HOP Command Line Tool
-----------------------------

Open a terminal in the folder where you downloaded the ``hop-cli.jar``
file and run it using Babashka. All the available subcommands provided
by the tool will be printed:

.. code-block:: console

   $: bb hop-cli.jar
   Usage:  <subcommand> <options>

   Subcommands
     bootstrap  HOP bootstrap commands
     aws        AWS utility commands
     keycloak   Keycloak utility commands

.. note::

   You can save the ``hop-cli.jar`` in any directory of your
   choice. You just need to specify the path to the ``hop-cli.jar``
   file whenever executing ``bb``.

You are now ready to bootstrap your first HOP application. You can
follow the :doc:`/get-started/aws-run-project/main` tutorial to
create and deploya HOP application on Amazon Web Services cloud
provider.
