Workflow Plugin module for jenkins-job-builder
===============================================

Python module that extends `jenkins-job-builder
<http://ci.openstack.org/jenkins-job-builder/>`_ to support ``workflow`` jobs

.. raw:: html

    <a href="https://travis-ci.org/finnhaedicke/jenkins-job-builder-workflow" target="_blank"><img src="https://travis-ci.org/finnhaedicke/jenkins-job-builder-workflow.svg"></a>

Based on https://github.com/thomasvandoren/jenkins-job-builder-naginator

Workflow Publisher
-------------------

.. automodule:: workflow_job.project_workflow
    :members:

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
