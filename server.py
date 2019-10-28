import http.server
import socketserver

PORT = 8000

Handler = http.server.CGIHTTPRequestHandler

print("serving at port", PORT)
http.server.HTTPServer(("", PORT), Handler).serve_forever()