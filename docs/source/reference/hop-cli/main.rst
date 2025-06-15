HOP Command Line Interface tool (HOP CLI) reference
===================================================

In this documentation, the commands described in each synopsis
sections are not meant to be copy-pasted directly into your terminal
console. They are just a description of their capabilities.

Every command's synopsis will have the following notation:

.. code-block:: text

   <COMMAND>
   --OPTION <value>
   [--OPTIONAL-OPTION <value>]
   ...

version
-------

version
~~~~~~~

Description
+++++++++++

Get HOP CLI version.

Synopsis
++++++++

.. code-block:: text

   version

Options
+++++++

None

Output
++++++

.. code-block:: text

   0.1.0-SNAPSHOT

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

Command for provisioning the infrastructure for the production
environment.

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

bootstrap open-settings-editor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Description
+++++++++++

Opens a web-based wizard for creating or editing the settings file.

Synopsis
++++++++
.. code-block:: text

   $ bootstrap open-settings-editor
     [--port <value>]

Options
+++++++

``-p, --port`` (number)

Port on which the web server will be launched. If not specified, the
default port number (8090) will be used.

Output
++++++

.. code-block:: text

   Settings Editor running at http://localhost:8090

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

.. warning::

   In order to use this command you need run it with some AWS
   credentials that have the permissions to list, read and write
   parameters in the SSM Parameter Store. Probably the easiest way to
   do it is by using `aws-vault` tool to run HOP CLI.

Synopsis
++++++++

.. code-block:: text

   aws env-vars sync
   --project-name <value>
   --environment <value>
   --file <value>
   --kms-key-alias <value>
   --region <value>

Options
+++++++

``-p, --project-name`` (string)

Name of the project, the one used to originally create it with HOP CLI.

``-e, --environment`` (string)

Target environment to update. E.g., prod, test, etc.

``-f, --file`` (string)

Path to a file with a list of environment variables, with the
following format:

.. code-block:: text

   ENV_VAR_1='VALUE ONE'
   # Comments are ignored
   ENV_VAR_2='VALUE TWO'

``-k, --kms-key-alias`` (string)

Alias of the AWS KMS Key that will be used to encrypt the environment
variables in the AWS SSM Parameter Store.

``-r, --region`` (string)

AWS region to use for the operation.

env-vars download
~~~~~~~~~~~~~~~~~

Description
+++++++++++

Command for downloading the environment variables from the AWS SSM
Parameter Store into a file.

.. warning::

   In order to use this command you need run it with some AWS
   credentials that have the permissions to list, read and write
   parameters in the SSM Parameter Store. Probably the easiest way to
   do it is by using `aws-vault` tool to run HOP CLI.

Synopsis
++++++++

.. code-block:: text

   aws env-vars download
   --project-name <value>
   --environment <value>
   --file <value>
   --kms-key-alias <value>
   --region <value>

Options
+++++++

``-p, --project-name`` (string)

Name of the project, the one used to originally create it with HOP CLI.

``-e, --environment`` (string)

Environment from where the variables will be obtained. E.g., prod,
test, etc.

``-f, --file`` (string)

Path of the file where the environment variables will be saved to.

``-k, --kms-key-alias`` (string)

Alias of the AWS KMS Key that will be used to decrypt the environment
variables from the AWS SSM Parameter Store.

``-r, --region`` (string)

AWS region to use for the operation.

Outputs
+++++++

The environment variables will be saved to the file specified by
``file``.

env-vars apply-changes
~~~~~~~~~~~~~~~~~~~~~~

Description
+++++++++++

Command for triggering an AWS Elastic Beanstalk environment
restart. In order to update the environment variables in AWS Elastic
Beanstalk, the environment has to be restarted. This can be done
automatically by AWS Elastic Beanstalk (deploying a new application
version, etc.), using the AWS Console, or by running this command.

.. warning::

   In order to use this command you need run it with some AWS
   credentials that have the permissions to update an environment in
   AWS Elastic Beanstalk. Probably the easiest way to do it is by
   using `aws-vault` tool to run HOP CLI.

Synopsis
++++++++
.. code-block:: text

   aws env-vars apply-changes
   --project-name <value>
   --environment <value>
   --region <value>

Options
+++++++

``-p, --project-name`` (string)

Name of the project, the one used to originally create it with HOP CLI.

``-e, --environment`` (string)

Environment where the changes will be applied. E.g., prod, test, etc.

``-r, --region`` (string)

AWS region to use for the operation.

aws ssl
------------

ssl create-and-upload-self-signed-certificate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Description
+++++++++++

Command for creating and uploading a self-signed certificate to AWS
Certificate Manager.

.. warning::

   In order to use this command you need run it with some AWS
   credentials that have the permissions to import certificates in the
   Certificate Manager. Probably the easiest way to do it is by using
   `aws-vault` tool to run HOP CLI.

Synopsis
++++++++

.. code-block:: text

   aws ssl create-and-upload-self-signed-certificate
   --region <value>

Options
+++++++

``-r, --region`` (string)

AWS region to use for the operation.

Outputs
+++++++

None.

aws cognito
-----------

aws cognito create-user
~~~~~~~~~~~~~~~~~~~~~~~

Description
+++++++++++

Create a user in the specified AWS Cognito User Pool.

.. warning::

   In order to use this command you need run it with some AWS
   credentials that have the permissions to create new users in
   Cognito User Pools. Probably the easiest way to do it is by using
   `aws-vault` tool to run HOP CLI.

Synopsis
++++++++

.. code-block:: text

   aws cognito create-user
   --user-pool-id <value>
   --username <value>
   [--attributes <value>]
   [--temporary-password <value>]
   --region <value>


Options
+++++++

``-up, --user-pool-id`` (string)

ID of the AWS Cognito UserPool in which the user whose password you
want to create will be located.

``-u, ---username`` (string)

Value to be used as the Username. The type of value to specify here
will depend on the configuration of the User Pool (e.g., an email
address, a phone number, etc.)

``-a, --attributes`` (string)

Collection of attributes to assign to the user, in the form of
``ATTRIBUTE=VALUE``. Use the option multiple times to assign multiple
attributes to the user. E.g., ``aws cognito-idp create-user
... --attributes 'email=user@mail.invalid' --attributes
'phone_number=+34000000001'``

``-p, --temporary-password`` (string)

Temporary password to assign to the newly created user. This
temporary password must conform to the password policy of the User
Pool.

If not specified, AWS Cognito will create a random password and send
it to the newly created email or phone number (depending on the
configuration of the User Pool).

``-r, --region`` (string)

AWS region to use for the operation.

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

Change the password of the specified AWS Cognito User Pool user.

.. warning::

   In order to use this command you need run it with some AWS
   credentials that have the permissions to administratively reset the
   password of a Cognito User Pool user. Probably the easiest way to
   do it is by using `aws-vault` tool to run HOP CLI.

Synopsis
++++++++

.. code-block:: text

   aws cognito set-user-password
   --user-pool-id <value>
   --username <value>
   --password <value>
   [--temporary? <value>]
   --region <value>

Options
+++++++

``-up, --user-pool-id`` (string)

ID of the AWS Cognito UserPool in which the user whose password you
want to reset is located.

``-u, ---username`` (string)

Username whose password you want to reset.

``-p, --password`` (string)

New password for the user whose password you want to reset.

``-t, --temporary?`` (boolean)

Set this argument to ``true`` to make the password temporary. That is,
the user will have to change it next time it logs on.

``-r, --region`` (string)

AWS region to use for the operation.

aws cognito get-id-token
~~~~~~~~~~~~~~~~~~~~~~~~

Description
+++++++++++

Get an OpenID Connect Identity Token (ID token) for the specified AWS
Cognito User Pool user.

.. warning::

   In order to use this command you need run it with some AWS
   credentials that have the permissions to authenticate any
   user. Probably the easiest way to do it is by using `aws-vault` tool
   to run HOP CLI.

Synopsis
++++++++

.. code-block:: text

   aws cognito get-id-token
   --user-pool-id <value>
   --client-id <value>
   --username <value>
   --password <value>
   --region <value>
   [--raw]


Options
+++++++

``-up, --user-pool-id`` (string)

ID of the AWS Cognito UserPool in which the user whose ID Token you
want to get is located.

``-c, --client-id`` (string)

ID of a valid App client for the AWS Cognito UserPool specified with
option ``--user-pool-id``.

``-u, --username`` (string)

Username of the user for which you want to get and ID Token.

``-p, --password`` (string)

Password of the user for which you want to get and ID Token.

``-r, --region`` (string)

AWS region to use for the operation.

``--raw``

Use this option to get the raw ID Token value, instead of a full EDN
map with the result.

Output
++++++

When executed without the ``--raw`` option:

.. code-block:: clojure

  {:success? true,
   :id-token
   "eyJraWQiOiJNTll6Z1VsR0VOQ0NBNUhYT0RGNFJcL1ArNmdSWml1MnJCMkNtYmRXaVZhND0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJlZGU5MWJiMS00MGI2LTRjYzAtYTRmMS1lNWIzNDE5MzdlNjMiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmV1LXdlc3QtMS5hbWF6b25hd3MuY29tXC9ldS13ZXN0LTFfeWxZc1J5VFNkIiwiY29nbml0bzp1c2VybmFtZSI6ImVkZTkxYmIxLTQwYjYtNGNjMC1hNGYxLWU1YjM0MTkzN2U2MyIsIm9yaWdpbl9qdGkiOiI2YjAyZjNmNy03ZDY2LTRlYTMtODk2MC1jNTAwYTg1YmVlODciLCJhdWQiOiI3c3RobHRtZjU5a2ZoY2RhajRlanIzdTZzMSIsImV2ZW50X2lkIjoiZGI3M2ViYjUtY2IxMC00NTc3LTljMmYtYWI5Y2JlY2IzYjFiIiwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE2NzExODYyMzAsImV4cCI6MTY3MTE4OTgzMCwiaWF0IjoxNjcxMTg2MjMwLCJqdGkiOiJiMzkyNzVhMy1hMTI4LTRkM2ItYjZlNS1hY2FjZDZjYzgxZjUiLCJlbWFpbCI6InRlc3RAbWFnbmV0LmNvb3AifQ.Oy6oSX3UUn8BxLZJbXD_9io7YpslfVQNne4aFkv7O18fBg0N6oCpkI3_kDuS1JSyvItF6xgA377v066hK8JBD_WqC2Cl4k61N79uCVLVCkyerrfEcVVHcX3khMeZaD3buv23p2qtyNK6Hhvghe-UXCJKSY5cyRtXSNlLTnoQleJB6anzALA4jh1L3fwEMFRvdaV36LA9MhTRbaW0gQUFj7P0DZC7DaaWjekGcrs3ro7ZH3ceOqXE-2pnD-pGaJ2JXIBMR_xxLHTjTDvvRORfHHu4UQ0x21znPBbfzVJYJDnDsIDD7Zw1HmlBZFV0RL6yDDS2DbHplJq8p3STtqXp1A"}

When executed with the ``--raw`` option:

.. code-block:: text

  eyJraWQiOiJNTll6Z1VsR0VOQ0NBNUhYT0RGNFJcL1ArNmdSWml1MnJCMkNtYmRXaVZhND0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJlZGU5MWJiMS00MGI2LTRjYzAtYTRmMS1lNWIzNDE5MzdlNjMiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmV1LXdlc3QtMS5hbWF6b25hd3MuY29tXC9ldS13ZXN0LTFfeWxZc1J5VFNkIiwiY29nbml0bzp1c2VybmFtZSI6ImVkZTkxYmIxLTQwYjYtNGNjMC1hNGYxLWU1YjM0MTkzN2U2MyIsIm9yaWdpbl9qdGkiOiI2YjAyZjNmNy03ZDY2LTRlYTMtODk2MC1jNTAwYTg1YmVlODciLCJhdWQiOiI3c3RobHRtZjU5a2ZoY2RhajRlanIzdTZzMSIsImV2ZW50X2lkIjoiZGI3M2ViYjUtY2IxMC00NTc3LTljMmYtYWI5Y2JlY2IzYjFiIiwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE2NzExODYyMzAsImV4cCI6MTY3MTE4OTgzMCwiaWF0IjoxNjcxMTg2MjMwLCJqdGkiOiJiMzkyNzVhMy1hMTI4LTRkM2ItYjZlNS1hY2FjZDZjYzgxZjUiLCJlbWFpbCI6InRlc3RAbWFnbmV0LmNvb3AifQ.Oy6oSX3UUn8BxLZJbXD_9io7YpslfVQNne4aFkv7O18fBg0N6oCpkI3_kDuS1JSyvItF6xgA377v066hK8JBD_WqC2Cl4k61N79uCVLVCkyerrfEcVVHcX3khMeZaD3buv23p2qtyNK6Hhvghe-UXCJKSY5cyRtXSNlLTnoQleJB6anzALA4jh1L3fwEMFRvdaV36LA9MhTRbaW0gQUFj7P0DZC7DaaWjekGcrs3ro7ZH3ceOqXE-2pnD-pGaJ2JXIBMR_xxLHTjTDvvRORfHHu4UQ0x21znPBbfzVJYJDnDsIDD7Zw1HmlBZFV0RL6yDDS2DbHplJq8p3STtqXp1A

aws rds
-------

aws rds start-port-forwarding-session
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Description
+++++++++++

Execute command to start a port forwarding session to the AWS RDS
instance associated with a given AWS Elastic Beanstalk project.

.. warning::

   In order to use this command you will need to have installed
   `awscli`_ and the `AWS Session Manager plugin`_ for the mentioned
   tool.

Synopsis
++++++++

.. code-block:: text

   aws rds start-port-forwarding-session
   --project-name <value>
   --environment <value>
   --local-port <value>
   --region <value>

Options
+++++++

``-p, --project-name`` (string)

Name of the project, the one used to originally create it with HOP CLI.

``-e, --environment`` (string)

Start the port forwarding session for the AWS RDS instance associated
with this environment. E.g., prod, test, etc.

``-lp, --local-port`` (string)

Local port, on your own machine, that will be port forwarded to the
AWS RDS instance port.

``-r, --region`` (string)

AWS region to use for the operation.

Output
++++++

If you execute the command to port-forward your local port 5433 to the
AWS RDS instance port, you will see the following output:

.. code-block:: text

   Running AWS Session Manager. Please, press ctrl+c in order to
   cancel the process.

   Starting session with SessionId: your-user-09f13864467cc8bb8
   Port 5433 opened for sessionId your-user-09f13864467cc8bb8.
   Waiting for connections...

keycloak
--------

keycloak create-user
~~~~~~~~~~~~~~~~~~~~

Description
+++++++++++

Create a user in the specified Keycloak Realm.

Synopsis
++++++++

.. code-block:: text

   keycloak set-user-password
   --base-url <value>
   [--insecure-connection]
   [--cacert <value>]
   --admin-username <value>
   --admin-password <value>
   --admin-realm-name <value>
   --admin-client-id <value>
   [--admin-client-secret <value>]
   --realm-name <value>
   --username <value>
   --temporary-password <value>
   [--attributes <value>]
   [--first-name <value>]
   [--last-name <value>]
   [--email <value>]
   [--email-verified <value>]

Options
+++++++

``-bu, --base-url`` (string)

The base URL for the Keycloak server. E.g., something like
``https://auth.project.domain``, or ``https://project.domain/auth``,
etc.

``-k, --insecure-connection``

If the Keycloak server is using a TLS/SSL certificate that is not
signed by one of the trusted Root Certification Authorities, you can
set this option to ``false`` to establish the connection to Keycloak,
ignoring the TLS/SSL certificate validation errors.

``--cacert`` (string)

If the Keycloak server is using a TLS/SSL certificate that is not
signed by one of the trusted Root Certification Authorities, but you
have a file that holds the Root Certification Authority certificate(s)
(in PEM format) that signed its TLS/SSL certificate, you can specify
the path of that file with this option.

``-au, --admin-username`` (string)

Username with administrator rights to perform the operation.

``-ap, --admin-password`` (string)

Password for the ``admin-username`` user.

``-ar, --admin-realm-name`` (string)

Name of the Keycloak realm where the ``admin-user`` exists.

``-ac, --admin-client-id`` (string)

Client Id to use with the ``admin-realm-name`` Keycloak realm.

``-acs, --admin-client-secret`` (string)

If the Client Id used with the ``admin-realm-name`` Keycloak realm has
a Client Secret configured, specify it with this option.

``-r, --realm-name`` (string)

Name of the Keycloak realm where the new user will be created.

``-u, --username`` (string)

Value to be used as the username of the user to create.

``-p, --temporary-password`` (string)

Temporary password to assign to the newly created user. This temporary
password must conform to the password policy of the ``realm-name``
Keycloak realm.

``--attributes`` (string)

Collection of attributes to assign to the user, in the form of
``ATTRIBUTE=VALUE``. Use the option multiple times to assign multiple
attributes to the user. E.g., ``keycloak create-user ... --attributes
'customer_id=123' --attributes 'customer_type=tier-1'``

``--first-name`` (string)

Value to be used as the first name of the user to create.

``--last-name`` (string)

Value to be used as the last name of the user to create.

``--email`` (string)

Value to be used as the email address of the user to create.

``--email-verified`` (boolean)

If set to ``true``, the email address of the user to create will be
configured as verified. The default value is ``false``, which means
the email address will be configured as unverified.

keycloak get-user
~~~~~~~~~~~~~~~~~

Description
+++++++++++

Get the details about the specified Keycloak user.

Synopsis
++++++++

.. code-block:: text

   keycloak get-user
   --base-url <value>
   [--insecure-connection]
   [--cacert <value>]
   --admin-username <value>
   --admin-password <value>
   --admin-realm-name <value>
   --admin-client-id <value>
   [--admin-client-secret <value>]
   --realm-name <value>
   --username <value>

Options
+++++++

``-bu, --base-url`` (string)

The base URL for the Keycloak server. E.g., something like
``https://auth.project.domain``, or ``https://project.domain/auth``,
etc.

``-k, --insecure-connection``

If the Keycloak server is using a TLS/SSL certificate that is not
signed by one of the trusted Root Certification Authorities, you can
set this option to ``false`` to establish the connection to Keycloak,
ignoring the TLS/SSL certificate validation errors.

``--cacert`` (string)

If the Keycloak server is using a TLS/SSL certificate that is not
signed by one of the trusted Root Certification Authorities, but you
have a file that holds the Root Certification Authority certificate(s)
(in PEM format) that signed its TLS/SSL certificate, you can specify
the path of that file with this option.

``-au, --admin-username`` (string)

Username with administrator rights to perform the operation.

``-ap, --admin-password`` (string)

Password for the ``admin-username`` user.

``-ar, --admin-realm-name`` (string)

Name of the Keycloak realm where the ``admin-user`` exists.

``-ac, --admin-client-id`` (string)

Client Id to use with the ``admin-realm-name`` Keycloak realm.

``-acs, --admin-client-secret`` (string)

If the Client Id used with the ``admin-realm-name`` Keycloak realm has
a Client Secret configured, specify it with this option.

``-r, --realm-name`` (string)

Name of the Keycloak realm where the user whose details you will get
resides.

``-u, --username`` (string)

Keycloak username whose details you want to get.

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

keycloak set-user-password
~~~~~~~~~~~~~~~~~~~~~~~~~~

Description
+++++++++++

Change the password of the specified Keycloak user.

Synopsis
++++++++

.. code-block:: text

   keycloak set-user-password
   --base-url <value>
   [--insecure-connection]
   [--cacert <value>]
   --admin-username <value>
   --admin-password <value>
   --admin-realm-name <value>
   --admin-client-id <value>
   [--admin-client-secret <value>]
   --realm-name <value>
   --user-id <value>
   --password <value>
   [--temporary? <value>]

Options
+++++++

``-bu, --base-url`` (string)

The base URL for the Keycloak server. E.g., something like
``https://auth.project.domain``, or ``https://project.domain/auth``,
etc.

``-k, --insecure-connection``

If the Keycloak server is using a TLS/SSL certificate that is not
signed by one of the trusted Root Certification Authorities, you can
set this option to ``false`` to establish the connection to Keycloak,
ignoring the TLS/SSL certificate validation errors.

``--cacert`` (string)

If the Keycloak server is using a TLS/SSL certificate that is not
signed by one of the trusted Root Certification Authorities, but you
have a file that holds the Root Certification Authority certificate(s)
(in PEM format) that signed its TLS/SSL certificate, you can specify
the path of that file with this option.

``-au, --admin-username`` (string)

Username with administrator rights to perform the operation.

``-ap, --admin-password`` (string)

Password for the ``admin-username`` user.

``-ar, --admin-realm-name`` (string)

Name of the Keycloak realm where the ``admin-user`` exists.

``-ac, --admin-client-id`` (string)

Client Id to use with the ``admin-realm-name`` Keycloak realm.

``-acs, --admin-client-secret`` (string)

If the Client Id used with the ``admin-realm-name`` Keycloak realm has
a Client Secret configured, specify it with this option.

``-r, --realm-name`` (string)

Name of the Keycloak realm where the user whose password you are going
to change resides.

``-u, --user-id`` (string)

Keycloak internal user ID for the user. You can get the user ID with
the ``get-user`` command.

``-p, --password`` (string)

New password to be assigned to the user.

``-t, --temporary?``

If set to ``true`` (the default value is ``false``), the new password
will be configured as temporary. In this case, the user will have to
change the password on first login.

keycloak get-id-token
~~~~~~~~~~~~~~~~~~~~~~~~

Description
+++++++++++

Get an OpenID Connect Identity Token (ID Token) for the specified
Keycloak user.

Synopsis
++++++++

.. code-block:: text

   keycloak get-id-token
   --base-url <value>
   [--insecure-connection]
   [--cacert <value>]
   --realm-name <value>
   --client-id <value>
   [--client-secret <value>]
   --username <value>
   --password <value>
   [--raw]

Options
+++++++

``-bu, --base-url`` (string)

The base URL for the Keycloak server. E.g., something like
``https://auth.project.domain``, or ``https://project.domain/auth``,
etc.

``-k, --insecure-connection``

If the Keycloak server is using a TLS/SSL certificate that is not
signed by one of the trusted Root Certification Authorities, you can
set this option to ``false`` to establish the connection to Keycloak,
ignoring the TLS/SSL certificate validation errors.

``--cacert`` (string)

If the Keycloak server is using a TLS/SSL certificate that is not
signed by one of the trusted Root Certification Authorities, but you
have a file that holds the Root Certification Authority certificate(s)
(in PEM format) that signed its TLS/SSL certificate, you can specify
the path of that file with this option.

``-r, --realm-name`` (string)

Name of the Keycloak realm where the user whose ID Token you want to
get resides.

``-c, --client-id`` (string)

Client Id to use with the ``realm-name`` Keycloak realm.

``-cs, --client-secret`` (string)

If the Client Id used with the ``realm-name`` Keycloak realm has
a Client Secret configured, specify it with this option.

``-u, --username`` (string)

The username of the user you want to get ID Token for.

``-p, --password`` (string)

Password for ``username``.

``--raw``

Use this option to get the raw ID Token value, instead of a full EDN
map with the result.


Output
++++++

When executed without the ``--raw`` option:

.. code-block:: clojure

   {:success? true,
    :id-token
    "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJXdzZNeV9PUURuMWJGalRqQ0ZVR3NVaEVqbTBBZVRXM0x4RENYTl9YZElZIn0.eyJleHAiOjE2NzExODcyNTMsImlhdCI6MTY3MTE4NzE5MywiYXV0aF90aW1lIjowLCJqdGkiOiI0Zjc2MWVmMi0xNjc0LTQ4YTMtODk0YS00ZDdlMDY3ZGIyODciLCJpc3MiOiJodHRwOi8vbG9jYWxob3N0OjgwODAvcmVhbG1zL21hc3RlciIsImF1ZCI6ImFkbWluLWNsaSIsInN1YiI6IjhiY2FmZDE1LTZlYTktNDA2YS1hYmQzLTFlMjBhMmFlZjAyNCIsInR5cCI6IklEIiwiYXpwIjoiYWRtaW4tY2xpIiwic2Vzc2lvbl9zdGF0ZSI6ImU0ZDAwMGIwLTY4NmItNDg2Ny1iNTk5LWRiYjNiNGJlYzNlMyIsImF0X2hhc2giOiI5Qk5fVmJBVFhhZmNCejRpQjdtdTl3IiwiYWNyIjoiMSIsInNpZCI6ImU0ZDAwMGIwLTY4NmItNDg2Ny1iNTk5LWRiYjNiNGJlYzNlMyIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJuYW1lIjoiaG9wLXVzZXIgaG9wLXVzZXIiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJob3AtdXNlciIsImdpdmVuX25hbWUiOiJob3AtdXNlciIsImZhbWlseV9uYW1lIjoiaG9wLXVzZXIiLCJlbWFpbCI6ImhvcC11c2VyQGludmFsaWQubWFpbCJ9.V0BrThYtjhvXKm9WlNLuDVSLrucBqRk4QllOC8U8IZj45jDGST7oFkqpnGIP6xSRbebe4Ow--56huDiXdPcymG9_A9Om_EiUvTbHN-Lm9fhx3JHSjt1w7vQ82SJXM2GuaLoF3FNda8MDc23HcFvfUvCPT_k7oIIflLy5udv5SFP7nWCWLFM8pknucHGEpeLLvzAD3mgL0Evdyw6X9DH6goAy0lRW_XtLYoNQj8ArpS4ZOCP8hglp2D66RYgxVl8uf2taps_70LtnL8-IkAUGw_Rc9QDINOHwPK3AnsCPgRp1RuEJPXQLP6-mWfJ-41YaPgB-1V6uvv90pyA8Ef4csQ"}

When executed with the ``--raw`` option:

.. code-block:: clojure

    eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJXdzZNeV9PUURuMWJGalRqQ0ZVR3NVaEVqbTBBZVRXM0x4RENYTl9YZElZIn0.eyJleHAiOjE2NzExODcyNTMsImlhdCI6MTY3MTE4NzE5MywiYXV0aF90aW1lIjowLCJqdGkiOiI0Zjc2MWVmMi0xNjc0LTQ4YTMtODk0YS00ZDdlMDY3ZGIyODciLCJpc3MiOiJodHRwOi8vbG9jYWxob3N0OjgwODAvcmVhbG1zL21hc3RlciIsImF1ZCI6ImFkbWluLWNsaSIsInN1YiI6IjhiY2FmZDE1LTZlYTktNDA2YS1hYmQzLTFlMjBhMmFlZjAyNCIsInR5cCI6IklEIiwiYXpwIjoiYWRtaW4tY2xpIiwic2Vzc2lvbl9zdGF0ZSI6ImU0ZDAwMGIwLTY4NmItNDg2Ny1iNTk5LWRiYjNiNGJlYzNlMyIsImF0X2hhc2giOiI5Qk5fVmJBVFhhZmNCejRpQjdtdTl3IiwiYWNyIjoiMSIsInNpZCI6ImU0ZDAwMGIwLTY4NmItNDg2Ny1iNTk5LWRiYjNiNGJlYzNlMyIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJuYW1lIjoiaG9wLXVzZXIgaG9wLXVzZXIiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJob3AtdXNlciIsImdpdmVuX25hbWUiOiJob3AtdXNlciIsImZhbWlseV9uYW1lIjoiaG9wLXVzZXIiLCJlbWFpbCI6ImhvcC11c2VyQGludmFsaWQubWFpbCJ9.V0BrThYtjhvXKm9WlNLuDVSLrucBqRk4QllOC8U8IZj45jDGST7oFkqpnGIP6xSRbebe4Ow--56huDiXdPcymG9_A9Om_EiUvTbHN-Lm9fhx3JHSjt1w7vQ82SJXM2GuaLoF3FNda8MDc23HcFvfUvCPT_k7oIIflLy5udv5SFP7nWCWLFM8pknucHGEpeLLvzAD3mgL0Evdyw6X9DH6goAy0lRW_XtLYoNQj8ArpS4ZOCP8hglp2D66RYgxVl8uf2taps_70LtnL8-IkAUGw_Rc9QDINOHwPK3AnsCPgRp1RuEJPXQLP6-mWfJ-41YaPgB-1V6uvv90pyA8Ef4csQ

.. _awscli: https://aws.amazon.com/cli/
.. _AWS Session Manager plugin: https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-install-plugin.html
