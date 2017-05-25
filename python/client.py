#-------cliente--------

import socket  
  
s = socket.socket()				#se crea un obj socket   
s.connect(("localhost", 8000))  #el host puede dejarse vacio, indica q any metodo q este disponible
  
while True:  
      mensaje = str(input("> "))  
      s.send(mensaje.encode())  
      if mensaje == "quit":  
         break  
  
print ("adios")  
  
s.close()  
