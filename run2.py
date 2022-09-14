import reclamaciones
import list_of_lists
import reclamaciones
import funciones_tiempo
import manipular_archivos
import flask
from flask import Flask, render_template, url_for, redirect, flash, session, request
import os
import flask_modulo
import webbrowser

# from functools import wraps
def valor_checkbox(checkbox):
	if checkbox==None:
		return False
	else:
		return True

nombre,numero_documento,domicilio,telefono,email,texto,expediente,fecha_Notificación,fecha_Emisión,direccion_provincia,impuesto,saldo,sueldo,patrimonio,terminos,patrimonio_renta,patrimonio_incrementos,Reclamaciones="","","","","","","","","","","","","","","","","",""
link=r"https://identificacion.seg-social.es/?origen=imv&destino=https%3A%2F%2Fimv.seg-social.es%2F&representante=true"

#TODOS ESTOS ESTAN SIN PREGUNTAR
numero_expediente="numero_expediente"
cantidad="cantidad"
provincia="provincia"
SOLICITUD_dia="SOLICITUD_dia"
SOLICITUD_mes="SOLICITUD_mes"
SOLICITUD_año="SOLICITUD_año"
firma="[VARIABLE 7 PARA COMPLETAR CON LA FIRMA DEL RECLAMANTE]"
propiedad="Escrituras de la propiedad"
residencia="Certificado de residencia"

#TODOS ESTOS ESTAN SIN PREGUNTAR

app = Flask(__name__)
app.secret_key = "flask"#POR QUE HACE FALTA ESTO
methods = ['GET', 'POST']
GET, POST = methods

@app.route('/', methods=methods)
def index():
	global nombre,numero_documento,domicilio,telefono,email,texto
	error = None
	if request.method == POST:
		nombre=request.form['nombre']
		numero_documento=request.form['numero_documento']
		domicilio=request.form['domicilio']
		telefono=request.form['telefono']
		email=request.form['correo']
		texto=nombre+", "+numero_documento+", "+domicilio+", "+telefono+", "+email
		flash("Todo bien: "+texto)
		return redirect(url_for('index2'),code=301)# redirect("./templates/index2.html", code=0)
	return render_template('index.html', error=error)

@app.route("/index2", methods=methods)
def index2():
	global texto,expediente,fecha_Notificación,fecha_Emisión,direccion_provincial
	error = None
	if request.method == POST:
		expediente=request.form['expediente']
		fecha_Notificación=request.form['fecha_Notificación']
		fecha_Emisión=request.form['fecha_Emisión']
		direccion_provincial=request.form['direccion_provincial']
		texto+=expediente+", "+fecha_Notificación+", "+fecha_Emisión+", "+direccion_provincial
		flash("Todo bien: "+texto)
		return redirect(url_for('index3'))# redirect("./templates/index2.html", code=0)
	return render_template('index2.html', error=error)

@app.route("/index3", methods=methods)
def index3():
	global nombre,numero_documento,domicilio,telefono,email,texto,expediente,fecha_Notificación,fecha_Emisión,direccion_provincia,impuesto,saldo,sueldo,patrimonio,terminos,link,Reclamaciones
	error = None
	if request.method == POST:
		impuesto=valor_checkbox(request.form.get('irpf'))
		if impuesto==True:
			impuesto="La declaración del Impuesto sobre la Renta de Personas Físicas correspondiente al ejercicio anterior"
		else:
			impuesto=""
		saldo=valor_checkbox(request.form.get('saldo'))
		if saldo==True:
			saldo="Los estados de cuenta bancaria correspondientes al ejercicio anterior"
		else:
			saldo=""
		sueldo=valor_checkbox(request.form.get('sueldo'))
		if sueldo==True:
			sueldo="Los documentos de pago emitidos por mi empleador durante el ejercicio anterior"
		else:
			sueldo=""
		patrimonio=valor_checkbox(request.form.get('patrimonio'))
		if patrimonio==True:
			patrimonio="patrimoniopatrimoniopatrimoniopatrimoniopatrimoniopatrimonio"
		else:
			patrimonio="patrimoniopatrimoniopatrimoniopatrimoniopatrimoniopatrimonio"
		terminos=valor_checkbox(request.form.get('terminos'))
		if terminos==True:
			terminos="terminosterminosterminosterminosterminosterminosterminosterminos"
		else:
			terminos="terminosterminosterminosterminosterminosterminosterminosterminos"
		Reclamaciones=request.form.getlist('Reclamaciones')
		patrimonio_renta=valor_checkbox(request.form.get('patrimonio'))
		if patrimonio_renta==True:
			patrimonio_renta="Información del registro mercantil sobre inexistencia de patrimonio cuya valoración equivale o supera tres veces la cuantía correspondiente de renta garantizada por el IMV (cuando se trate de beneficiario individual)"
		else:
			patrimonio_renta=""
		patrimonio_incrementos=valor_checkbox(request.form.get('patrimonio'))
		if patrimonio_incrementos==True:
			patrimonio_incrementos="Información del registro mercantil sobre inexistencia de patrimonio cuya valoración equivale o supera la cuantía resultante de aplicar la escala de incrementos que figura en el Anexo II de la LIMV (cuando el beneficiario sea una unidad de convivencia)"
		else:
			patrimonio_incrementos=""

		if fecha_Notificación!="":
			notificacion_dia=fecha_Notificación[8:10]
			notificacion_mes=fecha_Notificación[5:7]
			notificacion_mes=funciones_tiempo.nombre_del_mes(int(notificacion_mes))
			notificacion_año=fecha_Notificación[0:4]
		else:
			notificacion_dia="notificacion_dia"
			notificacion_mes="notificacion_mes"
			notificacion_año="notificacion_año"
		if fecha_Emisión!="":
			RESOLUCIÓN_dia=fecha_Emisión[8:10]
			RESOLUCIÓN_mes=fecha_Emisión[5:7]
			RESOLUCIÓN_mes=funciones_tiempo.nombre_del_mes(int(RESOLUCIÓN_mes))
			RESOLUCIÓN_año=fecha_Emisión[0:4]
		else:
			RESOLUCIÓN_dia="RESOLUCIÓN_dia"
			RESOLUCIÓN_mes="RESOLUCIÓN_mes"
			RESOLUCIÓN_año="RESOLUCIÓN_año"
		ruta=manipular_archivos.path_carpeta_actual()
		if list_of_lists.buscar_elemento(Reclamaciones,"ViviendaHabitual")==True:
			reclamaciones.Vivienda_Habitual(direccion_provincial,nombre,numero_documento,domicilio,telefono,email,notificacion_dia,notificacion_mes,notificacion_año,RESOLUCIÓN_dia,RESOLUCIÓN_mes,RESOLUCIÓN_año,link,numero_expediente,cantidad,provincia,SOLICITUD_dia,SOLICITUD_mes,SOLICITUD_año,firma,propiedad,residencia)
		if list_of_lists.buscar_elemento(Reclamaciones,"IngresosSuperiores")==True:
			reclamaciones.Ingresos_Superiores(direccion_provincial,nombre,numero_documento,domicilio,telefono,email,notificacion_dia,notificacion_mes,notificacion_año,RESOLUCIÓN_dia,RESOLUCIÓN_mes,RESOLUCIÓN_año,impuesto,saldo,sueldo,patrimonio_renta,patrimonio_incrementos,link,numero_expediente,cantidad,provincia,SOLICITUD_dia,SOLICITUD_mes,SOLICITUD_año,firma)
		if list_of_lists.buscar_elemento(Reclamaciones,"RectificaciónCuantía")==True:
			reclamaciones.Rectificación_cuantía(direccion_provincial,nombre,numero_documento,domicilio,telefono,email,notificacion_dia,notificacion_mes,notificacion_año,RESOLUCIÓN_dia,RESOLUCIÓN_mes,RESOLUCIÓN_año,numero_expediente,link,impuesto,saldo,sueldo,patrimonio_renta,patrimonio_incrementos,cantidad,provincia,SOLICITUD_dia,SOLICITUD_mes,SOLICITUD_año,firma)
		texto=nombre+", "+numero_documento+", "+domicilio+", "+telefono+", "+email
		flash("Todo bien: "+texto)
	return render_template('index3.html', error=error)


if __name__ == '__main__':
	app.run(debug=True)
