modulo="capturar_pantalla"
import import_install
try:
    import PIL
    import_install.actualizar_import_nueva_version('Pillow')
except ImportError:
    import_install.install_import('Pillow')
    import PIL
from PIL import ImageGrab
try:
    import cv2
    import_install.actualizar_import_nueva_version('opencv-python')
except ImportError:
    import_install.install_import('opencv-python')
    import cv2
try:
    import numpy
    import_install.actualizar_import_nueva_version('numpy')
except ImportError:
    import_install.install_import('numpy')
    import numpy
import numpy as np

    # PIL.ima
def capturar_pantalla_ImageGrab():
    return ImageGrab.grab().load()
def capturar_pantalla_PIL():
    try:
        return PIL.ImageGrab.grab()
    except Exception as e:
        print("Error en " + modulo +" capturar_pantalla_PIL()" )
        print(e)
        return ""
def capturar_zona_pantalla_ImageGrab(area=[10,10,500,500]):
    return ImageGrab.grab(bbox=area)
def color_pixel_imagen(imagen,posicion=[0,0]):
    return imagen.getpixel((posicion[0],posicion[1]))
def mostrar_imagen(imagen):
    imagen.show()
def cargar_imagen_PIL(path):
    imagen = PIL.Image.open(path)
    return imagen
def cargar_imagen_cv2(path):
    imagen = cv2.imread(path)
    return imagen
def cargar_imagen_PhotoImage(path_imagen):
    img = cargar_imagen_PIL(path_imagen)
    eimg = convertir_imagen_ImageGrab_a_PIL(img)
    return eimg
def guardar_imagen_ImageGrab(ImageGrab_imagen,path,extension="png"):
    ImageGrab_imagen.save(path,extension)
def guardar_imagen_PIL(PIL_imagen,path):
    PIL_imagen.save(path)
def convertir_pil_to_cv2(image_pil):
    return np.array(image_pil)
def convertir_imagen_ImageGrab_a_PIL(imagen):
    from PIL import ImageTk
    return ImageTk.PhotoImage(imagen)
def coger_color_pixel_pantalla(x,y):
	return PIL.ImageGrab.grab().load()[x, y]
def buscar_imagen_en_imagen(path_imagen,path_busqueda,margen_minimo=0.6):
    image = cv2.imread(path_imagen)
    template = cv2.imread(path_busqueda)
    result = cv2.matchTemplate(image,template,cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val>margen_minimo:
        StartButtonLocation = np.unravel_index(result.argmax(),result.shape)
        return [StartButtonLocation[1],StartButtonLocation[0]]
    else:
        return ""
def buscar_imagen_en_imagen_en_memoria(imagen_cv2,busqueda_cv2,margen_minimo=0.6):
    try:
        result = cv2.matchTemplate(imagen_cv2,busqueda_cv2,cv2.TM_CCOEFF_NORMED)#['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR','cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        if max_val>margen_minimo:
            StartButtonLocation = np.unravel_index(result.argmax(),result.shape)
            if [StartButtonLocation[1],StartButtonLocation[0]]==None:
                return ""
            else:
                return [StartButtonLocation[1],StartButtonLocation[0]]
        else:
            return ""
    except Exception as e:
        print("Error en " + modulo +" buscar_imagen_en_imagen_en_memoria()" )
        print(e)
def buscar_imagenes_en_imagen_en_memoria(imagen_cv2,busqueda_cv2,margen_minimo=0.6):
    try:
        # image = cv2.imread(imagen_cv2)
        # template = cv2.imread(busqueda_cv2)
        result = cv2.matchTemplate(imagen_cv2,busqueda_cv2,cv2.TM_CCOEFF_NORMED)#['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR','cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        loc = np.where( result >= margen_minimo)
        puntos=[]
        if len(loc[0])>0:
            for coor in range(0,len(loc[0])):
                puntos.append([loc[1][coor],loc[0][coor]])
            return puntos
        else:
            return ""
    except Exception as e:
        print("Error en " + modulo +" buscar_imagenes_en_imagen_en_memoria()" )
        print(e)
def imagen_to_cv2(imagen):
    nparr = np.frombuffer(imagen, np.uint8)
    return cv2.imdecode(nparr, cv2.IMREAD_COLOR)


