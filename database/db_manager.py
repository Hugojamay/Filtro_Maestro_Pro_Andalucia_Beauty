import sqlite3
import os

DB_PATH = os.path.join("database", "prospectos.db")

def inicializar_base_datos():
    """
    Crea la tabla de prospectos si no existe, asegurando campos para autor, texto,
    categoría, evidencia, scoring y estado de seguimiento.
    """
    os.makedirs("database", exist_ok=True)
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS prospectos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            autor TEXT,
            texto TEXT UNIQUE,
            categoria TEXT,
            evidencia TEXT,
            scoring INTEGER,
            fecha_captura TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            estado TEXT DEFAULT 'Nuevo'
        )
    """)
    
    conexion.commit()
    conexion.close()

def guardar_prospecto(autor: str, texto: str, categoria: str, evidencia: str, scoring: int) -> bool:
    """
    Guarda un prospecto en la base de datos evitando duplicados por texto exacto.
    Retorna True si se guardó con éxito, False si ya existía.
    """
    inicializar_base_datos()
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
    
    try:
        cursor.execute("""
            INSERT OR IGNORE INTO prospectos (autor, texto, categoria, evidencia, scoring)
            VALUES (?, ?, ?, ?, ?)
        """, (autor, texto, categoria, evidencia, scoring))
        
        conexion.commit()
        guardado = cursor.rowcount > 0
        conexion.close()
        return guardado
    except Exception as e:
        print(f"Error al guardar prospecto: {e}")
        conexion.close()
        return False

def obtener_todos_prospectos() -> list:
    """
    Recupera todos los prospectos almacenados ordenados por scoring de mayor a menor.
    """
    inicializar_base_datos()
    conexion = sqlite3.connect(DB_PATH)
    conexion.row_factory = sqlite3.Row
    cursor = conexion.cursor()
    
    cursor.execute("SELECT * FROM prospectos ORDER BY scoring DESC")
    filas = cursor.fetchall()
    
    prospectos = [dict(fila) for fila in filas]
    conexion.close()
    return prospectos