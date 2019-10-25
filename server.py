import http.server
import socketserver

PORT = 8000

Handler = http.server.CGIHTTPRequestHandler

print("serving at port", PORT)
socketserver.TCPServer(("", PORT), Handler).serve_forever()