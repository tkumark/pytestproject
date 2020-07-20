from test.base import BaseTestCase

class MyTest(BaseTestCase):
    def runTest(self):
        self.assertEqual(self.num, 1)

# unittest.TextTestRunner().run(MyTest())