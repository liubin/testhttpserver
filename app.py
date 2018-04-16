import http.server
import os

class Handle(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        body = str(os.environ).encode()
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.send_header('Content-length', len(body))
        self.end_headers()
        self.wfile.write(body)


server_address = ('', 80)
httpd = http.server.HTTPServer(server_address, Handle)
httpd.serve_forever()

