# Containerize a Web Application with Docker

## Table of Contents

- [[#The Deployment Environment Problem|The Deployment Environment Problem]]
- [[#Maven Is Not Enough|Maven Is Not Enough]]
- [[#Containerization|Containerization]]
- [[#Docker — Overview|Docker — Overview]]
  - [[#Containers vs Virtual Machines|Containers vs Virtual Machines]]
  - [[#Main Features of Docker|Main Features of Docker]]
- [[#Docker Objects|Docker Objects]]
  - [[#Docker Images|Docker Images]]
  - [[#Dockerfile|Dockerfile]]
  - [[#Docker Container|Docker Container]]
  - [[#Docker Volumes|Docker Volumes]]
  - [[#Docker Services|Docker Services]]
  - [[#Docker Networks|Docker Networks]]
- [[#Docker Compose|Docker Compose]]
  - [[#Structure of docker-compose.yml|Structure of docker-compose.yml]]
  - [[#Healthcheck and depends_on|Healthcheck and depends_on]]
- [[#Essential Commands|Essential Commands]]
- [[#Summary Table|Summary Table]]

---

## The Deployment Environment Problem

A web application is composed of multiple technologies (Java backend, HTML/CSS/JS frontend, PostgreSQL database) that must be configured and integrated correctly.

The standard life cycle is:

![[Pasted image 20260512203729.png]]

**Development → Maven (build) → WAR file → Web Server (Tomcat)**

The problem: if the target server has different versions of PostgreSQL, Java, or Tomcat compared to the development environment, the application may not work. Adapting the code to every environment is costly and error-prone.

> [!Important] The environment mismatch problem
> Small version differences between the development, build, and runtime environments can cause application failures. A solution is needed that is **independent of the infrastructure** where the webapp is deployed.
> **Insight:** this is the classic "it works on my machine" problem — Docker solves it by packaging everything together.

---

## Maven Is Not Enough

**Maven** standardizes the build, testing, and packaging of Java projects, but **it does not manage the deployment environment**. Compatibility with components such as Tomcat must be guaranteed manually. Maven produces a `.war`, but says nothing about which Tomcat version to use to run it.

---

## Containerization

> [!Important] Containerization
> Containerization encapsulates an application in an **isolated and self-sufficient** execution environment that guarantees consistent behavior across different platforms.
> **Insight:** like shipping a prefabricated house instead of building it on site — it brings everything it needs with it.

Typical use cases:
- You have Python 3.8 installed but need to run Python 3.11 code
- Your OS is Windows but you need tools available only on Linux
- You want to deploy the webapp on Tomcat 10 + PostgreSQL 15 without installing them on the host

---

## Docker — Overview

**Docker** is an open source platform for developing, distributing, and running applications. It separates the application from the underlying infrastructure, enabling faster delivery.

Three-level architecture:
1. **Host** — physical server with its own OS
2. **Docker Engine** — container engine that creates, starts, stops, and manages containers on the host
3. **Containers** — isolated applications, each with its own dependencies and libraries
![[Pasted image 20260512204151.png]]
### Containers vs Virtual Machines

| | Containers | Virtual Machines |
|---|---|---|
| Isolation | Process-level, they share the host kernel | Complete, separate Guest OS |
| Lightness | Lightweight, fast startup | Heavy, slow startup |
| Portability | High | Low |
| Replication | Easy | Difficult |
| Resources | Efficiently shared | Resource-intensive |

![[docker-containers-stack.jpg]]
*Container stack: App + Bins/Libs → Container Engine → Host OS → Infrastructure*

![[docker-vm-stack.jpg]]
*VM stack: App + Bins/Libs + **Guest OS** → Hypervisor → Host OS → Infrastructure*

> [!Important] Key difference between Container and VM
> Containers **share the host OS kernel** — they do not have a Guest OS. VMs include an entire guest operating system, managed by a **Hypervisor**.
> **Insight:** container = isolated process with its own libraries; VM = complete virtual computer.

### Main Features of Docker

- **Portability**: runs on any system that supports Docker, regardless of the underlying OS
- **Efficiency**: lightweight containers that share the host's resources
- **Scalability**: an application can be deployed as multiple parallel containers
- **Isolation**: process-level isolation — applications do not interfere with each other or with the host

---

## Docker Objects

The main Docker objects are: **Images**, **Dockerfiles**, **Container**, **Volumes**, **Services**, **Networks**. Others: plugins, registries.

### Docker Images

> [!Important] Docker Image
> **Read-only** template used to create containers. It contains libraries, dependencies, and instructions to run the application.
> Images are **immutable** and composed of **multiple layers**. Each layer represents changes to the filesystem (adding, removing, or modifying files).
> **Insight:** like a "snapshot" of the environment — each configuration step adds a layer.

### Dockerfile

> [!Important] Dockerfile
> Text file with declarative syntax that describes **how to build a Docker image**. It contains instructions about dependencies, configuration, exposed ports, and startup commands.
> An image is obtained by running `docker build` on a Dockerfile.

> [!Example] Dockerfile — complete example
> **Context:** CUDA-based image for deep learning training with Python 3.10
> **Code:**
> ```dockerfile
> FROM nvidia/cuda:12.4.1-cudnn-runtime-ubuntu22.04
> 
> RUN apt-get update && apt-get install -y \
>     python3.10 \
>     python3.10-dev \
>     python3-pip \
>     git \
>     curl \
>     build-essential \
>     && rm -rf /var/lib/apt/lists/*
> 
> RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.10 1
> 
> RUN python -m pip install --upgrade pip
> 
> WORKDIR /code/src
> ENV PYTHONPATH=/code
> COPY . /code
> COPY requirements.txt .
> 
> RUN pip install --no-cache-dir -r requirements.txt
> RUN pip install --no-cache-dir dgl -f https://data.dgl.ai/wheels/cu124/repo.html
> RUN pip install torch==2.10.0 --index-url https://download.pytorch.org/whl/cu124
> 
> ENV PATH="/root/.local/bin:${PATH}"
> CMD ["/bin/bash"]
> ```
> **Explanation:** every `RUN`, `COPY`, and `ENV` creates a new layer in the final image.

![[docker-dockerfile-image-container-flow.jpg]]
*Flow: Dockerfile → (build) → Docker Image → (run) → Docker Container*

### Docker Container

> [!Important] Docker Container
> **Lightweight and isolated** runtime environment for running applications. Created from a Docker image, managed by the Docker Engine.
> - Multiple containers can run on the same host from the same image without interfering
> - It has a **writable filesystem layer**, but the underlying image remains immutable

### Docker Volumes

> [!Important] Docker Volume
> Mechanism for the **persistence of data** generated and accessed by containers. A volume is a directory or file stored **outside the container's writable layer**: data persists even when the container is stopped or removed.
> Used for: databases, configuration files, logs, any data that must survive the container life cycle.

Volume properties:
- **Bind mount**: data sharing between host and container
- Multiple containers can mount the same volume
- Volumes persist independently of the container life cycle
- They can be attached to and detached from containers dynamically

### Docker Services

A **service** represents an application component (e.g. Tomcat web server, PostgreSQL database). Based on a single Docker image, it can be scaled with multiple container replicas that provide the same functionality.

### Docker Networks

> [!Important] Docker Networks
> Docker containers are isolated and **cannot communicate** with each other by default. Docker networks allow communication between containers.
> Only containers belonging to the **same network** can communicate. The network is specified when the container is instantiated.
> From outside, a container can be reached if the ports are specified correctly.
> **Insight:** the network is like a private virtual switch — only the "connected" containers talk to it.

---

## Docker Compose

> [!Important] Docker Compose
> Tool for managing and deploying **multi-container applications**. It allows defining and configuring multiple Docker services, networks, and volumes as a single application through a **YAML** file.
> The file is called `docker-compose.yml`.

![[docker-compose-webapp-architecture.jpg]]
*Complete architecture: web service (Tomcat, port 8080) ↔ Network ↔ db service (PostgreSQL, port 5432). Volumes for WAR file and Database. Everything described in YAML.*

Key advantages:
- Docker Compose automatically creates a **network** for the application
- Services communicate with each other using the **service name as hostname**
- Dependencies between services define the **startup order**

### Structure of docker-compose.yml

> [!Example] docker-compose.yml — Tomcat + PostgreSQL webapp
> **Context:** web application with Java backend (`crane.war`) on Tomcat 10 and PostgreSQL database
> **Code:**
> ```yaml
> services:
> 
>   web:
>     image: tomcat:10
>     ports:
>       - "8080:8080"
>     depends_on:
>       db:
>         condition: service_healthy
>     volumes:
>       - ./crane.war:/usr/local/tomcat/webapps/crane.war
> 
>   db:
>     image: postgres
>     ports:
>       - "5432:5432"
>     environment:
>       - POSTGRES_PASSWORD=postgres
>       - POSTGRES_USER=postgres
>     volumes:
>       - ./crane.sql:/docker-entrypoint-initdb.d/init.sql
>       - ./data/db:/var/lib/postgresql/data
>     healthcheck:
>       test: [ "CMD-SHELL", "pg_isready -U postgres" ]
>       interval: 5s
>       timeout: 10s
>       retries: 50
> ```
> **Line-by-line explanation:**
> - `image`: specifies the image from a registry (or the path to a Dockerfile with `build:`)
> - `ports: "8080:8080"` → `host_port:container_port`. For internal communication between containers: `http://web:8080/`
> - `environment`: environment variables passed to the container. Also used in Tomcat's `context.xml` for the DB connection
> - `volumes: ./crane.war:/usr/local/tomcat/webapps/crane.war` → mounts the WAR from the host into the Tomcat container
> - `volumes: ./crane.sql:/docker-entrypoint-initdb.d/init.sql` → `docker-entrypoint-initdb.d/` is a PostgreSQL convention: all SQL scripts in that directory are executed automatically at the **first instantiation** of the container
> - `volumes: ./data/db:/var/lib/postgresql/data` → persists the database data on the host filesystem

![[docker-compose-file-full.jpg]]

### Healthcheck and depends_on

> [!Important] Healthcheck vs depends_on
> `depends_on` alone **does not wait** for the service to be fully initialized and ready. It only waits for the container to be running.
> To wait for a service to be **healthy** (e.g. PostgreSQL accepts connections), `depends_on` must be combined with `condition: service_healthy` and a `healthcheck`.
> **Insight:** without a healthcheck Tomcat would start while Postgres is still initializing → connection refused.

`healthcheck` parameters:

| Field | Description |
|---|---|
| `test` | Command to execute to verify the status (e.g. `pg_isready -U postgres`) |
| `interval` | Test execution frequency |
| `timeout` | Maximum time to complete the check |
| `retries` | Number of consecutive failures before declaring unhealthy |

---

## Essential Commands

> [!Example] Docker container management
> **Startup:**
> ```bash
> # Creates and starts all containers defined in docker-compose.yml
> docker-compose up
> ```
> **Stop:**
> ```bash
> # Stops and removes the containers
> docker-compose down
> ```
> **Listing:**
> ```bash
> docker ps          # running containers
> docker ps -a       # all containers (including stopped ones)
> ```
> **DB access:**
> ```bash
> docker ps          # find the name of the PostgreSQL container (e.g. docker-db-1)
> docker exec docker-db-1 psql -U postgres   # access the psql CLI
> ```

![[docker-compose-up-output.jpg]]
*Output of `docker-compose up`: first `docker-db-1` starts, then `docker-web-1`. PostgreSQL automatically executes `init.sql` from the `docker-entrypoint-initdb.d/` directory.*

---

## Summary Table

| Docker Object | Type | Purpose | Notes |
|---|---|---|---|
| **Dockerfile** | Text file | Defines how to build an image | Each instruction = new layer |
| **Image** | Read-only template | Blueprint for creating containers | Immutable, composed of layers |
| **Container** | Runtime instance | Runs the application in isolation | Writable layer above the image |
| **Volume** | Persistent storage | Data that survives the container | Bind mount or named volume |
| **Service** | Logical abstraction | App component (web, db) | Scalable with replicas |
| **Network** | Virtual network | Inter-container communication | Only containers on the same network |
| **Docker Compose** | Orchestrator | Manages multi-container apps | YAML configuration |

| Command | Effect |
|---|---|
| `docker-compose up` | Creates and starts all services |
| `docker-compose down` | Stops and removes the containers |
| `docker ps` | Lists running containers |
| `docker ps -a` | Lists all containers |
| `docker exec <name> <cmd>` | Executes a command inside a container |
| `docker build` | Builds an image from a Dockerfile |
