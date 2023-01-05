HOP Command Line Interface tool (HOP CLI) reference
===================================================

In this documentation, the commands described in each synopsis sections are not meant
to be copy-pasted directly into your terminal console. They are just a description of
their capabilities.

Every command's synopsis will have the following notation:

.. code-block:: text

   <COMMAND>
   --OPTION <value>
   [--OPTIONAL-OPTION <value>]
   ...

bootstrap
---------

bootstrap create-settings-file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Description
+++++++++++
Creates a file with a copy of the default HOP CLI configuration.

Synopsis
++++++++
.. code-block:: text

   bootstrap create-settings-file
   --settings-file-path <value>

Options
+++++++
``-s, --settings-file-path`` (string)

Path where the settings file will be copied to.

Output
++++++
The file will be copied to the specified ``settings-file-path``.

bootstrap copy-settings
~~~~~~~~~~~~~~~~~~~~~~~

Description
+++++++++++
This is an alias for the ``bootstrap create-settings-file`` command.

bootstrap new-project
~~~~~~~~~~~~~~~~~~~~~

Description
+++++++++++
Command for bootstrapping a new HOP Application. That includes
provisioning the infrastructure and generating the project files.

Synopsis
++++++++
.. code-block:: text

   bootstrap new-project
   --settings-file-path <value>
   --target-project-dir <value>

Options
+++++++

``-s, --settings-file-path`` (string)

Path to the HOP CLI settings file.

``-d, --target-project-dir`` (string)

Directory in which the new project will be created.

Output
++++++

The HOP Project will be created in the specified ``target-project-dir``
directory.

The HOP CLI will also display post-installation messages containing
actions that have to be performed manually to complete the bootstrap.

bootstrap prod-infrastructure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Description
+++++++++++
Command for provisioning the infrastructure for the production environment.

Synopsis
++++++++

.. code-block:: text

   bootstrap prod-infrastructure
   --settings-file-path <value>


Options
+++++++

``-s, --settings-file-path`` (string)

Path to the HOP CLI settings file. It should be the same file used
when bootstrapping the HOP Application.

Outputs
+++++++

The HOP CLI will also display post-installation messages containing
actions that have to be performed manually to complete the production
environment setup.

aws env-vars
------------

Commands for getting, setting and updating environment variables in
AWS Elastic Beanstalk using AWS SSM Parameter Store.

env-vars sync
~~~~~~~~~~~~~

Description
+++++++++++

Command for synchronizing local environment variables with the remote
environment variables storage in AWS SSM Parameter Store.

Synopsis
++++++++

.. code-block:: text

   aws env-vars sync
   --project-name <value>
   --environment <value>
   --file <value>
   --kms-key-alias <value>
   [--region <value>]

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

Alias of the AWS KMS Key that will be used to encrypt the environment variables.

``-r, --region`` (string)

env-vars download
~~~~~~~~~~~~~~~~~

Description
+++++++++++

Command for downloading the environment variables from AWS SSM
Parameter Store into a file.

Synopsis
++++++++

.. code-block:: text

   aws env-vars download
   --project-name <value>
   --environment <value>
   --file <value>
   --kms-key-alias <value>
   [--region <value>]

Options
+++++++

``-p, --project-name`` (string)

``-e, --environment`` (string)

Environment from where the variables will be obtained. E.g., prod, test

``-f, --file`` (string)

Path where the environment variables will be saved to.

``-k, --kms-key-alias`` (string)

Alias of the AWS KMS Key that will be used to decrypt the environment variables.

``-r, --region`` (string)

Outputs
+++++++

The environment variables will be saved to the specified ``file``.

env-vars apply-changes
~~~~~~~~~~~~~~~~~~~~~~

Description
+++++++++++

Command for triggering an AWS Elastic Beanstalk environment
restart. In order to update the environment variables in AWS Elastic
Beanstalk, the environment has to be restarted. This can be done
automatically by AWS (deploying a new application version...), using
the AWS Console, or by running this command.

Synopsis
++++++++
.. code-block:: text

   aws env-vars apply-changes
   --project-name <value>
   --environment <value>
   [--region <value>]

Options
+++++++

``-p, --project-name`` (string)

``-e, --environment`` (string)

``-r, --region`` (string)

aws ssl
------------

ssl create-and-upload-self-signed-certificate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Description
+++++++++++

Command for creating and uploading a self-signed certificate to AWS
Certificate Manager.

Synopsis
++++++++

.. code-block:: text

   aws ssl create-and-upload-self-signed-certificate
   [--region <value>]

Options
+++++++

``-r, --region`` (string)

Outputs
+++++++
None.

aws cognito
-----------

aws cognito create-user
~~~~~~~~~~~~~~~~~~~~~~~

Description
+++++++++++

Create user in the specified AWS Cognito User Pool.

Synopsis
++++++++

.. code-block:: text

   aws cognito create-user
   --user-pool-id <value>
   --username <value>
   [--attributes <value>]
   [--temporary-password <value>]
   [--region <value>]


Options
+++++++

``-up, --user-pool-id`` (string)

``-u, ---username`` (string)

``-a, --attributes`` (string)

User attributes in the form of ``ATTRIBUTE1=VAL1 ATTRIBUTE2=VAL2``

``-p, --temporary-password`` (string)

``-r, --region`` (string)

Output
++++++

.. code-block:: clojure

  {:success? true,
   :user
   {:Username "aeb8a8c5-f136-49ca-be39-3a4923c0e9a1",
    :Attributes
    [{:Name "sub", :Value "aeb8a8c5-f136-49ca-be39-3a4923c0e9a1"}
     {:Name "name", :Value "TestUser"}
     {:Name "email", :Value "testuser1@invalid.invalid"}],
    :UserCreateDate #inst "2022-12-16T10:36:41.000-00:00",
    :UserLastModifiedDate #inst "2022-12-16T10:36:41.000-00:00",
    :Enabled true,
    :UserStatus "FORCE_CHANGE_PASSWORD"}}

aws cognito set-user-password
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Description
+++++++++++

Change the password of the specified user.

Synopsis
++++++++

.. code-block:: text

   aws cognito set-user-password
   --user-pool-id <value>
   --username <value>
   --password <value>
   [--temporary? <value>]
   [--region <value>]

Options
+++++++

``-up, --user-pool-id`` (string)

``-u, ---username`` (string)

``-p, --password`` (string)

``-t, --temporary?`` (boolean)

``-r, --region`` (string)

aws cognito get-id-token
~~~~~~~~~~~~~~~~~~~~~~~~

Description
+++++++++++

Get OIDC identity token for the specified user.

Synopsis
++++++++

.. code-block:: text

   aws cognito get-id-token
   --user-pool-id <value>
   --username <value>
   --password <value>
   [--region <value>]


Options
+++++++

``-up, --user-pool-id`` (string)

``-u, --username`` (string)

``-u, --password`` (string)

``-r, --region`` (string)

Output
++++++

.. code-block:: clojure

  {:success? true,
   :id-token
   "eyJraWQiOiJNTll6Z1VsR0VOQ0NBNUhYT0RGNFJcL1ArNmdSWml1MnJCMkNtYmRXaVZhND0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJlZGU5MWJiMS00MGI2LTRjYzAtYTRmMS1lNWIzNDE5MzdlNjMiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmV1LXdlc3QtMS5hbWF6b25hd3MuY29tXC9ldS13ZXN0LTFfeWxZc1J5VFNkIiwiY29nbml0bzp1c2VybmFtZSI6ImVkZTkxYmIxLTQwYjYtNGNjMC1hNGYxLWU1YjM0MTkzN2U2MyIsIm9yaWdpbl9qdGkiOiI2YjAyZjNmNy03ZDY2LTRlYTMtODk2MC1jNTAwYTg1YmVlODciLCJhdWQiOiI3c3RobHRtZjU5a2ZoY2RhajRlanIzdTZzMSIsImV2ZW50X2lkIjoiZGI3M2ViYjUtY2IxMC00NTc3LTljMmYtYWI5Y2JlY2IzYjFiIiwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE2NzExODYyMzAsImV4cCI6MTY3MTE4OTgzMCwiaWF0IjoxNjcxMTg2MjMwLCJqdGkiOiJiMzkyNzVhMy1hMTI4LTRkM2ItYjZlNS1hY2FjZDZjYzgxZjUiLCJlbWFpbCI6InRlc3RAbWFnbmV0LmNvb3AifQ.Oy6oSX3UUn8BxLZJbXD_9io7YpslfVQNne4aFkv7O18fBg0N6oCpkI3_kDuS1JSyvItF6xgA377v066hK8JBD_WqC2Cl4k61N79uCVLVCkyerrfEcVVHcX3khMeZaD3buv23p2qtyNK6Hhvghe-UXCJKSY5cyRtXSNlLTnoQleJB6anzALA4jh1L3fwEMFRvdaV36LA9MhTRbaW0gQUFj7P0DZC7DaaWjekGcrs3ro7ZH3ceOqXE-2pnD-pGaJ2JXIBMR_xxLHTjTDvvRORfHHu4UQ0x21znPBbfzVJYJDnDsIDD7Zw1HmlBZFV0RL6yDDS2DbHplJq8p3STtqXp1A"}

aws rds
-------

aws rds start-port-forwarding-session
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Description
+++++++++++

Execute command to start a port forwarding session to a RDS instance.

.. warning::

   In order to use this command you will need to have installed `awscli`_
   and the `AWS Session Manager plugin`_ for the mentioned tool.

Synopsis
++++++++

.. code-block:: text

   aws rds start-port-forwarding-session
   --project-name <value>
   --environment <value>
   --local-port <value>
   [--region <value>]

Options
+++++++

``-p, --project-name`` (string)

``-e, --environment`` (string)

``-lp, --local-port`` (string)

``-r, --region`` (string)

Output
++++++

If you execute the command to port-forward to the local port 5433, you will see the following output:

.. code-block:: text

   Running AWS Session Manager. Please, press ctrl+c in order to cancel the process.

   Starting session with SessionId: your-user-09f13864467cc8bb8
   Port 5433 opened for sessionId your-user-09f13864467cc8bb8.
   Waiting for connections...

keycloak
---------

keycloak create-user
~~~~~~~~~~~~~~~~~~~~~~

Description
+++++++++++

Create user in the specified Keycloak Realm.

Synopsis
++++++++

.. code-block:: text

   keycloak create-user
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

``--email`` (string)

``--email-verified`` (string)

keycloak set-user-password
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Description
+++++++++++

Change the password of the specified user.

Synopsis
++++++++

.. code-block:: text

   keycloak set-user-password
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

.. code-block:: text

   keycloak get-user
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

Output
++++++

.. code-block:: clojure

   {:success? true,
    :user
    {:requiredActions [],
     :email "hop-user@invalid.mail",
     :username "hop-user",
     :disableableCredentialTypes [],
     :firstName "hop-user",
     :emailVerified true,
     :id "8bcafd15-6ea9-406a-abd3-1e20a2aef024",
     :lastName "hop-user",
     :notBefore 0,
     :totp false,
     :access
     {:manageGroupMembership true,
      :view true,
      :mapRoles true,
      :impersonate true,
      :manage true},
     :enabled true,
     :createdTimestamp 1671186913182}}

keycloak get-id-token
~~~~~~~~~~~~~~~~~~~~~~~~

Description
+++++++++++

Get OIDC identity token for the specified user.

Synopsis
++++++++

.. code-block:: text

   keycloak get-id-token
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

Output
++++++

.. code-block:: clojure

   {:success? true,
    :id-token
    "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJXdzZNeV9PUURuMWJGalRqQ0ZVR3NVaEVqbTBBZVRXM0x4RENYTl9YZElZIn0.eyJleHAiOjE2NzExODcyNTMsImlhdCI6MTY3MTE4NzE5MywiYXV0aF90aW1lIjowLCJqdGkiOiI0Zjc2MWVmMi0xNjc0LTQ4YTMtODk0YS00ZDdlMDY3ZGIyODciLCJpc3MiOiJodHRwOi8vbG9jYWxob3N0OjgwODAvcmVhbG1zL21hc3RlciIsImF1ZCI6ImFkbWluLWNsaSIsInN1YiI6IjhiY2FmZDE1LTZlYTktNDA2YS1hYmQzLTFlMjBhMmFlZjAyNCIsInR5cCI6IklEIiwiYXpwIjoiYWRtaW4tY2xpIiwic2Vzc2lvbl9zdGF0ZSI6ImU0ZDAwMGIwLTY4NmItNDg2Ny1iNTk5LWRiYjNiNGJlYzNlMyIsImF0X2hhc2giOiI5Qk5fVmJBVFhhZmNCejRpQjdtdTl3IiwiYWNyIjoiMSIsInNpZCI6ImU0ZDAwMGIwLTY4NmItNDg2Ny1iNTk5LWRiYjNiNGJlYzNlMyIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJuYW1lIjoiaG9wLXVzZXIgaG9wLXVzZXIiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJob3AtdXNlciIsImdpdmVuX25hbWUiOiJob3AtdXNlciIsImZhbWlseV9uYW1lIjoiaG9wLXVzZXIiLCJlbWFpbCI6ImhvcC11c2VyQGludmFsaWQubWFpbCJ9.V0BrThYtjhvXKm9WlNLuDVSLrucBqRk4QllOC8U8IZj45jDGST7oFkqpnGIP6xSRbebe4Ow--56huDiXdPcymG9_A9Om_EiUvTbHN-Lm9fhx3JHSjt1w7vQ82SJXM2GuaLoF3FNda8MDc23HcFvfUvCPT_k7oIIflLy5udv5SFP7nWCWLFM8pknucHGEpeLLvzAD3mgL0Evdyw6X9DH6goAy0lRW_XtLYoNQj8ArpS4ZOCP8hglp2D66RYgxVl8uf2taps_70LtnL8-IkAUGw_Rc9QDINOHwPK3AnsCPgRp1RuEJPXQLP6-mWfJ-41YaPgB-1V6uvv90pyA8Ef4csQ"}

.. _awscli: https://aws.amazon.com/cli/
.. _AWS Session Manager plugin: https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-install-plugin.html
