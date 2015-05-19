Workflow Plugin module for jenkins-job-builder
===============================================

Python module that extends `jenkins-job-builder
<http://ci.openstack.org/jenkins-job-builder/>`_ to support new project type,
``workflow``.

.. image:: https://travis-ci.org/finnhaedicke/jenkins-job-builder-workflow.svg?branch=master
    :target: https://travis-ci.org/finnhaedicke/jenkins-job-builder-workflow
.. image:: https://readthedocs.org/projects/jenkins-job-builder-workflow/badge/?version=latest
    :target: https://readthedocs.org/projects/jenkins-job-builder-workflow/?badge=latest
    :alt: Documentation Status

Based on https://github.com/thomasvandoren/jenkins-job-builder-naginator

Documentation
-------------

Please see http://jenkins-job-builder-workflow.readthedocs.org/

Installation
------------

.. code-block:: bash

    pip install jenkins-job-builder-workflow

Development
-----------

To work on this project, install the dependencies, install the develop branch,
make change, and run tests with tox:

.. code-block:: bash

    pip install -r requirements.txt -r test-requirements.txt
    python setup.py develop
    # ... make changes ...
    tox

.. note:: It is best to use a virtualenv for developing this package.
