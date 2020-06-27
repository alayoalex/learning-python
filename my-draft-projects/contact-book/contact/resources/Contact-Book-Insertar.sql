INSERT INTO contacto(id, nombre, address) VALUES (?, ?, ?);
INSERT INTO phone(id, tipo, numero, contactoid) VALUES (?, ?, ?, ?);
INSERT INTO email(contactoid, id, correo) VALUES (?, ?, ?);

