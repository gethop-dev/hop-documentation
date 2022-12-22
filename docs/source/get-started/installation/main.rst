Installation
============

This document describes the steps to install the HOP Command Line
Interface tool (HOP CLI, from here on). The main usage of the tool is
bootstrapping new HOP-based web applications [#HopCliRef]_, or HOP
applications for short.

At the end of this tutorial you will be ready to bootstrap your first
HOP application.

Prerequisites
-------------

Two third-party programs are required to run the HOP CLI:

* `Babashka <https://github.com/babashka/babashka>`_, that provides a
  fast-starting, native Clojure interpreter. It is used to interpret
  (run) the HOP CLI itself, as it is written in Clojure.
* `OpenSSL <https://www.openssl.org/>`_, that provides cryptographic
  capabilities to the HOP CLI. The HOP CLI uses it to store
  credentials securely, and to run other cryptographic operations like
  creating self-signed SSL certificates.

Install Babashka
++++++++++++++++

There are multiple installation options available depending on your
operating system and package manager of choice. You can find them
described in the `official documentation
<https://github.com/babashka/babashka#installation>`_.

Once you are done with the installation, you can check that the
installation was successful by running the following command from a
terminal:

.. code-block:: console

   $ bb version
   Babashka v1.0.168

As of this writing, the HOP CLI requires Babashka v1.0.168 or
later. Using the latest available version is generally recommended.

Install OpenSSL
+++++++++++++++

OpenSSL is a widely used tool, so you might have it installed on your
system already. You can check that by running the following command
from a terminal:

.. code-block:: console

   $ openssl version
   bash: openssl: command not found

If a version number is returned, you already have it installed and no
further steps are needed. No specific version of OpenSSL is required,
but using the latest available version is recommended.

If not, you will have to install the program.

For Debian/Ubuntu you can run the following command:

.. code-block:: console

   $ sudo apt install openssl

For macOS you can run the following command (assuming you already have
``brew`` installed):

.. code-block:: console

   $ brew install openssl

We do not provide installation steps for other operating systems. But,
as it is a very common tool, it should be straightforward to find the
steps on the web.

You can check that OpenSSL has been successfully installed by running
the version command again:

.. code-block:: console

   $ openssl version
   OpenSSL 1.1.1n  15 Mar 2022

Download the HOP CLI
--------------------

The HOP CLI is distributed as a Babashka Uberjar. All the required
Clojure dependencies and resources are packed in a single JAR file
that can be run from the command line using Babashka.

The mentioned file can be downloaded from the `GitHub Releases
section`_. Download the ``hop-cli.jar`` file for the latest available
release.

.. _GitHub Releases section: https://github.com/gethop-dev/hop-cli/releases

Run the HOP CLI
---------------

Open a terminal in the folder where you downloaded the ``hop-cli.jar``
file and run it using Babashka. All the available sub-commands provided
by the tool will be printed:

.. code-block:: console

   $ bb hop-cli.jar
   Usage:  <subcommand> <options>

   Subcommands
     bootstrap  HOP bootstrap commands
     aws        AWS utility commands
     keycloak   Keycloak utility commands

.. note::

   You can save the ``hop-cli.jar`` in any directory of your
   choice. You just need to specify the path to the ``hop-cli.jar``
   file whenever you want to execute it with ``bb``.

You are now ready to bootstrap your first HOP application. You can
follow the :doc:`/get-started/run-hop-application-on-aws/main`
tutorial to create and deploy a HOP application on Amazon Web Services
cloud provider.

.. rubric:: Footnotes

.. [#HopCliRef] It also provides utilities for managing already
   deployed HOP applications. All the available utilities are
   described in the :doc:`/reference/hop-cli/main` page.
