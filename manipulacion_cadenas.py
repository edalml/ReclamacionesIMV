modulo="manipulacion_cadenas"
import import_install
import unicodedata


def TEORIA_TEORIA_TEORIA_TEORIA():
    #TIPOS DE CADENA u"Unicode string" r"raw string" b
    pass
def remplazar_texto(cadena,caracter,sustituto,veces=0):
    try:
        cad=str(cadena)
        if veces>0:
            return cad.replace(caracter,sustituto,veces)
        else:
            return cad.replace(caracter,sustituto)
    except Exception as e:
        print('Error en manipulacion_cadenas.remplazar_texto ')
        print( e)
def remplazar_byte(cadena,byte,byte_sustituto):
    try:
        mybytes = '\xa0'.encode()
        bytes=string_to_bytes(cadena)
        # cadena = bytes.decode().encode('ascii',errors='ignore')
        pass
        for x in range(len(bytes)-1):
            if bytes[x]==byte:#byte.decode()#str(byte, 'utf-8'):
                bytes[x]=byte_sustituto
                pass
        return bytes
    except Exception as e:
        print("Error en "+modulo+".remplazar_byte()")
        print( e)

def partir_texto_en_lineas(cadena,caracter='\n'):
    lineas=[]
    cursor=0
    try:
        while cursor<len(cadena):
           x=encontrar_cadena(cadena,caracter,cursor)
           if x==-1:
                if len(cadena)>cursor:#añadimos el ultimo trozo de la cadena
                    lineas.append(cadena[cursor:len(cadena)])
                return lineas
           lineas.append(cadena[cursor:x])
           cursor=x+len(caracter)
        return lineas
    except Exception as e:
        print('Error en manipulacion_cadenas.partir_texto_en_lineas ')
        print( e)
def partir_texto_en_lineas_split(cadena,caracter='\n'):
    try:
        lineas=cadena.split(caracter)
        return lineas
    except Exception as e:
        print('Error en '+modulo+'.partir_texto_en_lineas_split()')
        print( e)
def encontrar_cadena(texto,busqueda,inicio=0,fin =-1):
    try:
        cadena=str(texto)
        fin =len(texto)
        x= cadena.find(busqueda,inicio,fin)
        return x 
    except Exception as e:
        print('Error en manipulacion_cadenas.encontrar_cadena')
        print( e)
def encontrar_cadena_entre_cadenas(texto,cadena_inicio,cadena_fin,inicio =0,fin =-1):
    try:
        if cadena_inicio!="":
            x= encontrar_cadena(texto,cadena_inicio,inicio,fin)
            if x!=-1:
                x+=len(cadena_inicio)
            else:#no encontro la primera palabra
                return "",fin
        else:
            x=0
        if cadena_fin!="":
            z= encontrar_cadena(texto,cadena_fin,x,fin)
        else:
            z=len(texto)
        if z==-1:#no encontro la segunda palabra
            return "",fin
        cadena=mid_cadena(texto,x,z)
        return cadena,z +len(cadena_fin)
    except Exception as e:
        print('Error en manipulacion_cadenas.encontrar_cadena')
        print( e)
def encontrar_cadena_bytes(texto,busqueda,inicio=0,fin =-1):
    try:
        b = busqueda.encode()
        x=texto.find(b)
        return x 
    except Exception as e:
        print("Error en " + modulo + ".encontrar_cadena_bytes")
        print( e)
def encontrar_cadena_entre_corchetes(texto,posicion_inicial,caracter_inicio,caracter_fin):
    x=posicion_inicial
    llaves_inicio,llaves=-1,0

    while x<len(texto):
        if texto[x]==caracter_inicio:
            llaves+=1
            if llaves_inicio==-1:
                llaves_inicio=x
        elif texto[x]==caracter_fin:
            llaves-=1
        if llaves==0 and llaves_inicio!=-1:
            trozo_entre_llaves=mid_cadena(texto,llaves_inicio,x+1)
            return trozo_entre_llaves
        x+=1
def encontrar_cadena_desde_cadena_hacia_atras(texto,busqueda,cantidad_caracteres,inicio=0):
    posicion=encontrar_cadena(texto,busqueda,inicio)
    if posicion!=None:
        posicion_inicial=(posicion-cantidad_caracteres)
        if posicion_inicial<0:
            posicion_inicial=0
        cadena=texto[posicion_inicial:posicion+len(busqueda)]
    return cadena,posicion
def encontrar_cadenas_de_numeros(descripcion,tamaño=4):
    cadena_resultado=""
    lista_cadenas=[]
    for char in descripcion:
        if char.isdigit()==True:
            cadena_resultado+=char
        else:
            if cadena_resultado!="":
                if len(cadena_resultado)>=tamaño or tamaño==-1:#las tamaño==-1 añade todas
                    lista_cadenas.append(cadena_resultado)
            cadena_resultado=""
    if len(cadena_resultado)>=tamaño:#la ultima por si termina con numeros
        lista_cadenas.append(cadena_resultado)
    return lista_cadenas
def encontrar_posiciones_cadena(texto,cadena):
    lista=[]
    posicion=0
    ultima_posicion=encontrar_cadena(texto,cadena,0)
    while posicion<ultima_posicion:
        lista.append(ultima_posicion)
        posicion=ultima_posicion
        ultima_posicion=encontrar_cadena(texto,cadena,posicion+1)
    return lista
def es_una_cadena_alfanumerica(cadena):
    try:
        aux=str(cadena)
        return aux.isalnum() 
    except Exception as e:
        print('Error en manipulacion_cadenas.encontrar_cadena')
        print( e)
def es_una_cadena_solo_letras(cadena):
    try:
        aux=str(cadena)
        return aux.isalpha() 
    except Exception as e:
        print('Error en manipulacion_cadenas.encontrar_cadena')
        print( e)
def es_una_cadena_solo_numeros(cadena):
    try:
        aux=str(cadena)
        return aux.isdigit() 
    except Exception as e:
        print('Error en manipulacion_cadenas.encontrar_cadena')
        print( e)
def es_una_cadena_solo_minusculas(cadena):
    try:
        aux=str(cadena)
        return aux.islower() 
    except Exception as e:
        print('Error en manipulacion_cadenas.encontrar_cadena')
        print( e)
def es_una_cadena_solo_mayusculas(cadena):
    try:
        aux=str(cadena)
        return aux.isupper() 
    except Exception as e:
        print('Error en manipulacion_cadenas.encontrar_cadena')
        print( e)
def es_una_cadena_solo_espacios(cadena):
    try:
        aux=str(cadena)
        return aux.isspace() 
    except Exception as e:
        print('Error en manipulacion_cadenas.encontrar_cadena')
        print( e)
def es_una_cadena_la_primera_mayuscula(cadena):
    try:
        aux=str(cadena)
        return aux.istitle() 
    except Exception as e:
        print('Error en manipulacion_cadenas.encontrar_cadena')
        print( e)
def es_una_cadena_float(cadena):
    try:
        aux=set(str(cadena))
        chars = set('0123456789.-')
        vale=False
        for x in aux:
            for z in chars:
                if z== x :
                    vale=True
            if vale==False:
                return False
            else:
                vale=False
   
        return True
    except Exception as e:
        print('Error en manipulacion_cadenas.encontrar_cadena')
        print( e)
def es_una_cadena_numero(cadena):
    try:
        aux=set(str(cadena))
        chars = set('0123456789.,')
        vale=False
        for x in aux:
            for z in chars:
                if z==x :
                    vale=True
                    break
            if vale==False:
                return False
            else:
                vale=False
 
        return True
    except Exception as e:
        print('Error en manipulacion_cadenas.es_una_cadena_numero')
        print( e)
def contiene_numeros(cadena):
    return any(char.isdigit() for char in cadena)
def eliminar_caracteres(cadena,caracteres):
    try:
        aux=str(cadena)
        for letra in caracteres:
            aux = remplazar_texto(aux,letra,'',0)
        return aux
    except Exception as e:
        print("Error en " + modulo + ".eliminar_caracteres")
        print( e)
def todo_mayusculas(cadena):
    
    return cadena.upper()
def todo_minusculas(cadena):
    
    return cadena.lower()
def mid_cadena(cadena,inicio,fin):
    try:
        return cadena[inicio:fin]
    except Exception as e:
        print('Error en '+modulo+'.mid_cadena(',cadena,inicio,fin,")")
        print( e)    
def quitar_espacios_der_y_izq(cadena):
    try:
        return cadena.strip()
    except Exception as e:
        print('Error en '+modulo+'.quitar_espacios_der_y_izq()')
        print( e)    
def quitar_todo_menos(cadena,caracteres_dejar):
    try:
        resultado=""
        vale=False
        for x in range(0,len(cadena)):
            for z in range(0,len(caracteres_dejar)):
                if cadena[x:x+1]==caracteres_dejar[z:z+1]:
                    resultado+=cadena[x:x+1]
                    break
   
        return resultado
    except Exception as e:
        print("Error en "+modulo+".encontrar_cadena()")
        print( e)
def insertar_cadena(cadena,cadena_a_insertar,posicion):
    cadena= cadena[:posicion] + cadena_a_insertar + cadena[posicion:]
    return cadena
def string_to_bytes(cadena):
    return  bytes(cadena, 'utf-8')
