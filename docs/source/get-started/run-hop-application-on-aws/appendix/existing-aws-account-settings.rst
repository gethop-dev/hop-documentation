Settings file configuration for existing AWS account
====================================================

If you already have an AWS account and you are using some of its
services, there are some considerations to follow in order to avoid
conflicts or misbehavior when generating a new project using the HOP
CLI. When configuring the settings file, double-check the following
configuration options:

* ``cloud-provider`` → ``aws`` → ``account``

  * ``stack-name.value``: Name for the Cloudformation stack
    that will prepare your AWS account for running HOP Applications. The
    account stack name must be unique in your AWS account. Note that
    you should use the same account stack name for all of your HOP
    Applications. If the stack with that name exists, it will be used and
    no new stacks will be created or updated.
  * ``vpc`` → ``cidr.value``: IP block that will be used in
    your AWS VPC. Make sure to use a AWS VPC CIDR that does not conflict with an
    existing one in your account.

* ``cloud-provider`` → ``aws`` → ``project``

  * ``stack-name.value``: Name for the AWS Cloudformation stack
    that will be used to generate application-wide resources. The project
    stack name must be unique in your AWS account.
  * ``vpc``

    * ``subnet-1`` → ``cidr.value``: IP block that will be used
      in your ``subnet-1``. Make sure the AWS subnet IP CIDR align with
      the AWS VPC CIDR block and that it does not conflict with other
      AWS subnets CIDRs.
    * ``subnet-2`` → ``cidr.value``: IP block that will be used
      in your ``subnet-2``. Make sure the AWS subnet IP CIDR align with
      the AWS VPC CIDR block and that it does not conflict with other
      AWS subnets CIDRs.

* ``cloud-provider`` → ``aws`` → ``environment``

  * ``dev``

    * ``stack-name.value``: Name for the AWS Cloudformation stack
      that will generate application's environment-specific resources. The
      environment stack name must be unique in your AWS account.
  * ``test``

    * ``stack-name.value``: Name for the AWS Cloudformation stack
      that will generate application's environment-specific resources. The
      environment stack name must be unique in your AWS account.
    * ``kms`` → ``key-alias.value``: Name for the AWS KMS
      key-alias used to encrypt and decrypt test environment variables
      stored in AWS SSM Parameter Store. The key-alias name must be unique
      in your AWS account.
  * ``prod``

    * ``stack-name.value``: Name for the AWS Cloudformation stack
      that will generate environment-specific application's resources. The
      environment stack name must be unique in your AWS account.
    * ``kms`` → ``key-alias.value``: Name for the AWS KMS
      key-alias used to encrypt and decrypt production environment
      variables stored in AWS SSM Parameter Store. The key-alias name must
      be unique in your AWS account.

.. note::

   For additional context and information about AWS infrastructure
   created by the HOP CLI, please refer to the
   :doc:`/reference/aws-infrastructure/main`.
