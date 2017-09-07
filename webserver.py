from http.server import BaseHTTPRequestHandler, HTTPServer


class WebServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith("/hello"):
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()

            output = b"<html><title>Hello meu amor</title><body>Hello!!!!</body></html>"
            self.wfile.write(output)  # .wfile(output) .wfile.write(output)
            print(output)
        else:
            self.send_error(404, "File Not Found %s" % self.path)


def main():
    try:
        port = 8080
        server = HTTPServer(('', port), WebServerHandler)
        # httpd = make_server('', 8080, WebServerHandler)
        print("Executando web server HTTP na porta 8080")
        server.serve_forever()
        # httpd.serve_forever()

    except KeyboardInterrupt:
        print("^C presionado, servidor interrompido...")
        server.socket.close()
        # httpd.socket.close()


if __name__ == '__main__':
    main()
