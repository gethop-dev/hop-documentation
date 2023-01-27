Configure the project settings using a text editor
==================================================

The settings file is intended to be edited using the HOP CLI Settings
Editor, but you can also edit it with the text editor of your choice.

Obtain the default settings file
--------------------------------

The settings file is not intended to be written from scratch, as it is
quite big and needs to have a certain structure
[#SettingsFileStructure]_. The HOP CLI can generate a default settings
file that the user can then edit. To obtain that default settings
file, you can run the following command.

.. code-block:: console

   $ hop bootstrap create-settings-file --settings-file-path hop-tutorial-settings.edn
   {:success? true}

The command will create a file called ``hop-tutorial-settings.edn`` in
the current directory.

Edit the settings file
----------------------

The file has a tree-like structure in which each node has the
following properties:

* ``name``: The name of the node.
* ``tag``: Optional string explaining the node's purpose (using
  `Hiccup`_ syntax).
* ``type``: The type that the ``value`` field is of. The node can be a
  leaf (string, number, password, ...) or a branch (plain-group,
  single-choice-group and multiple-choice-group).
* ``value``: The configured value for the node.
* ``choices``: If the node is of type ``single-choice-group`` or
  ``multiple-choice-group``, this field will contain an array (vector)
  of branches that the user can select from. The selection is done
  using the ``value`` field, by specifying the name(s) of the selected
  branch(es).

.. _Hiccup: https://github.com/weavejester/hiccup

Here is a small `EDN`_ snippet depicting the settings file structure:

.. code-block:: clojure

   [{:name :root-node
     :tag "Root node"
     :type :plain-group
     :value [{:name :node-1
              :tag "Node 1"
              :type :single-choice
              :value :opt-1
              :choices [{:name :opt-1
                         :tag "Opt 1"
                         :type :string
                         :value "opt 1 value"}
                         {:name :opt-2
                         :tag "Opt 2"
                         :type :string
                         :value "opt 2 value"}]}
              {:name :node-2
               :tag "Node 2"
               :type :multiple-choice
               :value [:opt-3 :opt-4]
               :choices [{:name :opt-3
                         :tag "Opt 3"
                         :type :integer
                         :value 3}
                         {:name :opt-4
                         :tag "Opt 4"
                         :type :integer
                         :value 4}]}]}]

In order to navigate the data structure above we will use the
following notation:

* `node-1` → ... → `node-n.property`

For example, if we want to reference the ``:value`` property of the
``:opt-3`` node, inside the ``:node-2`` node, we would use the
following notation:

* ``root-node`` → ``node-2`` → ``opt-3.value``

.. note::

   While the settings file uses keywords for the node and property
   names (e.g., ``:root-node``, or ``:type``), the notation to refer
   to a particular node or property in this tutorial will use the
   string representation of those keywords (e.g., ``root-node``, or
   ``value``). This is just for reading convenience.

Having that structure and notation in mind, open the settings file you
just created with your favorite text editor, and edit the following
settings' values:

* ``project`` → ``name.value``: We will set the project name to
  ``"hop-tutorial"``.
* ``project`` → ``profiles.value``: HOP offers multiple profiles that
  enhance the bootstrapped project. But for this tutorial we will
  select some basic ones. We will set the value to ``[:core :frontend
  :aws :ci]``
* ``deployment-target`` → ``aws`` → ``account`` → ``region.value``: The
  AWS region where you want to create the project resources. Change to
  your desired region. So far the HOP CLI has been mainly tested on
  the ``eu-west-1`` region. So we recommend you to use that region in
  order to ensure that all the services required by HOP application
  will be available [#UsingOtherAWSRegion]_.

.. note::

   Make sure that the AWS region you configure is enabled in your AWS
   account. Not all the regions are enabled by default.

   Also, make sure that the AWS region you configure has the AWS
   Elastic Beanstalk service available. At the time of this writing,
   some of them (e.g., ``eu-south-2``) do not have it available. You
   can check the list of available regions at `AWS Elastic Beanstalk
   endpoints and quotas`_.

.. _`AWS Elastic Beanstalk endpoints and quotas`:
   https://docs.aws.amazon.com/general/latest/gr/elasticbeanstalk.html

.. warning::

   If you already have an AWS account with existing resources, please
   refer to
   :doc:`/get-started/run-hop-application-on-aws/appendix/existing-aws-account-settings`
   document for further considerations.

.. note::

   If this is the second time you are following this tutorial, some of
   the AWS resources created the first time you run the tutorial will
   still exist. The HOP CLI does not delete any AWS resources, to
   avoid deleting resources that may be in use. The HOP CLI does not
   overwrite any existing resource either, for the same reason.

   This means you will need to delete those AWS resources manually
   yourself. Refer to :doc:`/how-to/delete-aws-resources/main` for
   additional details.

Continue with the tutorial
--------------------------

Once you have finished editing the settings file you can continue with
the tutorial in the
:ref:`run-hop-application-on-aws_run-bootstrap-command` section. All
the further steps are the same regardless you used the graphical
Settings Editor or you edited the file manually.


.. rubric:: Footnotes

.. [#SettingsFileStructure] The file uses the `EDN`_ format, and it
   needs to conform to a HOP-specific `Malli Schema`_. Its structure
   is loosely based on GNU Emacs customization settings.

.. [#UsingOtherAWSRegion] If you use any other AWS region and find any
   problem, please open an issue in the `HOP CLI issue tracker`_
