modulo="formulario.py"
#from turtle import xcor
import formularios_tkinter
import reclamaciones
import consola
import pdf_modulo
import manipular_archivos

ventana,direccion_provincial,nombre,dni,numero_documento,domicilio,provincia,telefono,email,numero_expediente,fecha_resolucion,fecha_notificacion,fecha_solicitud,cantidad,propiedad,residencia,firma,lista_Reclamaciones,impuesto,saldo,sueldo,patrimonio_renta,condiciones,patrimonio_incrementos,boton_generar,textbox_pdf="","","","","","","","","","","","","","","","","","","","","","","","","",""
def nada():
    pass
def generar_pdf():
    global ventana,direccion_provincial,nombre,dni,numero_documento,domicilio,provincia,telefono,email,numero_expediente,fecha_resolucion,fecha_notificacion,fecha_solicitud,cantidad,propiedad,residencia,firma,lista_Reclamaciones,impuesto,saldo,sueldo,patrimonio_renta,condiciones,patrimonio_incrementos,boton_generar
    lista_Reclamaciones_seleccionadas=formularios_tkinter.list_box_elementos_seleccionados(lista_Reclamaciones)
    if lista_Reclamaciones_seleccionadas!=[]:
        fecha_noti=formularios_tkinter.selector_fecha_coger(fecha_notificacion) #funciones_tiempo.str_a_datetime(fecha_notificacion.get(),r'%d/%m/%y')
        fecha_reso=formularios_tkinter.selector_fecha_coger(fecha_resolucion) #funciones_tiempo.str_a_datetime(fecha_emision.get(),r'%d/%m/%y')
        fecha_soli=formularios_tkinter.selector_fecha_coger(fecha_solicitud) #funciones_tiempo.str_a_datetime(fecha_emision.get(),r'%d/%m/%y')
        
        var_direccion_provincial=direccion_provincial.get()
        var_nombre=nombre.get()
        var_numero_documento=numero_documento.get()
        var_dni=dni.get()
        var_domicilio=domicilio.get()
        var_telefono=telefono.get()
        var_email=email.get()
        var_notificacion_dia=fecha_noti.day
        var_notificacion_mes=fecha_noti.month
        var_notificacion_año=fecha_noti.year
        var_RESOLUCIÓN_dia=fecha_reso.day
        var_RESOLUCIÓN_mes=fecha_reso.month
        var_RESOLUCIÓN_año=fecha_reso.year
        if formularios_tkinter.checkbox_estado(impuesto):
            var_impuesto ="La declaración del Impuesto sobre la Renta de Personas Físicas correspondiente al ejercicio anterior "
        else:
            var_impuesto =""
        if formularios_tkinter.checkbox_estado(saldo):
            var_saldo ="Los estados de cuenta bancaria correspondientes al ejercicio anterior "
        else:
            var_saldo =""
        if formularios_tkinter.checkbox_estado(sueldo):
            var_sueldo ="Los documentos de pago emitidos por mi empleador durante el ejercicio anterior "
        else:
            var_sueldo =""
        if formularios_tkinter.checkbox_estado(patrimonio_renta):
            var_patrimonio_renta ="Información del registro mercantil sobre inexistencia de patrimonio cuya valoración equivale o supera tres veces la cuantía correspondiente de renta garantizada por el IMV (cuando se trate de beneficiario individual "
        else:
            var_patrimonio_renta =""
        if formularios_tkinter.checkbox_estado(patrimonio_incrementos):
            var_patrimonio_incrementos ="Información del registro mercantil sobre inexistencia de patrimonio cuya valoración equivale o supera la cuantía resultante de aplicar la escala de incrementos que figura en el Anexo II de la LIMV (cuando el beneficiario sea una unidad de convivencia "
        else:
            var_patrimonio_incrementos =""

    



        var_link=r"https://identificacion.seg-social.es/?origen=imv&destino=https%3A%2F%2Fimv.seg-social.es%2F&representante=true"
        var_numero_expediente=numero_expediente.get()
        var_cantidad=cantidad.get()
        var_provincia=provincia.get()
        var_SOLICITUD_dia=fecha_soli.day
        var_SOLICITUD_mes=fecha_soli.month
        var_SOLICITUD_año=fecha_soli.year
        var_firma=firma.get()
        var_propiedad=propiedad.get()
        var_residencia=residencia.get()

        ruta=manipular_archivos.path_carpeta_actual()
        for reclamacion in lista_Reclamaciones_seleccionadas:
            if reclamacion.lower()=="ingresos superiores":
                reclamaciones.Ingresos_Superiores(direccion_provincial= var_direccion_provincial,nombre= var_nombre,dni= var_dni,domicilio=var_domicilio,telefono=var_telefono,email=var_email,notificacion_dia=var_notificacion_dia,notificacion_mes=var_notificacion_mes,notificacion_año=var_notificacion_año,RESOLUCIÓN_dia=var_RESOLUCIÓN_dia,RESOLUCIÓN_mes=var_RESOLUCIÓN_mes,RESOLUCIÓN_año=var_RESOLUCIÓN_año,impuesto=var_impuesto,saldo=var_saldo,sueldo=var_sueldo,patrimonio_renta=var_patrimonio_renta,patrimonio_incrementos=var_patrimonio_incrementos,link=var_link,numero_expediente=var_numero_expediente,cantidad=var_cantidad,provincia=var_provincia,SOLICITUD_dia=var_SOLICITUD_dia,SOLICITUD_mes=var_SOLICITUD_mes,SOLICITUD_año=var_SOLICITUD_año,firma=var_firma)
                formularios_tkinter.escribir_richtextbox(textbox_pdf,pdf_modulo.leer_texto_pdf(ruta+"/ingresos superiores.pdf"))
            elif reclamacion.lower()=="vivienda habitual":
                reclamaciones.Vivienda_Habitual(direccion_provincial= var_direccion_provincial,nombre= var_nombre,dni= var_dni,domicilio=var_domicilio,telefono=var_telefono,email=var_email,notificacion_dia=var_notificacion_dia,notificacion_mes=var_notificacion_mes,notificacion_año=var_notificacion_año,RESOLUCIÓN_dia=var_RESOLUCIÓN_dia,RESOLUCIÓN_mes=var_RESOLUCIÓN_mes,RESOLUCIÓN_año=var_RESOLUCIÓN_año,link=var_link,numero_expediente=var_numero_expediente,cantidad=var_cantidad,provincia=var_provincia,SOLICITUD_dia=var_SOLICITUD_dia,SOLICITUD_mes=var_SOLICITUD_mes,SOLICITUD_año=var_SOLICITUD_año,firma=var_firma,propiedad=var_propiedad,residencia=var_residencia)
                formularios_tkinter.escribir_richtextbox(textbox_pdf,pdf_modulo.leer_texto_pdf(ruta+"/vivienda habitual.pdf"))
            elif reclamacion.lower()=="rectificacion cuantia":
                reclamaciones.Rectificación_cuantía(direccion_provincial= var_direccion_provincial,nombre= var_nombre,dni= var_dni,domicilio=var_domicilio,telefono=var_telefono,email=var_email,notificacion_dia=var_notificacion_dia,notificacion_mes=var_notificacion_mes,notificacion_año=var_notificacion_año,RESOLUCIÓN_dia=var_RESOLUCIÓN_dia,RESOLUCIÓN_mes=var_RESOLUCIÓN_mes,RESOLUCIÓN_año=var_RESOLUCIÓN_año,impuesto=var_impuesto,saldo=var_saldo,sueldo=var_sueldo,patrimonio_renta=var_patrimonio_renta,patrimonio_incrementos=var_patrimonio_incrementos,link=var_link,numero_expediente=var_numero_expediente,cantidad=var_cantidad,provincia=var_provincia,SOLICITUD_dia=var_SOLICITUD_dia,SOLICITUD_mes=var_SOLICITUD_mes,SOLICITUD_año=var_SOLICITUD_año,firma=var_firma)
                formularios_tkinter.escribir_richtextbox(textbox_pdf,pdf_modulo.leer_texto_pdf(ruta+"/Rectificación cuantía.pdf"))
def generar_menus():
    global ventana
    menu_principal=formularios_tkinter.crear_menu_principal(ventana)
    menu_archivo=formularios_tkinter.crear_menu()
    formularios_tkinter.submenu_añadir_item(menu_archivo,"Abrir",nada)
    formularios_tkinter.submenu_añadir_item(menu_archivo,"Buscar Entidades",nada)
    formularios_tkinter.submenu_añadir_item(menu_archivo,"Generar",nada)
    formularios_tkinter.añadir_submenu_al_principal(menu_principal,menu_archivo,"Archivo")
    menu_plantillas=formularios_tkinter.crear_menu()
    formularios_tkinter.submenu_añadir_item(menu_plantillas,"Nueva",nada)
    formularios_tkinter.submenu_añadir_item(menu_plantillas,"Cargar",nada)
    formularios_tkinter.submenu_añadir_item(menu_plantillas,"Buscar Entidades",nada)
    formularios_tkinter.submenu_añadir_item(menu_plantillas,"Generar Automatica",nada)
    formularios_tkinter.añadir_submenu_al_principal(menu_principal,menu_plantillas,"Plantillas")
    menu_text=formularios_tkinter.crear_menu()
    formularios_tkinter.submenu_añadir_item(menu_text,"Pruebas del entorno",nada)
    formularios_tkinter.submenu_añadir_item(menu_text,"Pruebas unitarias",nada)
    formularios_tkinter.submenu_añadir_item(menu_text,"Pruebas de integracion",nada)
    formularios_tkinter.añadir_submenu_al_principal(menu_principal,menu_text,"Test")
    menu_ayuda=formularios_tkinter.crear_menu()
    formularios_tkinter.submenu_añadir_item(menu_ayuda,"Web",nada)
    formularios_tkinter.submenu_añadir_item(menu_ayuda,"Aplicacion",nada)
    formularios_tkinter.añadir_submenu_al_principal(menu_principal,menu_ayuda,"Ayuda")
    formularios_tkinter.submenu_añadir_item(menu_principal,"EAPN",nada)

    
    pass
def crear_formulario():
    global ventana,direccion_provincial,nombre,dni,numero_documento,domicilio,provincia,telefono,email,numero_expediente,fecha_resolucion,fecha_notificacion,fecha_solicitud,cantidad,propiedad,residencia,firma,lista_Reclamaciones,impuesto,saldo,sueldo,patrimonio_renta,condiciones,patrimonio_incrementos,boton_generar,textbox_pdf
    generar_menus()
    frame_usuario=formularios_tkinter.crear_labelframe(ventana,"Usuario",5,0,250)
    linea_y=0
    linea_x_2=130
    linea_y_global=0
    formularios_tkinter.crear_label(frame_usuario,"direccion provincial",10,linea_y)
    direccion_provincial=formularios_tkinter.crear_combobox(frame_usuario,["Madid","La Rioja"],linea_x_2,linea_y,seleccionado=1)
    textbox_pdf=formularios_tkinter.crear_richtextbox(ventana,300,5,470,530)
    linea_y+=30
    formularios_tkinter.crear_label(frame_usuario,"Nombre",10,linea_y)
    nombre=formularios_tkinter.crear_textbox(frame_usuario,linea_x_2,linea_y)
    linea_y+=30
    formularios_tkinter.crear_label(frame_usuario,"dni",10,linea_y)
    dni=formularios_tkinter.crear_textbox(frame_usuario,linea_x_2,linea_y)
    linea_y+=30
    formularios_tkinter.crear_label(frame_usuario,"numero_documento",10,linea_y)
    numero_documento=formularios_tkinter.crear_textbox(frame_usuario,linea_x_2,linea_y)
    linea_y+=30
    formularios_tkinter.crear_label(frame_usuario,"domicilio",10,linea_y)
    domicilio=formularios_tkinter.crear_textbox(frame_usuario,linea_x_2,linea_y)
    linea_y+=30
    formularios_tkinter.crear_label(frame_usuario,"provincia",10,linea_y)
    provincia=formularios_tkinter.crear_textbox(frame_usuario,linea_x_2,linea_y)
    linea_y+=30
    formularios_tkinter.crear_label(frame_usuario,"telefono",10,linea_y)
    telefono=formularios_tkinter.crear_textbox(frame_usuario,linea_x_2,linea_y)
    linea_y+=30
    formularios_tkinter.crear_label(frame_usuario,"email",10,linea_y)
    email=formularios_tkinter.crear_textbox(frame_usuario,linea_x_2,linea_y)
    linea_y+=45
    frame_usuario.configure(height=linea_y)

    linea_y_global+=linea_y
    linea_y=0
    linea_x_2=130
    frame_datos=formularios_tkinter.crear_labelframe(ventana,"",5,linea_y_global,275)
    formularios_tkinter.crear_label(frame_datos,"numero expediente",10,linea_y)
    numero_expediente=formularios_tkinter.crear_textbox(frame_datos,linea_x_2,linea_y)
    linea_y+=30
    formularios_tkinter.crear_label(frame_datos,"fecha resolucion",10,linea_y)
    fecha_resolucion=formularios_tkinter.crear_selector_fecha(frame_datos,linea_x_2,linea_y,100)
    linea_y+=30
    formularios_tkinter.crear_label(frame_datos,"fecha notificacion",10,linea_y)
    fecha_notificacion=formularios_tkinter.crear_selector_fecha(frame_datos,linea_x_2,linea_y,100)
    linea_y+=30
    formularios_tkinter.crear_label(frame_datos,"fecha solicitud",10,linea_y)
    fecha_solicitud=formularios_tkinter.crear_selector_fecha(frame_datos,linea_x_2,linea_y,100)
    linea_y+=30
    formularios_tkinter.crear_label(frame_datos,"cantidad",10,linea_y)
    cantidad=formularios_tkinter.crear_textbox(frame_datos,linea_x_2,linea_y)
    linea_y+=30
    formularios_tkinter.crear_label(frame_datos,"propiedad",10,linea_y)
    propiedad=formularios_tkinter.crear_textbox(frame_datos,linea_x_2,linea_y)
    linea_y+=30
    formularios_tkinter.crear_label(frame_datos,"residencia",10,linea_y)
    residencia=formularios_tkinter.crear_textbox(frame_datos,linea_x_2,linea_y)
    linea_y+=30
    formularios_tkinter.crear_label(frame_datos,"firma",10,linea_y)
    firma=formularios_tkinter.crear_textbox(frame_datos,linea_x_2,linea_y)
    linea_y+=30
    formularios_tkinter.crear_label(frame_datos,"Reclamaciones",10,linea_y)
    lista_Reclamaciones=formularios_tkinter.crear_listbox(frame_datos,linea_x_2,linea_y,numero_elementos=3,modo_seleccion="")
    formularios_tkinter.listbox_cambiar_lista_elementos(lista_Reclamaciones,["ingresos superiores","vivienda habitual","rectificacion cuantia"])
    linea_y+=70
    frame_datos.configure(height=linea_y+10)

    linea_y_global+=linea_y+10
    linea_y=0
    frame_checks=formularios_tkinter.crear_labelframe(ventana,"",5,linea_y_global,600)
    impuesto=formularios_tkinter.crear_checkbox(frame_checks,"La declaración del Impuesto sobre la Renta de Personas Físicas correspondiente al ejercicio anterior.",posicion_x=10,posicion_y=linea_y)
    linea_y+=30
    saldo=formularios_tkinter.crear_checkbox(frame_checks,"Los estados de cuenta bancaria correspondientes al ejercicio anterior.",posicion_x=10,posicion_y=linea_y)
    linea_y+=30
    sueldo=formularios_tkinter.crear_checkbox(frame_checks,"Los documentos de pago emitidos por mi empleador durante el ejercicio anterior.",posicion_x=10,posicion_y=linea_y)
    linea_y+=30
    patrimonio_renta=formularios_tkinter.crear_checkbox(frame_checks,"Información del registro mercantil sobre inexistencia de patrimonio.",posicion_x=10,posicion_y=linea_y)
    linea_y+=30
    condiciones=formularios_tkinter.crear_checkbox(frame_checks,"Estoy de acuerdo con los terminos y condiciones.",posicion_x=10,posicion_y=linea_y)
    linea_y+=30
    patrimonio_incrementos=formularios_tkinter.crear_checkbox(frame_checks,"patrimonio_incrementos",posicion_x=10,posicion_y=linea_y)
    linea_y+=30
    frame_checks.configure(height=linea_y+10)

    linea_y_global+=linea_y+20
    boton_generar=formularios_tkinter.crear_boton(ventana,generar_pdf,"Generar",150,linea_y_global)

    linea_y_global+=50
    formularios_tkinter.ajustar_tamaño_ventana(ventana,"800x"+str(linea_y_global))

consola.cambiar_nombre_ventana_consola("Formulario IMV.py")
ventana=formularios_tkinter.crear_ventana("Proyecto IMV","800x550",icono=r"./imagenes\eapn.ico")
crear_formulario()
ventana.mainloop()
