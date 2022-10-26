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

Build the Docker image and tag it.

`sudo docker build -t party-manager .` No, that "." at the end of the line is not a typo.

You can validate that the image was successfully built by executing:

`sudo docker image ls` And you should see the image tag we specified above. If you can see the image but with no tag,
there probably was an error with the building process.

Finally, you can run the image inside a container.

`sudo docker run --network host party-manager`

You can also run it in detached mode so that it does not consume the terminal.

`sudo docker run -d --network host party-manager`

You may also want to list the running containers.

`sudo docker ps`

Then you can use the CONTAINER ID to stop the running container.

`sudo docker stop {CONTAINER ID}`

