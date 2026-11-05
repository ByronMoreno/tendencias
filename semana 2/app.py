import os
import time
from flask import Flask, request, redirect, url_for, render_template_string
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

# Configuración de conexión a PostgreSQL mediante variables de entorno
DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "instituto_db")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres123")
DB_PORT = os.getenv("DB_PORT", "5432")


def get_db_connection(max_reintentos=5, espera=2):
    """
    Establece conexión con la base de datos PostgreSQL.
    Incluye reintentos para dar tiempo a que PostgreSQL termine de inicializarse.
    """
    intentos = 0
    while intentos < max_reintentos:
        try:
            conn = psycopg2.connect(
                host=DB_HOST,
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD,
                port=DB_PORT,
                cursor_factory=RealDictCursor
            )
            return conn
        except psycopg2.OperationalError as error:
            intentos += 1
            print(f"[*] Esperando que PostgreSQL esté listo... (Intento {intentos}/{max_reintentos})")
            time.sleep(espera)
    raise Exception(f"No fue posible conectar a PostgreSQL después de {max_reintentos} intentos.")


def inicializar_base_datos():
    """Crea la tabla si no existe al arrancar la aplicación."""
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS estudiantes (
                id SERIAL PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL,
                correo VARCHAR(100) NOT NULL,
                carrera VARCHAR(100) NOT NULL,
                fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        conn.commit()
        cur.close()
        conn.close()
        print("[+] Base de datos y tabla 'estudiantes' listas.")
    except Exception as e:
        print(f"[-] Error inicializando tabla: {e}")


# Plantilla HTML con diseño moderno responsivo
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Semana 2: Python + PostgreSQL en Docker</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: #f0f2f5;
            color: #333;
            padding: 30px 15px;
        }
        .container {
            max-width: 900px;
            margin: 0 auto;
        }
        .header {
            background: linear-gradient(135deg, #1f4037 0%, #99f2c8 100%);
            color: white;
            padding: 25px;
            border-radius: 12px;
            margin-bottom: 25px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }
        .header h1 { font-size: 1.8rem; margin-bottom: 8px; }
        .header p { opacity: 0.9; font-size: 0.95rem; }
        .badges { margin-top: 12px; }
        .badge {
            display: inline-block;
            background: rgba(255,255,255,0.25);
            padding: 4px 10px;
            border-radius: 20px;
            font-size: 0.8rem;
            margin-right: 6px;
        }
        .grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 25px;
        }
        @media(min-width: 768px) {
            .grid { grid-template-columns: 320px 1fr; }
        }
        .card {
            background: white;
            padding: 22px;
            border-radius: 10px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.06);
        }
        .card h2 {
            font-size: 1.2rem;
            margin-bottom: 15px;
            color: #1f4037;
            border-bottom: 2px solid #e2e8f0;
            padding-bottom: 8px;
        }
        .form-group { margin-bottom: 14px; }
        label { display: block; margin-bottom: 5px; font-weight: 600; font-size: 0.85rem; color: #4a5568; }
        input[type="text"], input[type="email"], select {
            width: 100%;
            padding: 10px;
            border: 1px solid #cbd5e0;
            border-radius: 6px;
            font-size: 0.9rem;
        }
        input:focus, select:focus {
            outline: none;
            border-color: #1f4037;
            box-shadow: 0 0 0 2px rgba(31,64,55,0.2);
        }
        button.btn-primary {
            width: 100%;
            background: #1f4037;
            color: white;
            padding: 10px;
            border: none;
            border-radius: 6px;
            font-size: 0.95rem;
            font-weight: bold;
            cursor: pointer;
            transition: background 0.2s;
        }
        button.btn-primary:hover { background: #163028; }
        table {
            width: 100%;
            border-collapse: collapse;
            font-size: 0.88rem;
        }
        th, td {
            padding: 10px 12px;
            text-align: left;
            border-bottom: 1px solid #e2e8f0;
        }
        th {
            background: #f7fafc;
            color: #4a5568;
            font-weight: 600;
        }
        tr:hover { background: #f8fafc; }
        .btn-delete {
            background: #e53e3e;
            color: white;
            border: none;
            padding: 4px 8px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 0.75rem;
        }
        .empty-state {
            text-align: center;
            padding: 30px;
            color: #a0aec0;
        }
        .info-footer {
            margin-top: 20px;
            padding: 12px;
            background: #edf2f7;
            border-radius: 8px;
            font-size: 0.8rem;
            color: #4a5568;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🐘 Registro de Estudiantes (Docker + PostgreSQL)</h1>
            <p>Instituto Superior Tecnológico Yavirac - Tendencias Actuales de Programación</p>
            <div class="badges">
                <span class="badge">🌐 Contenedor Web: Python 3.12 / Flask</span>
                <span class="badge">🗄️ Contenedor DB: PostgreSQL 16</span>
                <span class="badge">🔗 Red Docker: compose-network</span>
            </div>
        </div>

        <div class="grid">
            <!-- Formulario de Registro -->
            <div class="card">
                <h2>Nuevo Registro</h2>
                <form action="/guardar" method="POST">
                    <div class="form-group">
                        <label for="nombre">Nombre completo:</label>
                        <input type="text" id="nombre" name="nombre" required placeholder="Ej: Carlos Andrade">
                    </div>
                    <div class="form-group">
                        <label for="correo">Correo electrónico:</label>
                        <input type="email" id="correo" name="correo" required placeholder="carlos@yavirac.edu.ec">
                    </div>
                    <div class="form-group">
                        <label for="carrera">Carrera / Especialidad:</label>
                        <select id="carrera" name="carrera" required>
                            <option value="">-- Seleccionar --</option>
                            <option value="Desarrollo de Software">Desarrollo de Software</option>
                            <option value="Redes y Ciberseguridad">Redes y Ciberseguridad</option>
                            <option value="Diseño Gráfico">Diseño Gráfico</option>
                            <option value="Administración">Administración</option>
                        </select>
                    </div>
                    <button type="submit" class="btn-primary">Guardar en PostgreSQL</button>
                </form>
            </div>

            <!-- Tabla de Datos -->
            <div class="card">
                <h2>Estudiantes Registrados ({{ estudiantes|length }})</h2>
                {% if estudiantes %}
                <table>
                    <thead>
                        <tr>
                            <th>#</th>
                            <th>Nombre</th>
                            <th>Correo</th>
                            <th>Carrera</th>
                            <th>Acción</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for e in estudiantes %}
                        <tr>
                            <td><strong>{{ e.id }}</strong></td>
                            <td>{{ e.nombre }}</td>
                            <td>{{ e.correo }}</td>
                            <td>{{ e.carrera }}</td>
                            <td>
                                <form action="/eliminar/{{ e.id }}" method="POST" style="display:inline;" onsubmit="return confirm('¿Seguro de eliminar este registro?');">
                                    <button type="submit" class="btn-delete">Eliminar</button>
                                </form>
                            </td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
                {% else %}
                <div class="empty-state">
                    <p>No hay estudiantes guardados aún en PostgreSQL.</p>
                    <p style="font-size: 0.8rem; margin-top: 5px;">¡Completa el formulario de la izquierda para agregar el primero!</p>
                </div>
                {% endif %}
            </div>
        </div>

        <div class="info-footer">
            <strong>Arquitectura Multi-contenedor:</strong> La aplicación web se comunica con la base de datos a través del host interno <code>db:5432</code> resuelto por el DNS de Docker Compose. Los datos se almacenan en un volumen persistente de Docker.
        </div>
    </div>
</body>
</html>
"""


@app.route("/")
def index():
    """Consulta la lista de estudiantes guardados en PostgreSQL y los presenta."""
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM estudiantes ORDER BY id DESC;")
    estudiantes = cur.fetchall()
    cur.close()
    conn.close()
    return render_template_string(HTML_TEMPLATE, estudiantes=estudiantes)


@app.route("/guardar", methods=["POST"])
def guardar():
    """Recibe los datos del formulario y los inserta en PostgreSQL."""
    nombre = request.form.get("nombre")
    correo = request.form.get("correo")
    carrera = request.form.get("carrera")

    if nombre and correo and carrera:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO estudiantes (nombre, correo, carrera) VALUES (%s, %s, %s);",
            (nombre, correo, carrera)
        )
        conn.commit()
        cur.close()
        conn.close()

    return redirect(url_for("index"))


@app.route("/eliminar/<int:id>", methods=["POST"])
def eliminar(id):
    """Elimina un registro específico por su ID."""
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM estudiantes WHERE id = %s;", (id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for("index"))


if __name__ == "__main__":
    # Inicializar la base de datos antes de empezar a recibir peticiones
    inicializar_base_datos()
    # Ejecución en el puerto 5000 y accesible externamente
    app.run(host="0.0.0.0", port=5000)
