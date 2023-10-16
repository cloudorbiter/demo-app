import http.server
import time
import os
from socketserver import ThreadingMixIn

PORT_NUMBER = 8080 # Maybe set this to 9000.

VERSION = "v1.2"

class MyHandler(http.server.BaseHTTPRequestHandler):
    def write_message(s, msg):
        s.wfile.write(msg.encode())

    def do_GET(s):
        """Respond to a GET request."""
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        s.write_message("<html><head><title>Coredge.io Demo app</title></head>")
        s.write_message("<body><h2>Demo App Version:- " + os.environ.get('VERSION', VERSION) + "</h2>")
        s.write_message("</body></html>")

class ThreadingHTTPServer(ThreadingMixIn, http.server.HTTPServer):
    pass

if __name__ == '__main__':
    #server_class = BaseHTTPServer.HTTPServer
    server_class = ThreadingHTTPServer
    httpd = server_class(("", PORT_NUMBER), MyHandler)
    print(time.asctime(), "Server Starts - :%s" % (PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(), "Server Stops - :%s" % (PORT_NUMBER))