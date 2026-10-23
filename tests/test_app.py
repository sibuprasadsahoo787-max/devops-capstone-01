import json
import unittest
from http.server import HTTPServer
from threading import Thread
from urllib.request import urlopen
from urllib.error import HTTPError

from app.main import AppHandler


class TestApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = HTTPServer(("127.0.0.1", 0), AppHandler)
        cls.port = cls.server.server_address[1]
        cls.thread = Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()

    def test_health_endpoint(self):
        with urlopen(
            f"http://127.0.0.1:{self.port}/health"
        ) as response:
            self.assertEqual(response.status, 200)
            data = json.loads(response.read().decode())

        self.assertEqual(data["status"], "healthy")
        self.assertEqual(data["service"], "devops-capstone-01")

    def test_invalid_endpoint(self):
        with self.assertRaises(HTTPError) as error:
            urlopen(f"http://127.0.0.1:{self.port}/invalid")

        self.assertEqual(error.exception.code, 404)


if __name__ == "__main__":
    unittest.main()
