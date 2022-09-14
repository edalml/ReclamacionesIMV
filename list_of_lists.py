modulo="list_of_lists"
#from operator import itemgetter
import sys
import copy

def eliminar_linea_de_lista(lista,posicion):
    try:
        lista.pop(posicion)
    except Exception as e:
        print("Error en "+modulo+".eliminar_linea_de_lista")
        print( e)
def eliminar_item_de_list_of_list(lista,item,posicion):
    try:
        lista.pop(item,posicion)
    except Exception as e:
        print("Error en "+modulo+".eliminar_linea_de_lista")
        print( e)
def eliminar_columna_de_list_of_list(lista,columna):
    try:
        [j.pop(columna) for j in lista]
    except Exception as e:
        print("Error en "+modulo+".eliminar_columna_de_list_of_list")
        print( e)
def eliminar_lista(lista):
    try:
        del lista
    except Exception as e:
        print("Error en "+modulo+".eliminar_lista()")
        print( e)
def eliminar_las_repetidas_list(lista):
    try:
        ordenar_lista(lista)
        x=0
        while x <len(lista)-1: 
            while x <len(lista)-1 and lista[x]==lista[x+1]:
                eliminar_linea_de_lista(lista,x)
            x+=1

    except Exception as e:
        print("Error en "+modulo+".eliminar_repetidas")
        print( e)
def eliminar_las_repetidas_list_of_list(lista,columna=0):
    try:
        ordenar_lista(lista,columna)
        x=0
        while x <len(lista)-1: 
            while x <len(lista)-1 and lista[x][columna]==lista[x+1][columna]:
                eliminar_linea_de_lista(lista,x)
            x+=1

    except Exception as e:
        print("Error en "+modulo+".eliminar_las_repetidas_list_of_list")
        print( e)
def ordenar_lista2(lista,num_columna=0,descendente=False):
    try:
        if num_columna==0:
            lista.sort(reverse = descendente)
        else:
            lista.sort(key = lambda i:i[num_columna],reverse = descendente)# sorted(lista,key=lambda x: x[num_columna])# sorted(lista,key=lambda x: float(x[num_columna])) #key=lambda x: float(x[5]) sorted(li,key=lambda x: x[1])
        return lista
    except Exception as e:
        print("Error en "+modulo+".ordenar_lista")
        print( e)
def ordenar_lista(lista,num_columna=0,descendente=False,num_columna_2=-1):
    try:
        if num_columna==0 and num_columna_2==-1:
            lista.sort(reverse = descendente)
        elif num_columna_2==-1:
            lista.sort(key = lambda i:i[num_columna],reverse = descendente)# sorted(lista,key=lambda x: x[num_columna])# sorted(lista,key=lambda x: float(x[num_columna])) #key=lambda x: float(x[5]) sorted(li,key=lambda x: x[1])
        elif num_columna_2!= -1:
            #lista.sort(key = lambda i:i[num_columna],reverse = descendente)# sorted(lista,key=lambda x: x[num_columna])# sorted(lista,key=lambda x: float(x[num_columna])) #key=lambda x: float(x[5]) sorted(li,key=lambda x: x[1])
            #s = sorted(my_list, key=lambda i: ( criteria_1(i), criteria_2(i) ), reverse=True)
            #b = sorted(a, key = lambda x: (-x[1], x[0]))
            lista = sorted(lista, key = lambda x: (x[num_columna], x[num_columna_2]))
            
            #lista.sort(key = lambda i:i[num_columna,num_columna_2],reverse = descendente)
        return lista
    except Exception as e:
        print("Error en "+modulo+".ordenar_lista")
        print( e)
def añadir_lista_a_lista_debajo(lista1,lista2):
    try:
        lista_resultado=[]
        lista_resultado=lista1
        if es_una_list_of_list(lista2)==True:
            for x in lista2:
                linea=[]
                for cell in x:
                    linea.append(cell)
                lista_resultado.append(linea)
        else:
            for x in lista2:
                lista_resultado.append(x)
        return lista_resultado
    except Exception as e:
        print("Error en "+modulo+".añadir_lista_a_lista_debajo")
        print( e)
def añadir_lista_a_lista_derecha(lista1,lista2):
    try:
        for x in range(0,len(lista1)):
            if len(lista2)>=x:
                lista1[x]=[lista1[x],lista2[x]]
        return lista1
    except Exception as e:
        print("Error en "+modulo+".añadir_lista_a_lista_debajo")
        print( e)
def añadir_lista_a_lista_derecha_por_id(lista1,lista2,col_id_1,col_id_2):
    try:
        lista_final=[]
        for x1 in range(0,len(lista1)):
            for x2 in range(0,len(lista2)):
                if lista1[x1][col_id_1]==lista2[x2][col_id_2]:
                    nueva_linea=[]
                    for r in range(0,len(lista1[x1])):
                        nueva_linea.append(lista1[x1][r])
                    for r in range(0,len(lista2[x2])):
                        if r!=col_id_2:#no añadimos el indice otra vez
                            nueva_linea.append(lista2[x2][r])
                    lista1[x1]=nueva_linea
                    lista_final.append(nueva_linea)
                    break
        return lista_final
    except Exception as e:
        print("Error en "+modulo+".añadir_lista_a_lista_debajo")
        print( e)
def añadir_linea_a_lista(lista,linea,posicion):
    try:
        lista.insert(posicion,linea)
    except Exception as e:
        print("Error en "+modulo+".crear_conexion")
        print( e)
def lista_eliminar_repetidos(lista):
    try:
        ordenar_lista(lista)
        x=0
        while x < len(lista):
            while x+1<len(lista) and lista[x]==lista[x+1]:
                lista.pop(x+1)
            x+=1
    except Exception as e:
        print("Error en "+modulo+".lista_eliminar_repetidos")
        print( e)
def cargar_columna(lista,columna=0,primera_fila=0,sin_nulas=True):
    datos_columna=[]
    for c in range(primera_fila,len(lista)):
        if sin_nulas==True:
            if lista[c][columna]!="":
                datos_columna.append(lista[c][columna])
        else:
            datos_columna.append(lista[c][columna])
    return datos_columna
def usos_de_la_lista(lista):
    try:
        return sys.getrefcount(lista)#=2 es que la lista no tiene mas referencias no se usa se puede borrar
    except Exception as e:
        print("Error en "+modulo+".usos_de_la_lista()")
        print( e)
def memoria_ocupada_por_lista(obj, seen=None):
    try:
        """Recursively finds size of objects"""
        size = sys.getsizeof(obj)
        if seen is None:
            seen = set()
        obj_id = id(obj)
        if obj_id in seen:
            return 0
        # Important mark as seen *before* entering recursion to gracefully handle
        # self-referential objects
        seen.add(obj_id)
        if isinstance(obj, dict):
            size += sum([memoria_ocupada_por_lista(v, seen) for v in obj.values()])
            size += sum([memoria_ocupada_por_lista(k, seen) for k in obj.keys()])
        elif hasattr(obj, '__dict__'):
            size += memoria_ocupada_por_lista(obj.__dict__, seen)
        elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
            size += sum([memoria_ocupada_por_lista(i, seen) for i in obj])
        return size
    except Exception as e:
        print("Error en "+modulo+".memoria_ocupada_por_lista()")
        print( e)
def copiar_lista(lista):
    return copy.deepcopy(lista)
def es_una_lista(lista):
    return isinstance(lista, list)
def es_una_list_of_list(lista):
    return any(isinstance(el, list) for el in lista)
def buscar_elemento(lista,elemento,minusculas=False):
    if minusculas==False:
        for ele in lista:
            if ele==elemento:
                return True
    else:
        for ele in lista:
            if ele.lower()==elemento.lower():
                return True
    return False 
def buscar_elemento_list_of_lists(lista,elemento,columna=0):
    for ele in lista:
        if ele[columna]==elemento:
            return True
    return False
def buscar_id_libre_lista(lista,mayor_que=0):
    lista=ordenar_lista(lista)
    encontrado=False
    libre=mayor_que
    while encontrado==False:
        encontrado=True
        for id in lista:
            if id==libre:
                libre+=1
                encontrado==False
                break
            elif id>libre:
                break
    return libre
def buscar_elementos_en_lista1_que_no_estan_lista2(lista1,lista2):
    diferentes = []
    for element in lista1:
        if element not in lista2:
            diferentes.append(element)
    return diferentes
