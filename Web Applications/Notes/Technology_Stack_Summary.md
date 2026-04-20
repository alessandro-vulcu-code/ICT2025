# Web Applications Technology Stack Summary (2025-2026)

This document summarizes the core technologies (Maven, Tomcat, and Docker) used for the Web Applications course, based on the provided slides and tutoring sessions. It focuses on their roles and how they are integrated to create, build, and deploy a web application.

---

## 1. Apache Maven: Build Automation & Project Management
Maven is primarily used for **Java project management** and **build automation**. It standardizes the process of compiling code, managing dependencies, and packaging the application.

### Key Components
- **`pom.xml` (Project Object Model)**: The central configuration file.
    - **Project Info**: `groupId`, `artifactId`, `version`, `packaging` (typically `war` for web apps).
    - **Dependencies**: External libraries (e.g., PostgreSQL driver, Servlet API) retrieved from [Maven Central](https://central.sonatype.com/).
    - **Build Config & Plugins**: Controls how the project is compiled and packaged.
- **Lifecycle Phases**:
    - `clean`: Removes previous build artifacts (`target/` folder).
    - `compile`: Compiles source code into bytecode.
    - `test`: Runs unit tests.
    - `package`: Bundles the compiled code into a distributable format (**.war** file).
    - `install`: Installs the package into the local `.m2` repository for use by other local projects.

### How to Use (Teacher's Requirements)
1.  Place yourself in the project folder via terminal.
2.  Run the command: `mvn clean package`.
3.  **Output**: A `.war` file in the `target/` directory, which is ready to be deployed to a web server.
4.  **Note**: In IntelliJ, you can also use the Maven panel on the right to trigger these phases.

---

## 2. Apache Tomcat: Web Server & Servlet Container
Tomcat is an open-source server used to **deploy and run Java web applications** (Servlets and JSPs).

### Role in the Project
- It hosts the `.war` file produced by Maven.
- It provides the environment (Servlet Container) required for Java code to handle HTTP requests.

### Configuration & Usage
- **`tomcat-users.xml`**: Used to define user roles (e.g., `manager-gui`) and credentials to access the Tomcat Manager App.
- **Deployment**:
    - **Direct**: Placing the `.war` file in the `webapps/` folder of the Tomcat installation.
    - **Manual**: Using the Manager App GUI (`http://localhost:8080/manager/html`) to upload the file.
- **Control**:
    - Start: `./bin/startup.sh`
    - Stop: `./bin/shutdown.sh`
    - Permissions: `chmod +x *.sh` (on Linux/macOS).

---

## 3. Docker & Docker Compose: Containerization
Docker allows packaging the application and its environment into **isolated containers**, ensuring "it works on my machine" translates to the production server.

### Key Concepts
- **Dockerfile**: A "recipe" to build a custom **Docker Image** (immutable template).
- **Docker Container**: A running instance of an image.
- **Docker Volume**: Persistently stores data (like databases) outside the container's lifecycle.
- **Docker Network**: Allows containers (e.g., `web` and `db`) to communicate with each other.

### Docker Compose (Multi-Container Management)
The teacher requires using `docker-compose.yml` to manage the complex system (Web + DB).

#### `docker-compose.yml` Structure:
- **`services`**:
    - **`web`**: Uses a `tomcat` image. Maps the `.war` file into `/usr/local/tomcat/webapps/` via volumes.
    - **`db`**: Uses a `postgres` image.
- **`ports`**: Maps container ports to local ports (e.g., `8081:8080` allows accessing the web app at `localhost:8081`).
- **`depends_on` & `healthcheck`**: 
    - The `web` service should depend on the `db` being "healthy."
    - A healthcheck (e.g., `pg_isready`) ensures the database is fully initialized before the web application starts to avoid "Connection Refused" errors.
- **Database Initialization**: Mounting a `.sql` file to `/docker-entrypoint-initdb.d/` automatically runs the schema and data scripts when the container is first created.

### Essential Commands
- `docker-compose up`: Create and start all services.
- `docker-compose down`: Stop and remove containers.
- `docker ps`: List running containers.
- `docker exec -it <container_name> psql -U postgres`: Access the database inside the container.

---

## 4. Integrated Project Workflow
The teacher's intended development cycle for HW1 and beyond is:

1.  **Code**: Develop the Java Backend, HTML/CSS/JS Frontend, and SQL scripts.
2.  **Build**: Run `mvn clean package` to generate the `.war` file.
3.  **Containerize**: 
    - Ensure the `docker-compose.yml` points to the correct `.war` file path.
    - Run `docker-compose up`.
4.  **Test**: Access the app via `http://localhost:<mapped_port>/<app_name>`.
5.  **Version Control**: Use **Git** for collaboration (clone, pull, add, commit, push) and keep features in separate **branches**. Always pull before committing to avoid conflicts.
