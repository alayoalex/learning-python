DROP TABLE IF EXISTS contacto;
DROP TABLE IF EXISTS phone;
DROP TABLE IF EXISTS email;

CREATE TABLE contacto (id integer(10) NOT NULL, nombre varchar(255) NOT NULL, address varchar(255), PRIMARY KEY (id)) autoincrement;
CREATE TABLE phone (id integer(10) NOT NULL, tipo varchar(255), numero varchar(255) UNIQUE, contactoid integer(10), PRIMARY KEY (id) autoincrement, FOREIGN KEY(contactoid) REFERENCES contacto(id));
CREATE TABLE email (contactoid integer(10) NOT NULL, id integer(10) NOT NULL, correo integer(10) UNIQUE, PRIMARY KEY (id) autoincrement, FOREIGN KEY(contactoid) REFERENCES contacto(id));

