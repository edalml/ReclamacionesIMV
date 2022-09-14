modulo = "manipular_archivos"
import import_install
import manipulacion_cadenas
import os
try:
    import glob
    import_install.actualizar_import_nueva_version('glob')
except ImportError:
    import_install.install_import('glob')
    import glob
try:
    import gzip
    import_install.actualizar_import_nueva_version("gzip")    
except ImportError:
    import_install.install_import('gzip')
    import gzip
try:
    import shutil
    import_install.actualizar_import_nueva_version("shutil")    
except ImportError:
    import_install.install_import('shutil')
    import shutil
import formatos_numericos
try:
    import psutil
    import_install.actualizar_import_nueva_version("psutil")    
except ImportError:
    import_install.install_import('psutil')
    import psutil
import consola
import filecmp
try:
    import zlib
    import_install.actualizar_import_nueva_version("zlib")    
except ImportError:
    import_install.install_import('zlib')
    import zlib
try:
    import win32com
    import_install.actualizar_import_nueva_version("win32com")    
except ImportError:
    import_install.install_import('win32com')
    import win32com
import win32com.client as com

import consola
import filecmp
import formatos_numericos
import list_of_lists
import time


def MODOS_ABRIR_ARCHIVO():
    #r	Lectura
    #r+	Lectura/Escritura
    #w	Sobreescritura. Si no existe archivo se creará
    #a	Añadir. Escribe al final del archivo
    #b	Binario
    #+	Permite lectura/escritura simultánea
    #U	Salto de línea universal: win cr+lf, linux lf y mac cr
    #rb	Lectura binaria
    #wb	Sobreescritura binaria
    #r+b	Lectura/Escritura binaria
    pass
def crear_directorio(directorio):
    try:
        if existe_el_directorio(directorio)==False:
            os.mkdir(directorio)
    except Exception as e:
       print('Error en '+ modulo +'.crear_directorio()' )
       print(e)
def cargar_archivo(archivo,modo="r",codificado='utf-8'):#"rb" lo lee raw
    try:
        if modo=="rb":
            f = open (archivo,modo)
        else:
            f = open (archivo,modo, encoding=codificado)#'utf-8' 'utf-16' ‘latin-1’
        mensaje = f.read()
        f.close()
        return(mensaje)
    except Exception as e:
       print('Error en '+ modulo +'.cargar_archivo' )
       print(e)
def añadir_a_archivo(archivo,texto,modo="a"):
    try:
        f = open(archivo,modo, encoding='utf-8')
        texto=manipulacion_cadenas.remplazar_texto(texto,'\u0142',"")#\u0142 es un caracter que da error al guardar
        f.write(texto)
        f.close()
    except Exception as e:
       print('Error en '+ modulo +'.añadir_a_archivo' )
       print(e)
def leer_lineas_archivo(archivo,modo="r",codificado='utf-8'):
    try:
        f = open(archivo, modo, encoding=codificado)
        lineas = f.readlines()
        for x in range(len(lineas)):
            if lineas[x][len(lineas[x])-1:]=="\n":
                lineas[x]=lineas[x][:len(lineas[x])-1]
        f.close()
        return lineas
    except Exception as e:
       print('Error en '+ modulo +'.leer_lineas_archivo' )
       print(e)
def eliminar_archivo(archivo):
    try:
        os.remove(archivo)
    except Exception as e:
        print('Error en '+ modulo +'.eliminar_archivo' )
        print(e)
def copiar_archivo(origen,destino):
    try:
       shutil.copy(origen, destino)
    except Exception as e:
       print('Error en '+ modulo +'.copiar_archivo' )
       print(e)
def copiar_archivo_con_espera(archivo_origen,archivo_destino,tamaño_bloque=4096,mostrar_por_pantalla=False,tiempo_espera_segundos=1):
    f1 = open(archivo_origen, 'rb', tamaño_bloque)
    f2 = open(archivo_destino, 'wb', tamaño_bloque)
    cursor=0
    while True:
        datos_f1=f1.read(tamaño_bloque)
        if datos_f1!=b"":
            f2.write(datos_f1)
            cursor+=tamaño_bloque
        else:
            break
        if mostrar_por_pantalla==True and (cursor % (tamaño_bloque*100))==0:
            consola.print_en_la_misma_linea("Copiado: "+formatos_numericos.poner_puntos_al_numero(cursor))
        if tiempo_espera_segundos>0:
            time.sleep(tiempo_espera_segundos)
    f1.close()
    f2.close()
    if mostrar_por_pantalla==True:print("")
    return  True
def copiar_archivo_a_carpeta(origen,carpeta_destino):
    nombre_archivo=detalles_archivo(origen)[5][1]
    carpeta_destino=añadir_contrabarra_al_final_del_path(carpeta_destino)
    nombre_destino=carpeta_destino+nombre_archivo
    copiar_archivo(origen,nombre_destino)
def copiar_carpeta(origen,destino):
    shutil.copytree(origen, destino,dirs_exist_ok=True)
def mover_archivo_a_carpeta(origen,carpeta_destino):
    nombre_archivo=detalles_archivo(origen)[5][1]
    carpeta_destino=añadir_contrabarra_al_final_del_path(carpeta_destino)
    nombre_destino=carpeta_destino+nombre_archivo
    mover_archivo(origen,nombre_destino)
def mover_archivo(origen,destino):
    shutil.move(origen, destino,copy_function=shutil.copy2)#copia el metadata
def mover_archivo2(origen,destino,comprobar_byte_a_byte=False):
    copiar_archivo(origen,destino)
    if comparar_archivos(origen,destino,comprobar_byte_a_byte)==True:
        eliminar_archivo(origen)
        return True
    else:
        print("los archivos no son igules")    
        print(origen)
        print(destino)
def guardar_archivo(archivo,texto,modo="w"):
    try:
        f = open (archivo,modo, encoding='utf-8')
        #texto=remplazar_texto(texto,'\u0142',"")#\u0142 es un caracter que da error al guardar
        #texto=remplazar_texto(texto,'\u202a',"")#\u0142 es un caracter que da error al guardar
        f.write(texto)
        f.close()
    except Exception as e:
       print('Error en '+ modulo +'.guardar_archivo' )
       print(e)
def guardar_lista_archivo(archivo,lista,modo="w"):
    try:
        f = open (archivo,modo, encoding='utf-8')
        for x in lista:
            if formatos_numericos.que_type_es(x)=="<class 'datetime.datetime'>":
                f.write(str(x)+"\n")
            elif x[len(x)-1:]=="\n":
                f.write(str(x))
            else:
                f.write(str(x)+"\n")
        f.close()
    except Exception as e:
       print('Error en '+ modulo +'.guardar_lista_archivo' )
       print(e)
def guardar_list_of_list_archivo(archivo,lista,modo="w"):
    try:
        f = open (archivo,modo, encoding='utf-8')
        for linea in lista:
            text=""
            for item in linea:
                text+=str(item)+" , "
            f.write(text+chr(13))
        f.close()
    except Exception as e:
       print('Error en '+ modulo +'.guardar_lista_archivo' )
       print(e)
def pruebas_csharp(archivo):
    try:
        import re

        fp = open(archivo, 'rb').read()
        match = re.search(r'str = "(.*?)"', fp)

        print("Str: %s" % match.group(1))
    except Exception as e:
       print('Error en '+ modulo +'.pruebas_csharp' )
       print(e)
def existe_el_archivo(archivo):
    try:
        if os.path.isfile(archivo):
            return True
        else:
            return False
    except Exception as e:
       print('Error en '+ modulo +'.existe_el_archivo' )
       print(e)
def existe_el_directorio(directorio):
    try:
        if os.path.isdir(directorio):
            return True
        else:
            return False
    except Exception as e:
       print('Error en '+ modulo +'.existe_el_directorio' )
       print(e)
def eliminar_carpeta(path):
    shutil.rmtree(path)
def tamaño_carpeta(path):
    # folderPath = r"D:\Software\Downloads"
    fso = com.Dispatch("Scripting.FileSystemObject")
    folder = fso.GetFolder(path)
    return folder.Size
def listar_carpetas(path):
    subfolders = [ f.path for f in os.scandir(path) if f.is_dir() ]
    return subfolders
def listar_archivos(path,pattern=""):
    try:
        archivos=[]
        with os.scandir(path) as ficheros:
            for fichero in ficheros:
                if pattern!="":
                    if fichero.name.find(pattern)>0:
                        archivos.append(fichero.name)
                else:
                    archivos.append(fichero.name)
        return archivos
    except Exception as e:
       print('Error en '+ modulo +'.listar_archivos' )
       print(e)
def listar_archivos_en_carpeta_sistema(path_en_ingles,pattern=""):#path_en_ingles='C:/Users/home/downloads/*.torrent'
    try:
        path_en_ingles=añadir_contrabarra_al_final_del_path(path_en_ingles)
        path_en_ingles=cambiar_contrabarras_dobles_por_divididos(path_en_ingles)
        if pattern[0:1]!="*":
            pattern="*"+pattern
        return glob.glob(path_en_ingles+pattern)#list_of_files = glob.glob('C:/Users/home/Downloads/*')
    except Exception as e:
       print('Error en '+ modulo +'.listar_archivos_en_carpeta_sistema()' )
       print(e)
def dir_path(path,archivo_con_ruta=True):
    if existe_el_directorio(path)==True:
        archivos=[]
        try:
            with os.scandir(path) as ficheros:
                for fichero in ficheros:
                    if archivo_con_ruta==True:
                        archivos.append(fichero.path)
                    else:
                        archivos.append(fichero.name)
        except Exception as e:
            print('Error en '+ modulo +'.listar_archivos()' )
            print(e)
        return archivos
def buscar_archivos(path,pattern=""):
    archivos=dir_path(path)
    if archivos==None:
        return []
    contador=0
    while contador <len(archivos):
        nuevos_archivos=dir_path(archivos[contador])
        if nuevos_archivos!=None:
            for archivo in nuevos_archivos:
                archivos.append(archivo)
        contador+=1
    ficheros=[]
    for fichero in archivos:
        if pattern!="":
            if manipulacion_cadenas.que_type_es(pattern)=="<class 'list'>":
                for pat in pattern:
                    if fichero.lower().find(pat.lower())>-1:
                        ficheros.append(fichero)
            elif manipulacion_cadenas.que_type_es(pattern)=="<class 'str'>":
                if fichero.lower().find(pattern.lower())>-1:
                    ficheros.append(fichero)
        else:
            ficheros.append(fichero)
    return ficheros
def buscar_archivos_extensiones(path,extensiones=["."]):
    return buscar_archivos(path,extensiones)
    # archivos=dir_path(path)
    # if archivos==None:
    #     return []
    # contador=0
    # while contador <len(archivos):
    #     nuevos_archivos=dir_path(archivos[contador])
    #     if nuevos_archivos!=None:
    #         for archivo in nuevos_archivos:
    #             archivos.append(archivo)
    #     contador+=1
    # ficheros=[]
    # for fichero in archivos:
    #     if existe_el_archivo(fichero)==True:
    #         if list_of_lists.buscar_elemento(extensiones,detalles_archivo(fichero)[7][1].lower())==True:
    #             ficheros.append(fichero)
    # return ficheros
def descomprimir_archivo(path_archivo_comprimido,path_archivo_descomprimido):
    with gzip.open(path_archivo_comprimido, 'rb') as f:
        file_content = f.read()
        guardar_archivo(path_archivo_descomprimido,file_content,"wb")
def comprimir_archivo(path_archivo, compresion=9):
    try:
        print("Comprimiendo archivo:",path_archivo)
        content = cargar_archivo(path_archivo,codificado="latin-1")#'utf-8'
        content =content.encode()
        #content = content.encode()
        with gzip.open(path_archivo+".gz", 'wb', compresslevel=compresion) as f:
            f.write(content)
        print("Fin comprimiendo archivo:",path_archivo)
    except Exception as e:
       print('Error en '+ modulo +'.comprimir_archivo()' )
       print(e)
def comprimir_directorio(path_directorio,path_archivo_comprimido):
    shutil.make_archive(path_archivo_comprimido  , 'zip', path_directorio )
def path_archivo_ejecutable(resultado_con_nombre_archivo=True):
    try:
        #appdir = sys.argv[0]
        appdir =os.path.abspath(__file__)
        if resultado_con_nombre_archivo==False:
            appdir = os.path.dirname(__file__)
        #print(appdir)
        return appdir
    except Exception as e:
       print('Error en '+ modulo +'.path_archivo_ejecutable' )
       print(e)
def path_archivo(nombre_archivo):
    try:
        filename=os.path.abspath(nombre_archivo)
        return filename
    except Exception as e:
       print('Error en '+ modulo +'.path_archivo()' )
       print(e)
def path_carpeta_programa(filename):
    try:
        appdir = os.path.dirname(filename)
        ##print(appdir)
        return appdir
    except Exception as e:
       print('Error en '+ modulo +'.path_carpeta_programa' )
       print(e)
def path_del_python():
    import sys
    return sys.executable
def path_del_modulo(resultado_con_nombre_archivo=True):
    import os
    appdir =os.path.abspath(__file__)
    if resultado_con_nombre_archivo==False:
        appdir= os.path.dirname(__file__)
    return appdir
def path_del_modulo_nombre(modulo):
    # USO print(manipular_archivos.path_del_modulo2("./pruebas.py"))
    import os
    appdir =os.path.abspath(modulo)
    return appdir
def path_carpeta_actual():
    return os.path.abspath(os.getcwd())
def detalles_archivo(archivo):
    lista=[]
    if existe_el_archivo(archivo)==True:
        lista.append(["Tamaño",os.path.getsize(archivo)])#0
        lista.append(["Modificado",os.path.getmtime(archivo)])#1
        lista.append(["Creado",os.path.getctime(archivo)])#2
        lista.append(["Path",os.path.dirname(archivo)])#3
        lista.append(["Nombre completo",os.path.normpath(archivo)])#4
        lista.append(["Nombre archivo",os.path.basename(archivo)])#5
        lista.append(["Real path",os.path.realpath(archivo)])#6
        lista.append(["Extension",os.path.splitext(archivo)[1]])#7
        lista.append(["Path+Nombre sin extension",os.path.splitext(archivo)[0]])#8
        lista.append(["Nombre archivo sin extension",os.path.splitext(os.path.basename(archivo))[0]])#9
        lista.append(["Disco",os.path.splitdrive(archivo)[0]+"\\"])#10
    return lista
def espacio_libre(path_ruta):
    # Indicamos la ruta del disco.
    if existe_el_archivo(path_ruta)==True:
        path=detalles_archivo(path_ruta)[3][1]
    elif existe_el_directorio(path_ruta):
        path=path_ruta
    return psutil.disk_usage(path)
def comparar_archivos(archivo1,archivo2,comprobar_byte_a_byte=False):
    if detalles_archivo(archivo1)[0][1]==detalles_archivo(archivo2)[0][1]:
        if comprobar_byte_a_byte==True:
            return comparar_archivos_byte_a_byte(archivo1,archivo2)
        else:
            return True
    else:
        return False
def comparar_archivos_byte_a_byte(archivo1,archivo2,filecmp=False,cantidad_para_mostrar_por_pantalla=-1):
    if detalles_archivo(archivo1)[0][1]!=detalles_archivo(archivo2)[0][1]:#los tamaños no son iguales
        return False
    if filecmp==True:
        return filecmp.cmp(archivo1,archivo2,shallow=True)
    else:
        cantidad_para_actualizar=0
        tamaño_bloque=tamaño_del_cluster(detalles_archivo(archivo2)[10][1])*10
        iguales=True
        f1 = open(archivo1, 'rb', tamaño_bloque)
        f2 = open(archivo2, 'rb', tamaño_bloque)
        cursor=0
        while True:
            datos_f1=f1.read(tamaño_bloque)
            datos_f2=f2.read(tamaño_bloque)
            if datos_f1!=datos_f2:
                iguales=False
                break
            elif datos_f1==b"" and datos_f2==b"":#EOF los dos
                iguales=True
                break
            elif datos_f1==b"":
                iguales=False
                break
            elif datos_f2==b"":
                iguales=False
                break
            cursor+=tamaño_bloque
            if cantidad_para_mostrar_por_pantalla>0:
                if cantidad_para_actualizar<=cursor:
                    consola.print_en_la_misma_linea("Comparado: "+formatos_numericos.poner_puntos_al_numero(cursor))
                    cantidad_para_actualizar+=cantidad_para_mostrar_por_pantalla
        f1.close()
        f2.close()
        if cantidad_para_mostrar_por_pantalla>0:print("")#eliminamos la linea sobreescrita
        return iguales
def montar_imagen(archivo):
    import platform
    archivo="'"+archivo+"'"#por si hay espacios en la ruta
    if (platform.system()  == "Windows"):
        os.system('PowerShell Mount-DiskImage '+archivo) 
        # as mount operates only in powershell
    elif (platform.system() == "Linux"):
        os.system("mount /dev/dvdrom /mount-point")
def desmontar_imagen(archivo):
    import platform
    archivo="'"+archivo+"'"#por si hay espacios en la ruta
    if (platform.system()  == "Windows"):
        os.system('PowerShell DisMount-DiskImage '+archivo) 
        # as mount operates only in powershell
    elif (platform.system() == "Linux"):
        os.system("mount /dev/dvdrom /mount-point")
def añadir_contrabarra_al_final_del_path(path):
    if path[len(path)-2:]!="\\" and path[len(path)-1:]!="/":
        path+="/"
    return path
def cambiar_contrabarras_dobles_por_divididos(path):
    path=manipulacion_cadenas.remplazar_texto(path,"\\","/")
    return path
def calcular_crc(path_archivo):
    crc = 0
    with open(path_archivo, 'rb', 65536) as ins:
        for x in range(int((os.stat(path_archivo).st_size / 65536)) + 1):
            crc = zlib.crc32(ins.read(65536), crc)
    return '%08X' % (crc & 0xFFFFFFFF)
def arreglar_copia_archivo(archivo1,archivo2,mostrar_por_pantalla=False):
    tamaño_bloque=65536# (4.096 bytes) 
    bloques_corregidos=0 
    f1 = open(archivo1, 'rb', tamaño_bloque)
    f2 = open(archivo2, 'r+b', tamaño_bloque)
    while True:
        cursor=f1.tell()
        if mostrar_por_pantalla==True:
            consola.print_en_la_misma_linea(formatos_numericos.poner_puntos_al_numero(cursor))
        datos_f1=f1.read(tamaño_bloque)
        datos_f2=f2.read(tamaño_bloque)
        if datos_f1!=datos_f2:
            f2.seek(cursor)
            f2.write(datos_f1)
            bloques_corregidos+=1
        elif datos_f1==b"":#fin del archivo
           if datos_f2!=b"":#fin del archivo
               print("El archivo ",archivo2,"es mayor que ",archivo1,"habria que copiarlo entero para quitarle el final al archivo")
               #ZEROS = b'\x00' * 13
               #f.write(ZEROS)
           break
    f1.close()
    f2.close()
    if mostrar_por_pantalla==True:
        print("")
        print("Bloque corregidos",formatos_numericos.poner_puntos_al_numero(bloques_corregidos))
    return bloques_corregidos
def tamaño_del_cluster(ruta=u"C:\\"):
    import ctypes
    sectorsPerCluster = ctypes.c_ulonglong(0)
    bytesPerSector = ctypes.c_ulonglong(0)
    rootPathName = ctypes.c_wchar_p(ruta)

    ctypes.windll.kernel32.GetDiskFreeSpaceW(rootPathName,ctypes.pointer(sectorsPerCluster),ctypes.pointer(bytesPerSector),None,None,)
    return(sectorsPerCluster.value*bytesPerSector.value)
def renombrar_archivo(path_nobre_antiguo,path_nombre_nuevo):
    os.rename(path_nobre_antiguo,path_nombre_nuevo)
def espacio_libre_unidad_red(path):
    import win32com.client as com
    import win32com
    """ Return the TotalSize of a shared drive [GB]"""
    try:
        fso = win32com.client.Dispatch("Scripting.FileSystemObject")
        drv = fso.GetDrive(path)
        return drv.TotalSize/2**30
    except:
        return 0
def mostrar_archivo(path_archivo):
    os.startfile(path_archivo)