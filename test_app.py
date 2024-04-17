from . import lambda_auth
import unittest

class TestHelloWorld(unittest.TestCase):

    # def setUp(self):
    #     self.app = lambda_auth.app.test_client()
    #     self.app.testing = True

    # def test_status_code(self):
    #     response = self.app.get('/')
    #     self.assertEqual(response.status_code, 200)

    def test_greeting_message(self):
        greeting = 'Teste lambda auth!'
        self.assertEqual(lambda_auth.greet(), greeting)


if __name__ == '__main__':
    unittest.main()
