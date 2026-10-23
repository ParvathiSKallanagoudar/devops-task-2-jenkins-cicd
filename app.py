from http.server import BaseHTTPRequestHandler, HTTPServer


class AppHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello from Elevate Labs Task 2 - Jenkins CI/CD!")


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8000), AppHandler)
    print("Application running on port 8000")
    server.serve_forever()
