import sqlite3

# Conectar (si no existe myDB.db, lo crea)
conn = sqlite3.connect("myDB.db")
cursor = conn.cursor()

# Leer el contenido del archivo SQL
with open("structureDB.sql", "r") as f:
    sql_script = f.read()

# Ejecutar el script SQL
cursor.executescript(sql_script)

conn.commit()
conn.close()

print("Base de datos creada correctamente.")
