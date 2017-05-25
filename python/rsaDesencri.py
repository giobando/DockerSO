from Crypto.PublicKey import RSA
from Crypto import Random


#el siguiente codigo se baso en http://www.laurentluce.com/posts/python-and-cryptography-with-pycrypto/
random_generator = Random.new().read



#ENCRIPTAR
def desencriptar():
	key = RSA.generate(1024, random_generator)
	msjDesencriptado = ""
	
	msjEncriptado = input("Inserte el msj: ");
	# #para verificar si trae llame privada
	if( key.has_private() ):

		msjDesencriptado= key.decrypt(msjEncriptado)
		print("\nDesencriptado:", msjDesencriptado)
	else:
		msjDesencriptado = "No se puede desencriptar"	
	return msjDesencriptado



if __name__=="__main__":

	print("vamo a desencriptar")
	desencriptar();
