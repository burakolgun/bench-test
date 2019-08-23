from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type','text/html')
    self.end_headers()

    with open('index.html', 'rb') as html_file:
    	self.wfile.write(html_file.read())
    	html_file.close()
    return

HOST = '127.0.0.1'
PORT = 1461
HTTPD = HTTPServer((HOST, PORT), RequestHandler)
print('server is listening on', PORT)
HTTPD.serve_forever()
