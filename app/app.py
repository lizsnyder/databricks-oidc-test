import http.server
import os

port = int(os.environ.get("DATABRICKS_APP_PORT", 8080))

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello from CI/CD!")
    def log_message(self, *args):
        pass

with http.server.HTTPServer(("", port), Handler) as httpd:
    httpd.serve_forever()
