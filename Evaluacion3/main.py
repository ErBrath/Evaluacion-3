from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/ejercicio1',methods=['GET', 'POST'])
def formularioNotas():
    if request.method == 'POST':
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])
        promedio = (nota1 + nota2 + nota3) / 3
        if promedio >= 40 and asistencia >= 75:
            estado = 'APROBADO'
        else:
            estado = 'REPROBADO'
        return render_template('ejercicio1.html', promedio=promedio, estado=estado, nota1=nota1, nota2=nota2, nota3=nota3, asistencia=asistencia)


    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def formularioNombres():
    nombre_mas_largo=""
    cant_letras=""
    error=""
    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']
        if nombre1 == nombre2 or nombre1 == nombre3 or nombre2 == nombre3:
            error = "Los nombres ingresados no pueden ser iguales"
        else:
            nombres = [nombre1, nombre2, nombre3]
            nombre_mas_largo = max(nombres, key=len)
            cant_letras = len(nombre_mas_largo)

        return render_template('ejercicio2.html', nombre_mas_largo=nombre_mas_largo, cant_letras=cant_letras, nombre1=nombre1, nombre2=nombre2, nombre3=nombre3, error=error)

    return render_template('ejercicio2.html')



if __name__ == '__main__':
    app.run(debug=True)