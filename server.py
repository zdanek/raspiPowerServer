import sys
import BaseHTTPServer
import SimpleHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
import os

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        print self.path

        if self.path == "/power/off":
            self.wfile.write("<html><body>")
            self.wfile.write("Powering off...")
            self.wfile.write("</body></html>")
            print os.system('shutdown -h now')
            return
        if self.path == '/reboot':
            self.wfile.write("<html><body>")
            self.wfile.write("Rebooting...")
            self.wfile.write("</body></html>")
            print os.system('reboot')
            return
        if self.path == '/':
            self.wfile.write("<html><body>")
            self.wfile.write("I'm ok")
            self.wfile.write("</body></html>")
            return

        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)


handler = MyHandler
ServerClass  = BaseHTTPServer.HTTPServer
Protocol     = "HTTP/1.0"

if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 7000
server_address = ('0.0.0.0', port)

handler.protocol_version = Protocol
httpd = ServerClass(server_address, handler)

sa = httpd.socket.getsockname()
print "Serving HTTP on", sa[0], "port", sa[1], "..."
httpd.serve_forever()
