                                DOCKER
Docker is a platform that allows you to develop, ship, and run applications inside containers. 
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
docker run --name <container name> -P 4000:4000 -d <image name>

                                RUN AN IMAGE WITH VERSION NUMBEDR
docker run --name <container name> -P 4000:4000 -d <image name>:<VERSION NUMBER>

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