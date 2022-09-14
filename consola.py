modulo="consola"
import sys
import time
import funciones_tiempo
import formatos_numericos
import import_install
import subprocess
try:
    import ctypes
    import_install.actualizar_import_nueva_version("ctypes")    
except ImportError:
    import_install.install_import('ctypes')
    import ctypes
import os

barra_progreso_hora_inicio=""#barra_progreso_hora_inicio=time.time()
barra_progreso_contador=0
barra_ultimo_progreso=0
original_stdout = sys.stdout

def barra_progreso(progreso, maximo, Texto='',actualizar_cada=0,misma_linea=True):
    try:
        global barra_progreso_hora_inicio,barra_progreso_contador,barra_ultimo_progreso
        refrescar=False
        if barra_progreso_hora_inicio=="" or progreso==0 or barra_ultimo_progreso>progreso:#resetea la hora de inicio
            barra_progreso_hora_inicio=time.time()
        if actualizar_cada==0:
            refrescar=True
        else:
            if barra_progreso_contador>=actualizar_cada:
                barra_progreso_contador=0
                refrescar=True
            if progreso==0:#para que actualica la primera vez
                refrescar=True
            barra_progreso_contador+=1
        if refrescar==True:
            porcentaje = round(100.0 * progreso / maximo, 2)
            diferencia=funciones_tiempo.restar_horas(barra_progreso_hora_inicio,time.time())
            if porcentaje<=0:
                queda=100
            else:
                queda=(100*diferencia)/porcentaje
            queda=queda-diferencia
            medida_tiempo="Segundos      "
            if queda>86400:
                queda=str(int(queda//86400))+":"+formatos_numericos.rellenar_de_ceros(int((queda%86400)/3600),2)
                medida_tiempo="Dias       "
            elif queda>3600:
                queda=str(int(queda//3600))+":"+formatos_numericos.rellenar_de_ceros(int((queda%3600)/60),2)
                medida_tiempo="Horas      "
            elif queda>60:
                queda=str(int(queda//60))+":"+formatos_numericos.rellenar_de_ceros(int(queda%60),2)
                medida_tiempo="Minutos   "
            else:
                queda=int(queda)
            #bar_len = 60
            #filled_len = int(round(bar_len * progreso / float(maximo)))

            #bar = '=' * filled_len + '-' * (bar_len - filled_len)
            if misma_linea==True:
                sys.stdout.write('%s %s %s %s %s %s %s %s %s\r' % (Texto,formatos_numericos.poner_puntos_al_numero(progreso),"de",formatos_numericos.poner_puntos_al_numero(maximo),"lleva:", str(formatos_numericos.redondear_numero(porcentaje,2))+'%',"Queda:",queda,medida_tiempo))
                sys.stdout.flush() 
            else:
                print(Texto,formatos_numericos.poner_puntos_al_numero(progreso),"de",formatos_numericos.poner_puntos_al_numero(maximo),"lleva:", str(formatos_numericos.redondear_numero(porcentaje,2))+'%',"Queda:",queda,medida_tiempo)
        if progreso>=maximo:
            print("")#la barra de progreso deja una linea escrita pero con el foco, asi no se sobreescribe con lo siguiente
            print(Texto,progreso,"de",maximo)
            barra_progreso_resetear()
        barra_ultimo_progreso=progreso
    except Exception as e:
        print('Error en '+modulo+'.barra_progreso(',progreso, maximo, Texto,")")
        print( e)
def barra_progreso_resetear():
    try:
        global barra_progreso_hora_inicio,barra_progreso_contador
        barra_progreso_hora_inicio=""
        barra_progreso_contador=0
    except Exception as e:
        print('Error en '+modulo+'.barra_progreso_resetear()')
        print( e)
def ajustar_print(lista_variables,lista_espacios):
    try:
        linea_final=""
        for dato in range(0,len(lista_variables)):
            aux_str=""
            if type(lista_variables[dato])!= str:
                aux_str+= str(lista_variables[dato])
            else:
                aux_str+= lista_variables[dato]
            while len(aux_str)<lista_espacios[dato]:
                aux_str+=" "
            if len(aux_str)>lista_espacios[dato]:
                aux_str=aux_str[0:lista_espacios[dato]]
            linea_final+=aux_str+" "
        print(linea_final)
    except Exception as e:
        print('Error en '+modulo+'.ajustar_print()')
        print( e)
def cambiar_nombre_ventana_consola(nombre_str):
    ctypes.windll.kernel32.SetConsoleTitleW(nombre_str)
def print_en_la_misma_linea(texto):
    sys.stdout.flush() 
    sys.stdout.write('%s \r' % (texto))
def borrar_ventana_consola(): #Definimos la función estableciendo el nombre que queramos
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")
def preguntar_al_usuario(pregunta):
    print(pregunta)
    return input()
def cargar_parametros_pasados_desde_el_bat():
    sys.argv
    dst = sys.argv
    return dst
def ejecutar_bat(path_bat):
    subprocess.call([path_bat])
    pass
def ejecutar_bat_Powershell(path_bat,oculto=False):
    completed = subprocess.run(["powershell", "-Command", path_bat], capture_output=oculto)
    return completed
def ejecutar_bat_ctypes(path_bat,oculto=False):
    completed =ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    return completed
def usuario_es_administrador():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
def arrancar_python_como_administrador():
    if usuario_es_administrador():
        # Code of your program here
        pass
    else:
        # Re-run the program with admin rights
        return ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
def iniciar_guardar_consola_a_archivo(path_archivo,modo="a"):#modo="a","w"
    sys.stdout = open(path_archivo, modo)
    stdout_copy=os.fdopen(os.dup(sys.stdout.fileno()))
def fin_guardar_consola_a_archivo():
    sys.stdout.close()
    sys.stdout = original_stdout
def print_por_pantalla_y_archivo(path_archivo,mensaje=[],modo="a",separador=" "):
    f= open(path_archivo, modo)
    print(*mensaje, file=f,sep=separador)
    print(*mensaje,sep=separador)
    f.close()