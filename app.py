"""Just a very simple http server - not for production use!"""

import http.server
import socketserver

PORT = 8000

# Setup the handler

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
