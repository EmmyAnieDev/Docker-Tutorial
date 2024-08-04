                                DOCKER
Docker is a platform that allows you to develop, ship, and run applications inside containers. and deploy as one package.
Containers are lightweight, standalone, and executable software packages that include everything needed to run a piece of software, 
including the code, runtime, libraries, and system tools.

                                Key Concepts
- Dockerfile: A text file that contains a series of instructions on how to build a Docker image.
- Docker Image: A read-only template used to create Docker containers. Images are built from Dockerfiles, and cannot be changed, to change an image we need to build a brand new image and add the changes.
- Docker Container: A runnable instance of an image. Containers can be started, stopped, and deleted. Each container is isolated but can communicate with other containers through defined channels.
- Docker Hub: A cloud-based repository where you can store and share Docker images.




                                DOCKER IMAGES

Images are BLUEPRINT for containers. they contain below

- Runtime environment
- Application code
- Dependencies
- Extra configuration (e.g. env variables)
- commands



                                DOCKER VOLUMES

Docker volume is a way to store data outside of a Docker container. 
It allows you to persist data across container restarts and share data between containers.

This is a feature of docker that allows us to specify folders on our host computer that can be made available to running containers,
and we can map those folders on our host computer to specific folders inside the container,
so that if something change in those folders on our host computer,
that change will also be reflected to those folders we mapped to inside the container. 

*Note* The image the container is running does not change itself. 
So if we want to update the image to share with others or create new containers, we have to rebuild the image using docker build. 




                                DOCKER COMPOSE
Docker Compose is a tool for defining and running multi-container Docker applications. 
It allows you to define your application's services, networks, and volumes in a docker-compose.yml file, 
which makes it easier to manage and run your Docker environment.




                                BUILD AN IMAGE 
docker build -t <TAG NAME> .
docker build -t flask-docker -f api/Dockerfile .


                                BUILD AN IMAGE GIVING IT A VERSION NUMBER
docker build -t <TAG NAME>:<VERSION NUMBER> .


                                LIST OF IMAGES
docker images


                                RUN AN IMAGE / CREATE A CONTAINER
docker run --name <container name> <image name>


                                RUN AN IMAGE / CREATE A CONTAINER MAPPING CONTAINER'S PORT TO OUR COMPUTER'S PORT
docker run --name <container name> -p 4000:4000 -d <image name>


                                RUN AN IMAGE WITH VERSION NUMBEDR
docker run --name <container name> -p 4000:4000 -d <image name>:<VERSION NUMBER>


                                RUN AN IMAGE WITH WITH DOCKER VOLUME WITHOUT DOCKER COMPOSE
*add this to the docker file beneath "ENV FLASK_APP=main.py"*  ENV FLASK_ENV=development
docker run --name flask-docker-container -p 4000:4000 -v $(pwd):/app -d flask-docker-image


                                BUILD AND RUN AN IMAGE USING DOCKER COMPOSE
docker-compose up --build


                                STOP THE CONTAINERS
docker-compose down


                                LIST OF RUNNNING CONTAINERS
docker ps

                                LIST OF ALL CONTAINERS
docker ps -a

                                STOP A RUNNING CONTAINER
docker stop <container name> or <container ID>

                                RESTART A CONTAINER
docker start <container name>

                                DELETE AN IMAGE 
docker image rm <image name> 

                                DELETE AN IMAGE STILL IN USE
docker image rm <image name> -f

                                DELETE A CONTAINER 
docker container rm <container name> 

                                DELETE MULTIPLE CONTAINER 
docker container rm <container name> <container name>  

                                DELETE ALL CONTAINERS, IMAGES AND VOLUMES 
docker system prune -a  