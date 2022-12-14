AWS run project
===============

Introduction
------------

In this tutorial you will bootstrap a basic HOP platform with the following features:
* `Duct Framework`_ based backend.
* `Reactive`_ ClojureScript frontend.
* Infrastructure provisioning in the Amazon Web Services cloud provider.
* CI/CD integration with `Github Actions`_.

.. -Reactive: https://github.com/reagent-project/reagent
.. -Duct Framework: https://github.com/duct-framework/duct
.. -Amazon Web Services: https://aws.amazon.com/
.. -Github Actions: https://docs.github.com/en/actions

.. note::

   The HOP platform provides more bootstraping features, but this
   tutorial will focus in a bare minimum installation.


Prerequisites
-------------

Having the HOP Command Line Tool installed as explained in the
:doc:`/get-started/installation/main` tutorial is enough for
bootstraping a new HOP project. But for running the generated project
locally you will need some additional tools:

* `Docker <https://docs.docker.com/engine/install/>`_
* `Docker Compose <https://docs.docker.com/compose/install/>`_
* `AWS Vault <https://github.com/99designs/aws-vault>`_

Apart from the software requirementes, you will also need an Amazon Web
Services account with admin credentials in order to create the needed
infrastructure.

Install Docker
++++++++++++++

Once you have installed Docker, you can check that it's installed
correctly by running:

.. code-block:: console

   $: docker run --rm hello-world

Install Docker Compose
++++++++++++++++++++++

Once you have installed Docker Compose, you can check that it's installed
correctly by running:

.. code-block:: console

   $: docker-compose --version
   docker-compose version 1.27.4, build unknown

For running HOP docker-compose version 1.27.0+ is required.

Install AWS Vault
+++++++++++++++++

Once you have installed Aws Vault, you can check that it's installed
correctly by running:

.. code-block:: console

   $: aws-vault --version
   v6.0.0

No specific version is required, but latest is recommended.

Prepare AWS credentials
-------------

The HOP bootstrap tool will automatically provision the needed
infrastructure to run the HOP platform using `AWS Cloudformation`_. In
order to run that you will need a pre-created Amazon Web Services
account and administrator credentials.

Although it's not mandatory, we strongly recommend to store the
administrator credentials using Aws Vault. The tool provides secure
storage for AWS credentials for the local development environment. The
tool is also used in later steps of running the project locally,

The tool will require to provide a AWS Access Key and its corresponding Secret Key. If you don't have any you can `create them`_ from the AWS Console.

.. -create them: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html?icmpid=docs_iam_console

Once you have the credentials you can store them using the following command:

.. code-block:: console

   $: aws-vault add hop/admin

The tool will ask you for the Key id and Secret and the setup will be done.

Obtain the default settings file
---------------------

The HOP Bootstraping tool allows the user to configure certain
characteristics of the project to be generated and provisioned in
AWS. That configuration is specified using the ``settings.edn``
file. At the moment the file has to be edited manually, but a user
interface will be provided in next versions of the tool.

The settings file is not intended to be written from scratch, but the
user has to edit the default file provided by the tool. To obtain that
file you can run the following command:

.. code-block:: console

   $: bb hop-cli.jar bootstrap bb cli bootstrap copy-settings -dst settings.edn

The command will create a `edn` file in the current directory.

.. note::

   The ``settings.edn`` file might look a bit intimidating, but it's
   due to the fact that it's intented for being consumed by a user
   interface that will come in a future early version of HOP. The file
   provides multiple preconfigured choices that the user is able to
   chose that make the file bigger.

Edit the settings file
----------------------

The settings file allows configuring multiple features and
characteristics of the platform. For this tutorial we will only edit a
few of them.

The file has a tree like structure in which each node has the following fields:
* ``name``: The name of the node.
* ``tag``: Optional string explaining the node's purpose.
* ``type``: The type that the ``value`` field is of. The node can be a
  leaf (string, number, password...) or a branch (plain-group,
  single-choice-group and multiple-choice-group).
* ``value``: The configured value of the node.
* ``choices``: If the node is of type ``single-choice-group`` or
  ``multiple-choice-group`` this will contain a list of branches that
  the user can select. The selection is done using the ``value`` field
  by specifying the name(s) of the selected branch(es).

Having that structure in mind open the file with your favourite text
editor and edit the following options

* ``project`` -> ``name`` -> ``value``: We will set the project name to ``"hop-tutorial"``.
* ``project`` -> ``profiles`` -> ``value``: HOP offers multiple
  profiles that enhance the bootstraped project, but for this tutorial
  we will select some basic ones. We will set the value to
  ``[:core :frontend :aws :ci]``
* TODO more?

Run the bootstrap command
-------------------------

Once we are happy with the selected configuration we can bootstrap the
project by running the following command:

.. code-block:: console

   $: aws-vault exec -n hop/admin -- bb hop-cli.jar bootstrap new-project --settings-file-path settings.edn --target-project-dir hop-tutorial

Bootstraping the project will take several minutes (mostly because of the AWS provisioning). The tool will keep us informed about each step that it performs:

* AWS infrastructure provisioning.

  * Account resources. The tool will create AWS resources that can be
    shared between multiple HOP projects.
  * Project resources. The tool will create AWS resources that can be
    shared between the different environments inside the hop-tutorial
    project.
  * Dev environment resources: The tool will create the AWS resources
    needed for local development.
  * Test environment resources: The tool will create the AWS
    resources for running the test environment.

* Project file creation. The tool will create the local project files
  in the hop-tutorial folder.

* Post-installation steps. If required the tool will print additional
  manual steps that have to be performed after the bootstrap has been
  completed.

Configure the local project credentials
-----------------------

Certain operations of the bootstrap process can't be easily and
securely automated, so the tool will print the user the missing steps
to be performed manually. Among them there is the step of configuring
Aws Vault with the credentials created for working in the dev
environment. The tool will print the exact commands we need to run.

First you will have to add the credentials for the AWS user used for
local development. Te user will be shared among all the HOP projects
you run on your system.

.. code-block:: console

   $: aws-vault add hop/hop-local-dev

Then you will have to configure the role used for running the
hop-tutorial project. That role contains the specific permissions for
interacting with the resources in the dev environment for the
hop-tutorial project. You will have to edit the ``~/.aws/config```file and add the rows printed by the tool:

| [profile hop/hop-tutorial-dev-env]
| source_profile=hop/hop-local-dev
| role_arn=arn:aws:iam::XXXXXXXXXX:role/hop-tutorial-eb

The tool will also print the AWS Access Key and Access Secret for the
CI/CD user. Take note of them, as you will need it in a next step to
configure Github Actions.

Start the project in the dev environment
----------------------------------------

Create and configure the external Github repository
---------------------------------------------------

Deploy application to test environment
--------------------------------------

Final notes
-----------
