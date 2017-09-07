import mysql.connector

conn = mysql.connector.connect(host="127.0.0.1",
                               user="root",
                               passwd="4879",
                               db="restaurantmenu")

c = conn.cursor()

c.execute('''
          CREATE TABLE restaurant
          (id INTEGER PRIMARY KEY ASC, name varchar(250) NOT NULL)
          ''')

c.execute('''
          CREATE TABLE menu_item
          (id INTEGER PRIMARY KEY ASC, name varchar(250), price VARCHAR(250),
          description VARCHAR(250) NOT NULL, restaurant_id INTEGER NOT NULL,
          FOREIGN KEY (restaurant_id) REFERENCES restaurant(id)
          ''')
