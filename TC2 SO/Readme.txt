========================================================================
==================Pasos para correr pruebas con docker==================
========================================================================
SE UTILIZO MEMCACHE PARA observar su funcionamiento ya que en teoria acelera 
el rendimiento de las aplicaciones .


1. Abrir terminal
2. istalacion del docker:
	https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-16-04

3. abrimos servicio docker
	sudo service docker start

4. creamos un dockerfile (ya creado en la carpeta python)


5. se crea la siguiente imagen etiquetada como centos_img .
	sudo docker build -t centos_img .

//No olvides el punto . para que Docker pueda encontrar el archivo Dockerfile.

6. creamos un nuevo contenedor 
	docker run centos

7 Asegúrate de que tu host tiene las librerías necesarias para Python:

	sudo apt-get update && sudo apt-get -y upgrade
	sudo apt-get install -y python-pip
	pip install python-memcached

8. creamos un contenedor con lo anterior mas un volumen asociado
	sudo docker run -name contenedorA -d -p 45001:11211 centos_img -v /carpetaDocker:/carpetaDocker






