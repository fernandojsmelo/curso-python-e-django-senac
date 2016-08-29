import sqlite3

conn = sqlite3.connect("clientes.db")

cursor = conn.cursor()

cursor.execute("""
	INSERT INTO cad_cliente (nome, idade) VALUES ("Regis", 35);
	""")
cursor.execute("""
	INSERT INTO cad_cliente (nome, idade) VALUES ("Alpisio", 87);
	""")
cursor.execute("""
	INSERT INTO cad_cliente (nome, idade) VALUES ("Bruna", 21);
	""")
cursor.execute("""
	INSERT INTO cad_cliente (nome, idade) VALUES ("Mateus", 19);
	""")

conn.commit()
conn.close()