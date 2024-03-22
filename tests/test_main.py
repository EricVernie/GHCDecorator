import unittest
from main import app

class TestMain(unittest.TestCase):
    def test_hello_world(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello, World!')

if __name__ == '__main__':
    unittest.main()