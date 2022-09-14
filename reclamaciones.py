modulo="Reclamaciones.py"
import pdf_modulo
import manipular_archivos

def Ingresos_Superiores(direccion_provincial,nombre,dni,domicilio,telefono,email,notificacion_dia,notificacion_mes,notificacion_año,RESOLUCIÓN_dia,RESOLUCIÓN_mes,RESOLUCIÓN_año,impuesto,saldo,sueldo,patrimonio_renta,patrimonio_incrementos,link,numero_expediente,cantidad,provincia,SOLICITUD_dia,SOLICITUD_mes,SOLICITUD_año,firma):
    # direccion_provincial="[CHECKBOX 1 PARA SELECCIONAR LA DIRECCIÓN PROVINCIAL DE LA SEGURIDAD SOCIAL A LA QUE SE DIRIGE LA RECLAMACIÓN]"
    # nombre="[VARIABLE 1: NOMBRES Y APELLIDOS DEL RECLAMANTE]"
    # dni="[VARIABLE 2: NÚMERO DE DOCUMENTO DE IDENTIFICACIÓN]"
    # domicilio="[VARIABLE 3: DOMICILIO]"
    # telefono="[VARIABLE 4: TELÉFONO]"
    # email="[VARIABLE 5: DIRECCIÓN DE CORREO ELECTRÓNICO]"
    # notificacion_dia="[CHECKBOX 2 PARA INDICAR DÍA DE NOTIFICACIÓN DE LA RESOLUCIÓN RECLAMADA]"
    # notificacion_mes="[CHECKBOX 3 PARA INDICAR MES DE NOTIFICACIÓN DE LA RESOLUCIÓN RECLAMADA]"
    # notificacion_año="[CHECKBOX 4 PARA INDICAR AÑO DE NOTIFICACIÓN DE LA RESOLUCIÓN RECLAMADA]"
    # RESOLUCIÓN_dia="[CHECKBOX 5 PARA INDICAR DÍA DE EMISIÓN DE LA RESOLUCIÓN RECLAMADA]"
    # RESOLUCIÓN_mes="[CHECKBOX 6 PARA INIDCAR MES DE EMISIÓN DE LA RESOLUCIÓN RECLAMADA]"
    # RESOLUCIÓN_año="[CHECKBOX 7 PARA INDICAR AÑO DE EMISIÓN DE LA RESOLUCIÓN RECLAMADA]"
    # impuesto="CHECKBOX_8 La declaración del Impuesto sobre la Renta de Personas Físicas correspondiente al ejercicio anterior "
    # saldo="CHECKBOX_9 Los estados de cuenta bancaria correspondientes al ejercicio anterior "
    # sueldo="CHECKBOX_10 Los documentos de pago emitidos por mi empleador durante el ejercicio "
    # patrimonio_renta="CHECKBOX_11 Información del registro mercantil sobre inexistencia de patrimonio cuya valoración equivale o supera tres veces la cuantía correspondiente de renta garantizada por el IMV (cuando se trate de beneficiario individual)"
    # patrimonio_incrementos="CHECKBOX_12 : Información del registro mercantil sobre inexistencia de patrimonio cuya valoración equivale o supera la cuantía resultante de aplicar la escala de incrementos que figura en el Anexo II de la LIMV (cuando el beneficiario sea una unidad de convivencia)"
    link=r"https://identificacion.seg-social.es/?origen=imv&destino=https%3A%2F%2Fimv.seg-social.es%2F&representante=true"
    # numero_expediente="[VARIABLE 6: número de expediente con el que se tramita la solicitud de otorgamiento de IMV (que debe mostrarse referida en la resolución reclamada)]"
    # cantidad=100
    # provincia="[CHECKBOX 13 PARA SELECCIONAR LA PROVINCIA]"
    # SOLICITUD_dia="[CHECKBOX 14 PARA INDICAR DÍA DE SUSCRIPCIÓN DE LA SOLICITUD]"
    # SOLICITUD_mes="[CHECKBOX 15 PARA INDICAR MES DE SUSCRIPCIÓN DE LA SOLICITUD]"
    # SOLICITUD_año="[CHECKBOX 16 PARA INDICAR AÑO DE SUSCRIPCIÓN DE LA SOLICITUD]"
    # firma="[VARIABLE 7 PARA COMPLETAR CON LA FIRMA DEL RECLAMANTE]"


    path_archivo=manipular_archivos.path_carpeta_actual() + r"\ingresos superiores.pdf"

    archivo_pdf=pdf_modulo.crear_pdf(margen_derecha= 20, margen_arriba = 20, margen_izquierda= 20)
    # pdf_modulo.añadir_fuente(archivo_pdf,'Times','c:/windows/fonts/Times.ttf')

    pdf_modulo.fuente(archivo_pdf,tipo_fuente="Times",tamaño_fuente=13.0,estilo="B")
    pdf_modulo.celda_lineas(archivo_pdf=archivo_pdf,alineacion="J",texto="A LA DIRECCIÓN PROVINCIAL DE LA SEGURIDAD SOCIAL DE " +direccion_provincial.upper())
    pdf_modulo.nueva_linea(archivo_pdf,5)

    pdf_modulo.fuente(archivo_pdf,tipo_fuente="Times",tamaño_fuente=13.0,estilo="")
    pdf_modulo.celda_lineas(archivo_pdf=archivo_pdf,alineacion="J",texto="D./Dña. "+nombre+", con DNI/NIE N.° "+dni+", y domicilio a efectos de notificación en "+domicilio+", teléfono "+telefono+", y e-mail "+email+", ante la Dirección Provincial de "+direccion_provincial+" comparezco y, como mejor en derecho proceda, **DIGO:**")
    pdf_modulo.nueva_linea(archivo_pdf,5)

    pdf_modulo.fuente(archivo_pdf,tipo_fuente="Times",tamaño_fuente=13.0,estilo="")
    pdf_modulo.celda_lineas(archivo_pdf=archivo_pdf,alineacion="J",texto="Que el día "+str(notificacion_dia)+" [DISCLAIMER: Las reclamaciones presentadas posteriormente a este plazo podrían ser declaradas improcedentes. Si ha excedido dicho plazo se recomienda presentar una nueva solicitud a través del formulario electrónico proporcionado por la Seguridad Social("+link+")] de "+str(notificacion_mes)+" de "+str(notificacion_año)+" me ha sido notificada Resolución de "+str(RESOLUCIÓN_dia)+" de "+str(RESOLUCIÓN_mes)+" de "+str(RESOLUCIÓN_año)+", de esta Dirección Provincial de la Seguridad Social, dictada en expediente N.° "+str(numero_expediente)+" por la que se deniega la prestación de ingreso mínimo vital (IMV) aludiendo haberse identificado rentas, ingresos o patrimonio que contradicen la situación de vulnerabilidad económica señalada por quien suscribe que contravienen lo dispuesto en los artículos 10.1.b y 11 de la Ley 19/2021, de 20 de diciembre, por el que se establece el Ingreso Mínimo Vital (en adelante ''LIMV'').")
    pdf_modulo.nueva_linea(archivo_pdf,5)
    
    pdf_modulo.fuente(archivo_pdf,tipo_fuente="Times",tamaño_fuente=13.0,estilo="")
    pdf_modulo.celda_lineas(archivo_pdf=archivo_pdf,alineacion="J",texto="Que, por medio del presente escrito, dentro del plazo de los treinta días desde la notificación de la citada resolución, de conformidad con el apartado 2 del artículo 71 de la Ley 36/2011, de 10 de octubre, de la Jurisdicción Social, interpongo contra la misma **RECLAMACIÓN ADMINISTRATIVA PREVIA** con fundamento en las siguientes:")
    pdf_modulo.nueva_linea(archivo_pdf,5)

    pdf_modulo.fuente(archivo_pdf,tipo_fuente="Times",tamaño_fuente=13.0,estilo="B")
    pdf_modulo.celda_lineas(archivo_pdf=archivo_pdf,alineacion="J",texto="ALEGACIONES")
    pdf_modulo.nueva_linea(archivo_pdf,5)

    pdf_modulo.fuente(archivo_pdf,tipo_fuente="Times",tamaño_fuente=13.0,estilo="")
    pdf_modulo.celda_lineas(archivo_pdf=archivo_pdf,alineacion="J",texto="**PRIMERA.-** De acuerdo a lo dispuesto en el apartado 2 del artículo 10 LIMV, la situación de vulnerabilidad económica se apreciará cuando el promedio mensual del conjunto de ingresos y rentas anuales computables correspondientes al ejercicio anterior, en los términos establecidos en el artículo 20, sea inferior, al menos en 10 euros, a la cuantía mensual de la renta garantizada como IMV (1).")
    pdf_modulo.nueva_linea(archivo_pdf,5)

    pdf_modulo.fuente(archivo_pdf,tipo_fuente="Times",tamaño_fuente=13.0,estilo="")
    pdf_modulo.celda_lineas(archivo_pdf=archivo_pdf,alineacion="J",texto="**SEGUNDA.-** En el numeral 7 del artículo 21 LIMV se señala que los requisitos de ingreso y patrimonio establecidos para el acceso y mantenimiento del IMV, serán revisados conforme a la información que se recabe por medios telemáticos de la Agencia Estatal de Administración Tributaria, tomando como referencia la información que conste respecto del ejercicio anterior a aquel en el que se realiza la actividad de reconocimiento o control, o en su defecto, la información que conste más actualizada en dichas administraciones públicas.")
    pdf_modulo.nueva_linea(archivo_pdf,5)

    pdf_modulo.fuente(archivo_pdf,tipo_fuente="Times",tamaño_fuente=13.0,estilo="")
    pdf_modulo.celda_lineas(archivo_pdf=archivo_pdf,alineacion="J",texto="**TERCERA.-** Conforme puede apreciarse de los anexos del presente recurso, conformados por: ")
    pdf_modulo.nueva_linea(archivo_pdf,5)

    if impuesto==True:
        pdf_modulo.fuente(archivo_pdf,tipo_fuente="Times",tamaño_fuente=13.0,estilo="")
        pdf_modulo.celda_lineas(archivo_pdf=archivo_pdf,alineacion="J",texto=impuesto)
        pdf_modulo.nueva_linea(archivo_pdf,5)
    if saldo==True:
        pdf_modulo.fuente(archivo_pdf,tipo_fuente="Times",tamaño_fuente=13.0,estilo="")
        pdf_modulo.celda_lineas(archivo_pdf=archivo_pdf,alineacion="J",texto=saldo)
        pdf_modulo.nueva_linea(archivo_pdf,5)
    if sueldo==True:
        pdf_modulo.fuente(archivo_pdf,tipo_fuente="Times",tamaño_fuente=13.0,estilo="")
        pdf_modulo.celda_lineas(archivo_pdf=archivo_pdf,alineacion="J",texto=sueldo)
        pdf_modulo.nueva_linea(archivo_pdf,5)
    if patrimonio_renta==True:
        pdf_modulo.fuente(archivo_pdf,tipo_fuente="Times",tamaño_fuente=13.0,estilo="")
        pdf_modulo.celda_lineas(archivo_pdf=archivo_pdf,alineacion="J",texto=patrimonio_renta)
        pdf_modulo.nueva_linea(archivo_pdf,5)
    if patrimonio_incrementos==True:
        pdf_modulo.fuente(archivo_pdf,tipo_fuente="Times",tamaño_fuente=13.0,estilo="")
        pdf_modulo.celda_lineas(archivo_pdf=archivo_pdf,alineacion="J",texto=patrimonio_incrementos)
        pdf_modulo.nueva_linea(archivo_pdf,5)

        pdf_modulo.fuente(archivo_pdf,tipo_fuente="Times",tamaño_fuente=13.0,estilo="")
        pdf_modulo.celda_lineas(archivo_pdf=archivo_pdf,alineacion="J",texto="quien suscribe se encuentra en la situación de vulnerabilidad económica que precisamente protege la LIMV. ")
        pdf_modulo.nueva_linea(archivo_pdf,5)

        pdf_modulo.fuente(archivo_pdf,tipo_fuente="Times",tamaño_fuente=13.0,estilo="")
        pdf_modulo.celda_lineas(archivo_pdf=archivo_pdf,alineacion="J",texto="**CUARTA.-** Cabe precisar que de acuerdo a lo dispuesto en el numeral 8 del artículo 21 LIMV, en ningún caso será exigible al solicitante la acreditación de hechos, datos o circunstancias que la Administración de la Seguridad Social deba conocer por sí misma, tales como la situación del beneficiario en relación con el sistema de la Seguridad Social; o la percepción por los miembros de la unidad de convivencia de otra prestación económica que conste en el Registro de Prestaciones Sociales Públicas.")
        pdf_modulo.nueva_linea(archivo_pdf,5)

        pdf_modulo.fuente(archivo_pdf,tipo_fuente="Times",tamaño_fuente=13.0,estilo="")
        pdf_modulo.celda_lineas(archivo_pdf=archivo_pdf,alineacion="J",texto="**POR TODO LO EXPUESTO**, agradeceré que cumpliendo con la debida motivación que todo acto administrativo requiere para su validez conforme a lo establecido en el artículo 35 de la Ley 39/2015, de 1 de octubre, del Procedimiento Administrativo Común de las Administraciones Públicas, se sirvan demostrar con el detalle respectivo de qué forma quien suscribe no acredita la situación de vulnerabilidad económica que protege la RDL IMV, caso contrario, se dicte nueva resolución estimatoria, en la que anulando y dejando sin efecto la impugnada, me reconozca la prestación solicitada en cuantía de "+str(cantidad)+" euros.")
        pdf_modulo.nueva_linea(archivo_pdf,5)

        pdf_modulo.fuente(archivo_pdf,tipo_fuente="Times",tamaño_fuente=13.0,estilo="")
        pdf_modulo.celda_lineas(archivo_pdf=archivo_pdf,alineacion="J",texto="En "+provincia+", a "+str(SOLICITUD_dia)+" de "+str(SOLICITUD_mes)+" de "+str(SOLICITUD_año)+".")
        pdf_modulo.nueva_linea(archivo_pdf,5)

        pdf_modulo.fuente(archivo_pdf,tipo_fuente="Times",tamaño_fuente=13.0,estilo="")
        pdf_modulo.celda_lineas(archivo_pdf=archivo_pdf,alineacion="J",texto=firma)
        pdf_modulo.nueva_linea(archivo_pdf,5)



    pdf_modulo.guardar_pdf(archivo_pdf,path_archivo)
    pdf_modulo.mostrar_archivo(path_archivo)
    print("Fin")
def Vivienda_Habitual(direccion_provincial,nombre,dni,domicilio,telefono,email,notificacion_dia,notificacion_mes,notificacion_año,RESOLUCIÓN_dia,RESOLUCIÓN_mes,RESOLUCIÓN_año,link,numero_expediente,cantidad,provincia,SOLICITUD_dia,SOLICITUD_mes,SOLICITUD_año,firma,propiedad,residencia):
    # direccion_provincial="[CHECKBOX 1 PARA SELECCIONAR LA DIRECCIÓN PROVINCIAL DE LA SEGURIDAD SOCIAL A LA QUE SE DIRIGE LA RECLAMACIÓN]"
    # nombre="[VARIABLE 1: NOMBRES Y APELLIDOS DEL RECLAMANTE]"
    # dni="[VARIABLE 2: NÚMERO DE DOCUMENTO DE IDENTIFICACIÓN]"
    # domicilio="[VARIABLE 3: DOMICILIO]"
    # telefono="[VARIABLE 4: TELÉFONO]"
    # email="[VARIABLE 5: DIRECCIÓN DE CORREO ELECTRÓNICO]"
    # notificacion_dia="[CHECKBOX 2 PARA INDICAR DÍA DE NOTIFICACIÓN DE LA RESOLUCIÓN RECLAMADA]"
    # notificacion_mes="[CHECKBOX 3 PARA INDICAR MES DE NOTIFICACIÓN DE LA RESOLUCIÓN RECLAMADA]"
    # notificacion_año="[CHECKBOX 4 PARA INDICAR AÑO DE NOTIFICACIÓN DE LA RESOLUCIÓN RECLAMADA]"
    # RESOLUCIÓN_dia="[CHECKBOX 5 PARA INDICAR DÍA DE EMISIÓN DE LA RESOLUCIÓN RECLAMADA]"
    # RESOLUCIÓN_mes="[CHECKBOX 6 PARA INIDCAR MES DE EMISIÓN DE LA RESOLUCIÓN RECLAMADA]"
    # RESOLUCIÓN_año="[CHECKBOX 7 PARA INDICAR AÑO DE EMISIÓN DE LA RESOLUCIÓN RECLAMADA]"
    # numero_expediente="[VARIABLE 6: número de expediente con el que se tramita la solicitud de otorgamiento de IMV (que debe mostrarse referida en la resolución reclamada)]"
    link=r"https://identificacion.seg-social.es/?origen=imv&destino=https%3A%2F%2Fimv.seg-social.es%2F&representante=true"
    # checkbox_evidencias="[CHECKBOX  ADJUNTOS LAS SIGUIENTES ALTERNATIVAS DE EVIDENCIAS: 1.- Escrituras de la propiedad / 2.- Certificado de residencia /"
    # cantidad=100
    # provincia="[CHECKBOX 13 PARA SELECCIONAR LA PROVINCIA]"
    # SOLICITUD_dia="[CHECKBOX 14 PARA INDICAR DÍA DE SUSCRIPCIÓN DE LA SOLICITUD]"
    # SOLICITUD_mes="[CHECKBOX 15 PARA INDICAR MES DE SUSCRIPCIÓN DE LA SOLICITUD]"
    # SOLICITUD_año="[CHECKBOX 16 PARA INDICAR AÑO DE SUSCRIPCIÓN DE LA SOLICITUD]"
    # firma="[VARIABLE 7 PARA COMPLETAR CON LA FIRMA DEL RECLAMANTE]"

    path_archivo=manipular_archivos.path_carpeta_actual() + r"\Vivienda Habitual.pdf"

    archivo_pdf=pdf_modulo.crear_pdf(margen_derecha= 20, margen_arriba = 20, margen_izquierda= 20)
    # pdf_modulo.añadir_fuente(archivo_pdf,'Times','c:/windows/fonts/Times.ttf')

    pdf_modulo.fuente(archivo_pdf,tipo_fuente="Times",tamaño_fuente=13.0,estilo="B")
    pdf_modulo.celda_lineas(archivo_pdf=archivo_pdf,alineacion="J",texto="A LA DIRECCIÓN PROVINCIAL DE LA SEGURIDAD SOCIAL DE "+direccion_provincial)
    pdf_modulo.nueva_linea(archivo_pdf,5)

    pdf_modulo.fuente(archivo_pdf,tipo_fuente="Times",tamaño_fuente=13.0,estilo="")
    pdf_modulo.celda_lineas(archivo_pdf=archivo_pdf,alineacion="J",texto="D./Dña. "+nombre+", con DNI/NIE N.° "+dni+", y domicilio a efectos de notificación en "+domicilio+", teléfono "+telefono+", y e-mail "+email+", ante la Dirección Provincial de "+direccion_provincial+" comparezco y, como mejor en derecho proceda, **DIGO:**")
    pdf_modulo.nueva_linea(archivo_pdf,5)

    pdf_modulo.fuente(archivo_pdf,tipo_fuente="Times",tamaño_fuente=13.0,estilo="")
    pdf_modulo.celda_lineas(archivo_pdf=archivo_pdf,alineacion="J",texto="Que el día "+str(notificacion_dia)+" [DISCLAIMER: Las reclamaciones presentadas posteriormente a este plazo podrían ser declaradas improcedentes. Si ha excedido dicho plazo se recomienda presentar una nueva solicitud a través del formulario electrónico proporcionado por la Seguridad Social("+link+")] de "+str(notificacion_mes)+" de "+str(notificacion_año)+" me ha sido notificada Resolución de "+str(RESOLUCIÓN_dia)+" de "+str(RESOLUCIÓN_mes)+" de "+str(RESOLUCIÓN_año)+", de esta Dirección Provincial de la Seguridad Social, dictada en expediente N.° "+str(numero_expediente)+" por la que se deniega la prestación de ingreso mínimo vital (IMV) aludiendo haberse patrimonio que contradicen la situación de vulnerabilidad económica señalada por quien suscribe que contravienen lo dispuesto en los artículos 10.1.b y 11 de la Ley 19/2021, de 20 de diciembre, por el que se establece el Ingreso Mínimo Vital (en adelante ''IMV'').")
    pdf_modulo.nueva_linea(archivo_pdf,5)

    pdf_modulo.fuente(archivo_pdf,tipo_fuente="Times",tamaño_fuente=13.0,estilo="")
    pdf_modulo.celda_lineas(archivo_pdf=archivo_pdf,alineacion="J",texto="Que, por medio del presente escrito, dentro del plazo de los treinta días desde la notificación de la citada resolución, de conformidad con el apartado 2 del artículo 71 de la Ley 36/2011, de 10 de octubre, de la Jurisdicción Social, interpongo contra la misma **RECLAMACIÓN ADMINISTRATIVA PREVIA** con fundamento en las siguientes:")
    pdf_modulo.nueva_linea(archivo_pdf,5)

    pdf_modulo.fuente(archivo_pdf,tipo_fuente="Times",tamaño_fuente=13.0,estilo="B")
    pdf_modulo.celda_lineas(archivo_pdf=archivo_pdf,alineacion="J",texto="ALEGACIONES")
    pdf_modulo.nueva_linea(archivo_pdf,5)

    pdf_modulo.fuente(archivo_pdf,tipo_fuente="Times",tamaño_fuente=13.0,estilo="")
    pdf_modulo.celda_lineas(archivo_pdf=archivo_pdf,alineacion="J",texto="**PRIMERA.-** De acuerdo a lo dispuesto en el apartado 2 del artículo 10 LIMV, la situación de vulnerabilidad económica se apreciará cuando el promedio mensual del conjunto de ingresos y rentas anuales computables correspondientes al ejercicio anterior, en los términos establecidos en el artículo 20, sea inferior, al menos en 10 euros, a la cuantía mensual de la renta garantizada como IMV (1).")
    pdf_modulo.nueva_linea(archivo_pdf,5)

    pdf_modulo.fuente(archivo_pdf,tipo_fuente="Times",tamaño_fuente=13.0,estilo="")
    pdf_modulo.celda_lineas(archivo_pdf=archivo_pdf,alineacion="J",texto="**SEGUNDA.-** En el numeral 7 del artículo 21 LIMV se señala que los requisitos de ingreso y patrimonio establecidos para el acceso y mantenimiento del IMV, serán revisados conforme a la información que se recabe por medios telemáticos de la Agencia Estatal de Administración Tributaria, tomando como referencia la información que conste respecto del ejercicio anterior a aquel en el que se realiza la actividad de reconocimiento o control, o en su defecto, la información que conste más actualizada en dichas administraciones públicas.")
    pdf_modulo.nueva_linea(archivo_pdf,5)

    pdf_modulo.fuente(archivo_pdf,tipo_fuente="Times",tamaño_fuente=13.0,estilo="")
    pdf_modulo.celda_lineas(archivo_pdf=archivo_pdf,alineacion="J",texto="**TERCERA.-** Al momento de analizar mi patrimonio para determinar que el mismo supera el umbral establecido por la legislación vigente para aplicar para el IMV se tuvo en cuenta mi vivienda habitual, hecho que contraviene lo establecido en la Ley 19/2021, de 20 de diciembre la cual establece lo siguiente:\n\n       El patrimonio no societario neto incluye el valor\n       b) de los activos no societarios y se descuenta el pasivo no societario que tuviera\n       asociado.\n       Los activos no societarios son la suma de los siguientes conceptos:\n       Los inmuebles, **excluida la vivienda habitual.**\n\nConforme puede apreciarse de los anexos del presente recurso, conformados por: "+propiedad+", "+residencia+"; quien suscribe se encuentra en la situación de vulnerabilidad económica que precisamente protege el RDL IMV. ")
    pdf_modulo.nueva_linea(archivo_pdf,5)

    pdf_modulo.fuente(archivo_pdf,tipo_fuente="Times",tamaño_fuente=13.0,estilo="")
    pdf_modulo.celda_lineas(archivo_pdf=archivo_pdf,alineacion="J",texto="**CUARTA.-** Cabe precisar que de acuerdo a lo dispuesto en el numeral 8 del artículo 21 LIMV, en ningún caso será exigible al solicitante la acreditación de hechos, datos o circunstancias que la Administración de la Seguridad Social deba conocer por sí misma, tales como la situación del beneficiario en relación con el sistema de la Seguridad Social; o la percepción por los miembros de la unidad de convivencia de otra prestación económica que conste en el Registro de Prestaciones Sociales Públicas.")
    pdf_modulo.nueva_linea(archivo_pdf,5)

    pdf_modulo.fuente(archivo_pdf,tipo_fuente="Times",tamaño_fuente=13.0,estilo="")
    pdf_modulo.celda_lineas(archivo_pdf=archivo_pdf,alineacion="J",texto="**POR TODO LO EXPUESTO,** agradeceré que cumpliendo con la debida motivación que todo acto administrativo requiere para su validez conforme a lo establecido en el artículo 35 de la Ley 39/2015, de 1 de octubre, del Procedimiento Administrativo Común de las Administraciones Públicas, se sirvan demostrar con el detalle respectivo de qué forma quien suscribe no acredita la situación de vulnerabilidad económica que protege la RDL IMV, caso contrario, se dicte nueva resolución estimatoria, en la que anulando y dejando sin efecto la impugnada, me reconozca la prestación solicitada en cuantía de "+str(cantidad)+" euros.")
    pdf_modulo.nueva_linea(archivo_pdf,5)

    pdf_modulo.fuente(archivo_pdf,tipo_fuente="Times",tamaño_fuente=13.0,estilo="")
    pdf_modulo.celda_lineas(archivo_pdf=archivo_pdf,alineacion="J",texto="En "+provincia+", a "+str(SOLICITUD_dia)+" de "+str(SOLICITUD_mes)+" de "+str(SOLICITUD_año)+".")
    pdf_modulo.nueva_linea(archivo_pdf,5)

    pdf_modulo.fuente(archivo_pdf,tipo_fuente="Times",tamaño_fuente=13.0,estilo="")
    pdf_modulo.celda_lineas(archivo_pdf=archivo_pdf,alineacion="J",texto=firma)
    pdf_modulo.nueva_linea(archivo_pdf,5)

    pdf_modulo.guardar_pdf(archivo_pdf,path_archivo)
    pdf_modulo.mostrar_archivo(path_archivo)
    print("Fin")
def Rectificación_cuantía(direccion_provincial,nombre,dni,domicilio,telefono,email,notificacion_dia,notificacion_mes,notificacion_año,RESOLUCIÓN_dia,RESOLUCIÓN_mes,RESOLUCIÓN_año,numero_expediente,link,impuesto,saldo,sueldo,patrimonio_renta,patrimonio_incrementos,cantidad,provincia,SOLICITUD_dia,SOLICITUD_mes,SOLICITUD_año,firma):
    # direccion_provincial="[CHECKBOX 1 PARA SELECCIONAR LA DIRECCIÓN PROVINCIAL DE LA SEGURIDAD SOCIAL A LA QUE SE DIRIGE LA RECLAMACIÓN]"
    # nombre="[VARIABLE 1: NOMBRES Y APELLIDOS DEL RECLAMANTE]"
    # dni="[VARIABLE 2: NÚMERO DE DOCUMENTO DE IDENTIFICACIÓN]"
    # domicilio="[VARIABLE 3: DOMICILIO]"
    # telefono="[VARIABLE 4: TELÉFONO]"
    # email="[VARIABLE 5: DIRECCIÓN DE CORREO ELECTRÓNICO]"

    # notificacion_dia="[CHECKBOX 2 PARA INDICAR DÍA DE NOTIFICACIÓN DE LA RESOLUCIÓN RECLAMADA]"
    # notificacion_mes="[CHECKBOX 3 PARA INDICAR MES DE NOTIFICACIÓN DE LA RESOLUCIÓN RECLAMADA]"
    # notificacion_año="[CHECKBOX 4 PARA INDICAR AÑO DE NOTIFICACIÓN DE LA RESOLUCIÓN RECLAMADA]"
    # RESOLUCIÓN_dia="[CHECKBOX 5 PARA INDICAR DÍA DE EMISIÓN DE LA RESOLUCIÓN RECLAMADA]"
    # RESOLUCIÓN_mes="[CHECKBOX 6 PARA INIDCAR MES DE EMISIÓN DE LA RESOLUCIÓN RECLAMADA]"
    # RESOLUCIÓN_año="[CHECKBOX 7 PARA INDICAR AÑO DE EMISIÓN DE LA RESOLUCIÓN RECLAMADA]"
    # numero_expediente="[VARIABLE 6: número de expediente con el que se tramita la solicitud de otorgamiento de IMV (que debe mostrarse referida en la resolución reclamada)]"
    link=r"https://identificacion.seg-social.es/?origen=imv&destino=https%3A%2F%2Fimv.seg-social.es%2F&representante=true"

    # impuesto="CHECKBOX 8:  La declaración del Impuesto sobre la Renta de Personas Físicas correspondiente al ejercicio anterior "
    # saldo="CHECKBOX 9: Los estados de cuenta bancaria correspondientes al ejercicio anterior "
    # sueldo="CHECKBOX 10: Los documentos de pago emitidos por mi empleador durante el ejercicio anterior "
    # patrimonio_renta="CHECKBOX 11: Información del registro mercantil sobre inexistencia de patrimonio cuya valoración equivale o supera tres veces la cuantía correspondiente de renta garantizada por el IMV (cuando se trate de beneficiario individual)"
    # patrimonio_incrementos="CHECKBOX 12: Información del registro mercantil sobre inexistencia de patrimonio cuya valoración equivale o supera la cuantía resultante de aplicar la escala de incrementos que figura en el Anexo II de la LIMV (cuando el beneficiario sea una unidad de convivencia)"
    # cantidad=100

    # provincia="[CHECKBOX 13 PARA SELECCIONAR LA PROVINCIA]"
    # SOLICITUD_dia="[CHECKBOX 14 PARA INDICAR DÍA DE SUSCRIPCIÓN DE LA SOLICITUD]"
    # SOLICITUD_mes="[CHECKBOX 15 PARA INDICAR MES DE SUSCRIPCIÓN DE LA SOLICITUD]"
    # SOLICITUD_año="[CHECKBOX 16 PARA INDICAR AÑO DE SUSCRIPCIÓN DE LA SOLICITUD]"
    # firma="[VARIABLE 7 PARA COMPLETAR CON LA FIRMA DEL RECLAMANTE]"

    path_archivo=manipular_archivos.path_carpeta_actual() + r"\Rectificación cuantía.pdf"
    archivo_pdf=pdf_modulo.crear_pdf(margen_derecha= 20, margen_arriba = 20, margen_izquierda= 20)

    pdf_modulo.fuente(archivo_pdf,tipo_fuente="Times",tamaño_fuente=13.0,estilo="B")
    pdf_modulo.celda_lineas(archivo_pdf=archivo_pdf,alineacion="J",texto="A LA DIRECCIÓN PROVINCIAL DE LA SEGURIDAD SOCIAL DE "+direccion_provincial)
    pdf_modulo.nueva_linea(archivo_pdf,5)

    pdf_modulo.fuente(archivo_pdf,tipo_fuente="Times",tamaño_fuente=13.0,estilo="")
    pdf_modulo.celda_lineas(archivo_pdf=archivo_pdf,alineacion="J",texto="D./Dña. "+nombre+", con DNI/NIE N.° "+dni+", y domicilio a efectos de notificación en "+domicilio+", teléfono "+telefono+", y e-mail "+email+", ante la Dirección Provincial de "+direccion_provincial+" comparezco y, como mejor en derecho proceda, **DIGO:**")
    pdf_modulo.nueva_linea(archivo_pdf,5)

    pdf_modulo.fuente(archivo_pdf,tipo_fuente="Times",tamaño_fuente=13.0,estilo="")
    pdf_modulo.celda_lineas(archivo_pdf=archivo_pdf,alineacion="J",texto="Que el día "+str(notificacion_dia)+" [DISCLAIMER: Las reclamaciones presentadas posteriormente a este plazo podrían ser declaradas improcedentes. Si ha excedido dicho plazo se recomienda presentar una nueva solicitud a través del formulario electrónico proporcionado por la Seguridad Social ("+link+")] de "+str(notificacion_mes)+" de "+str(notificacion_año)+" me ha sido notificada Resolución de "+str(RESOLUCIÓN_dia)+" de "+str(RESOLUCIÓN_mes)+" de "+str(RESOLUCIÓN_año)+", de esta Dirección Provincial de la Seguridad Social, dictada en expediente N.° "+str(numero_expediente)+" por la que se estima la prestación de ingreso mínimo vital (IMV) en una cuantía que no se corresponde con verdadera la situación de vulnerabilidad del beneficiario, contraviniendo a lo dispuesto en los artículos 10.1.b, 11 y 13 de la Ley 19/2021, de 20 de diciembre, por el que se establece el Ingreso Mínimo Vital (en adelante ''IMV''.")
    pdf_modulo.nueva_linea(archivo_pdf,5)

    pdf_modulo.fuente(archivo_pdf,tipo_fuente="Times",tamaño_fuente=13.0,estilo="")
    pdf_modulo.celda_lineas(archivo_pdf=archivo_pdf,alineacion="J",texto="Que, por medio del presente escrito, dentro del plazo de los treinta días desde la notificación de la citada resolución, de conformidad con el apartado 2 del artículo 71 de la Ley 36/2011, de 10 de octubre, de la Jurisdicción Social, interpongo contra la misma **RECLAMACIÓN ADMINISTRATIVA PREVIA** con fundamento en las siguientes:")
    pdf_modulo.nueva_linea(archivo_pdf,5)

    pdf_modulo.fuente(archivo_pdf,tipo_fuente="Times",tamaño_fuente=13.0,estilo="B")
    pdf_modulo.celda_lineas(archivo_pdf=archivo_pdf,alineacion="J",texto="ALEGACIONES")
    pdf_modulo.nueva_linea(archivo_pdf,5)

    pdf_modulo.fuente(archivo_pdf,tipo_fuente="Times",tamaño_fuente=13.0,estilo="")
    pdf_modulo.celda_lineas(archivo_pdf=archivo_pdf,alineacion="J",texto="**PRIMERA.-** De acuerdo a lo dispuesto en el apartado 2 del artículo 10 LIMV, la situación de vulnerabilidad económica se apreciará cuando el promedio mensual del conjunto de ingresos y rentas anuales computables correspondientes al ejercicio anterior, en los términos establecidos en el artículo 20, sea inferior, al menos en 10 euros, a la cuantía mensual de la renta garantizada como IMV (1).")
    pdf_modulo.nueva_linea(archivo_pdf,5)

    pdf_modulo.fuente(archivo_pdf,tipo_fuente="Times",tamaño_fuente=13.0,estilo="")
    pdf_modulo.celda_lineas(archivo_pdf=archivo_pdf,alineacion="J",texto="**SEGUNDA.-** En el numeral 7 del artículo 21 LIMV se señala que los requisitos de ingreso y patrimonio establecidos para el acceso y mantenimiento del IMV, serán revisados conforme a la información que se recabe por medios telemáticos de la Agencia Estatal de Administración Tributaria, tomando como referencia la información que conste respecto del ejercicio anterior a aquel en el que se realiza la actividad de reconocimiento o control, o en su defecto, la información que conste más actualizada en dichas administraciones públicas.")
    pdf_modulo.nueva_linea(archivo_pdf,5)

    pdf_modulo.fuente(archivo_pdf,tipo_fuente="Times",tamaño_fuente=13.0,estilo="")
    pdf_modulo.celda_lineas(archivo_pdf=archivo_pdf,alineacion="J",texto="**TERCERA.-** Conforme puede apreciarse de los anexos del presente recurso, conformados por: "+impuesto+""+saldo+" "+sueldo+" "+patrimonio_renta+" "+patrimonio_incrementos+"; quien suscribe se encuentra en la situación de vulnerabilidad económica que precisamente protege la LIMV, correspondiéndole la prestación solicitada en cuantía de "+str(cantidad)+" euros. ")
    pdf_modulo.nueva_linea(archivo_pdf,5)

    pdf_modulo.fuente(archivo_pdf,tipo_fuente="Times",tamaño_fuente=13.0,estilo="")
    pdf_modulo.celda_lineas(archivo_pdf=archivo_pdf,alineacion="J",texto="**CUARTA.-** Cabe precisar que de acuerdo a lo dispuesto en el numeral 8 del artículo 21 LIMV, en ningún caso será exigible al solicitante la acreditación de hechos, datos o circunstancias que la Administración de la Seguridad Social deba conocer por sí misma, tales como la situación del beneficiario en relación con el sistema de la Seguridad Social; o la percepción por los miembros de la unidad de convivencia de otra prestación económica que conste en el Registro de Prestaciones Sociales Públicas.")
    pdf_modulo.nueva_linea(archivo_pdf,5)

    pdf_modulo.fuente(archivo_pdf,tipo_fuente="Times",tamaño_fuente=13.0,estilo="")
    pdf_modulo.celda_lineas(archivo_pdf=archivo_pdf,alineacion="J",texto="**POR TODO LO EXPUESTO,** agradeceré que cumpliendo con la debida motivación que todo acto administrativo requiere para su validez conforme a lo establecido en el artículo 35 de la Ley 39/2015, de 1 de octubre, del Procedimiento Administrativo Común de las Administraciones Públicas, se sirvan demostrar con el detalle respectivo de qué forma quien suscribe acredita la situación de vulnerabilidad económica que protege la LIMV y se dicte nueva resolución estimatoria en la que se reconozca la prestación solicitada en cuantía de "+str(cantidad)+" euros, rectificando la presente resolución recurrida.")
    pdf_modulo.nueva_linea(archivo_pdf,5)




    pdf_modulo.fuente(archivo_pdf,tipo_fuente="Times",tamaño_fuente=13.0,estilo="")
    pdf_modulo.celda_lineas(archivo_pdf=archivo_pdf,alineacion="J",texto="En "+provincia+", a "+str(SOLICITUD_dia)+" de "+str(SOLICITUD_mes)+" de "+str(SOLICITUD_año)+".")
    pdf_modulo.nueva_linea(archivo_pdf,5)

    pdf_modulo.fuente(archivo_pdf,tipo_fuente="Times",tamaño_fuente=13.0,estilo="")
    pdf_modulo.celda_lineas(archivo_pdf=archivo_pdf,alineacion="J",texto=firma)
    pdf_modulo.nueva_linea(archivo_pdf,5)

    pdf_modulo.guardar_pdf(archivo_pdf,path_archivo)
    pdf_modulo.mostrar_archivo(path_archivo)
    import webbrowser
    webbrowser.open_new_tab(path_archivo)
    print("Fin")

# Ingresos_Superiores()
# Vivienda_Habitual()
# Rectificación_cuantía()

# pass