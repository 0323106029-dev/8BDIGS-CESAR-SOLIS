import sqlite3
conn = sqlite3.connect('cesar.db')
cursor = conn.cursor()  
cursor.execute('''CREATE TABLE IF NOT EXISTS clientes
                 (id INTEGER PRIMARY KEY autoincrement, nombre TEXT not null, telefono TEXT)''')
cursor.execute("INSERT INTO clientes (nombre, telefono) VALUES ('cesar', '6644590201')")
conn.commit()
conn.close()
