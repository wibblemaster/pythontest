#!/usr/bin/env python
import http.server
import socketserver

"""Just a very simple http server - not for production use!"""

PORT = 8000

# Setup the handler

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
