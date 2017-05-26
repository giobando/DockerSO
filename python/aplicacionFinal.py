
from Crypto.PublicKey import RSA
from Crypto import Random


random_generator =#Random.new().read
key = RSA.generate(256, random_generator)				#for key public, private

def encriptar():
		
	msjEncriptado = ""
	
	if( key.can_encrypt() ):							#Verifica si se puede encriptar

		#-----------public key----------------------
		public_key = key.publickey().export("PEM")
		print("\nLa llave publica es: ",public_key)	

		#-----------private key---------------------
		# private_Key	= key.export("PEM")
		# print("\nLa llave privada es: ",private_Key)	

		#-----------encriptacion--------------------
		msjAencriptar = input("\nDigite msj a encriptar (entre comillas): ")
		msjEncriptado = public_key.encrypt(msjAencriptar.encode(), 32)	##encriptando
		print("\nEncriptado:")
		# print(msjEncriptado)

	else:
		msjEncriptado = "No se puede encriptar"	
	return msjEncriptado


def desencriptar():
	# key = RSA.generate(1024, random_generator)
	msjDesencriptado = ""

	msjEncriptado = input("Inserte el msj a desencriptar(en comillas): ");
	privateKey = input("Digite la llave privada(entre comillas):")

	msjDesencriptado= privateKey.decrypt(msjEncriptado)	#desencriptando
	print("\nDesencriptado:")
	# print(msjDesencriptado)
	
	return msjDesencriptado


def main():
	

	operacion = {1:encriptar,2:desencriptar}
	terminar = False

	while(terminar!=True):

		try:
			#seleccion
			opc = int(input("\nDigite: 1.Encriptar, 2.Desencriptar\n=>"))
			# choose = 
			print(operacion[opc]()	)

		except:
			print("\n\tError, Opcion invalida")
			salir = int(input("Desea 1. continuar 2. Salir ?"))
			if(salir==2):
				terminar = True

if __name__=="__main__":

	main()	
