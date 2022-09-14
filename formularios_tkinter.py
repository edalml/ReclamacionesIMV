modulo = "formularios_tkinter"
# from tabnanny import check
import import_install
# import_install.actualizar_imports_siempre=True
try:
    import tkinter
    import_install.actualizar_import_nueva_version("tkinter")    
except ImportError:
    import_install.install_import('tkinter')
    import tkinter
from tkinter import filedialog
from tkinter import *
import os
# from tkinter import font
# from tkinter.font import Font
from tkinter.ttk import Progressbar
import tkinter as tk
from tkinter import ttk
# from tkinter import messagebox 
import manipulacion_imagenes
try:
    import tkcalendar
    import_install.actualizar_import_nueva_version('tkcalendar')
except ImportError:
    import_install.install_import('tkcalendar')
    import tkcalendar
import funciones_tiempo
try:
    import pyautogui
    import_install.actualizar_import_nueva_version('pyautogui')
except ImportError:
    import_install.install_import('pyautogui')
    import pyautogui
try:
    import tkPDFViewer
    import_install.actualizar_import_nueva_version('tkPDFViewer')
except ImportError:
    import_install.install_import('tkPDFViewer')
    import tkPDFViewer

def cambiar_path_carpeta():
    try:
        directorio=filedialog.askdirectory()
        if directorio!="":
            os.chdir(directorio)
    except Exception as e:
       print('Error en '+ modulo +'.cambiar_path_carpeta ' )
       print(e)
def cambiar_puntero_raton(ventana,icon="arrow"):
    #cursors =["arrow", "circle", "clock", "cross", "dotbox", "exchange", "fleur", "heart", "man", "mouse", "pirate", "plus", "shuttle", "sizing", "spider", "spraycan", "star", "target", "tcross", "trek"
    ventana.config(cursor=icon) 
def mensaje_pyautogui(texto,titulo,texto_boton="Aceptar",raiz=None,espera=None):#"ctrl", "f5" #print(pyautogui.KEYBOARD_KEYS)
    pyautogui.alert(texto, titulo,texto_boton,raiz,espera)    #genera ub msgbox
def msgbox(texto,titulo,tipo="showinfo",icono="warning"):
    if tipo=="showinfo":
        return tkinter.messagebox.showinfo(titulo,texto)
    elif tipo=="showwarning":
        return tkinter.messagebox.showwarning(title=titulo, message=texto)
    elif tipo=="showerror":
        return tkinter.messagebox.showerror(title=titulo, message=texto)
    elif tipo=="askquestion":
        return tkinter.messagebox.askquestion(title=titulo, message=texto)
    elif tipo=="askokcancel":
        return tkinter.messagebox.askokcancel(title=titulo, message=texto,icon=icono)
    elif tipo=="askretrycancel":
        return tkinter.messagebox.askretrycancel(title=titulo, message=texto,icon=icono)
    elif tipo=="askyesno":
        return tkinter.messagebox.askyesno(title=titulo, message=texto,icon=icono)#, default="no"  return True False
    elif tipo=="askyesnocancel":
        return tkinter.messagebox.askyesnocancel(title=titulo, message=texto,icon=icono)#messagebox.askokcancel("Close", confirmtxt, default="cancel", icon="warning"):
def crear_timer(ventana,milisegundos,subrutina):

    ventana.after(milisegundos,subrutina)
def dibujar_punto(canvas,x0,y0,x1,y1,ancho,color='white'):
    #canvas.create_rectangle(10,10,20,20,fill=color)
    #canvas.create_line(x0,y0,x1,y1, width=ancho, fill=color)
    #canvas.create_rectangle(x0,y0,x1,y1, width=ancho, fill=color)
    canvas.create_oval(x0,y0,x1,y1, width=ancho, fill=color)
def canvas_crear(ventana,ancho,alto,color_fondo="black"):
    w = Canvas(ventana, height=alto, width=ancho,background=color_fondo)
    w.pack(expand=YES, fill=BOTH)#ventana_canvas.winfo_width()#w.bind("<B1-Motion>", paint)
    return w
def canvas_limpiar(canvas):

    canvas.delete(tk.ALL)
def mostrar_imagen(ventana,imagen_pah,x,y,ancho,alto):
    img = PhotoImage(file=imagen_pah)  
    frame=crear_frame(ventana,x,y,ancho,alto)
    canvas=canvas_crear(frame,ancho,alto)    
    canvas.create_image(ancho,alto, anchor=NW, image=img) 
    actualizar_ventana(ventana)
#SCROLLBAR
def crear_scrollbar(widget,pos_x=1,pos_y=1,anchura_scrollbar=20,largura_scrollbar=100,scrollcommand="yscrollcommand"): #lado ="RIGHT" "BOTTON" "vertical" horizontal ,scrollcommand="xscrollcommand" "yscrollcommand"
    try:

        # pb1 = Scrollbar(ventana,side="vertical", fill="y")#https://www.tutorialspoint.com/python/tk_listbox.htm
        # return pb1
        if scrollcommand=="yscrollcommand":
            scrollbar = ttk.Scrollbar(master=widget, orient=tkinter.VERTICAL, command=widget.yview)
            widget.configure(yscrollcommand=scrollbar.set)
            widget.configure(yscroll=scrollbar.set)
        elif scrollcommand=="xscrollcommand":
            scrollbar = ttk.Scrollbar(master=widget, orient=tkinter.HORIZONTAL, command=widget.xview)
            widget.configure(xscrollcommand=scrollbar.set)
            widget.configure(xscroll=scrollbar.set)
            #widget.configure(scrollregion="all")
        scrollbar.place(x=pos_x,y=pos_y,width=anchura_scrollbar,height=largura_scrollbar)#,bordermode="outside"
        #widget[scrollcommand] = scrollbar.set
        return scrollbar
    except Exception as e:
       print('Error en '+ modulo +'.crear_scrollbar' )
       print(e)
def colocar_scrollbar_a_widget(widget,scrollcommand="vertical",anchura_scrollbar=20): #lado ="RIGHT" "BOTTON" "vertical" horizontal ,scrollcommand="xscrollcommand" "yscrollcommand"
    try:
        widget.update()
        alto=widget.winfo_height()
        ancho=widget.winfo_width()
        # x=widget.winfo_x()#x=widget.winfo_rootx()
        # y=widget.winfo_y()#y=widget.winfo_rooty()
        if scrollcommand=="vertical":
            vertical_x=ancho-anchura_scrollbar# 470
            scrollbar = ttk.Scrollbar(master=widget, orient=tkinter.VERTICAL, command=widget.yview)
            widget.configure(yscrollcommand=scrollbar.set)
            widget.configure(yscroll=scrollbar.set)
            scrollbar.place(x=vertical_x,y=0,width=anchura_scrollbar,height=alto)#,bordermode="outside"
        elif scrollcommand=="horizontal":
            horizontal_y=alto - anchura_scrollbar #470
            scrollbar = ttk.Scrollbar(master=widget, orient=tkinter.HORIZONTAL, command=widget.xview)
            widget.configure(xscrollcommand=scrollbar.set)
            widget.configure(xscroll=scrollbar.set)
            scrollbar.place(x=0,y=horizontal_y,width=ancho,height=anchura_scrollbar)#,bordermode="outside"
        return scrollbar
    except Exception as e:
       print('Error en '+ modulo +'.crear_scrollbar' )
       print(e)

#WIDGET ELEMENTO
def cambiar_tamaño_widget(widget,nuevo_tamaño="500x500"):
    widget.geometry(nuevo_tamaño)
def modificar_widget(widget,texto):
    widget.configure(text=texto)
def widget_leer_propiedad(widget,propiedad='text'):
    for item in widget.keys():
        if item.lower()==propiedad.lower():
            return widget.cget(item)
    return ""
def widget_listar_propiedades(widget):
    lista=[]
    for item in widget.keys():
        lista.append([item,widget.cget(item)])
    return lista
def ocultar_elemento(elemento):
    elemento.place_forget()#grid_remove()
def colocar_elemento(elemento,x,y):
    elemento.place(x=x,y=y)#grid()
def posicion_x_y_del_elemento_en_pantalla(ventana,elemento):
    ventana.update()
    win_x, win_y = ventana.winfo_rootx(),ventana.winfo_rooty()
    x, y = elemento.winfo_rootx(),elemento.winfo_rooty()
    return x-win_x,y-win_y
#FRAME
def crear_frame(ventana,posicion_x=10,posicion_y=10,ancho=200,alto=200,color_fondo="LightGray"): 
    try:
        frame1 = Frame(ventana, width=ancho, height=alto,bg=color_fondo)
        frame1.place(x=posicion_x,y=posicion_y)
        #frame1.pack(fill='both', expand=1)
        #frame1.config(cursor="pirate")
        #frame1.config(bg="lightblue")
        #frame1.config(bd=25)
        #frame1.config(relief="sunken")
        return frame1

    except Exception as e:
       print('Error en '+ modulo +'.crear_frame' )
       print(e)
def crear_labelframe(ventana,titulo,posicion_x=0,posicion_y=0,ancho=200,alto=200):
    labelframe = LabelFrame(ventana, text=titulo, width=ancho, height=alto)
    labelframe.place(x=posicion_x,y=posicion_y)
    return labelframe
#VENTANA PARA EXAMINAR
def examinar_archivo(path_inicial="/", extension_name = "all files",extensiones = "*.*",titulo="Seleccione archivo"):
    try:
        archivo_abierto=filedialog.askopenfilename(initialdir = path_inicial,title = titulo,filetypes = ((extension_name,extensiones),("all files", "*.*"))) #("Excel file","*.xlsx"),("Excel file", "*.xls")
        return archivo_abierto
    except Exception as e:
       print('Error en '+ modulo +'.cambiar_path_carpeta ' )
       print(e)
def examinar_carpeta(path_inicial="/", extension_name = "all files",extensiones = "*.*",titulo="Seleccione archivo"):
    try:
        # carpeta=filedialog.askdirectory(initialdir = path_inicial,title = titulo)
        if path_inicial[0:1]=="\\" and path_inicial[0:3]!="\\\\":
            path_inicial="\\"+path_inicial
        carpeta=filedialog.askdirectory(initialdir = path_inicial,title = titulo)
        # carpeta=filedialog.askdirectory(initialdir = r"\\\\PORTATIL\\compartida\\",title = titulo)#\\\\PORTATIL\\compartida\\ \\PORTATIL\compartida
        return carpeta
    except Exception as e:
       print('Error en '+ modulo +'.examinar_carpeta()' )
       print(e)
def guardar_archivo(path_inicial="/", extension_name = "all files",extensiones = "*.*",titulo="Guardar archivo" ,extension_archivo=".*"):
    try:
        archivo_guardado=filedialog.asksaveasfilename(initialdir = path_inicial ,
                                                      title = titulo ,
                                                      defaultextension=extension_archivo,
                                                      filetypes = ((extension_name,extensiones),("all files", "*.*")))
    
        return archivo_guardado
    except Exception as e:
       print('Error en '+ modulo +'.cambiar_path_carpeta ' )
       print(e)
#LABEL
def crear_label(ventana,texto="hola",posicion_x=10, posicion_y=10,tamaño_letra=10):
    try:
        var = StringVar()
        label1 = Label( ventana,  textvariable=var ,font=(None, tamaño_letra))#relief=SUNKEN,
        label1.config(fg="black",bg="SystemButtonFace",font=("arial",10)) 
        label1.place(x=posicion_x,y=posicion_y)
        var.set(texto)
        return var
    except Exception as e:
       print('Error en '+ modulo +'.crear_label ' )
       print(e)
def crear_label_imagen(ventana,PIL_imagen,posicion_x,posicion_y):
    try:
        #USO
        # PIL_imagen=manipulacion_imagenes.convertir_imagen_ImageGrab_a_PIL(imagen)
        label1 = tkinter.Label( ventana,  image=PIL_imagen )
        label1.place(x=posicion_x,y=posicion_y)
        actualizar_ventana(ventana)
        return label1
    except Exception as e:
       print('Error en '+ modulo +'.crear_label_imagen()' )
       print(e)
def crear_label_dict(ventana,label_dict):
    try:
        #USO
        #label_dict = {"control":"","texto":formularios_tkinter.StringVar(),"x":100,"y":100,"fontsize":10,"textcolor":"black","color_fondo":formularios_tkinter.propiedades_ventana(ventana,'bg'),"font":"Arial"}
        #label_dict["texto"].set("hola")#uso font="Times" "Arial" "Verdana"
        #formularios_tkinter.crear_label_dict(ventana,label_dict)
        if label_dict["control"]!="":
            label_dict["control"].destroy()
        if label_dict["color_fondo"]=="":
            label_dict["color_fondo"]=propiedades_ventana(ventana,'bg')
        label_dict["control"] = Label( ventana,  textvariable=label_dict["texto"] ,font=(label_dict["font"],label_dict["fontsize"]),fg =label_dict["textcolor"],bg= label_dict["color_fondo"])#relief=SUNKEN,,width=100
        label_dict["control"].place(x=label_dict["x"],y=label_dict["y"])
        label_dict["control"].update()

    except Exception as e:
       print('Error en '+ modulo +'.modificar_label_dict()' )
       print(e)
def eliminar_label_dict(label_dict):
    if label_dict["control"]!="":
        label_dict["control"].destroy()
def actualizar_imagen_label_imagen(label_imagen,pil_image):
    label_imagen.configure(image=pil_image)
    label_imagen.image=pil_image
#TEXTBOX
def crear_textbox(ventana,posicion_x=10,posicion_y=10,ancho=100,alto=18,estado=tk.NORMAL): #lado ="RIGHT" "BOTTON" "vertical", orient="vertical"
    try:
        # if estado=="disabled":
        #     estado='disabled' #estado="disabled" state='disabled'
        entry = Entry(ventana,justify=tk.LEFT,state=estado )#, show="*" password ,state=tk.DISABLED,state="readonly", state=tk.NORMAL
        entry.place(x=posicion_x, y=posicion_y,width=ancho,height=alto)
        return entry #textbox_borrar(text_box) #textbox_escribir(text_box,texto) #entry.get() entry.insert(0, "Hola mundo!") 
        #entry.insert(tk.END, " mundo!") entry.delete(0, tk.END) entry.select_range(7, 12) entry.focus() 
        # text_venta.bind("<Key>",text_stop_loss_keypress) "<Key>" "<KeyRelease>" "<KeyPress>"

    except Exception as e:
       print('Error en '+ modulo +'.crear_textbox' )
       print(e)
def textbox_borrar(text_box):
    if text_box!="":
        text_box.delete(0,tk.END)
def textbox_escribir(text_box,texto):
    textbox_borrar(text_box)
    text_box.insert(tk.END, str(texto))
def textbox_leer(text_box):
    return text_box.get()
#BOTON
def crear_boton(ventana,subrutina,texto="Boton1",posicion_x=10, posicion_y=10,color_fondo="LightGray",alto=0,ancho=0):
    try:
        # parametros button https://www.tutorialspoint.com/python/tk_button.htm 
        boton = Button(ventana,text=texto,bg=color_fondo,command= subrutina,height =alto ,width=ancho)
        boton.place(x=posicion_x,y=posicion_y)# para que no se apreten al arrancar si el command tiene parametros crear_boton(ventana,lambda:  examinar_base_datos("destino"),"...","grey",10,42)
        #Button(text="Guardar archivo",bg="light blue",command=guardar_archivo).place(x=10,y=40)
        #Button(text="Directorio",bg="salmon",command=carpeta).place(x=10,y=70)
        return boton 
    except Exception as e:
       print('Error en '+ modulo +'.crear_boton ' )
       print(e)
#PROGRESSBAR
def crear_progressbar(ventana,tamaño=100,posicion_x=10, posicion_y=10,maximo=100):
    try:
        pb1 = Progressbar(ventana, orient=HORIZONTAL,value=0, length=tamaño,maximum=maximo, mode='determinate') #pb1['max']=400 #pb1['value'] += 200 #pb1.destroy()
        pb1.place(x=posicion_x,y=posicion_y)
        return pb1#ventana.update_idletasks()
    except Exception as e:
       print('Error en '+ modulo +'.crear_progressbar ' )
       print(e)
#COMBOBOX
def crear_combobox(ventana,valores,posicion_x=10,posicion_y=10,ancho=100,estado="normal",alto=18,seleccionado=-1):
    try:
        entry =ttk.Combobox(ventana,justify=tk.LEFT,values=valores,state=estado)
        entry.place(x=posicion_x, y=posicion_y,width=ancho,height=alto)#estado=normal readonly disabled combo["state"]="readonly"
        if seleccionado!=-1:
            entry.current(seleccionado)
        return entry 
        #combo.current(1) combo.set("hola") combo.get() x=combo.current() combo.bind("<<ComboboxSelected>>", subrutina) combo["values"] = ["July","August","September","October"]
        #combo['values'] += (string,)
    except Exception as e:
       print('Error en '+ modulo +'.crear_textbox' )
       print(e)
def combobox_cambiar_lista_elementos(combobox,lista):
    combobox['values']=("")
    for x in lista:
        if combobox['values']=="":
            combobox['values']=(x,)#sobreescribimos la primera que esta en blanco
        else:
            combobox['values']+=(x,)#añadimos
    combobox.update()
#MENUS
def USO_MENUS():
    # menu_principal=formularios_tkinter.crear_menu_principal(ventana)
    # menu_archivo=formularios_tkinter.crear_menu()
    # formularios_tkinter.submenu_añadir_item(menu_archivo,"Abrir",nada)
    # formularios_tkinter.submenu_añadir_item(menu_archivo,"Buscar Entidades",nada)
    # formularios_tkinter.submenu_añadir_item(menu_archivo,"Generar",nada)
    # formularios_tkinter.añadir_submenu_al_principal(menu_principal,menu_archivo,"Archivo")
    # formularios_tkinter.submenu_añadir_item(menu_principal,"EAPN",nada)

    # popup=formularios_tkinter.crear_submenu(ventana)
    # formularios_tkinter.añadir_menu_al_menu("cascada",popup,test1Menu)
    # formularios_tkinter.submenu_añadir_item(popup,"Siguiente",siguiente)
    # formularios_tkinter.submenu_añadir_item(popup,"anterior",anterior)
    # formularios_tkinter.submenu_añadir_item(popup,"separador","")
    # formularios_tkinter.submenu_añadir_item(popup,"casa",casa)
    # def do_popup(event):
    #     formularios_tkinter.mostrar_menu_popup(popup,event)
    # ventana.bind("<Button-3>",do_popup)
    pass
def crear_menu_principal(ventana):
    nombre_menu = tkinter.Menu(ventana)
    ventana.config(menu=nombre_menu)
    return nombre_menu
def crear_submenu(menu_principal):#puede ser la ventana para menus popups
    sub_menu = tkinter.Menu(menu_principal, tearoff=0)
    return sub_menu
def submenu_añadir_item(submenu,nombre_menu,funcion_menu):
    try:
        if nombre_menu=="separador":
            submenu.add_separator()
        else:
            submenu.add_command(label=nombre_menu, command = funcion_menu)# filemenu.add_command(label="Salir", command=ventana.quit)
    except Exception as e:
       print('Error en '+ modulo +'.submenu_añadir_item()' )
       print(e)
def añadir_submenu_al_principal(menu_principal,submenu,nombre_submenu):
    menu_principal.add_cascade(label=nombre_submenu, menu=submenu)
def mostrar_menu_popup(popup,event):
    popup.tk_popup(event.x_root, event.y_root, 0)
    popup.grab_release()
def crear_menu():
    return tkinter.Menu(tearoff=0)
def añadir_menu_al_menu(label_menu,menu_principal,menu):
    menu_principal.add_cascade(label=label_menu, menu=menu)
#TOOLBAR
def crear_toolbar(ventana):
    toolbar = tkinter.Frame(ventana, bd=1, relief=tkinter.RAISED)
    toolbar.pack(side=tkinter.TOP, fill=tkinter.X)
    return toolbar
def añadir_boton_toolbar(toolbar,path_imagen,subrutina,texto=""):
    #btn_new = tk.Button(toolbar, text='New file', bd = 4, command=parar_arrancar_segundero)
    if path_imagen!="":
        eimg=manipulacion_imagenes.cargar_imagen_PhotoImage(path_imagen)
    else:
        eimg=None
    boton = tkinter.Button(toolbar, image=eimg, relief=tkinter.FLAT,command=subrutina, text=texto, bd = 4)
    boton.image = eimg
    boton.pack(side=tkinter.LEFT, padx=2, pady=2)
    return boton
def toolbar_modificar_texto_boton(boton,texto):
     boton.configure(text=texto)
#ESTILO
def cargar_estilos():#('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
    s = tkinter.ttk.Style()
    return s.theme_names()
def estilo_familias_fuentes():
    lista=tkinter.font.families()
    return lista
def estilo_nombres_fuentes():
    return tkinter.font.names()
def modificar_estilo(str_widget,estilo='clam', color_fondo="green",fuente_nombre='Helvetica',fuente_tamaño=15,fuente_weight="normal", color_letra="blue",alto_fila=-1):#family="Helvetica", size=12, weight="bold"
    s = ttk.Style()
    s.theme_use(estilo)#('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative') #(tkinter.font.NORMAL tkinter.font.BOLD tkinter.font.ITALIC tkinter.font.ROMAN)
    # Configure the style of Heading in Treeview widget
    s.configure(style=str_widget, background=color_fondo,font=(fuente_nombre,fuente_tamaño,fuente_weight), foreground=color_letra)#str_widget='Treeview.Heading'
    if alto_fila!=-1:
        s.configure(rowheight=alto_fila)
    return s
#TREEVIEW
def crear_treeview(ventana,columnas=[["col_name",tkinter.E,10],["col_name",tkinter.CENTER,10]],posicion_x=1, posicion_y=1,ancho=100,alto=100):
    #columnas=[["Ticker",formularios_tkinter.tkinter.W,90,subrutina_hola]]
    tree = ttk.Treeview(ventana, column=columnas, show='headings', height=50,selectmode='browse')#, selectmode='browse' selectmode='none'
    tree.place(x=posicion_x, y=posicion_y,width=ancho,height=alto)#estado=normal readonly disabled combo["state"]="readonly"
    # estilo=modificar_estilo('Treeview')
    # estilo=modificar_estilo('Treeview.Heading')

    numero=0
    while numero < len(columnas):
        treeview_añadir_columnas(tree,numero,columnas[numero][0],columnas[numero][1],columnas[numero][2],subrutina=columnas[numero][3])
        numero+=1
    return tree
def treeview_añadir_columnas(widget_treeview,numero_columna,text_columna,alineacion=CENTER,ancho=10,subrutina=""):
    widget_treeview.column(numero_columna, anchor=alineacion,width=ancho,stretch=NO,minwidth=0)
    if subrutina!="":
        widget_treeview.heading(numero_columna, text=text_columna,command=subrutina)
    else:
        widget_treeview.heading(numero_columna, text=text_columna)
def treeview_añadir_valores_a_columnas(widget_treeview,valores=[],nombre_detalles_linea=""):
    if nombre_detalles_linea=="":#treeview_crear_detalles_linea(widget_treeview,nombre="roja",background_color="#D3D3D3",fuente=('Verdana',10),foreground_color='red')
        widget_treeview.insert( '', 'end', text="1", values=valores )
    else:
        widget_treeview.insert('', 'end', text="1", values=valores, tags=(nombre_detalles_linea))
def treeview_elemento_seleccionado(lista_treeview):# lista_treeview.bind('<ButtonRelease-1>', selectItem)
    curItem = lista_treeview.focus()
    return lista_treeview.item(curItem)#evento lista_treeview.bind('<ButtonRelease-1>', selectItem)
def treeview_crear_detalles_linea(widget_treeview,nombre="roja",background_color="#D3D3D3",fuente=('Verdana',10),foreground_color='red'):
    widget_treeview.tag_configure(nombre, background = background_color,font=fuente,foreground=foreground_color)#tienes colores Colores
def treeview_enable(widget,enabled=False):
    if enabled==False:
        widget.state(('disabled',))
    else:
        widget.state(('!disabled',))
    z=0
def treeview_esta_disabled(widget):
    return 'disabled' in widget.state()
def treeview_titulo_columna_clickeada(widget_treeview):
    # USO
    # columnas=[["Ticker",formularios_tkinter.tkinter.W,90,columna_click]
    # def columna_click():
    #   columna_num=formularios_tkinter.treeview_titulo_columna_clickeada(lista_treeview)
    x=0
    while True:
        try:
            if widget_treeview.heading(x)["state"]=="active":
                return x
        except :
            break
        x+=1
    treeview_enable(widget_treeview,True)
def treeview_eliminar_todas_lineas(widget_treeview):
    for row in widget_treeview.get_children():
        widget_treeview.delete(row)
def treeview_lista_todas_lineas(widget_treeview):
    lista_lineas=[]
    for row in widget_treeview.get_children():
        lista_lineas.append(widget_treeview.item(row)["values"])
    return lista_lineas
def treeview_mostrar_columnas(widget_treeview,columnas=(0,1)):
    widget_treeview["displaycolumns"]=columnas #widget_treeview["displaycolumns"]=(0,1,2,3,4,5,6,7,8,0)# self.tree["displaycolumns"]=("artistCat", "artistDisplay")
#AFTER
def cancelar_timer(ventana,id_after):
    ventana.after_cancel(id_after)
#FECHA
def crear_selector_fecha(ventana,posicion_x=10,posicion_y=10,ancho=50,alto=20):#fecha.get()
    fecha = tkcalendar.DateEntry( ventana, width= 16, background= "magenta3", foreground= "white",bd=2,xcor=120,ycor=210)
    fecha.place(x=posicion_x, y=posicion_y,width=ancho,height=alto)
    return fecha
def selector_fecha_coger(selector_fecha):
    return funciones_tiempo.str_a_datetime(selector_fecha.get(),r'%d/%m/%y')
#LISTBOX
def crear_listbox(ventana,posicion_x=10,posicion_y=10,caracteres_ancho=20,numero_elementos=10,modo_seleccion="simple"): #lado ="RIGHT" "BOTTON" "vertical", orient="vertical" selectmode = BROWSE EXTENDED
    try:#listbox.bind('<<ListboxSelect>>', onselect)
        if modo_seleccion=="BROWSE":
            modo_seleccion=tk.BROWSE
        else:
            modo_seleccion=tk.EXTENDED
        frame1 = crear_frame(ventana,posicion_x,posicion_y)
        listbox_lista = Listbox(frame1,height=numero_elementos ,width=caracteres_ancho,selectmode = modo_seleccion)#https://www.tutorialspoint.com/python/tk_listbox.htm #font=("Helvetica", 12)
        listbox_lista.place(x=posicion_x,y=posicion_y)

        scrollbar_v = Scrollbar(frame1, orient="vertical")
        scrollbar_v.config(command=listbox_lista.yview)

        scrollbar_h = Scrollbar(frame1, orient="horizontal")
        scrollbar_h.config(command=listbox_lista.xview)

        listbox_lista.config(yscrollcommand=scrollbar_v.set ,xscrollcommand=scrollbar_h.set)


        scrollbar_h.pack(side="bottom", fill="x")#,anchor = "w", fill="both"
        listbox_lista.pack(side="left", fill="y")
        scrollbar_v.pack(side="left", fill="y")

        listbox_lista.configure(exportselection=False)#al perder el foco no pierde los elementos seleccionados
        return listbox_lista

    except Exception as e:
       print('Error en '+ modulo +'.crear_listbox' )
       print(e)
def listbox_cambiar_lista_elementos(listbox,lista):

    listbox.insert(0, *lista)
    listbox.update()
def list_box_elementos_seleccionados(listbox):
    lista=[]
    for i in listbox.curselection():
        lista.append(listbox.get(i))
    return lista
def list_box_elementos_seleccionados_index(listbox):
    lista=[]
    for i in listbox.curselection():
        lista.append(i)
    return lista
def listbox_coger_todos_elementos(listbox):
    return list(listbox.get(0, END))
def listbox_limpiar_elementos(listbox):
    listbox.delete(0,END)
    listbox.update()
#VENTANA
def actualizar_ventana(ventana):
    ventana.update()
    ventana.update_idletasks()
def crear_ventana(texto="Formulario",tamaño="500x200",icono="",topmost=False):
    ventana = Tk()#ventana.after(1000, my_mainloop)  #ventana.mainloop() className = texto
    ventana.geometry(tamaño)
    ventana.iconbitmap(icono)
    ventana.resizable(True,True)
    ventana.title(texto)
    ventana.attributes("-topmost", topmost)
    return ventana
def destruir_ventana(ventana):
    ventana.destroy()
def propiedades_ventana(ventana,propiedad):
    if propiedad=="bg":#color de fondo del formulario
        return ventana.cget('bg')        
def ajustar_tamaño_ventana(ventana,tamaño="750x250+400+300"):
    ventana.geometry(tamaño)
def averiguar_color_ventana(ventana):
    s = ttk.Style()
    bg = s.lookup('TFrame', 'background')
    return bg
#CHECKBOX
def crear_checkbox(ventana,texto="checkbox",marcado= False,posicion_x=10, posicion_y=10):
    try:
        checkbox= IntVar()
        widget_checkbox=Checkbutton(ventana, text=texto, variable=checkbox).place(x=posicion_x,y=posicion_y) #var.get() 
        checkbox.set(marcado)
        return checkbox
    except Exception as e:
       print('Error en '+ modulo +'.crear_checkbox ' )
       print(e)
def checkbox_estado(checkbox):
    try:
        if checkbox.get()==0:
            return False
        else:
            True
    except Exception as e:
       print('Error en '+ modulo +'.checkbox_estado()' )
       print(e)
#PDF
def mostrar_pdf(ventana,ruta_pdf,x=0,y=0,ancho=200,alto=200):
    from tkPDFViewer import tkPDFViewer as pdf
    pdfviewer = pdf.ShowPdf()
    pdfframe = pdfviewer.pdf_view(ventana, pdf_location=ruta_pdf,load="before")
    pdfviewer.img_object_li.clear() # clear loaded pages
    pdfframe.place(x=x, y=y,width=ancho,height=alto)
    
    # pdf.ShowPdf().pdf_view(ventana,pdf_location=ruta_pdf,width=75,height=100).pack()
    return pdfframe
#RICHTEXTBOX
def crear_richtextbox(ventana,posicion_x=10,posicion_y=10,ancho=100,alto=18,estado=tk.NORMAL): #lado ="RIGHT" "BOTTON" "vertical", orient="vertical"
    try:
        # if estado=="disabled":
        #     estado='disabled' #estado="disabled" state='disabled'
        richtextbox = Text(master=ventana, wrap=tkinter.NONE)#wrap=WORD, CHARS, or NONE
        richtextbox.place(x=posicion_x, y=posicion_y,width=ancho,height=alto)
        return richtextbox #textbox_borrar(text_box) #textbox_escribir(text_box,texto) #entry.get() entry.insert(0, "Hola mundo!") 
        #entry.insert(tk.END, " mundo!") entry.delete(0, tk.END) entry.select_range(7, 12) entry.focus() 
        # text_venta.bind("<Key>",text_stop_loss_keypress) "<Key>" "<KeyRelease>" "<KeyPress>"

    except Exception as e:
       print('Error en '+ modulo +'.crear_richtextbox' )
       print(e)
def escribir_richtextbox(richtextbox,texto,justificado="left"):
        richtextbox.tag_configure("tag_name", justify=justificado) #justificado=left, right, or center
        richtextbox.insert("1.0", texto)
        richtextbox.tag_add("tag_name", "1.0", "end")
