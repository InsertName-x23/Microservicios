# Microservicios

# ¿Como se usa?
Copiamos los archivos del repositorio en donde queramos, una vez los tengas vas a entrar 
a la terminal y vas a ir a la carpeta donde guardaste estos archivos; usando el comando 
"sudo docker build . -t id:tag" vamos a iniciar el archivo docker y esperamos a termine 
la instalacion; una vez que termine revisamos las imagenes que tenemos y comprobamos que 
se haya creado correctamente, por ultimo la vamos a iniciar con el comando 
"sudo docker run -d -p 80:80 name:tag python3.8 app.py"

