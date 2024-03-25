from flask import Flask, request, jsonify

app = Flask(__name__)

# Datos de usuario (simplificado para el ejemplo)
users = {"admin": "123"}
 #sqed
# Ruta de inicio de sesión
@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    if username in users and users[username] == password:
        return "Inicio de sesión exitoso", 200
    else:
        return "Credenciales incorrectas", 401

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=8080)
