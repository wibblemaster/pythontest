#!/usr/bin/env python
import SimpleHTTPServer
import SocketServer

PORT = 8000

# Setup the handler

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print("serving at port {0}".format(PORT))
httpd.serve_forever()
