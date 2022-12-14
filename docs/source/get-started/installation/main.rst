Installation
============

This document describes the steps for installing the HOP Command Line
Tool. The main usage of the tool is bootstraping new HOP based web
platforms, but it also provides utilities for managing already
deployed applications. All the available utilities are described in
the :ref:`/reference/hop-cli/main` page.

At the end of this tutorial you will be ready to start bootstraping
your first HOP based project.

Prerequisites
-------------

For running the HOP Command Line Tool two programs are required:

* `Babashka <https://github.com/babashka/babashka>`_ is a fast
starting native Clojure interpreter, and it's leveraged by HOP for
running the Command Line Tool.
* `OpenSSL <https://www.openssl.org/>`_ provides cryptographical
capabilities to the HOP Command Line Tool. It's used to safely store
credentials, and to run other crypto operations like creating
self-signed SSL certificates.

Install Babashka
++++++++++++++++

There are multiple installation options available depending on your
Operation System and package manager of choice. You can find them
described in the `official documentation
<https://github.com/babashka/babashka#installation>`_.

Once you are done with the installation, you check that the
installation was succesfull by running the following:

.. code-block:: console
   $: bb version
   Babashka v0.10.163

At the moment the HOP Command Line Tool doesn't require a specific
version of Babashka. Using the latest available version is
recommended.

Install OpenSSL
++++++++++++++++

OpenSSL is a widely used tool, so you might already have it installed
in your system. You can check that by running the following command:

.. code-block:: console
   $: openssl version
   bash: openssl: command not found

If a version number is returned, you already have it installed, and no
further steps are needed. No specific version of OpenSSL is
required, but using the latest available version is recommended.

If not, you will have to install the program.

For ``Ubuntu`` you can:
.. code-block:: console
   $: sudo apt install openssl

For MacOs:
.. code-block:: console
   $: TODO

We don't provide installation steps for other Operating Systems, but
as it's a very common tool it should be straightfordward to find the
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
jar file that can be run from the command line using Babashka.

The mentioned file can be downloaded from the `Github Releases section
<https://github.com/gethop-dev/hop-cli/releases>`_. Download the
``hop-cli.jar` file from the latest available release, and place it in
the directory in which you will run the tool.

Run the HOP Command Line Tool
-----------------------------

Open a terminal in the folder where you downloaded the `hop-cli.jar`
file and run it using Babashka. All the available subcommands provided
by the tool will be printed.

.. code-block:: console
   $: bb hop-cli.jar
   Usage:  <subcommand> <options>

   Subcommands
     bootstrap  HOP bootstrap commands
     aws        AWS utility commands
     keycloak   Keycloak utility commands

You are now ready for bootstraping your first HOP project. You can
follow the :ref:`/get-started/aws-run-project/main` tutorial for
creating and deploying a HOP application into the Amazon Web Services
cloud provider.
