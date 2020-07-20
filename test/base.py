import unittest

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.num = 1
    def tearDown(self):
        self.num = None