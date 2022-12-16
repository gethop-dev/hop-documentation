HOP Command Line Tool reference
===============================

bootstrap
---------

bootstrap copy-settings
~~~~~~~~~~~~~~~~~~~~~

Description
+++++++++++
Command for getting a copy of the sample ``settings.edn`` file used by
the Bootstrap tool.

Synopsis
++++++++
.. code-block:: console

   $: bb hop-cli.jar bootstrap copy-settings
      --settings-file-path <value>

Options
+++++++
``-s, --settings-file-path`` (string)
Path where the ``settings.edn`` file will be copied to.

Output
++++++
The file will be copied to the specified ``settings-file-path``.
