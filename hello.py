import unittest
class TestHello(unittest.TestCase):
    def setUp(self):
        self.message = "hello world"
    def test_hello(self):
        self.assertEqual(len(self.message), 11)
    def test_world(self):
        self.assertCountEqual(self.message, "hello world")
if __name__ == '__main__':
    unittest.main()