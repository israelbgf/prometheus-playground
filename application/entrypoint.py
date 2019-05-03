import http.server
from prometheus_client import start_http_server


class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello World")


sever_address = ('0.0.0.0', 8080)
prometheus_port = 8081

if __name__ == "__main__":
    print("Server started... {}".format(sever_address))
    start_http_server(prometheus_port)
    server = http.server.HTTPServer(sever_address, MyHandler)
    server.serve_forever()
