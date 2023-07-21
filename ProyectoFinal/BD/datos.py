import pymysql

def insertar_datos(nombres,apellidos,username,password,edad,genero):
    bd=pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="bdproyecto"
    )

    fcursor= bd.cursor()

    sql=f"INSERT INTO login (nombres, apellidos, username, password, edad, genero) VALUES ('{nombres}','{apellidos}','{username}','{password}',{int(edad)},'{genero}')"
    try:
        fcursor.execute(sql)
        bd.commit()
        bandera=1
        mensaje ="Registro exitoso!"
    except:
        bd.rollback()
        mensaje = "No se ha podido registrar"
        bandera=0
    bd.close()

    return mensaje,bandera

def validar_datos(username, password):
    bd=pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="bdproyecto"
    )
    fcursor=bd.cursor()

    fcursor.execute("SELECT password FROM login WHERE username='"+username+"' and password='"+password+"'")
    if fcursor.fetchall():
        mensaje="El usuario y contraseña son correctos"
        bandera=1
    else:
        mensaje="El usuario y contraseña son incorrectos"
        bandera=0

    bd.close()
    return mensaje,bandera
