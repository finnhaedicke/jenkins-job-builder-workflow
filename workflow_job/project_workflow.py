# -*- coding: utf-8 -*-
# Copyright (C) 2013 eNovance SAS <licensing@enovance.com>
# 2015 Finn Haedicke
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


"""
The workflow Project module handles creating Jenkins workflow projects.
You may specify ``workflow`` in the ``project-type`` attribute of
the Job definition.

Requires the Jenkins `Workflow Plugin
<https://wiki.jenkins-ci.org/display/JENKINS/Workflow+Plugin>`.

In order to use it for job-template you have to escape the curly braces by
doubling them in the DSL: { -> {{ , otherwise it will be interpreted by the
python str.format() command.

:Job Parameters:
    * **dsl** (`str`): The DSL content. (optional)

Job example:

    .. literalinclude::
      /../test/fixtures/project_workflow_001.yaml

Job template example:

    .. literalinclude::
      /../test/fixtures/project_workflow_002.yaml


"""

import xml.etree.ElementTree as XML
import jenkins_jobs.modules.base


class Workflow(jenkins_jobs.modules.base.Base):
    sequence = 0

    def root_xml(self, data):
        xml_parent = XML.Element('flow-definition')
        xml_parent.attrib['plugin'] = 'workflow-job'

        definition = XML.SubElement(xml_parent, 'definition')
        definition.attrib['class'] = \
            'org.jenkinsci.plugins.workflow.cps.CpsFlowDefinition'
        definition.attrib['plugin'] = 'workflow-cps'

        XML.SubElement(definition, 'script').text = data.get('dsl', '')

        return xml_parent


# vim: ts=4 sw=4 sts=4 et
