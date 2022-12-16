HOP Command Line Tool reference
===============================

Bootstrap
---------

bootstrap copy-settings
~~~~~~~~~~~~~~~~~~~~~

Command for getting a copy of the sample ``settings.edn`` file used by
the Bootstrap tool.

.. code-block:: console

   $: bb hop-cli.jar bootstrap copy-settings [OPTIONS]

Options
+++++++

.. code-block:: console

   -s, --settings-file-path

Path where the ``settings.edn`` file will be copied to.

bootstrap new-project
~~~~~~~~~~~~~~~~~~~~~

Command for bootstraping a new HOP based project. That includes
provisioning the infrastructure and generating the project files.

.. code-block:: console

   $: bb hop-cli.jar bootstrap new-project [OPTIONS]

Options
+++++++

.. code-block:: console

   -s, --settings-file-path

Path to the HOP CLI ``settings.edn`` file.

.. code-block:: console

   -d, --target-project-dir

Directory in which the new project will be created.

bootstrap prod-infrastructure
~~~~~~~~~~~~~~~~~~~~~

Command for provisioning the infrastructure for the production environment.

.. code-block:: console

   $: bb hop-cli.jar bootstrap prod-infrastructure [OPTIONS]

Options
+++++++

.. code-block:: console

   -s, --settings-file-path

Path to the HOP CLI ``settings.edn`` file. It should be the same file
used when bootstrapping the project.


AWS
---

Keycloak
--------
