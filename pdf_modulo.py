modulo = "pdf_modulo.py"
import import_install
try:
    import fpdf
    import_install.actualizar_import_nueva_version('fpdf')
except ImportError:
    import_install.install_import('fpdf')
    import fpdf
import manipulacion_imagenes
from fpdf import FPDF
import os

def crear_pdf(formato_pagina='A4',orientacion="P",medida='mm',auto_page_break=True,margen_derecha=25,margen_arriba=20,margen_izquierda= 25):
    pdf=FPDF(orientation=orientacion,unit=medida,format=formato_pagina)#orientation='L' orientation='P'  unit='pt''mm'
    fuente(pdf)
    ajustar_margenes(pdf,derecha=margen_derecha,arriba=margen_arriba,izquierda= margen_izquierda)
    añadir_pagina(pdf)
    pdf.set_auto_page_break(auto=auto_page_break,margin=10)
    return pdf
def añadir_pagina(pdf, igual_anterior = True,orientacion = '', formato = ''):#orientacion=P,L formato=A3,A4,A5,Letter,Legal,(width, height)
    if igual_anterior==True:
        pdf.add_page()
    else:
        pdf.add_page(orientation=orientacion)#),size=formato)#format=formato,orientation=orientacion
def guardar_pdf(pdf,path="./python.pdf"):
    pdf.output(path,'F')
def fuente(archivo_pdf,tipo_fuente="helvetica",tamaño_fuente=14.0,estilo=""):#estilo = 'B' "" italic underline
    try:
        archivo_pdf.set_font(tipo_fuente, estilo, tamaño_fuente)#tipo_fuente=Times arial
    except Exception as e:
       print('Error en '+ modulo +'.fuente()' )
       print(e)
def añadir_fuente(archivo_pdf,nombre="helvetica",path_fuente=''):#helvetica times arial path_fuente='c:/windows/fonts/helvetica.ttf'
    try:
        if path_fuente!="":
            archivo_pdf.add_font(nombre ,'', path_fuente , uni=True)
        else:
            archivo_pdf.add_font(nombre ,'', uni=True)
    except Exception as e:
       print('Error en '+ modulo +'.añadir_fuente()' )
       print(e)
def multiples_celdas(pdf,x=0,y=0,texto="Welcome to PythonGuides",alineacion="C", rellenar = False,marco=0):
    # pdf.multi_cell(w=y, h=x, txt=texto, align=alineacion,fill=rellenar, border = borde,ln=0)#align = 'R''C''L' J: justification  , fill = False , border = 1 , ln = 0
    pdf.multi_cell(w=x , h=y, txt=texto, border = marco,align= alineacion, fill = rellenar)
def añadir_imagen(pdf,path_imagen=r"D:\programacion\Python\bolsa\+caixa\imagenes\brokernow.png",pos_x=100,pos_y=100,ancho=0,alto=0,tipo="",enlace_url=""):
    pdf.image(path_imagen, x = pos_x, y = pos_y, w = ancho, h = alto, type = tipo, link = enlace_url)
def escribir(pdf,y=0,texto="",enlace_url=""):
    pdf.write(h=y, txt=texto,link = enlace_url)
def ajustar_color(pdf,rojo=0,verde=0,azul=0):
    pdf.set_text_color(rojo, verde, azul)
def ajustar_color_nombre(pdf,color):
    if color.lower()=="link":
        pdf.set_text_color(26,13,161)
    elif color.lower()=="negro":
        pdf.set_text_color(0,0,0)
    elif color.lower()=="rojo":
        pdf.set_text_color(255,0,0)
def ajustar_margenes(archivo_pdf,derecha=-1,arriba=10,izquierda=10):
    archivo_pdf.set_margins(left=izquierda, top=arriba, right=derecha)
def celda(archivo_pdf,ancho,alto,texto,borde=0,lineas=0,alineacion="C",relleno=False,link_url=""):#,centro=False,center=centro ,markdown=marca ,marca=False
    archivo_pdf.cell(w=ancho,h=alto,txt=texto,border=borde,ln=lineas,align=alineacion,fill=relleno,link=link_url)
def celda_ajustada(archivo_pdf,texto,borde=0,lineas=0,alineacion="C",relleno=False,link_url=""):#,centro=False,center=centro ,markdown=marca ,marca=False
    archivo_pdf.cell(w=archivo_pdf.get_string_width(texto),h=0,txt=texto,border=borde,ln=lineas,align=alineacion,fill=relleno,link=link_url)
def celda_lineas(archivo_pdf,anchura=0,altura=5,texto="Hola",borde=0,alineacion="J",relleno=False,con_estilo=True):#,centro=False,center=centro ,markdown=marca ,marca=False
    # ajustar margenes **bold**, __italics__, --underlined--
    try:
        archivo_pdf.multi_cell(w=anchura, h=altura, txt=texto, border =borde,align=alineacion, fill=relleno,markdown=con_estilo)
    except Exception as e:
       print('Error en '+ modulo +'.celda_lineas()' )
       print(e)
def tamaño_pagina(archivo_pdf):
    return [archivo_pdf.w,archivo_pdf.h]
def posicion_cursor(archivo_pdf):
    return [archivo_pdf.get_x(),archivo_pdf.get_y()]
# def posicion_cursor(archivo_pdf,salto=5):
#     archivo_pdf.ln(salto)
def posicionar_cursor_y(archivo_pdf,y=10):
    archivo_pdf.set_y(y)
def posicionar_cursor_x(archivo_pdf,x=10):
    archivo_pdf.set_x(x)
def posicionar_cursor_xy(archivo_pdf,x=10,y=10):
    archivo_pdf.set_xy(x,y)
def nueva_linea(archivo_pdf,tamaño_salto=""):
    archivo_pdf.ln(tamaño_salto)
def mostrar_archivo(path_archivo):
    os.startfile(path_archivo)
def lista_fonts(archivo_pdf):
    lista=[]
    for font in archivo_pdf.fonts:
        lista.append(font)
    return lista
def lista_core_fonts(archivo_pdf):
    lista=[]
    for font in archivo_pdf.core_fonts:
        lista.append([font,archivo_pdf.core_fonts[font]])
    return lista
def current_font(archivo_pdf):
    return archivo_pdf.current_font["name"]