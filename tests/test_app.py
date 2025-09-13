import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_home_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_content(self):
        response = self.client.get('/')
        self.assertIn(b'Aplicacao rodando no Docker', response.data)

    def test_hello_status_code(self):
        response = self.client.get('/hello')
        self.assertEqual(response.status_code, 200)

    def test_hello_content(self):
        response = self.client.get('/hello')
        self.assertIn(b'Hello, World!', response.data)

    def test_route_not_found(self):
        response = self.client.get('/nao-existe')
        self.assertEqual(response.status_code, 404)

if __name__ == "__main__":
    unittest.main()
