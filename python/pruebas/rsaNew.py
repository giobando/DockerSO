from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5


msg = 'hola'
print("encriptadn: ",msg)
key = RSA.generate(1024)    # I know this is a huge overkill
print("key: ",key)
pubkey = RSA.importKey(key.publickey().exportKey('PEM'))

print("public: ")
print(pubkey)

privkey = RSA.importKey(key.exportKey('PEM'))
print("private")
print(privkey)

cipher = PKCS1_v1_5.new(pubkey)
ciphertext = cipher.encrypt(msg)
print("encriptad: ")
print("",ciphertext)

dcipher = PKCS1_v1_5.new(privkey)
secret = dcipher.decrypt(ciphertext, key.exportKey('PEM'))
print("desenriptado: ",secret)

# /


#########3


# from Crypto.PublicKey import RSA
# from Crypto.Cipher import PKCS1_v1_5
# from Crypto import Random


# random_generator =Random.new().read
# key = RSA.generate(1024, random_generator)				#for key public, private

# def encriptar():
		
# 	msjEncriptado = ""
	
# 	if( key.can_encrypt() ):							#Verifica si se puede encriptar

# 		#-----------public key----------------------
# 		public_key = RSA.importKey(key.publickey().exportKey("PEM"))
# 		print("\nLa llave publica es: ")
# 		print(public_key)	

# 		#-----------private key---------------------
# 		private_Key	= RSA.importKey(key.exportKey("PEM"))
# 		print("\nLa llave privada es: ")
# 		print(private_Key)	

# 		#-----------encriptacion--------------------
# 		msj = input("\nDigite msj a encriptar (entre comillas): ")

# 		cipher = PKCS1_v1_5.new(public_key)				##encriptando
# 		msjEncriptado = cipher.encrypt(msj)
# 		print("\nEncriptado:")
# 		print("",msjEncriptado)
# 		print("\n")

# 	else:
# 		msjEncriptado = "No se puede encriptar"	
# 	return msjEncriptado


# def desencriptar():
# 	# key = RSA.generate(1024, random_generator)
# 	msjDesencriptado = ""

# 	msjEncriptado = input("Inserte el msj a desencriptar(en comillas): ");
# 	privateKey = input("Digite la llave privada(entre comillas):")

# 	dcipher = PKCS1_v1_5.new(privateKey)

# 	msjDesencriptado= dcipher.decrypt(ciphertext, 'thisIsSecret')	#desencriptando
# 	print("\nDesencriptado:")
# 	print(msjDesencriptado)
# 	print("\n")
	
# 	return msjDesencriptado


# def main():
	

# 	operacion = {1:encriptar,2:desencriptar}
# 	terminar = False

# 	while(terminar!=True):

# 		try:
# 			#seleccion
# 			opc = int(input("\nDigite: 1.Encriptar, 2.Desencriptar\n=>"))
# 			# choose = 
# 			print(operacion[opc]()	)

# 		except:
# 			print("\n\tError, Opcion invalida")
# 			salir = int(input("Desea 1. continuar 2. Salir ?"))
# 			if(salir==2):
# 				terminar = True

# if __name__=="__main__":

# 	main()	
