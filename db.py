import sqlite3

DB_PATH = "myDB.db"

def _connect():
    """Conectar a la BD y configurar row_factory para obtener diccionarios."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


# ---------------------------
# READ (GET)
# ---------------------------
def get():
    """Obtiene todos los usuarios como lista de diccionarios."""
    conn = _connect()
    cur = conn.cursor()
    cur.execute("SELECT id, name, email FROM users")
    rows = cur.fetchall()
    conn.close()
    return [dict(row) for row in rows]


# ---------------------------
# CREATE (POST)
# ---------------------------
def post(data):
    """Crea un usuario nuevo. data = {'name':..., 'email':...}"""
    conn = _connect()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            (data["name"], data["email"])
        )
        conn.commit()
        new_id = cur.lastrowid
        conn.close()
        return {"message": "Usuario creado", "id": new_id}
    except sqlite3.IntegrityError:
        conn.close()
        return {"error": "Ya existe un usuario con ese correo."}


# ---------------------------
# UPDATE (PUT)
# ---------------------------
def put(user_id, data):
    """Actualiza un usuario existente."""
    conn = _connect()
    cur = conn.cursor()

    cur.execute(
        "UPDATE users SET name = ?, email = ? WHERE id = ?",
        (data["name"], data["email"], user_id)
    )

    conn.commit()
    conn.close()

    return {"message": "Usuario actualizado"}


# ---------------------------
# DELETE
# ---------------------------
def delete(user_id):
    """Elimina un usuario por ID."""
    conn = _connect()
    cur = conn.cursor()

    cur.execute("DELETE FROM users WHERE id = ?", (user_id,))

    conn.commit()
    conn.close()

    return {"message": "Usuario eliminado"}
