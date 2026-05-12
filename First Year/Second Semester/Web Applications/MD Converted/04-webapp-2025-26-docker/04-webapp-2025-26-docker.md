# 04-webapp-2025-26-docker

_Source: `04-webapp-2025-26-docker.pdf`_

## Slide 1 - Containerize a web

Containerize a web
application with Docker

Web Applications
Master Degree in Computer Engineering

Academic Year 2025/2026

Ornella Irrera

Intelligent Interactive Information Access (IIIA) Hub

![Figura 1 dalla slide 1](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-001-fig-01.jpg)

![Figura 2 dalla slide 1](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-001-fig-02.jpg)

## Slide 2 - Introduction

Introduction

![Figura 1 dalla slide 2](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-002-fig-01.jpg)

## Slide 3 - Web application development

Web application development

A web application is composed of multiple technologies that
must be correctly configured and integrated to work together.

![Figura 1 dalla slide 3](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-003-fig-01.jpg)

## Slide 4 - Web application architecture

Web application architecture

A web application is composed of multiple technologies that
must be correctly configured and integrated to work together.

Data layer
Backend: business

logic and API

Frontend: User
interface design

![Figura 1 dalla slide 4](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-004-fig-01.jpg)

![Figura 2 dalla slide 4](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-004-fig-02.jpg)

## Slide 5 - Web application life cycle

Web application life cycle

The development of a web application is a multi-step process
involving coding, building, and deployment.

Dependencies

Source code

Resources

Development

War file

Maven (build)
Web server
(Deployment)

Developed code (java servlets…)

![Figura 1 dalla slide 5](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-005-fig-01.jpg)

## Slide 6 - Web application development

Web application development

Web applications are complex systems that require
compatibility across multiple layers.

Even small version mismatches between development,
build, and runtime environments can cause application
failures.

![Figura 1 dalla slide 6](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-006-fig-01.jpg)

## Slide 7 - Local deployment

Local deployment

As a result, running a web application locally depends on
the correct configuration of all its components.

Running and maintaining the application locally is usually
straightforward, as you have full control over the data,
backend, and frontend layers.

![Figura 1 dalla slide 7](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-007-fig-01.jpg)

![Figura 2 dalla slide 7](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-007-fig-02.jpg)

## Slide 8 - Problem

Problem

What would happen if you have to deploy your
web application on a new server that has
different configurations, for example different
PostgreSQL or java versions than yours?

![Figura 1 dalla slide 8](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-008-fig-01.jpg)

## Slide 9 - Problem

Problem

Adapting your code to a different environment is
extremely time-consuming and requires code and
dependencies modifications

We need a solution independent of the environment
where the web app is deployed

![Figura 1 dalla slide 9](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-009-fig-01.jpg)

![Figura 2 dalla slide 9](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-009-fig-02.jpg)

![Figura 3 dalla slide 9](slide-009-fig-03.jpg)

## Slide 10 - Is Maven enough?

Is Maven enough?

No. Maven helps manage Java projects by standardizing
the build, testing, and packaging processes. However, it
does not manage the deployment environment.

Therefore, compatibility between components such as
Tomcat must still be ensured.

![Figura 1 dalla slide 10](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-010-fig-01.jpg)

## Slide 11 - Containerization

Containerization

![Figura 1 dalla slide 11](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-011-fig-01.jpg)

## Slide 12 - Containerization

Containerization

Containerization involves packaging an application into
an isolated and self-sufficient execution environment that
ensures consistent behavior across different platforms.

![Figura 1 dalla slide 12](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-012-fig-01.jpg)

## Slide 13 - Containerization

Containerization

This is useful not only when you have to deploy a web
application, but in a wide range of scenarios.

Scenario 1: You have Python3.8 installed in your machine and you need to
run some code in python3.11

Scenario 2: Your OS is Windows and you want to use some tools which
can be installed exclusively on Linux.

Linux
Python 3.11

Windows
Python 3.6

Java21

Java11

Containerization creates isolated environments which are
independent of your host machine.

![Figura 1 dalla slide 13](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-013-fig-01.jpg)

## Slide 14 - Docker

Docker

![Figura 1 dalla slide 14](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-014-fig-01.jpg)

## Slide 15 - What is Docker?

What is Docker?

Docker is an open platform for developing, shipping, and
running applications. It allows you to separate applications
from the underlying infrastructure, enabling faster software
delivery.

Docker allows you to package and run applications in isolated
environments called containers. This isolation makes it possible to
run multiple containers simultaneously on a single host.

Documentation is available here: https://docs.docker.com/get-
started/overview/

## Slide 16 - Docker: an overview

Docker: an overview

Where docker runs. It is the host server which
typically has its own operating system.

## Slide 17 - Docker: an overview

Docker: an overview

The docker engine, or more in general container engine, is a software
component responsible for running and managing containers on a host
machine.
It provides the necessary functionality to create, start, stop, and manage
containers, allowing applications to run in isolated environments.

## Slide 18 - Docker: an overview

Docker: an overview

Isolated containerized applications. Each container has its
own dependencies, its own libraries and are all
independent of the underlying infrastructure and OS.

## Slide 19 - Containers vs VMs

Containers vs VMs

Virtual machines are more isolated.

Containers are: portable, lightweight,
fast, easy deployment.

They all share the same kernel.

However, they are slower, difficult to be
replicated, resource intensive.

![Figura 1 dalla slide 19](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-019-fig-01.jpg)

![Figura 2 dalla slide 19](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-019-fig-02.jpg)

## Slide 20 - Docker main features

Docker main features

Portability as containers can be easily run on any system that supports
Docker, regardless of the underlying infrastructure or operating system.

Efficiency as containers are lightweight and share the host system
resources, resulting in different resources utilization.

Scalability as applications can be deployed as multiple containers.

Isolation as Docker containers provide process-level isolation, ensuring
that applications and their dependencies run without interfering with
each other or the host system.

![Figura 1 dalla slide 20](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-020-fig-01.jpg)

## Slide 21 - Docker — the most important components

Docker — the most important components

The Docker objects collaborate together to run, access and
manage the applications containers. The essential objects are the
following:

Images

Dockerfiles

Container

Volumes

Services

Networks

Other objects are plugins, registries

![Figura 1 dalla slide 21](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-021-fig-01.jpg)

## Slide 22 - Docker images

Docker images

A Docker image is a read-only template used to create
containers. It contains the libraries, dependencies, and
instructions required for an application to run.

Docker images are immutable and are composed of
multiple layers. Each layer represents filesystem changes
such as adding, removing, or modifying files.

For example, you can start from a Python 3.11 base image, install
required packages, and clone a repository, with each step creating a
new layer.

![Figura 1 dalla slide 22](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-022-fig-01.jpg)

## Slide 23 - Dockerfiles

Dockerfiles

How can we create an image?

![Figura 1 dalla slide 23](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-023-fig-01.jpg)

## Slide 24 - Dockerfiles

Dockerfiles

To build user-defined Docker images, users create a
Dockerfile, which is a text file that describes how the
image should be built using a simple and declarative
syntax.

Dockerfiles contain instructions about dependencies,
application configuration, port exposure, and commands
required to run the application.

![Figura 1 dalla slide 24](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-024-fig-01.jpg)

## Slide 25 - Dockerfiles

Dockerfiles

![Figura 1 dalla slide 25](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-025-fig-01.jpg)

## Slide 26 - Docker container

Docker container

A Docker container is a lightweight and isolated runtime
environment used to run applications.

Containers are created from Docker images and are
managed by the Docker Engine.

Multiple containers can run on the same host using the
same image without interfering with each other.

Containers have a writable filesystem layer, but the
underlying image remains immutable.

![Figura 1 dalla slide 26](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-026-fig-01.jpg)

## Slide 27 - Recap

Recap

A Docker image is built based on instructions defined in a Dockerfile,
which specifies the steps to create the image.

![Figura 1 dalla slide 27](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-027-fig-01.jpg)

## Slide 28 - Recap

Recap

Images are created using the Docker build process, where the Docker Engine
reads the Dockerfile and executes the instructions to build the image layer by
layer.

Each layer represents a specific step in the build process.

![Figura 1 dalla slide 28](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-028-fig-01.jpg)

## Slide 29 - Recap

Recap

When a Docker image is built, it is possible to create an instance of it called a container,
which runs the application using the resources of the host machine.

Multiple containers can be created and run from the same image, each with its own
isolated execution environment and state.

![Figura 1 dalla slide 29](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-029-fig-01.jpg)

## Slide 30 - Docker volumes

Docker volumes

In Docker, a volume is a mechanism for persistently storing data
generated by and accessed by the docker containers.

A Docker volume is a directory or file stored outside the container’s
writable layer, allowing data to persist even when containers are stopped
or removed.

It can be used to store databases, configuration files, logs, and any other
data that needs to persist beyond the lifecycle of a container.

![Figura 1 dalla slide 30](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-030-fig-01.jpg)

## Slide 31 - Docker volumes

Docker volumes

Bind mount allows us to share data

between host and container

Multiple containers can mount the same volumes

Volumes persist independently of the lifecycle of the container

Volumes can be attached and detached from the containers as needed

![Figura 1 dalla slide 31](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-031-fig-01.jpg)

## Slide 32 - Your web application

Your web application

Tomcat
PostgreSQL

War file
Database

![Figura 1 dalla slide 32](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-032-fig-01.jpg)

![Figura 2 dalla slide 32](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-032-fig-02.jpg)

![Figura 3 dalla slide 32](slide-032-fig-03.jpg)

## Slide 33 - Your web application

Your web application

Tomcat
PostgreSQL

War file
Database
Volumes

![Figura 1 dalla slide 33](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-033-fig-01.jpg)

## Slide 34 - Problem

Problem

Web applications are complex systems composed of several
components, such as the database, and web server, which
must communicate by exchanging requests, responses, and
processed data.

How can we assemble and manage all these components using
Docker?

![Figura 1 dalla slide 34](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-034-fig-01.jpg)

## Slide 35 - Docker services

Docker services

A service represents a component of an application, such as a
web server (e.g., Tomcat) or a database (e.g., PostgreSQL)

A service is typically based on a single Docker image and can be
scaled by running multiple container replicas that provide the
same functionality.

Services allow you to manage and deploy different application
components as independent units.

![Figura 1 dalla slide 35](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-035-fig-01.jpg)

## Slide 36 - Your web application

Your web application

Service: web
Service: db

Container
Container

Tomcat
PostgreSQL

War file
Database
Volumes

![Figura 1 dalla slide 36](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-036-fig-01.jpg)

![Figura 2 dalla slide 36](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-036-fig-02.jpg)

## Slide 37 - Docker networks

Docker networks

Docker containers are all isolated and they cannot communicate: hence,
given two containers, A and B, exposing different ports, A cannot
communicate with B.

On the other hand, we can reach A and B from outside the container, if
the ports are properly specified.

Docker networks are the solution to let containers communicate.

Only the containers belonging to the same network can communicate.
When a container is instantiated, the network it belongs to should be
specified.

![Figura 1 dalla slide 37](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-037-fig-01.jpg)

## Slide 38 - Your web application

Your web application

Service: web
Service: db

Container
Container

Network

Port 8080
Port 5432

Tomcat
PostgreSQL

War file
Database
Volumes

![Figura 1 dalla slide 38](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-038-fig-01.jpg)

![Figura 2 dalla slide 38](slide-038-fig-02.jpg)

## Slide 39 - Docker compose

Docker compose

Docker Compose is a tool that simplifies the management and
deployment of multi-containers applications —our web application is multi
container!!

It allows you to define and configure multiple Docker services, networks
and volumes as a single application using a YAML file.

Typical use-case: you have a web application. Each of these component is
treated as a separate container which is part of the same web application.

![Figura 1 dalla slide 39](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-039-fig-01.jpg)

## Slide 40 - Your web application

Your web application

Service: web
Service: db

Container
Container

Network

Port 8080
Port 5432

Tomcat
PostgreSQL

War file
Database
Volumes

Docker compose

![Figura 1 dalla slide 40](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-040-fig-01.jpg)

## Slide 41 - Summing up

Summing up

We developed our entire web application which includes the backend
developed in java, the frontend developed in css, html and js, and a
postgreSQL database.

Maven produces a .war file which can be deployed on a web server
(Tomcat).

We want to deploy our web application on multi-containerized
environment which implements two different services:

Tomcat

PostgreSQL

This allows you to deploy your war file you created locally on the version of
tomcat and postgreSQL you prefer, without having to adapt your web
application to the hosting infrastructure.

![Figura 1 dalla slide 41](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-041-fig-01.jpg)

## Slide 42 - Summing up

Summing up

All the services in a multi-containerized environment are described in the docker-
compose.yml file.

Docker Compose creates a network for your application, and each service is
connected to that network. Services can communicate with each other using
their service names as hostnames.

 We need to understand which are the services we need to deploy our web
application: in this case we have tomcat and PostgreSQL.

We need to specify some dependencies: establishing a hierarchies of
dependencies allows to determine the order in which the services are executed.

 Each service relies on a specific image, ports, volumes, environment variables e
developed our entire web application which includes the backend developed in
java, the frontend developed in css, html and js, and a postgreSQL database.

![Figura 1 dalla slide 42](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-042-fig-01.jpg)

## Slide 43 - Hands on

Hands on

![Figura 1 dalla slide 43](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-043-fig-01.jpg)

## Slide 44 - Install

Install

You need to install docker and docker compose following the guidelines in
the documentation

Docker: https://docs.docker.com/get-docker/

Docker compose: https://docs.docker.com/compose/

![Figura 1 dalla slide 44](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-044-fig-01.jpg)

## Slide 45 - The docker compose file

The docker compose file

![Figura 1 dalla slide 45](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-045-fig-01.jpg)

## Slide 46 - The docker compose file

The docker compose file

In the docker-compose.yml file we define the
services needed to run our web application.

## Slide 47 - The docker compose file

The docker compose file

web and db are the names of the
two services we are defining.
These names are useful not only to
identify the individual services, but
also to establish connections and
let the services communicate.

![Figura 1 dalla slide 47](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-047-fig-01.jpg)

## Slide 48 - The docker compose file

The docker compose file

Web and db run two containers,
hence, we need to specify the image
they refer to. The image can be found on a registry
(as in this case), and we need only to
specify the image name; alternatively,
it might be defined in a dockerfile
and we have to specify the location
of the dockerfile.

![Figura 1 dalla slide 48](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-048-fig-01.jpg)

## Slide 49 - The docker compose file

The docker compose file

To access the service from within the container:
- the hostname is the name of the service (web)
- The port is the container port (8080)
- http://web:8080/ to access web from the Postgres service container.

8080:8080 is host_port:container:port

![Figura 1 dalla slide 49](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-049-fig-01.jpg)

## Slide 50 - The docker compose file

The docker compose file

A service allows us to specify environment variables.

These information will also be used in the context.xml file!!

![Figura 1 dalla slide 50](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-050-fig-01.jpg)

## Slide 51 - The docker compose file

The docker compose file

In order to define volumes we need
to specify the (relative) path to the
file in the hosting machine.
After the «:» we specify where this file will be
mounted inside the container.

The docker-entrypoint-init-db.d directory
is a convention to provide a mechanism
for initializing a database when a
container is first started.

The crane.sql file contains the code to create the
database. The tables and the data will be automatically
created as soon as the container is instantiated for the
first time.

![Figura 1 dalla slide 51](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-051-fig-01.jpg)

## Slide 52 - The docker compose file

The docker compose file

Healthchecks allow us to define commands to
check the status of a service.

test is the command to execute. In this case we
want to check the connection status of a
postgreSQL server. Without this check we would
try to establish the connection when postgres is
not ready and this would lead to connection
refused.

Interval is the interval at which the test is
executed.

Timeout is the max amount of time the check has
to finish

Retries is number of consecutive failures allowed

![Figura 1 dalla slide 52](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-052-fig-01.jpg)

## Slide 53 - The docker compose file

The docker compose file

Dependencies establish the execution order .
In this example, the db is initiated first; then,
the web service is run as soon as the
healthcheck is satisfied. depends_on in
general does not wait a service to be fully
initialized and healthy. It only waits for the
dependent service to be running. To wait a
service to be ready we need to establish
healthchecks.

![Figura 1 dalla slide 53](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-053-fig-01.jpg)

## Slide 54 - The docker compose file

The docker compose file

Dependencies establish the execution order .
In this example, the db is initiated first; then,
the web service is run as soon as the
healthcheck is satisfied.
depends_on in general does not wait a
service to be fully initialized and healthy. It
only waits for the
dependent service to be running. To wait a
service to be ready we need to establish
healthchecks.

![Figura 1 dalla slide 54](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-054-fig-01.jpg)

## Slide 55 - Running

Running

![Figura 1 dalla slide 55](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-055-fig-01.jpg)

## Slide 56 - Running

Running

![Figura 1 dalla slide 56](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-056-fig-01.jpg)

## Slide 57 - Running

Running

![Figura 1 dalla slide 57](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-057-fig-01.jpg)

## Slide 58 - How to…

How to…

To containerize your group project you have to:

 Install docker on your machine;

Modify the docker-compose.yml file provided for crane project
accordingly;

Place this file in the same folder of your war file generated with
maven;

You have to install docker and docker compose following the guidelines in
the documentation

Docker: https://docs.docker.com/get-docker/

Docker compose: https://docs.docker.com/compose/

![Figura 1 dalla slide 58](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-058-fig-01.jpg)

## Slide 59 - How to…

How to…

To manage, run, stop, remove your container and have a clear overview of
what is going on you can download Docker Desktop.

Open a new terminal, place in the same folder of your docker-
compose.yaml file and  check that the docker deamon is alive. Then type:

docker-compose up to create and run a new container

docker-compose down to stop the container (your web app won’t be
visible anymore

docker ps to list the running containers

docker ps -a to list the containers — also those not running anymore

![Figura 1 dalla slide 59](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-059-fig-01.jpg)

## Slide 60 - How to…

How to…

To interact with the database:

docker ps to list the running containers. Then, select the name of the
Postgres container in my case docker-db-1

Docker exec docker-db-1 psql -U postgres to access the psql
command line

![Figura 1 dalla slide 60](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-060-fig-01.jpg)
