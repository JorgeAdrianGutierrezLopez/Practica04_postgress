from flask import Flask, render_template, request
from CMySql import f_agregar_registro, f_listar_clientes

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/mostrar_cliente", methods=["POST"])
def mostrar_cliente():
    nombre = request.form["nombre"]
    apellido_paterno = request.form["apellido_paterno"]
    apellido_materno = request.form["apellido_materno"]
    fecha_nacimiento = request.form["fecha_nacimiento"]
    genero = request.form.get("genero", "")
    
    correo = request.form["correo"]
    telefono = request.form["telefono"]
    
    estado = request.form["estado"]
    ciudad = request.form["ciudad"]
    codigo_postal = request.form["codigo_postal"]
    
    tipo_cliente = request.form["tipo_cliente"]
    intereses = request.form.getlist("intereses")
    intereses_texto = ", ".join(intereses)
    limite_credito = request.form["limite_credito"]
    observaciones = request.form["observaciones"]

    f_agregar_registro(
        nombre,
        apellido_paterno,
        apellido_materno,
        fecha_nacimiento,
        genero,
        correo,
        telefono,
        estado,
        ciudad,
        codigo_postal,
        tipo_cliente,
        intereses_texto,
        limite_credito,
        observaciones
    )

    return render_template(
        "mostrar_cliente.html",
        nombre=nombre,
        apellido_paterno=apellido_paterno,
        apellido_materno=apellido_materno,
        fecha_nacimiento=fecha_nacimiento,
        genero=genero,
        correo=correo,
        telefono=telefono,
        estado=estado,
        ciudad=ciudad,
        codigo_postal=codigo_postal,
        tipo_cliente=tipo_cliente,
        limite_credito=limite_credito,
        observaciones=observaciones
    )

@app.route("/clientes")
def listar_clientes():
    clientes = f_listar_clientes()
    return render_template(
        "listar_clientes.html",
        clientes=clientes
    )

if __name__ == "__main__":
    app.run(debug=True)