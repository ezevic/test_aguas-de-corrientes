# test_aguas-de-corrientes

## Project Setup

### Local Run

Python 3.8

Instalar requerimientos (pip install -r requirements.txt)

Correr migraciones(solo si es necesario, la primera vez es obligatorio)

`python manage.py migrate`

Correr el servidor django

`python manage.py runserver`


### Docker Run

Para correr la aplicación, se necesita tener instalado docker en el sistema. Puede ayudarse de la [documentación oficial](https://docs.docker.com/desktop/).

Una vez que docker esté instalado, a través de la consola ingresar a la carpeta raiz del proyecto (donde está localizado el archivo Dockerfile) y ejecutar los siguientes comandos:

Crear la imagen.

`sudo docker build -t test_aguas-de-corrientes .`

Para verificar si la imagen se creó correctamente, ejecutar el siguiente comando:

`sudo docker image ls` y debería aparecer la imagen con el tag especificado anteriormente. Si se puede ver la imagen pero no el tag, probablemente algo salió mal y hay que repetir el proceso.


Finalmente, ya se puede correr la imagen.

`sudo docker run --network host test_aguas-de-corrientes`


Para terminar de correr el container, primero listamos los containers e identificamos su CONTAINER_ID

`sudo docker ps`


Finalmente, ejecutamos el siguiente comando

`sudo docker stop {CONTAINER ID}`


### Endpoints Disponibles

Server url: localhost:8000

- `/` Home o index. En esta ruta se encuentra el formualrio para ingresar una palabra, y la view se encarga de verificar si es palíndroma.
-`palabra/` Vista de detalle de la palabra. Aqui podemos observar si la palabra cumple con la condición de palíndroma y si la misma ya estaba en la base de datos antes de ser ingresada. A su vez, si ya fue ingresada anteriormente, retorna un campo datetimefield con la ultima modificación de la misma.
-`lista_palabra/` Aquí se encuentran listadas todas las palabras introducidas desde la creación de la bases de datos. Note que para ingresar a este endpoint, es necesario crear un usuario e iniciar sesión a través de los siguientes endpoints respectivamente.
-`register/` Aquí creamos nuestro usuario
-`login/` Aquí iniciamos sesión
-`accounts/logout/` Para cerrar sesión
-`accounts/password_change/ Para recuperar la contraseña de un usuario cuando sea necesario
