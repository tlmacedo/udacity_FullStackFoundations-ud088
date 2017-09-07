from http.server import BaseHTTPRequestHandler, HTTPServer


class WebServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith("/hello"):
                self.send_response(200)
                self.send_header('content-type', 'text/html')
                self.end_headers()

                output = b"<html><title>Hello meu amor</title><body>Hello!!!!</body></html>"
                output = b"<html><title>Hello meu amor</title><body>Hello!!!!<a href='/hola'> vai para &#161&#161&#161Hola</a></body></html>"
                self.wfile.write(output)  # .wfile(output) .wfile.write(output)
                print(output)
                return

            if self.path.endswith("/hola"):
                self.send_response(200)
                self.send_header('content-type', 'text/html')
                self.end_headers()

                output = b"<html><title>Hola mi amor</title><body>&#161&#161&#161Hola  <a href='/hello'> volta para Hello!!!!</a></body></html>"
                self.wfile.write(output)  # .wfile(output) .wfile.write(output)
                print(output)
                return

        except IOError:
            self.send_error(404, "File Not Found %s" % self.path)


def main():
    try:
        port = 8080
        server = HTTPServer(('127.0.0.1', port), WebServerHandler)
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
