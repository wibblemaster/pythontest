#!/usr/bin/env python
import SimpleHTTPServer
import SocketServer

# Very trivial http server

PORT = 8000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print("serving at port {0}".format(PORT))
httpd.serve_forever()
