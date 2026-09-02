import os
import psycopg2

# =========================================================
# CONEXIÓN A POSTGRESQL
# =========================================================
def f_conectar():
    # Lee la URI de la base de datos desde el entorno de Render, 
    # o usa la URI directa de Clever Cloud si se ejecuta de forma local.
    database_url = os.getenv(
        "DATABASE_URL", 
        "postgresql://utllnbasrubg5k96abp9:pKOXTbQ75tkiecP4Ne1WYmlDqBzkRi@b6dbt85joiddwjpcrjs2-postgresql.services.clever-cloud.com:5432/b6dbt85joiddwjpcrjs2"
    )
    conexion = psycopg2.connect(database_url)
    return conexion

# =========================================================
# CREAR TABLA AUTOMÁTICAMENTE
# =========================================================
def f_crear_tabla():
    conexion = f_conectar()
    cursor = conexion.cursor()
    sql = """
    CREATE TABLE IF NOT EXISTS clientes (
        id_cliente SERIAL PRIMARY KEY,
        nombre VARCHAR(50) NOT NULL,
        apellido_paterno VARCHAR(50) NOT NULL,
        apellido_materno VARCHAR(50),
        fecha_nacimiento DATE,
        genero VARCHAR(15),
        correo VARCHAR(100) NOT NULL,
        telefono VARCHAR(20),
        estado VARCHAR(50),
        ciudad VARCHAR(50),
        codigo_postal VARCHAR(10),
        tipo_cliente VARCHAR(20),
        intereses VARCHAR(200),
        limite_credito DECIMAL(10,2),
        observaciones VARCHAR(250)
    );
    """
    cursor.execute(sql)
    conexion.commit()
    cursor.close()
    conexion.close()

# Ejecutar la creación de la tabla al iniciar el módulo
f_crear_tabla()

# =========================================================
# AGREGAR CLIENTE
# =========================================================
def f_agregar_registro(
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
    intereses,
    limite_credito,
    observaciones
):
    conexion = f_conectar()
    cursor = conexion.cursor()
    sql = """
    INSERT INTO clientes
    (
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
        intereses,
        limite_credito,
        observaciones
    )
    VALUES
    (
        %s, %s, %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s, %s, %s
    )
    """
    valores = (
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
        intereses,
        limite_credito,
        observaciones
    )
    cursor.execute(sql, valores)
    conexion.commit()
    cursor.close()
    conexion.close()

# =========================================================
# LISTAR CLIENTES
# =========================================================
def f_listar_clientes():
    conexion = f_conectar()
    cursor = conexion.cursor()
    sql = """
    SELECT
        id_cliente,
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
        intereses,
        limite_credito,
        observaciones
    FROM clientes
    ORDER BY id_cliente
    """
    cursor.execute(sql)
    clientes = cursor.fetchall()
    cursor.close()
    conexion.close()
    return clientes