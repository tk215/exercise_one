from tkinter import *
from tkinter import messagebox
import sqlite3

root=Tk()
root.title("Conexion")
root.config(bg="yellow")

#-----------funciones------------
def conexionBBDD():
	try:
		miConexion=sqlite3.connect("USUARIOS")
		miCursor=miConexion.cursor()
		miCursor.execute('''
			CREATE TABLE DATOS_USUARIOS(
			ID INTEGER PRIMARY KEY AUTOINCREMENT,
			NOMBRE_USUARIO VARCHAR(20),
			PASSWORD VARCHAR(20),
			APE_USUARIO VARCHAR(20),
			DIRE_USUARIO VARCHAR(20),
			COMEN_USUARIO VARCHAR(2000))
			''')
		messagebox.showinfo("BBDD","BBDD creada con exito")
	except:
		messagebox.showwarning("!Atencion!","BBDD ya existe")	

def cerrarVentana():
	valor=messagebox.askquestion("Salir","Deseas salir")
	if valor =="yes":
		root.destroy()

def limpiar_Campos():
	miID.set("")
	miNombre.set("")
	miPass.set("")
	miApe.set("")
	miDire.set("")
	textoComentario.delete(1.0, END)

def crear():
	miConexion=sqlite3.connect("USUARIOS")
	miCursor=miConexion.cursor()
	miCursor.execute("INSERT INTO DATOS_USUARIOS VALUES(NULL,'"+ miNombre.get()+
		"','"+miPass.get()+
		"','"+ miApe.get()+
		"','"+miDire.get()+
		"','"+textoComentario.get("1.0",END)+"')")
	miConexion.commit()
	messagebox.showinfo("BBDD","Registro creado con exito")

def leer():
	miConexion=sqlite3.connect("USUARIOS")
	miCursor=miConexion.cursor()
	miCursor.execute("SELECT * FROM DATOS_USUARIOS WHERE ID="+miID.get())
	elUsuario=miCursor.fetchall()
	for usuario in elUsuario:
		miID.set(usuario[0])
		miNombre.set(usuario[1])
		miPass.set(usuario[2])
		miApe.set(usuario[3])
		miDire.set(usuario[4])
		textoComentario.insert(1.0, usuario[5])

	miConexion.commit()

def actualizar():
	miConexion=sqlite3.connect("USUARIOS")
	miCursor=miConexion.cursor()
	miCursor.execute("UPDATE DATOS_USUARIOS SET NOMBRE_USUARIO='"+miNombre.get()+
		"',PASSWORD='"+miPass.get()+
		"',APE_USUARIO='"+miApe.get()+
		"',DIRE_USUARIO='"+miDire.get()+
		"',COMEN_USUARIO='"+textoComentario.get("1.0",END)+
		"'WHERE ID="+miID.get())
	miConexion.commit()
	messagebox.showinfo("BBDD","Registro actualizado con exito")

def eliminar():
	miConexion=sqlite3.connect("USUARIOS")
	miCursor=miConexion.cursor()
	miCursor.execute("DELETE FROM DATOS_USUARIOS WHERE ID="+miID.get())
	miConexion.commit()
	messagebox.showinfo("BBDD","Registro eliminado")

#------menu despegable-------

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300,bg="red")
bbddMenu=Menu(barraMenu,tearoff=0)
bbddMenu.add_command(label="Conectar",command=conexionBBDD)
bbddMenu.add_command(label="Salir",command=cerrarVentana)

borrarMenu=Menu(barraMenu, tearoff=0,bg="green")
borrarMenu.add_command(label="Borrar Campos",command=limpiar_Campos)

crudMenu=Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear",command=crear)
crudMenu.add_command(label="Leer",command=leer)
crudMenu.add_command(label="Actualizar",command=actualizar)
crudMenu.add_command(label="Borrar",command=eliminar)

ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")

barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar",menu=borrarMenu)
barraMenu.add_cascade(label="CRUD",menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

#------comienzo de campos..........

miFrame=Frame(root)
miFrame.pack()

miID=StringVar()
miNombre=StringVar()
miPass=StringVar()
miApe=StringVar()
miDire=StringVar()

cuadroID=Entry(miFrame,textvariable=miID)
cuadroID.grid(row=0, column=1,padx=10,pady=10)

cuadroNombre=Entry(miFrame,textvariable=miNombre)
cuadroNombre.grid(row=1,column=1,padx=10,pady=10)
cuadroNombre.config(fg="green",justify="right")

cuadroPass=Entry(miFrame,textvariable=miPass)
cuadroPass.grid(row=2,column=1,padx=10,pady=10)
cuadroPass.config(fg="red",show="*",justify="center")

cuadroApe=Entry(miFrame,textvariable=miApe)
cuadroApe.grid(row=3,column=1,padx=10,pady=10)

cuadroDire=Entry(miFrame,textvariable=miDire)
cuadroDire.grid(row=4,column=1,padx=10,pady=10)

textoComentario=Text(miFrame,width=16,height=5)
textoComentario.grid(row=5,column=1,padx=10,pady=10)

scroll=Scrollbar(miFrame,command=textoComentario.yview)
scroll.grid(row=5,column=2,sticky="nsew")
textoComentario.config(yscrollcommand=scroll.set)

#----------nombres de campo---------
cuadroID=Label(miFrame,text="id")
cuadroID.grid(row=0, column=0,padx=10,pady=10,sticky="e")

cuadroNombre=Label(miFrame,text="Nombre")
cuadroNombre.grid(row=1,column=0,padx=10,pady=10,sticky="e")

cuadroPass=Label(miFrame,text="Password")
cuadroPass.grid(row=2,column=0,padx=10,pady=10,sticky="e")

cuadroApe=Label(miFrame,text="Apellido")
cuadroApe.grid(row=3,column=0,padx=10,pady=10,sticky="e")

cuadroDire=Label(miFrame,text="Direccion")
cuadroDire.grid(row=4,column=0,padx=10,pady=10,sticky="e")

textoComen=Label(miFrame,text="Comentarios")
textoComen.grid(row=5,column=0,padx=10,pady=10,sticky="e")

#-----------botones----------------
m2=Frame(root)
m2.pack()

b1=Button(m2,text="Create",width=8,height=1,command=crear)
b1.grid(row=1,column=0,padx=10,pady=10,sticky="e")

b2=Button(m2,text="Read",width=8,height=1,command=leer)
b2.grid(row=1,column=1,padx=10,pady=10,sticky="e")

b3=Button(m2,text="Update",width=8,height=1,command=actualizar)
b3.grid(row=1,column=2,padx=10,pady=10,sticky="e")

b4=Button(m2,text="Delete",width=8,height=1,command=eliminar)
b4.grid(row=1,column=3,padx=10,pady=10,sticky="e")

root.mainloop()