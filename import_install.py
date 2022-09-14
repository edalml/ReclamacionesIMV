#       USO
##importamos los modulos para que se instalen en python si no estan
Url_proyectos = "https://pypi.org" #para encontar los pip install
#import import_install
# try:
#     import selenium
#     import_install.actualizar_import_nueva_version('selenium')
# except ImportError:
#     import_install.install_import('selenium')
#     import selenium

modulo="import_install"
import sys
import pip #hay que instalarlo a mano: python -m pip install --upgrade pip
import wheel #hay que instalarlo a mano: python -m pip install --upgrade wheel
import requests #hay que instalarlo a mano: python -m pip install --upgrade requests
import setuptools
import subprocess
import sys
from importlib.metadata import version 
import manipulacion_cadenas

#VARIABLES
actualizar_imports_siempre =False #False True para que no actualize cada vez que arrancas el programa
def actualizar_import_nueva_version(paquete="pip",forzar_instalacion=False):
    try:
        if actualizar_imports_siempre==True or forzar_instalacion==True:
            paquete=averiguar_nombre_paquete(paquete)
            ver_instalada=version_import_instalada(paquete)
            ver_descargable=version_import_para_descargar(paquete)
            if ver_instalada!= ver_descargable:
                print("Version instalada de "+paquete +":",ver_instalada,"version descargable de:",ver_descargable)
                try:
                    install_import(paquete)
                except:
                    print("el paquete",paquete,"no existe")
            else:
                print("Version instalada de "+paquete +":",ver_instalada)
        
    except Exception as e:
        print(e,"Error en "+modulo+".actualizar_import_nueva_version()")
        install_import(paquete)       
def install_import_whl(package):
    try:
        subprocess.check_call([sys.executable,"pip","install", package]) #-o
    except Exception as e:
        print("Error en " + modulo + ".install_import_whl()")
        print(e)
def version_import_instalada(paquete="pip"):
    try:
        return version(paquete)
    except Exception as e:
        print(e,"Error en " + modulo + ".version_import_instalada()")
def version_import_para_descargar(paquete="pip"):
    response = requests.get(f'https://pypi.org/pypi/{paquete}/json')
    return response.json()['info']['version']
def install_import(package,version=""):#version="1.3.5"
    try:#pip install 'PackageName==1.4'
        if package !="pip":actualizar_import_nueva_version(paquete="pip",forzar_instalacion=True)#para que actualiza el pip
        package=averiguar_nombre_paquete(package)
        if version=="":
            subprocess.check_call([sys.executable, '-m', 'pip', 'install',"-U", package]) #-o
        elif version!="":
            version_instalada=version_import_instalada(package)
            if version!=version_instalada:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install',"-U", package,package+"=="+str(version)]) #-o

        #__import__(package)
    except Exception as e:
        print("Error en " + modulo + ".install_import()")
        print(e)

def desintalar_package(package):
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'uninstall', package])
    except Exception as e:
        print("Error en " + modulo + ".desintalar_package()")
        print(e)    
def averiguar_nombre_paquete(paquete):
    if paquete.upper()=="win32con".upper():
        return "pywin32"
    elif paquete.upper()=="win32api".upper():
        return "pywin32"
    elif paquete.upper()=="dateutil".upper():
        return("python-dateutil")
    elif paquete.upper()=="pyodbc".upper():
        #actualizar_import_nueva_version("pyodbc-4.0.32-cp310-cp310-win_amd64.whl")#
        print("Si da un error hay que instalar microsoft c++")
        return "pyodbc"
    elif paquete.upper()=="ctypes".upper():
        return("ctypes-callable")
    elif paquete.upper()=="msedge".upper():
        return("msedge-selenium-tools")
    elif paquete.upper()=="dateutil".upper():
        return('python-dateutil')
    elif paquete.upper()=="gzip".upper():
        return('gzip-reader')
    elif paquete.upper()=="tkinter".upper():
        return('tk')
    elif paquete.upper()=="pil".upper():
        return('Pillow')
    elif paquete.upper()=="cv2".upper():
        return('opencv-python')
    elif paquete.upper()=="glob".upper():
        return('glob2')
    elif paquete.upper()=="fpdf".upper():
        return('fpdf2')
    elif paquete.upper()=="docx".upper():
        return('python-docx')
    elif paquete.upper()=="BeautifulSoup".upper():
        return('beautifulsoup4')
    elif paquete.upper()=="bs4".upper():
        return('beautifulsoup4')
        
    # elif paquete.upper()=="pandas".upper():
    #     return('panda')
    else:
        return paquete
def import_modulo_desde_path(nombre,path):
    import importlib.util
    # specify the module that needs to be 
    # imported relative to the path of the 
    # module
    spec=importlib.util.spec_from_file_location(nombre,path)#spec=importlib.util.spec_from_file_location("manipular_cadenas","D:\programacion\Python\+Modulos/manipular_cadenas.py")
    # creates a new module based on spec
    foo = importlib.util.module_from_spec(spec)
    # executes the module in its own namespace
    # when a module is imported or reloaded.
    spec.loader.exec_module(foo)
    return foo



if actualizar_imports_siempre==True:
    actualizar_import_nueva_version('pip')
    actualizar_import_nueva_version('wheel')
    actualizar_import_nueva_version('requests')
    actualizar_import_nueva_version('setuptools')


