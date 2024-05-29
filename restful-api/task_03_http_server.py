#!/usr/bin/python3
import http.server
import json


class MyHTTPRequestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()

            self.wfile.write("Hello, this is a simple API!".encode('utf-8'))
        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            sentData = json.dumps({"version": "1.0", "description": "A simple API built with http.server"})
            self.wfile.write(sentData.encode('utf-8'))
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            sentData = json.dumps({"name": "John", "age": 30, "city": "New York"})
            self.wfile.write(sentData.encode('utf-8'))
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()

            self.wfile.write("OK".encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()

            self.wfile.write("Endpoint not found".encode('utf-8'))


httpd = http.server.HTTPServer(('', 8000), MyHTTPRequestHandler)
print("starting server")
httpd.serve_forever()
