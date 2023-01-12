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

Three third-party programs are required to run the HOP CLI:

* `Babashka <https://github.com/babashka/babashka>`_, that provides a
  fast-starting, native Clojure interpreter. It is used to interpret
  (run) the HOP CLI itself, as it is written in Clojure.
* `bbin <https://github.com/babashka/bbin>`_, that provides utility
  commands for installing Babashka based tools.
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

Install bbin
++++++++++++

There are multiple installation options available depending on your
operation system. You can find them described in the `bbin
Installation page`_.

.. _bbin Installation page: https://github.com/babashka/bbin/blob/main/docs/installation.md

Once you are done with the installation, you can check that the
installation was successful by running the following command from a
terminal:

.. code-block:: console

   $ bbin version
   bbin 0.1.3

As of this writing, the HOP CLI requires bbin 0.1.3 or
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

Install the HOP CLI
-------------------

The HOP CLI is distributed as a Babashka Uberjar. All the required
Clojure dependencies and resources are packed in a single JAR file
that can be installed using bbin running the following command in a
terminal.

.. code-block:: console

   $ bbin install --as hop https://github.com/gethop-dev/hop-cli/releases/latest/download/hop-cli.jar

Run the HOP CLI
---------------

You can now run the HOP CLI by typing ``hop`` in a terminal. All the
available sub-commands provided by the tool will be printed:

.. code-block:: console

   $ hop
   Usage:  <subcommand> <options>

   Subcommands
     version    Get HOP CLI version
     bootstrap  HOP bootstrap commands
     aws        AWS utility commands
     keycloak   Keycloak utility commands

You are now ready to bootstrap your first HOP application. You can
follow the :doc:`/get-started/run-hop-application-on-aws/main`
tutorial to create and deploy a HOP application on Amazon Web Services
cloud provider.

.. rubric:: Footnotes

.. [#HopCliRef] It also provides utilities for managing already
   deployed HOP applications. All the available utilities are
   described in the :doc:`/reference/hop-cli/main` page.
