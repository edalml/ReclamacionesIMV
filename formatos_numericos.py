modulo = "formatos_numericos"
from random import randrange
import manipulacion_cadenas
import datetime

def cambiar_comas_a_puntos(numero):
    cadena=str(numero)
    return cadena.replace('.', '').replace(',', '.')
def cambiar_puntos_a_comas(numero):
    cadena=str(numero)
    return cadena.replace(',', '').replace('.', ',')
def es_texto(cadena): 
    
    return isinstance(cadena, str) #float,int,bool,str
def es_bytes(cadena): 
   if str(type(cadena)).find("bytes") != -1:
       return True
   else:
       return False
def es_un_int(cadena):  
    
    return isinstance(cadena, int) #float,int,bool,str
def es_un_float(cadena):  
    
    return isinstance(cadena, float) #float,int,bool,str
def es_un_bool(cadena):  
    
    return isinstance(cadena, bool) #float,int,bool,str
def es_una_lista(cadena):  
    return isinstance(cadena, list) #float,int,bool,str
def es_una_list_of_list(lista):
    return any(isinstance(el, list) for el in lista)
def es_un_numero(cadena,carateres_validos="0123456789.-"):
    try:
        # aux=set(str(cadena))
        # chars = set(carateres_validos)
        # vale=False
        # for x in aux:
        #     for z in chars:
        #         if z== x:
        #             vale=True
        #     if vale==False:
        #         return False
        #     else:
        #         vale=False
   
        # return True
        aux=set(str(cadena))
        for x in aux:
            if manipulacion_cadenas.encontrar_cadena(carateres_validos,x)==-1:
                return False
        return True
    except Exception as e:
        print('Error en manipulacion_cadenas.encontrar_cadena')
        print( e)
def que_type_es(valor):
    return str(type(valor))
def es_un_nan(valor):
    return not(valor==valor)
def numero_aleatorio(maximo=101 ,minimo=0,salto=1):
    #puede salir el 0 hasta maximo-1 el salto no puede ser decimal
    return randrange(minimo,maximo,salto)
def rellenar_de_ceros(numero,numero_de_ceros):#"0001"
    
    return str(numero).zfill(numero_de_ceros)
def redondear_numero(numero,decimales):#"0001"
    
    return round(numero, decimales)
def quitar_signo(numero):
    if numero <0:
        numero*= -1
    return numero
def datetime_to_string(fecha=""):
    try:
        if fecha=="":
            fecha=datetime.now().time()
        currentTime = str(fecha.year)+"-"+str( fecha.month)+"-"+str( fecha.day)+" "+str( fecha.hour)+":"+str( fecha.minute)+":"+str(fecha.second)
        return currentTime

    except Exception as e:
        print("Error en "+modulo+'datetime_to_string()')
        print(e)
def datetime_to_string_solo_fecha(fecha):
    try:
        currentTime = str(fecha.year)+"/"+str( fecha.month)+"/"+str( fecha.day)
        return currentTime

    except Exception as e:
        print("Error en "+modulo+'datetime_to_string()')
        print(e)
def bytes_to_string(text, encoding = 'utf-8'):

    return text.decode(encoding,'ignore')
def poner_puntos_al_numero(numero):
    import locale
    locale.setlocale(locale.LC_ALL,"")
    #'Italian_Italy.1252'
    return f"{numero:n}"#'1.000'
        