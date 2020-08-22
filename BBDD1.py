import sqlite3 
miConexion=sqlite3.connect("gestion_productos")
miCursor=miConexion.cursor()
miCursor.execute("UPDATE PRODUCTOS SET PRECIO=200 WHERE NOM_PRODU='PELOTA'")
productos=miCursor.fetchall()
print(productos)
miConexion.commit()
miConexion.close()