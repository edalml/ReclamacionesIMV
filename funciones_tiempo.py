modulo="funciones_tiempo"
from ctypes.wintypes import LONG
import time
import datetime as dt
import import_install
try:
    import dateutil
    import_install.actualizar_import_nueva_version('python-dateutil')
except ImportError:
    import_install.install_import('python-dateutil')
    import dateutil
from datetime import datetime,timedelta
from dateutil import parser
try:
    import pandas
    import_install.actualizar_import_nueva_version('pandas')
except ImportError:
    import_install.install_import('pandas')
    import pandas
from pandas._libs.tslibs.timestamps import Timestamp
import formatos_numericos

#CONSTANTES
variable_cronometro=""
#RUTINAS
def restar_horas(hora_inicio,hora_fin,medida="dias"): #start = time.time()
    diferencia = hora_fin - hora_inicio
    return diferencia
def crear_fecha(dias=0, horas=0, minutos=0, segundos=0, microsegundos=0, milisegundos=0,semanas=0):
    #ni meses ni años 
    return dt.timedelta(days=dias, hours=horas,minutes=minutos, seconds=segundos,microseconds=microsegundos,milliseconds=milisegundos,weeks=semanas)
def dar_forma_fecha(fecha,formato=r'%Y-%m-%d %H:%M:%S'):#%Y=2007 %y=07 r'%d/%m/%Y %H:%M' r'%Y-%m-%d %H:%M:%S' r'%Y-%m-%d %H:%M:%S.%f' r'%Y-%m-%d %H:%M:%S.%f%z'
    str_fecha=str(fecha)#%p AM/PM
    return datetime.strptime(str_fecha,formato)
def str_a_fecha(str_fecha,formato=r'%Y-%m-%d %H:%M:%S'):
    return parser.parse(str_fecha).utctimetuple()
def str_a_datetime(str_fecha,formato=r'%Y-%m-%d %H:%M:%S'):
    try:
        return datetime.strptime(str_fecha,formato)
    except Exception as e:
        print('Error en ' + modulo + '.str_a_datetime()')
        print(e)      
def int_to_datetime(numero,formato=r'%Y-%m-%d %H:%M:%S'):
    timestamp = datetime.fromtimestamp(numero)
    return(timestamp.strftime(formato))
def restar_horas_datetime(hora_inicio,hora_fin,medida="dias"): #start = time.time()
    diferencia = hora_fin - hora_inicio
    if medida=="dias":
        diferencia = diferencia / timedelta(days=1)
    elif medida=="microsegundos":
        diferencia = diferencia / timedelta(microseconds=1)
    elif medida=="segundos":
        diferencia = diferencia / timedelta(seconds=1)
    elif medida=="horas":
        diferencia = diferencia / timedelta(hours=1)
    return diferencia
def restar_dos_datetime_segundos(datetime_mayor,datetime_menor):
    if datetime_mayor>datetime_menor:
        return int((datetime_mayor - datetime_menor).total_seconds())
    else:
        return int((datetime_menor-datetime_mayor).total_seconds())
def restar_dos_datetime_dias(datetime_mayor,datetime_menor):
    try:
        return (datetime_mayor - datetime_menor).days
    except Exception as e:
        print('Error en ' + modulo + '.restar_dos_datetime_dias()')
        print(e)
def datetime_restar_a_la_fecha(fecha_datetime,dias=0,horas=0,minutos=0,segundos=0,semanas=0,microsegundos=0,milisegundos=0):
    nueva_fecha=fecha_datetime-crear_fecha(dias,horas,minutos,segundos,microsegundos,milisegundos,semanas)
    return nueva_fecha
def dame_la_hora_datetime(hora="",con_microsegundos=False):
    from datetime import time
    if hora=="":
        hora=datetime.now().time()
    # return datetime.now().time()
    if con_microsegundos==False:
        hora2=time(int(hora.hour), int(hora.minute), int(hora.second))#, microsecond=123456 ,int(hora.microsecond)
    else:
        hora2=time(int(hora.hour), int(hora.minute), int(hora.second),int(hora.microsecond))#, microsecond=123456 ,int(hora.microsecond)
    return hora2
def dame_la_hora_datetime_sin_microsecs():
    from datetime import time
    x=time(hour = dame_la_hora_datetime().hour, minute = dame_la_hora_datetime().minute, second = dame_la_hora_datetime().second)
    return x
def dame_la_fecha_y_hora_datetime():
    
    return datetime.now()
def dame_la_fecha_datetime(hora=""):
    if hora=="":
        hora=datetime.now()
    return hora.date()# datetime.date(hora).today()
def dame_la_hora_time():
    
    return time.localtime()
def dame_la_hora_time_numero():

    return time.time()
def time_para_access(fecha_time):
    fecha=str(fecha_time.tm_year)+"/"+str(fecha_time.tm_mon)+"/"+str(fecha_time.tm_mday)+" "+str(fecha_time.tm_hour)+":"+str(formatos_numericos.rellenar_de_ceros(fecha_time.tm_min,2))+":"+str(formatos_numericos.rellenar_de_ceros(fecha_time.tm_sec,2))
    return fecha
def fecha_para_access(fecha="",formato_fecha_str=r'%d/%m/%Y'):
    if fecha=="":
        fecha=dame_la_fecha_datetime()
    if str(type(fecha))== "<class 'datetime.date'>" or type(fecha) is datetime:# if type(fecha) is type(dame_la_fecha_datetime()):
        fecha_access=str(fecha.year)+"/"+str(formatos_numericos.rellenar_de_ceros(fecha.month,2))+"/"+str(formatos_numericos.rellenar_de_ceros(fecha.day,2))
    elif type(fecha)==time:
        fecha_access=str(fecha.year)+"/"+str(formatos_numericos.rellenar_de_ceros(fecha.month,2))+"/"+str(formatos_numericos.rellenar_de_ceros(fecha.day,2))
    elif str(type(fecha))=="<class 'str'>":
        fecha_access=dar_forma_fecha(fecha,formato_fecha_str)
        fecha_access=str(fecha_access.year)+"/"+str(formatos_numericos.rellenar_de_ceros(fecha_access.month,2))+"/"+str(formatos_numericos.rellenar_de_ceros(fecha_access.day,2))
    else:
        print(modulo,"fecha_para_access()",str(type(fecha)),"NO TENEMOS ESE TIPO")
    return fecha_access
def fecha_y_hora_para_access(fecha=""):
    if fecha=="":
        fecha=dame_la_fecha_y_hora_datetime()
    if type(fecha)==datetime:
        fecha_access=str(fecha.year)+"/"+str(fecha.month)+"/"+str(fecha.day)+" "+str(fecha.hour)+":"+str(formatos_numericos.rellenar_de_ceros(fecha.minute,2))+":"+str(formatos_numericos.rellenar_de_ceros(fecha.second,2))
    elif type(fecha)==time:
        fecha_access=str(fecha.hour)+"/"+str(formatos_numericos.rellenar_de_ceros(fecha.minute,2))+"/"+str(formatos_numericos.rellenar_de_ceros(fecha.second,2))
    elif type(fecha)==str:
        return fecha
    return fecha_access
def fecha_y_hora_para_path(fecha):
    if type(fecha)==datetime:
        fecha_access=str(fecha.year)+"-"+str(fecha.month)+"-"+str(fecha.day)+" "+str(fecha.hour)+"-"+str(formatos_numericos.rellenar_de_ceros(fecha.minute,2))+"-"+str(formatos_numericos.rellenar_de_ceros(fecha.second,2))
    elif type(fecha)==time:
        fecha_access=str(fecha.hour)+"-"+str(formatos_numericos.rellenar_de_ceros(fecha.minute,2))+"-"+str(formatos_numericos.rellenar_de_ceros(fecha.second,2))
    elif type(fecha)==str:
        return fecha
        
    return fecha_access
def fecha_y_hora_para_nombres_archivo(fecha="",con_milisegundos=False):
    if fecha=="":
        fecha=dame_la_fecha_y_hora_datetime()
    if type(fecha)==datetime:
        if con_milisegundos==False:
            fecha_access=str(fecha.year)+"-"+str(fecha.month)+"-"+str(fecha.day)+" "+str(fecha.hour)+"-"+str(formatos_numericos.rellenar_de_ceros(fecha.minute,2))+"-"+str(formatos_numericos.rellenar_de_ceros(fecha.second,2))
        else:
            fecha_access=str(fecha.year)+"-"+str(fecha.month)+"-"+str(fecha.day)+" "+str(fecha.hour)+"-"+str(formatos_numericos.rellenar_de_ceros(fecha.minute,2))+"-"+str(formatos_numericos.rellenar_de_ceros(fecha.second,2))+"-"+str(formatos_numericos.rellenar_de_ceros(fecha.microsecond,6))
    elif type(fecha)==time:
        fecha_access=str(fecha.hour)+"-"+str(formatos_numericos.rellenar_de_ceros(fecha.minute,2))+"-"+str(formatos_numericos.rellenar_de_ceros(fecha.second,2))
    elif type(fecha)==str:
        return fecha
        
    return fecha_access
def datetime_sumar_a_la_fecha(fecha_datetime="",dias=0,horas=0,minutos=0,segundos=0,semanas=0,microsegundos=0,milisegundos=0):
    if fecha_datetime=="":fecha_datetime=dame_la_fecha_y_hora_datetime()
    nueva_fecha=fecha_datetime+crear_fecha(dias,horas,minutos,segundos,microsegundos,milisegundos,semanas)
    return nueva_fecha
def cronometro(iniciar=True,variable=-1):#variable para tener varios cronometros en marcha
    #USO con mas de uno 
    # variable=funciones_tiempo.cronometro(True,"")
    # segundos_empleados=funciones_tiempo.cronometro(False,variable)
    global variable_cronometro
    if iniciar==True:
        if variable==-1:
            variable_cronometro=dame_la_fecha_y_hora_datetime()
        else:
            return dame_la_fecha_y_hora_datetime()
    else:
        if variable==-1:
            return restar_dos_datetime_segundos(dame_la_fecha_y_hora_datetime(),variable_cronometro)
        else:
            return restar_dos_datetime_segundos(dame_la_fecha_y_hora_datetime(),variable)
def dia_de_la_semana(fecha_datetime=""):#1-Monday 2-Tuesday 3-Wednesday 4-Thursday 5-Friday 6-Saturday 7-Sunday
    if fecha_datetime=="":
        fecha_datetime = dame_la_fecha_datetime()
    return fecha_datetime.isoweekday()
def nombre_del_mes(numero_mes):#1-Monday 2-Tuesday 3-Wednesday 4-Thursday 5-Friday 6-Saturday 7-Sunday
    numero_mes=int(numero_mes)
    if numero_mes==1:
        return "Enero"
    elif numero_mes==2:
        return "Febrero"
    elif numero_mes==3:
        return "Marzo"
    elif numero_mes==4:
        return "Abril"
    elif numero_mes==5:
        return "Mayo"
    elif numero_mes==6:
        return "Junio"
    elif numero_mes==7:
        return "Julio"
    elif numero_mes==8:
        return "Agosto"
    elif numero_mes==9:
        return "Septiembre"
    elif numero_mes==10:
        return "Octubre"
    elif numero_mes==11:
        return "Noviembre"
    elif numero_mes==12:
        return "Diciembre"
    else:
        return ""
    return fecha_datetime.isoweekday()
