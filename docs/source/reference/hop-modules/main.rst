HOP Module reference
====================

HOP offers various modules or libraries that extend the functionality
of the platform.

Authentication and authorization
--------------------------------

* `buddy-auth.jwt-oidc`_ - Library implementing a
  ``:duct.middleware.buddy/authentication`` compatible JWT token
  validation function for OpenID Connect ID Tokens.
* `rbac`_ - Library that provides role-based access control.
* `session.re-frame.cognito`_ - A library that provides re-frame
  events for managing AWS Cognito user sessions.
* `user-manager.cognito`_ - A Library for interacting with the AWS
  Cognito User Pools API.

Object storage
--------------

* `object-storage.core`_ - Library that provides an object-storage
  protocol that can be implemented by other libraries.
* `object-storage.s3`_ - Object storage implementation for Amazon S3.
* `object-storage.ftp`_ - Object storage implementation for FTP.

Business Intelligence
---------------------

* `dashboard-manager.grafana`_ - Library for managing dashboards and
  associated users and organizations in Grafana.

Observability
-------------

* `timbre.appenders.cloudwatch`_ - Cloudwatch Timbre log appender with
  batching and rate limiting.

CLJS Compilation
----------------

* `duct.module.cljs-compiler`_ - Duct module for configuring the cljs
  compiler.
* `duct.server.figwheel-main`_ - Library for compiling and dynamically
  reloading ClojureScript files in the Duct framework using Figwheel
  Main.

Messaging protocols
-------------------

* `pubsub`_ - MQTT and AMQP Publish Subscribe library.
* `notifications.firebase`_ - Library for sending notifications
  through Google Firebase.

Persistence
-----------

* `sql-utils`_ - Thin convenience wrapper over clojure.java.jdbc.

Encryption
----------

* `encryption`_ - A library for encrypting and decrypting arbitrary
  Clojure values, using caesium symmetric encryption primitives.
* `secret-storage.aws-ssm-ps`_ - Library for managing secrets stored
  in AWS System Manager Parameter Store.

Payments
--------

* `payments.stripe`_ - Library for interacting with the Stripe API.

Electronic signatures
---------------------

* `esignatures.docusign`_ - Library for interacting with the Docusign
  eSignature API.

.. note::

   The listed modules have been developed with HOP in mind, and they
   have been designed to be effortlessly integrated in the
   HOP Platform. Nevertheless, they can be also used in non-HOP applications.


.. _timbre.appenders.cloudwatch: https://github.com/gethop-dev/timbre.appenders.cloudwatch
.. _user-manager.cognito: https://github.com/gethop-dev/user-manager.cognito
.. _duct.module.cljs-compiler: https://github.com/gethop-dev/duct.module.cljs-compiler
.. _duct.server.figwheel-main: https://github.com/gethop-dev/duct.server.figwheel-main
.. _rbac: https://github.com/gethop-dev/rbac
.. _notifications.firebase: https://github.com/gethop-dev/notifications.firebase
.. _session.re-frame.cognito: https://github.com/gethop-dev/session.re-frame.cognito
.. _dashboard-manager.grafana: https://github.com/gethop-dev/dashboard-manager.grafana
.. _sql-utils: https://github.com/gethop-dev/sql-utils
.. _payments.stripe: https://github.com/gethop-dev/payments.stripe
.. _pubsub: https://github.com/gethop-dev/pubsub
.. _buddy-auth.jwt-oidc: https://github.com/gethop-dev/buddy-auth.jwt-oidc
.. _esignatures.docusign: https://github.com/gethop-dev/esignatures.docusign
.. _object-storage.core: https://github.com/gethop-dev/object-storage.core
.. _object-storage.s3: https://github.com/gethop-dev/object-storage.s3
.. _object-storage.ftp: https://github.com/gethop-dev/object-storage.ftp
.. _encryption: https://github.com/gethop-dev/encryption
.. _secret-storage.aws-ssm-ps: https://github.com/gethop-dev/secret-storage.aws-ssm-ps
