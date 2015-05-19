import os
from testtools import TestCase
from testscenarios.testcase import TestWithScenarios
from base import get_scenarios, SingleJobTestCase


class TestCaseModuleWorkflow(TestWithScenarios, TestCase,
                             SingleJobTestCase):
    fixtures_path = os.path.join(os.path.dirname(__file__), 'fixtures')
    scenarios = get_scenarios(fixtures_path)
