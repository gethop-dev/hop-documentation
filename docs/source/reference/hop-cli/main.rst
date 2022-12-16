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

bootstrap new-project
~~~~~~~~~~~~~~~~~~~~~

Description
+++++++++++
Command for bootstraping a new HOP based project. That includes
provisioning the infrastructure and generating the project files.

Synopsis
++++++++
.. code-block:: console

   $: bb hop-cli.jar bootstrap new-project
      --settings-file-path <value>
      --target-project-dir <value>

Options
+++++++

``-s, --settings-file-path`` (string)

Path to the HOP CLI ``settings.edn`` file.

``-d, --target-project-dir`` (string)

Directory in which the new project will be created.

Output
++++++

The project will be created in the specified ``target-project-dir``
directory.

The program will also display post-installation messages containing
actions that have to be performed manually to complete the bootstrap.

bootstrap prod-infrastructure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Description
+++++++++++
Command for provisioning the infrastructure for the production environment.

Synopsis
++++++++
.. code-block:: console

   $: bb hop-cli.jar bootstrap prod-infrastructure
      --settings-file-path <value>


Options
+++++++

``-s, --settings-file-path`` (string)

Path to the HOP CLI ``settings.edn`` file. It should be the same file
used when bootstrapping the project.

Outputs
+++++++

The program will also display post-installation messages containing
actions that have to be performed manually to complete the production
environment setup.

aws env-vars
------------

Commands for getting, setting and updating environment variables in
Elastic Beanstalk using SSM Parameter Store.

env-vars sync
~~~~~~~~~~~~~

Description
+++++++++++

Command for synchronizing local environment variables with the remote
environment variable storage in SSM Parameter Store.

Synopsis
++++++++

.. code-block:: console
   $: bb aws-cli.jar aws env-vars sync
      --project-name <value>
      --environment <value>
      --file <value>
      --kms-key-alias <value>

Options
+++++++

``-p, --project-name`` (string)

``-e, --environment`` (string)

Target environment to update. E.g., prod, test

``-f, --file`` (string)

Path to a file with a list of environment variables with the following
format:

.. code-block:: text
   ENV_VAR_1=VALUE ONE
   # Comments are ignored
   ENV_VAR_2=VALUE TWO

``-k, --kms-key-alias`` (string)

Alias of the KMS Key that will be used to encrypt the environment variables.

env-vars download
~~~~~~~~~~~~~~~~

Description
+++++++++++

Command for downloading the environment variables from AWS SSM
Parameter Store into a file.

Synopsis
++++++++

.. code-block:: console
   $: bb aws-cli.jar aws env-vars download
      --project-name <value>
      --environment <value>
      --file <value>
      --kms-key-alias <value>

Options
+++++++

``-p, --project-name`` (string)

``-e, --environment`` (string)

Environment from where the variables will be obtained. E.g., prod, test

``-f, --file`` (string)

Path where the environment variables will be saved to.

``-k, --kms-key-alias`` (string)

Alias of the KMS Key that will be used to decrypt the environment variables.

Outputs
+++++++

The environment variables will be saved to the specified ``file``.

env-vars apply-changes
~~~~~~~~~~~~~~~~~~~~~~

Description
+++++++++++

Command for triggering an Elastic Beanstalk environment restart. In
order to update the environment variables in Elastic Beanstalk, the
environment has to be restarted. This can be done automatically by AWS
(deploying a new application version...), using the AWS Console, or by
running this command.

Synopsis
++++++++
.. code-block:: console
   $: bb aws-cli.jar aws env-vars apply-changes
      --project-name <value>
      --environment <value>

Options
+++++++

``-p, --project-name`` (string)

``-e, --environment`` (string)


aws ssl
------------

ssl create-and-upload-self-signed-certificate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Description
+++++++++++

Command for creating and uploading a self-signed certificate to AWS
Certificate Manager.

Synopsis
++++++++

.. code-block:: console

   $: bb hop-cli.jar aws ssl create-and-upload-self-signed-certificate

Options
+++++++
None

Outputs
+++++++
None

aws cognito
-----------

aws cognito create-user
~~~~~~~~~~~~~~~~~~~~~~

Description
+++++++++++

Create user in the specified Cognito User Pool.

Synopsis
++++++++

.. code-block:: console

   $: bb hop-cli.jar aws cognito create-user
      --user-pool-id <value>
      --username <value>
      [--attributes <value>]
      [--temporary-password <value>]


Options
+++++++

``-up, --user-pool-id`` (string)

``-u, ---username`` (string)

``-a, --attributes`` (string)

User attributes in the form of ``ATTRIBUTE1=VAL1 ATTRIBUTE2=VAL2``

``-p, --temporary-password`` (string)

aws cognito set-user-password
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Description
+++++++++++

Change the password of the specified user.

Synopsis
++++++++

.. code-block:: console

   $: bb hop-cli.jar aws cognito set-user-password
      --user-pool-id <value>
      --username <value>
      --password <value>
      [--temporary? <value>]

Options
+++++++

``-up, --user-pool-id`` (string)

``-u, ---username`` (string)

``-p, --password`` (string)

``-t, --temporary?`` (boolean)

aws cognito get-id-token
~~~~~~~~~~~~~~~~~~~~~~~~

Description
+++++++++++

Get OIDC identity token for the specified user.

Synopsis
++++++++

.. code-block:: console

   $: bb hop-cli.jar aws cognito get-id-token
      --user-pool-id <value>
      --username <value>
      --password <value>


Options
+++++++

``-up, --user-pool-id`` (string)

``-u, --username`` (string)

``-u, --password`` (string)

Output
++++++

.. code-block:: clojure
  {:success? true,
   :id-token
   "eyJraWQiOiJNTll6Z1VsR0VOQ0NBNUhYT0RGNFJcL1ArNmdSWml1MnJCMkNtYmRXaVZhND0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJlZGU5MWJiMS00MGI2LTRjYzAtYTRmMS1lNWIzNDE5MzdlNjMiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmV1LXdlc3QtMS5hbWF6b25hd3MuY29tXC9ldS13ZXN0LTFfeWxZc1J5VFNkIiwiY29nbml0bzp1c2VybmFtZSI6ImVkZTkxYmIxLTQwYjYtNGNjMC1hNGYxLWU1YjM0MTkzN2U2MyIsIm9yaWdpbl9qdGkiOiI2YjAyZjNmNy03ZDY2LTRlYTMtODk2MC1jNTAwYTg1YmVlODciLCJhdWQiOiI3c3RobHRtZjU5a2ZoY2RhajRlanIzdTZzMSIsImV2ZW50X2lkIjoiZGI3M2ViYjUtY2IxMC00NTc3LTljMmYtYWI5Y2JlY2IzYjFiIiwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE2NzExODYyMzAsImV4cCI6MTY3MTE4OTgzMCwiaWF0IjoxNjcxMTg2MjMwLCJqdGkiOiJiMzkyNzVhMy1hMTI4LTRkM2ItYjZlNS1hY2FjZDZjYzgxZjUiLCJlbWFpbCI6InRlc3RAbWFnbmV0LmNvb3AifQ.Oy6oSX3UUn8BxLZJbXD_9io7YpslfVQNne4aFkv7O18fBg0N6oCpkI3_kDuS1JSyvItF6xgA377v066hK8JBD_WqC2Cl4k61N79uCVLVCkyerrfEcVVHcX3khMeZaD3buv23p2qtyNK6Hhvghe-UXCJKSY5cyRtXSNlLTnoQleJB6anzALA4jh1L3fwEMFRvdaV36LA9MhTRbaW0gQUFj7P0DZC7DaaWjekGcrs3ro7ZH3ceOqXE-2pnD-pGaJ2JXIBMR_xxLHTjTDvvRORfHHu4UQ0x21znPBbfzVJYJDnDsIDD7Zw1HmlBZFV0RL6yDDS2DbHplJq8p3STtqXp1A"}

keycloak
---------

keycloak create-user
~~~~~~~~~~~~~~~~~~~~~~

Description
+++++++++++

Create user in the specified Keycloak Realm.

Synopsis
++++++++

.. code-block:: console

   $: bb hop-cli.jar keycloak create-user
      --base-url <value>
      --admin-realm-name <value>
      --admin-client-id <value>
      --admin-username <value>
      --admin-password <value>
      --realm-name <value>
      --username <value>
      [--temporary-password <value>]
      [--attributes <value>]
      [--first-name <value>]
      [--last-name <value>]
      [--email <value>]
      [--email-verified <value>]


Options
+++++++

``-bu, --base-url`` (string)

``-ar, --admin-realm-name`` (string)

``-ac, --admin-client-id`` (string)

``-au, --admin-username`` (string)

``-ap, --admin-password`` (string)

``-r, --realm-name`` (string)

``-u, --username`` (string

``-p, --temporary-password`` (string

``-a, --attributes`` (string)

User attributes in the form of ``ATTRIBUTE1=VAL1 ATTRIBUTE2=VAL2``

``--first-name`` (string)

``--last-name`` (string)

``email`` (string)

``email-verified`` (string)

keycloak set-user-password
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Description
+++++++++++

Change the password of the specified user.

Synopsis
++++++++

.. code-block:: console

   $: bb hop-cli.jar keycloak set-user-password
      --base-url <value>
      --admin-realm-name <value>
      --admin-client-id <value>
      --admin-username <value>
      --admin-password <value>
      --realm-name <value>
      --user-id <value>
      --password <value>
      [--temporary? <value>]

Options
+++++++

``-bu, --base-url`` (string)

``-ar, --admin-realm-name`` (string)

``-ac, --admin-client-id`` (string)

``-au, --admin-username`` (string)

``-ap, --admin-password`` (string)

``-r, --realm-name`` (string)

``-p, --password`` (string)

``-t, --temporary?`` (boolean)

keycloak get-user
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Description
+++++++++++

Get the details about the specified Keycloak user.

Synopsis
++++++++

.. code-block:: console

   $: bb hop-cli.jar keycloak set-user-password
      --base-url <value>
      --admin-realm-name <value>
      --admin-client-id <value>
      --admin-username <value>
      --admin-password <value>
      --realm-name <value>
      --username <value>

Options
+++++++

``-bu, --base-url`` (string)

``-ar, --admin-realm-name`` (string)

``-ac, --admin-client-id`` (string)

``-au, --admin-username`` (string)

``-ap, --admin-password`` (string)

``-u, --username`` (string)


aws cognito get-id-token
~~~~~~~~~~~~~~~~~~~~~~~~

Description
+++++++++++

Get OIDC identity token for the specified user.

Synopsis
++++++++

.. code-block:: console

   $: bb hop-cli.jar keycloak get-id-token
      --base-url <value>
      --realm-name <value>
      --client-id <value>
      --username <value>
      --password <value>


Options
+++++++

``-bu, --base-url`` (string)

``-r, --realm-name`` (string)

``-c, --client-id`` (string)

``-u, --username`` (string)

``-p, --password`` (string)
