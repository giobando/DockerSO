
from Crypto.PublicKey import RSA
from Crypto import Random


random_generator = Random.new().read
key = RSA.generate(1024, random_generator)				#for key public, private

def encriptar():
		
	msjEncriptado = ""
	
	if( key.can_encrypt() ):							#Verifica si se puede encriptar
		public_key = key.publickey()
		print("\nLa llave publica es: ",public_key)		

		msjAencriptar = input("\nDigite msj a encriptar (entre comillas): ")
		msjEncriptado = public_key.encrypt(msjAencriptar.encode(), 32)	##encriptando
		print("\nEncriptado:")
		print(msjEncriptado)

	else:
		msjEncriptado = "No se puede encriptar"	
	return msjEncriptado


def desencriptar():
	# key = RSA.generate(1024, random_generator)
	msjDesencriptado = ""
	
	if( key.has_private() ):							#para verificar si trae llame privada
		msjEncriptado = input("Inserte el msj a desencriptar: ");
		msjDesencriptado= key.decrypt(msjEncriptado)	#desencriptando
		print("\nDesencriptado:")
		print(msjDesencriptado)
	else:
		msjDesencriptado = "No se puede desencriptar"	
	return msjDesencriptado


def main():
	

	operacion = {1:"hola",2:"adios"}
	terminar = False

	while(terminar!=True):

		try:
			#seleccion
			opc = int(input("\nDigite: 1.Encriptar, 2.Desencriptar\n=>"))
			# choose = 
			print(operacion[opc]	)
		except:
			print("\n\tError, Opcion invalida")
			salir = int(input("Desea 1. Salir 2. continuar ?"))
			if(salir==1):
				terminar = True

if __name__=="__main__":

	main()	
