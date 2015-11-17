# -*- encode utf-8 -*-
import unittest
import sys
sys.path.append("../../../gdd20/")
from gdd20 import app


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass
