from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Mi Primer Docker con Flask</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #1d2671 0%, #c33764 100%);
                color: #333;
                display: flex;
                align-items: center;
                justify-content: center;
                min-height: 100vh;
                margin: 0;
            }
            .card {
                background: white;
                border-radius: 16px;
                padding: 40px;
                box-shadow: 0 10px 25px rgba(0,0,0,0.3);
                text-align: center;
                max-width: 500px;
                width: 90%;
            }
            h1 {
                color: #0db7ed;
                margin-bottom: 10px;
            }
            p {
                font-size: 1.1rem;
                color: #555;
            }
            .badge {
                display: inline-block;
                background-color: #28a745;
                color: white;
                padding: 8px 18px;
                border-radius: 50px;
                font-weight: bold;
                font-size: 0.95rem;
                margin-top: 15px;
            }
            .info-box {
                margin-top: 25px;
                padding: 15px;
                background-color: #f8f9fa;
                border-left: 4px solid #0db7ed;
                text-align: left;
                font-size: 0.9rem;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>¡Hola Mundo! 🐳</h1>
            <p><strong>Mi primera aplicación con Python y Flask.</strong></p>
            <p>Esta aplicación se está ejecutando dentro de un contenedor Docker en Linux con WSL 2.</p>
            <span class="badge">Estado: Activo y Conectado</span>
            <div class="info-box">
                <strong>Docente / Alumno:</strong> Tendencias Actuales de Programación<br>
                <strong>Entorno:</strong> Python 3.12-slim | Flask 3.1.2<br>
                <strong>Host:</strong> 0.0.0.0 | <strong>Puerto:</strong> 5000
            </div>
        </div>
    </body>
    </html>
    """

@app.route("/saludo/<nombre>")
def saludo(nombre):
    return f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Saludo Personalizado</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #f0f4f8;
                text-align: center;
                padding: 50px;
            }}
            .box {{
                background: white;
                padding: 30px;
                border-radius: 10px;
                display: inline-block;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            }}
            h2 {{ color: #2b6cb0; }}
        </style>
    </head>
    <body>
        <div class="box">
            <h2>¡Hola, {nombre}! 🚀</h2>
            <p>¡Felicitaciones! Has completado el reto práctico de Docker y Flask.</p>
            <a href="/">Volver al Inicio</a>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    # Importante: host="0.0.0.0" permite que la aplicación acepte conexiones externas al contenedor
    app.run(host="0.0.0.0", port=5000)
