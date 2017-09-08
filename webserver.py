import cgifrom http.server import BaseHTTPRequestHandler, HTTPServer# import CRUD Operations from Lesson 1from database_setup import Base, Restaurant, MenuItemfrom sqlalchemy import create_enginefrom sqlalchemy.orm import sessionmaker# Create sesion and connect to DBengine = create_engine('sqlite:///restaurantmenu.db')Base.metadata.bind = engineDBSession = sessionmaker(bind=engine)session = DBSession()class webServerHandler(BaseHTTPRequestHandler):    def do_GET(self):        try:            if self.path.endswith("/restaurants/new"):                output = ""                output += "<html><body>"                output += "<h1>Make a New Restaurant</h1>"                output += "<form method = 'POST' enctype='multipart/form-data' action = '/restaurants/new'>"                output += "<input name = 'newRestaurantName' type = 'text' placeholder = 'New Restaurant Name' > "                output += "<input type='submit' value='Create'>"                output += "</form></body></html>"                self.send_response(200)                self.send_header('Content-type', 'text/html')                self.end_headers()                self.wfile.write(output.encode())                return            if self.path.endswith("/restaurants"):                restaurants = session.query(Restaurant).all()                output = ""                # Objetivo 3 passo 1 -- Criar um Link para novo item menu                output += "<a href='/restaurants/new'>Criar novo Restaurante aqui</a>"                output += "</br></br>"                output += "<html><body>"                for restaurant in restaurants:                    output += restaurant.name                    output += "<br>"                    # Objetivo 2 -- Adicionar link de edição e delete                    output += "<a href='#'>Editar</a>"                    output += "<br>"                    output += "<a href=' #'>Deletar</a>"                    output += "</br></br></br>"                output += "</body></html>"                self.send_response(200)                self.send_header('Content-type', 'text/html')                self.end_headers()                self.wfile.write(output.encode())                return        except IOError:            self.send_error(404, 'File Not Found: %s' % self.path)    def do_POST(self):        try:            if self.path.endswith("/restaurants/new"):                ctype, pdict = cgi.parse_header(self.headers['content-type'])                pdict['boundary'] = bytes(pdict['boundary'], "utf-8")                if ctype == 'multipart/form-data':                    fields = cgi.parse_multipart(self.rfile, pdict)                    messagecontent = fields.get('newRestaurantName')                    # Create new Restaurant Object                    newRestaurant = Restaurant(name=messagecontent[0].decode('utf-8'))                    session.add(newRestaurant)                    session.commit()                    self.send_response(301)                    self.send_header('Content-type', 'text/html')                    self.send_header('Location', '/restaurants')                    self.end_headers()        except:            self.send_error("%d" % self.error_content_type)def main():    try:        server = HTTPServer(('127.0.0.1', 8080), webServerHandler)        print("Web server running...open %s no seu browser!"              % ("http://127.0.0.1:8080/restaurants"))        server.serve_forever()    except KeyboardInterrupt:        print("^C presionado, servidor interrompido...")        server.socket.close()if __name__ == '__main__':    main()