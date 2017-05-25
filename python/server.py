#----servidor------
//http://mundogeek.net/archivos/2008/04/12/sockets-en-python/
import socket  
  
s = socket.socket()   

s.bind(("localhost", 8000))	#el host puede dejarse vacio, indica q any metodo q este disponible
s.listen(1)					#la cantidad d conexiones que quiero escuchar
  
sc, addr = s.accept()  
  
while True:  
      recibido = sc.recv(4096)  #cant bits a aceptar
      if recibido == "quit":  
         break        
      print ("Recibido:", recibido  )
      sc.send(recibido)  		#toma parametro datos a enviar.(en este caso envia lo q recibe)
  
print("adios")  
  
sc.close()  
s.close() 
