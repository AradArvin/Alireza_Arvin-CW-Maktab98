import time
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

HOST = "192.168.1.102"
PORT = 8000

database = dict()

class NeuralHTTP(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(database).encode())


    def do_POST(self):
        if self.path == "/":
            content_length = int(self.headers['Content-Length'])
            data = self.rfile.read(content_length)
            database['1'] = (json.loads(data.decode()))
            # database["1"] = data.decode() 
            self.send_response(201)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"Success..")


server = HTTPServer((HOST, PORT), NeuralHTTP)
print("server is running...")

server.serve_forever()

# curl http://192.168.1.102:8000/ -X POST -H "Content-Type:application/json" -d {'id':1,'title':'moo','description':'cow'}