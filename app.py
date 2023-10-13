import BaseHTTPServer
import time
import os
from SocketServer import ThreadingMixIn

PORT_NUMBER = 8080 # Maybe set this to 9000.

VERSION = "v1.0"

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(s):
        """Respond to a GET request."""
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        s.wfile.write("<html><head><title>Coredge.io Demo app</title></head>")
        s.wfile.write("<body><h2>Demo App Version:- " + os.environ.get('VERSION', VERSION) + "</h2>")
        s.wfile.write("</body></html>")

class ThreadingHTTPServer(ThreadingMixIn, BaseHTTPServer.HTTPServer):
    pass

if __name__ == '__main__':
    #server_class = BaseHTTPServer.HTTPServer
    server_class = ThreadingHTTPServer
    httpd = server_class(("", PORT_NUMBER), MyHandler)
    print time.asctime(), "Server Starts - :%s" % (PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Server Stops - :%s" % (PORT_NUMBER)