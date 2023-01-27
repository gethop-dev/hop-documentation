How to create and install an on-premises HOP Application
===========================================================

This guide describes how to carry on the creation and first
installation of an On-premises HOP Application. There are two parts,
firstly, it will describe how to generate a new project with
On-premises deployment characteristics. Secondly, how to
deploy/install the final artifact on your on-premises
infrastructure.

While reading this guide, you will see the terms "deployment machine"
or "installation machine". They refer to where the final artificat
will be deployed and run. Although you can do the installation on your
development machine, this guide commands assumes a completely new
GNU/Linux machine.

Requirements
------------

Apart of having HOP CLI installed, as explained on the
:doc:`/get-started/installation/main` tutorial, you will need the
following tools to complete this guide steps on your development
machine.

- `Docker`_ and `Docker Compose`_ for running and building your project.
- `yq`_ YAML, JSON and XML processor to help merging Docker Compose files.
- tar to bundle the final artifact that you will deploy.
- sha256sum to generate the hash of final artifact bundle.

.. _Docker: https://www.docker.com/
.. _Docker Compose: https://docs.docker.com/compose/
.. _yq: https://github.com/mikefarah/yq

Generate a new project using On-premises deployment target
----------------------------------------------------------

First, you need to create a new project using the On-premises as
profile and deployment target. To do that, you need to create a
settings file that the HOP Command Line Interface tool (from now on
HOP CLI) can use. In order to create the settings file, open the HOP
CLI Settings Editor by running the following command on your terminal
console:

.. code-block:: console

   $ hop bootstrap open-settings-editor

After running the command, it will output the URL to access the Settings Editor.

.. code-block:: text

   Settings Editor running at http://localhost:8090

As a reference, this guide assumes the following profile selections
and configuration:

- Core.

  - With the setting ``project -> docker -> registry`` set to ``Custom Registry Provider``
- Frontend.
- CI/CD.

  - With the setting ``project -> profiles -> ci -> provider`` set to ``Custom``.
  - With the setting ``project -> profiles -> ci -> continuous-deployment -> provider`` set to ``On-premises``.
- On-premises.

  - With the settings ``project -> profiles -> on-premises -> persistent-data-dir`` set to ``/usr/local/hop/<your-project-name>/persistent-data-dir``.

    - You can set the folder of your choice but to make this guide
      simpler we recommend that you use the same setting. Just do not
      forget to put your project name (the same you configured in
      ``project -> name``) after ``/usr/local/hop/``.
  - With the settings ``project -> profiles -> on-premises -> ssl-termination`` set to ``NGINX configuration file``
- Persistence - SQL.

.. note::

   The notation used above is simply the path to a setting on the
   Settings Editor. If use the sidebar you can easily track the
   sections described above.

.. note::

   You can optionally select more profiles such as Business
   Intelligence - Grafana and Authentication - Keycloak (which are
   suitable for On-premises deployment), but you have to do extra
   steps to finish their production setup such as creating a Keycloak
   realm.

Once you have configured the settings to fit your needs export it and run
the following command to create the new project:

.. code-block:: console

   $ hop bootstrap new-project \
   --settings-file-path <the-path-to-the-exported-settings-file> \
   --target-project-dir <the-directory-path-of-your-new-project>

.. warning::

   Make sure the project folder you pass to ``--target-project-dir``
   does not exist or the HOP CLI will error out.

Once you execute the command, HOP CLI will create the project files in
the directory you specified. It will also print out some steps that
you need to do during the on-premises installation. Save that output
somewhere from where you can refer to them later on this guide.

Among all the files HOP CLI generated take special notice at the file
``.env.test``. Save this file somewhere safe as it is the environment
variables required to run the application on your deployment machine.

With that out of the way, you can go to the project's directory and
run the following script to start the development environment:

.. code-block:: console

   $ ./start-dev.sh

That script will run your development, basically running
``docker-compose up`` using the development YAML files. If you want to
test the web application, you can connect to a nREPL running on
``localhost:4001`` and do:

.. code-block:: clojure

   user> (dev)

And then:

.. code-block:: clojure

   dev> (go)

That will endup running a web server on the port ``3000`` on
``localhost`` but since the setup uses a reverse proxy, you actually
have to go to ``localhost:8081`` to view the web application.

You can turn down the environment at any moment by running the
``stop-dev.sh`` script.

.. note::

   If you want to execute any other ``docker-compose`` commands (such
   as showing the logs) please use the ``dc.sh`` script to do so. That
   script will tell ``docker-compose`` which YAML files to use in
   order to run the commands. So, if you want to show the logs for
   example, you can run ``./dc.sh logs -tf``.

As you may have noticed, Unlike the ``Amazon Web Services`` deployment
target, the ``On-premises`` one does not provision the infrastructure
for you when generating the project. It provides you with the
necessary files and script for deploying and installing the final
artifact.

Creating the application bundle
-------------------------------

Regardless of your Continuous Integration provider of choice (Github
Actions, Bitbucket Pipelines or Custom) there is an important detail
about the Continuous Delivery side of it. Because HOP does not assume
your deployment methodology and infrastructure, it only provides you
with a script to create the application bundle
(``ci/on-premises/create-app-bundle.sh``). And optionally you have a
``deploy.sh`` script which is just a placeholder for you to implement
your own deployment strategy.

The ``create-app-bundle.sh`` script bundles all the necessary
files for deployment and installation into a ``TAR`` file. It also
provides you the ``sha256sum`` of the ``TAR`` file in case you need it.

The bundle is not the only thing you have to care of. You will also
have to make sure to build and store your application on a Docker
Registry that is accesible later on when deploying the final
artifact. HOP assumes the deployment machine will have internet
connectivity which is required to download the required Docker images.

The scripts ``ci/build-app-prod-docker-image.sh`` and
``ci/publish-app-prod-docker-image.sh`` is what you need to build and
publish the application's Docker image. Those scripts use
configuration variables from ``ci/common-vars.sh`` where you can find
``DOCKER_IMAGE_REPOSITORY`` value. The value of this variable is what
you configured on the Settings Editor ``project -> docker -> registry
-> custom -> app-repository-url``.

So in order to proceed to the next step which is doing the
installation and first deployment you will need to bundle the
application. To do so, first you need to create your local ``git``
repository and do your initial commit:

.. code-block:: console

   $ git init --initial-branch=<the-branch-you-chose-in-the-settings-editor>
   $ git add .
   $ git commit -m "Initial commit"

.. note::

   When running the first command ``git init`` the
   ``--initial-branch`` value should be what you chose while editing
   the settings on the Settings Editor. If you did not change the
   default value, then it should be ``main``. If you are unsure about
   your decision, you can either take a look at ``ci/common-vars.sh``
   and look for ``DEPLOYMENT_BRANCH``, or import your settings file on
   the Settings Editor and check the value there.

Once you have done that, run the ``create-app-bundle.sh`` script from
the project root directory:

.. code-block:: console

   $ ./ci/on-premises/create-app-bundle.sh

The script will create two files in your project's root directory, the
``TAR`` file and a file containing the ``sha256sum`` of the
bundle. Now you will proceed to do the installation on your deployment
machine.

Installing On-premises
----------------------

This guide is going to use a Debian 11 virtual machine to carry on
with the installation. So beware that some commands, such as package
manager commands, will have to be adjusted to work on your
distribution of choice.

Before starting this section make sure you have the following tools
installed on your deployment machine.

- `Docker`_ and `Docker Compose`_.
- systemd

.. _Docker: https://www.docker.com/
.. _Docker Compose: https://docs.docker.com/compose/

.. warning::
   Having a GNU/Linux distribution running with ``systemd`` is strictly
   mandatory to complete the installation.

Setting up tools, users and groups
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. warning::

   All the steps starting from here, assumes a GNU/Linux based
   machine.

First you have to install the necessary tools for this part of the
guide. All the following commands should be executed as the ``root``
user of your system and you should only change users when requested by
the guide. So make sure you are logged in as ``root`` before starting:

.. code-block:: console

   $ su -

If you are going to do the installation on a Debian 11 machine, as
in this guide, you can run the following commands to install the
packages:

.. code-block:: console

   # apt-get install -y docker

HOP minimum version requirement for ``docker-compose`` is
``1.27.x``. As of the time of writing, Debian 11 default repository
has an older version of ``docker-compose``, ``1.25.0``. Therefore, to
install a newer version you have to use Debian backports. To do so,
use the following commands:

.. code-block:: console

   # echo "deb http://deb.debian.org/debian bullseye-backports main" >> /etc/apt/sources.list
   # apt-get update
   # apt-get install -y docker-compose/bullseye-backports

That should install a newer ``docker-compose`` version, higher than or
equal to ``1.27.4``.

The next step to create the docker group. Use the following command to
do so:

.. code-block:: console

   # sudo groupadd docker

After that, enable the ``docker`` service so it starts automatically
if the machine restarts. Then restart the service.

.. code-block:: console

   # systemctl enable docker
   # systemctl restart docker

You should also check for the ``docker`` service status and make sure
it is active and running.

.. code-block:: console

   # systemctl status docker

Now you will need to create the user that will run and own the
application files. The user and group name must be the same value as
the name of your project. That is, the same value you configured in
the Settings Editor.

.. code-block:: console

   # useradd -d /usr/local/hop/<your-project-name>/ -m -U -G docker -s /bin/bash <your-project-name>

Installing application
~~~~~~~~~~~~~~~~~~~~~~

Now that you have installed the required packages and set up the user
and group, the next step is to prepare the application files
directories for installation.

First you have to create the application files folder where all the
files to run the system will reside:

.. code-block:: console

   # mkdir -p /usr/local/hop/<your-project-name>/app-files

Apart from the ``app-files`` folder we need to create another very
important folder which is the ``persistent-data-dir`` folder. This
folder is where any of your application's system persistent data will
be stored. For example, you will need it to store the database
files. Make sure it is the same path you specified in the Settings
Editor when configuring the ``On-premises`` settings.

.. code-block:: console

   # mkdir -p <your-persistence-data-dir>

Since this setup is using a PostgreSQL database we need to create its
folder inside the ``persistent-data-dir`` as well:

.. code-block:: console

   # mkdir -p <your-persistence-data-dir>/postgres-data-dir

.. warning::

   If you choose ``HTTPS Portal container`` as the SSL termination
   option, you will also have to create the
   ``<your-persistent-data-dir>/https-portal-data-dir``. And please
   refer to the :ref:`installation-on-premises_https-portal` section
   at the end of this guide.

Once you have done that, change directory to the application files
``app-files`` folder.

.. code-block:: console

   # cd /usr/local/hop/<your-project-name>/app-files

Now you need to bring the application bundle you created previously
using the ``create-app-bundle.sh`` script to your installation
machine. Move the ``.tar`` file to
``/usr/local/hop/<your-project-name>/app-files``. And extract it with
the command:

.. code-block:: console

   # tar xf <your-tar-file-name>

After extracting the file you will need to copy to the same directory
the ``.env.test`` file mentioned at the beginning of this guide. Move
it to the ``/usr/local/hop/<your-project-name>/app-files`` and at the
same time rename the file name to just ``.env``:

.. code-block:: console

   # mv <path-to-your-dot-env-file>/.env.test .env

Next, copy both ``start-app.sh`` and ``stop-app.sh`` from the
``on-premises-files`` folder to the root ``app-files`` folder:

.. code-block:: console

   # cp on-premises-files/usr/local/hop/<your-project-name>/bin/{start-app.sh,stop-app.sh} .

Now change the permissions of the files in the directory to be owned
by the application's user and group. You created them in a previous
step. If you followed the guide, both user and group should have the
same name. That is, the name of your project.

.. code-block:: console

   # chown -R <your-project-name>:<your-project-name> * .??*

Next step is to setup the ``systemd`` files. Assuming you are in the
same folder as in the previous command, copy the file in
``on-premises-files/etc/systemd/system/<your-project-name>-app.service`` to ``/etc/systemd/system/``:

.. code-block:: console

   # cp on-premises-files/etc/systemd/system/<your-project-name>-app.service /etc/systemd/system/

The next steps requires you to login as the application user. So login
as the application user first and then proceed with the next steps:

.. code-block:: console

   # su - <your-project-name>

If you type ``pwd`` on your console you should be in
``/usr/local/hop/<your-project-name>``, your home folder. With that in
mind, copy the files ``.bashrc`` and ``.profile`` from
``~/app-files/on-premises-files/usr/local/hop/<your-project-name>/{.bashrc,.profile}``
to your home folder:

.. code-block:: console

   $ cp ~/app-files/on-premises-files/usr/local/hop/<your-project-name>/{.bashrc,.profile} ~/

Now create the a ``bin`` folder in your home directory and copy the
script that will run the application with healthchecks:

.. code-block:: console

   $ mkdir -p ~/bin
   $ cp ~/app-files/on-premises-files/usr/local/hop/<your-project-name>/bin/app-with-healthchecks.sh ~/bin
   $ chmod 755 ~/bin/app-with-healthchecks.sh

At this point you can already run the application. As it is the first
time, you have to run the application and do the steps listed in the
output of the HOP CLI when you generated the project. In the case of
this guide, our single post-installation step is to create the
database schema and users. To do so, you need to run the application
environment and connect to the database to execute the SQL statements
that appear in the post-installation steps.

But before you do it, logout and login back so the changes you made to
the files ``.bashrc`` and ``.profile`` take effect. More importantly,
it will set an environment variable required to run the
``app-with-healthchecks.sh`` script.

.. code-block:: console

   $ logout
   # su - <your-project-name>

Now run the following to start the application:

.. code-block:: console

   $ ~/bin/app-with-healthchecks.sh start

This might take a bit depending on your internet connection as it has
to download the required Docker images to run the environment. Once it
finishs downloading the images, it will print out the logs. Do not
worry if you see any errors in the ``app`` logs, that is because the
database is not configured yet. To do so, go to ``~/app-files`` and
use ``docker-compose`` to access the ``psql`` shell:

.. code-block:: console

   $ cd ~/app-files
   $ docker-compose exec psql --user <admin-user> <the-database-name-you-chose>

This will open the ``psql`` shell. Now execute the SQL statements that
appear in the HOP CLI post-installation steps and then exit.

Now stop the application service:

.. code-block:: console

   $ ~/bin/app-with-healthchecks.sh stop

The remaining tasks will require you be a root user again, so logout:

.. code-block:: console

   $ logout

Finally you have to enable and run your application service:

.. code-block:: console

   # systemctl enable <your-project-name>-app.service
   # systemctl start <your-project-name>-app.service

If everything works as expected you should see that the application
service is up and running using the following command:

.. code-block:: console

   # systemctl status <your-project-name>-app.service

SSL Termination
~~~~~~~~~~~~~~~

Now, the system is running but it is still available only on localhost
and with no SSL termination. HOP offers two ways of achieving this:

- Configuration for NGINX reverse proxy (the option selected by this guide).
- `HTTPS Portal`_ which automatically issues certificates with `Let's Encrypt`_.

.. _HTTPS Portal: https://github.com/SteveLTN/https-portal
.. _Let's Encrypt: https://letsencrypt.org/

NGINX
+++++

This guide is using NGINX reverse proxy configuration option which
only provides a ``.conf`` file with the necessary configuration to do
SSL termination using NGINX. The file can be found in
``/usr/local/hop/<your-project-name>/app-files/on-premises-files/etc/nginx/nginx.conf``. However
how you install NGINX and generate the certificates is up to you.

From this file point of view, you would only need to change the lines
68 and 69 to point to your certificate PEM and key file. The rest of
the configuration is ready to send the plain HTTP traffic to the
application's reverse proxy sitting on ``127.0.0.1:8081``.

.. _installation-on-premises_https-portal:

HTTPS Portal
++++++++++++

If you choose HTTPS Portal, this is the easiest way to setup SSL
termination for your application. It uses Let's Encrypt to get the SSL
certificates for your domain and checks if they are expired every week
and renew them 30 days before they expire.

HOP CLI will add to the generated project a ``docker-compose`` file
named ``docker-compose.https-portal.to-deploy.yml`` which is only used
for test and production environments (i.e., it will not run on
development). There is one important setting in that YAML file that
you need to change when going live which is the ``STAGE`` environment
variable.

By default HOP sets it to ``staging``, which is also the default value
on HTTPS Portal. This means, HTTPS Portal will get test (untrusted)
certificates from Let's Encrypt. When you are ready to go live, please
change that value in the ``.env`` file located in the ``app-files``
folder. Look for the ``HTTPS_PORTAL_STAGE`` environment variable and
change its value to ``production``. For this change to take effect,
you will have to stop and start the application service:

.. code-block:: console

   # systemctl stop <your-project-name>-app.service
   # systemctl start <your-project-name>-app.service

Now the application should be back up and running with new trusted
Let's Encrypt certificates.

.. warning::

   It is extremely important that you know about `Let's Encrypt rate
   limits`_ and `how HTTPS Portal works`_ in order to avoid hitting
   any road blocks when testing or setting up the production
   configuration.

.. _Let's Encrypt rate limits: https://letsencrypt.org/docs/rate-limits/
.. _how HTTPS Portal works: https://github.com/SteveLTN/https-portal#how-it-works
