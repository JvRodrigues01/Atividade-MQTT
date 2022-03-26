import http.server, socketserver
import json

PORT = 8000

arrayRequests = []

class SimpleHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        global arrayRequests
        self.send_response(200)
        self.send_header("Content-Type","application/json")
        self.end_headers()
        self.wfile.write(bytes(json.dumps(arrayRequests), "UTF-8"))

    def do_POST(self):
        global arrayRequests
        self.send_response(200)
        body = self.rfile.read(int(self.headers.get("Content-Length")))
        self.end_headers()
        print(body)
        arrayRequests.append(json.loads(body))

Handler = SimpleHandler
httpd = socketserver.TCPServer(("", PORT), Handler)
httpd.serve_forever()