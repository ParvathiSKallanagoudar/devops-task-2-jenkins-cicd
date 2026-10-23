import unittest
from unittest.mock import patch
from io import BytesIO
import app


class TestApp(unittest.TestCase):
    def test_home_response(self):
        handler = app.AppHandler.__new__(app.AppHandler)
        handler.path = "/"
        handler.wfile = BytesIO()

        with patch.object(handler, "send_response") as response, \
             patch.object(handler, "send_header"), \
             patch.object(handler, "end_headers"):
            handler.do_GET()

        response.assert_called_once_with(200)
        self.assertEqual(
            handler.wfile.getvalue(),
            b"Hello from Elevate Labs Task 2 - Jenkins CI/CD!"
        )


if __name__ == "__main__":
    unittest.main()
