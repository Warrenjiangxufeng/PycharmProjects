import unittest
class baseTest(unittest.TestCase):
    def setUp(self):
        print("start test")

    def tearDown(self):
        print("end test")