from Crypto.PublicKey import RSA
from Crypto import Random


#el siguiente codigo se baso en http://www.laurentluce.com/posts/python-and-cryptography-with-pycrypto/
random_generator = Random.new().read

#para correr: 
#			python3 rsa.py

#ENCRIPTAR
def encriptar():
	key = RSA.generate(1024, random_generator)
	
	msjEncriptado = ""

	# #para verificar si se puede encriptar
	if( key.can_encrypt() ):
		public_key = key.publickey()

		print("\nLa llave publica es: ",public_key)
		

		msjAencriptar = input("\nDigite msj a encriptar: ")
		#encriptando
		msjEncriptado = public_key.encrypt(msjAencriptar.encode(), 32)
		print("\nEncriptado:")
		print(msjEncriptado)
	else:
		msjEncriptado = "No se puede encriptar"	
	return msjEncriptado



if __name__=="__main__":

	print("vamo a encriptar")
	encriptar();
