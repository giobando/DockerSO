#!/usr/bin/env python
 
 #Este codigo basicamente espera en recibir una solicitud la cual consiste
 #en un palabra encriptada
 #Si la palabra es "fin" almacena dicha palabra en un archivo mensaje.txt
 #Si no, entonces responde y la envia nuevamente encriptada.

from Crypto.Hash import MD5
from Crypto.PublicKey import RSA
from Crypto.Util import randpool
 
import pickle
import socket
import sys
 #https://webstersprodigy.net/2008/05/05/encrypt-a-message-with-rsa-in-python/
#generate the RSA key
blah = randpool.RandomPool()
RSAKey = RSA.generate(1024, blah.get_bytes)
 
RSAPubKey = RSAKey.publickey()
 
#listen for a connection
host = ''
port = 12345
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host,port))
s.listen(1)
 
print "Server is running on port %d; press Ctrl-C to terminate." % port
 
while 1:
  clientsock, clientaddr = s.accept()
  print "got connection from ", clientsock.getpeername()
  #send the public key over
  clientsock.send(pickle.dumps(RSAPubKey))
 
  rcstring = ''
  while 1:
    buf = clientsock.recv(1024)
    rcstring += buf
    if not len(buf):
      break

 
  #Mensaje encriptado
  encmessage = pickle.loads(rcstring) 
  desencriptado = RSAKey.decrypt(encmessage)

  print desencriptado

  #----Agrega palabra al txt-----------
  f=open("mensaje.txt","a")
  f.write(desencriptado+" ")
  f.close()

  #----Verifica si termina conexion----
  if(encmessage=="fin"):
	  print("Fin recibido!")
  else:
  	clientsock.send()
  
  clientsock.close()
  