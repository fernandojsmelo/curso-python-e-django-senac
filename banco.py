import sqlite3

conn = sqlite3.connect("clientes.db")
cursor = conn.cursor()

cursor.execute(
	"""
	   CREATE TABLE cad_cliente (
	         id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	         nome TEXT NOT NULL,
	         idade INTEGER
	    );
	"""
)
print("tabela criada com sucesso!")
conn.close()