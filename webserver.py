import cgi
from http.server import BaseHTTPRequestHandler, HTTPServer


class WebServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith("/hello"):
                self.send_response(200)
                self.send_header('content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body>"
                output += "<h1>Hello!</h1>"
                output += '''<form method='post' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name='message' type='text' required><input type='submit' value='Submeter'></form>'''
                output += "</body></html>"
                self.wfile.write(output.encode())  # .wfile(output) .wfile.write(output)
                print(output)
                return

            if self.path.endswith("/hola"):
                self.send_response(200)
                self.send_header('content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body>"
                output += "<h1>&#161 Hola !</h1>"
                output += '''<form method='post' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name='message' type='text' required><input type='submit' value='Submeter'></form>'''
                output += "</body></html>"
                self.wfile.write(output.encode())  # .wfile(output) .wfile.write(output)
                print(output)
                return

        except IOError:
            self.send_error(404, "File Not Found %s" % self.path)

    def do_POST(self):
        try:
            ctype, pdict = cgi.parse_header(self.headers['content-type'])
            pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                messagecontent = fields.get('message')
            output = ""
            output += "<!DOCTYPE html><html lang='pt-br'><head><meta charset='UTF-8'>"
            output += "<title>Hello meu amor</title></head><body>"
            output += "<h2>Okay, how about this:</h2>"
            output += "<h1> %s </h1>" % messagecontent[0].decode('utf-8')  # % str(messagecontent[0])
            output += '''<form method='post' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name='message' type='text'><input type='submit' value='Submeter'></form>'''
            output += "</body></html>"
            self.send_response(301)
            self.send_header('content-type', 'text/html')
            self.end_headers()
            self.wfile.write(output.encode('utf-8'))
        except:
            self.send_error("%d" % self.error_content_type)


def main():
    try:
        HOST, PORT = "127.0.0.1", 8080
        with HTTPServer((HOST, PORT), WebServerHandler) as server:
            # port = 8080
            # server = HTTPServer(('127.0.0.1', port), WebServerHandler)
            # httpd = make_server('', 8080, WebServerHandler)
            print("Executando web server HTTP na porta 8080")
            server.serve_forever()
            # httpd.serve_forever()

    except KeyboardInterrupt:
        print("^C presionado, servidor interrompido...")
        server.socket.close()


if __name__ == '__main__':
    main()
