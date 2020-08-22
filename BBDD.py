import sqlite3

miConexion=sqlite3.connect("PrimeraData")
miCursor=miConexion.cursor()

#miCursor.execute("CREATE TABLE PRODUCTOS(NOMBRE_ARTI VARCHAR(50),PRECIO INTEGER,SECCION VARCHAR(20))")
#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON',20,'DEPORTES')")

#variosProductos=[
   # ('camiseta',20,'DEPORTES'),
  #  ('glocor',50,'CERAMICA'),
 #   ('mesa',40,'CARPINTERIA')

#]agregar muchos registros
#miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)",variosProductos)

miCursor.execute("SELECT * FROM PRODUCTOS")
variosProductos=miCursor.fetchall()#muestra los datos completos
for producto in variosProductos:
    print("NOMBRE_ARTI: ", producto[0], "SECCION: ",producto[2])
miConexion.commit()#confirma los valores 


miConexion.close()