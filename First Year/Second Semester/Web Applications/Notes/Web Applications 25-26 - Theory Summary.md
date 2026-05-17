# Web Applications 25-26 - Theory Summary

This summary follows the order of `Notes/Web Applications 25-26.md`. It is meant for
theory study: the goal is not to memorize every line of code, but to understand the
concepts well enough to explain them in 3-4 open answers.

Past multiple-choice exams repeatedly touched definitions and precise distinctions:
Web architectures, URI/HTTP/MIME, servlets/JSP/MVC, XML/DOM/JSON, HTML/CSS/JS,
AJAX, jQuery, canvas, and Semantic Web/RDF. They are useful signals, but not a full
syllabus.

---

## 1. Introduction to Web Applications

### Historical foundations

The Web did not appear from nothing. It evolved from earlier ideas about linked
information.

| Person / System | Main contribution |
|---|---|
| Vannevar Bush, Memex (1945) | Vision of a machine for storing and retrieving linked information. |
| Ted Nelson, Hypertext / Xanadu | Coined "hypertext"; imagined bidirectional links and versioning. |
| Douglas Engelbart, NLS | Early system with mouse, windows, hyperlinks, collaborative editing. |
| NoteCards | Hypertext system for organizing information into cards and links. |
| Tim Berners-Lee, WWW | Practical Web architecture at CERN: simple hypertext over the Internet. |

> [!important] Definition - Hypertext
> Hypertext is text connected by links, so the reader can move non-linearly between
> related pieces of information.

The first popular graphical browser was **Mosaic** (1993). Later browsers include
Netscape Navigator, Internet Explorer, Firefox, Safari, Chrome, and Edge.

### Evolution of the Web

![[intro-web10.jpg|520]]

*Figure 1: Diagram of Web 1.0 as an informative read-only Web*

| Phase | Informal name | Core technologies | Main idea |
|---|---|---|---|
| Web 1.0 | Read Web | HTTP, HTML, MIME, URL | Producers publish, users mostly read. |
| Web 2.0 | Read/Write Web | XML, AJAX, JSON, Web services, REST | Users also create content and services interact. |
| Web 3.0 | Web of Data / Semantic Web | RDF, OWL, SPARQL | Data has explicit semantics and machine-readable links. |
| Web3 | Decentralized Web | Blockchain, crypto, DeFi, NFT | User-controlled data and decentralized infrastructure. |

**Deep Web** means content not indexed by ordinary search engines: private databases,
login-protected systems, dynamically generated pages. **Dark Web** means anonymous
access through systems such as Tor or I2P. They are not the same thing.

### Application layers and architectures

Every application can be described with three logical layers.

| Layer | Responsibility |
|---|---|
| Presentation logic | User interface, input/output format, first validation. |
| Application logic | Business rules, operation flow, constraints. |
| Data logic | Persistent storage, retrieval, consistency. |

The physical architecture says where those layers run.

![[intro-three-tier.jpg|520]]

*Figure 2: Three-tier architecture with separate presentation, application, and data tiers*

| Architecture | Distribution | Strength | Weakness |
|---|---|---|---|
| Single-tier | All layers on one machine, e.g. mainframe | Simple, no client management | Poor scalability, single point of load |
| Two-tier, fat client | Presentation + application on client, data on server | Client does much work | Client maintenance, tight DB coupling |
| Two-tier, fat server | Presentation on client, application + data on server | Centralized logic | Server can become heavy |
| Three-tier | Client, application server, database server | Scalable, clearer separation | More complex to implement |

![[intro-webapp-three-tier.jpg|520]]

*Figure 3: Web application mapped to a three-tier architecture with browser, server, and database*

A typical Web application is a **three-tier application**:
browser as presentation tier, web/application server as application logic, DBMS as
data tier. The browser and server communicate through HTTP over the network stack.

**Open-question focus:** explain the three logical layers, then map them onto
single-tier, two-tier, and three-tier architectures. Be precise: the application
logic layer controls the flow of operations; the data layer manages persistent data.

### Extended study notes

When writing an open answer about Web application architecture, start from the
logical model, not from the physical machines. The same logical application always
has presentation, application, and data logic, even if a small prototype puts all of
them in one process. The architectural question is: where are these responsibilities
executed and how do they communicate?

The **presentation layer** is not "only graphics". It includes everything related to
user interaction: form layout, navigation, input collection, first feedback, and
sometimes simple client-side validation. In a Web application it is mostly the
browser running HTML, CSS, and JavaScript.

The **application layer** is the center of the system. It decides which operation is
being requested, checks business rules, calls persistence logic, chooses the response,
and handles errors. In the course examples, servlets and REST resources perform this
role.

The **data layer** is where long-term state is stored and kept consistent. A DBMS
does not just "save files"; it enforces schemas, constraints, transactions, indexes,
and queries.

Single-tier systems are easy to understand because all logic is in the same place.
The cost is that scalability and fault isolation are poor. If the central machine is
overloaded or unavailable, the whole application suffers.

Two-tier systems split work between clients and a server. In a fat-client design, the
client contains much application logic and talks directly to the DB server. This can
reduce server work, but it makes clients hard to update and exposes the database
model to the client. In a fat-server design, the client is simpler and the server
does more work.

Three-tier systems introduce a middle tier. The browser does not talk directly to the
database; it talks to a web/application server. This server can validate requests,
apply business rules, reuse connection pools, enforce security, and expose stable
APIs even if the database schema changes.

A good exam answer should also mention that three-tier does not automatically mean
"three physical machines". It means three logical roles. In a development setup, all
roles may run on the same laptop; in production, they may be separated across many
servers and containers.

Typical flow in a Web application:

```text
Browser
  -> HTTP request
  -> Web/Application server
  -> DAO or service layer
  -> DBMS
  -> result data
  -> generated HTML/JSON response
  -> Browser rendering
```

Load balancing becomes easier in this model because multiple application servers can
run the same code behind a load balancer while sharing a database or a replicated
data layer. This is one of the practical reasons Web applications moved away from
single-tier designs.

Exam-style distinction:

| Question wording | Best answer direction |
|---|---|
| "Purpose of application logic layer" | Controls operation flow and business rules. |
| "Purpose of data logic layer" | Persistent storage, retrieval, consistency. |
| "Web application architecture" | Usually a three-tier architecture. |
| "Disadvantage of three-tier" | More complex implementation and deployment. |
| "Advantage of three-tier" | Scalability, separation of concerns, load balancing. |

Avoid saying that Web 3.0 and Web3 are the same. In these notes, **Web 3.0** is the
Semantic Web / Web of Data, based on RDF, OWL, and SPARQL. **Web3** is the
blockchain/decentralized Web movement.

---

## 2. Git and Maven

### Git

**Git** is a distributed version control system. Each local copy is a complete
repository, not only a checkout from a central server.

![[git-workflow-three-trees.jpg|520]]

*Figure 4: Git workflow between working directory, index, and HEAD*

Git's local workflow has three areas:

| Area | Meaning |
|---|---|
| Working directory | Actual files you are editing. |
| Index / staging area | Snapshot prepared for the next commit. |
| HEAD | Last committed version of the current branch. |

```bash
git add file.md
git commit -m "Add note"
git push origin main
```

Explanation:
- `git add` copies selected changes from the working directory to the index.
- `git commit` records staged changes into local history.
- `git push` sends local commits to a remote branch.

Branches are independent lines of development. A feature branch can diverge from
`main` and later be merged back.

![[git-branch-merge.jpg|520]]

*Figure 5: Feature branch diverging from and merging back into the main branch*

A **pull request** is not the same as `git pull`. A pull request is a collaboration
mechanism on platforms such as GitHub or Bitbucket: it asks others to review a branch
before merging it.

### Maven

**Maven** is a Java project management tool. It standardizes building, packaging,
dependency resolution, documentation, and deployment.

![[maven-phases-goals-plugins-pom.jpg|520]]

*Figure 6: Relationship between Maven lifecycle phases, goals, plugins, and the POM*

Core Maven concepts:

| Concept | Meaning |
|---|---|
| Lifecycle | Ordered build process, such as `clean`, `default`, or `site`. |
| Phase | Step inside a lifecycle, such as `compile`, `test`, `package`. |
| Goal | Concrete operation, implemented by a plugin. |
| Plugin | Component that provides one or more goals. |
| POM | `pom.xml`, declarative description of project coordinates, dependencies, plugins. |

Invoking a Maven phase also executes all previous phases in that lifecycle. For
example, `mvn package` validates, compiles, tests, and then packages.

```xml
<groupId>it.unipd.dei.webapp</groupId>
<artifactId>employee-webapp</artifactId>
<version>1.00</version>
<packaging>war</packaging>
```

These are Maven **coordinates**. They identify the artifact. `packaging` says what
Maven produces: `jar` for ordinary Java archives, `war` for web applications.

Maven uses remote repositories, such as Maven Central, and a local cache under
`~/.m2/repository`. If a dependency is missing locally, Maven downloads it.

**Open-question focus:** connect lifecycle -> phase -> goal -> plugin, and explain
why the POM is declarative. Also know why generated files such as `target/` do not
belong in Git.

### Extended study notes

Git and Maven solve different problems and are often confused in short answers.
Git manages the **history of source files**. Maven manages the **build process and
dependencies**. A good project normally uses both: Git tracks the human-written
source code and configuration, while Maven regenerates compiled artifacts.

Git is distributed because every clone contains the full repository history. This is
why a developer can commit locally without network access. Synchronization with
others happens later through `push`, `pull`, `fetch`, and merge operations.

The three-area Git model is useful because it explains why `git add` is separate
from `git commit`. You can edit many files in the working directory and stage only
some of them. The commit records exactly what is in the index, not every modified
file automatically.

```text
working directory --git add--> index --git commit--> HEAD
```

Branches are cheap pointers to commits. Creating a branch does not copy the entire
project; it creates a new name for a line of development. A merge creates a history
where changes from two lines are combined. If the same lines changed differently,
Git may ask the developer to resolve conflicts.

Files generated from the build should not be versioned because they can be recreated.
For a Maven project, `target/`, `.class`, `.jar`, `.war`, generated Javadoc, IDE
metadata, and logs usually go into `.gitignore`. Versioning generated files creates
noise and increases the chance of inconsistent builds.

Maven is declarative: the POM describes what the project is and what it needs, not
the exact shell commands for every step. The lifecycle model then gives standard
meaning to commands such as `mvn test` or `mvn package`.

Important Maven flow:

```text
validate -> compile -> test -> package -> verify -> install -> deploy
```

If the command is:

```bash
mvn package
```

Maven does not only package. It first runs the earlier phases in order. This is why
`mvn package` also compiles code and runs tests before producing a JAR or WAR.

Dependencies are identified through coordinates:

```xml
<dependency>
  <groupId>org.postgresql</groupId>
  <artifactId>postgresql</artifactId>
  <version>42.2.2</version>
</dependency>
```

The coordinate says which artifact to download. Maven first checks the local
repository cache, then remote repositories. This makes projects reproducible: the
POM documents the required libraries instead of requiring each developer to download
them manually.

For Web applications, `war` packaging matters. A WAR has the layout expected by a Web
container such as Tomcat. Servlet API dependencies are usually marked `provided`
because Tomcat already provides them at runtime. Application libraries such as JDBC
drivers, Log4J, JSTL, Jackson, or Jakarta Mail normally must be packaged unless the
container explicitly provides them.

Exam-style distinction:

| Tool / concept | What to say |
|---|---|
| Git | Version control for cooperative development. |
| Maven | Build and dependency management for Java projects. |
| POM | Declarative project model in XML. |
| Lifecycle | Ordered sequence of build phases. |
| Plugin | Implements concrete goals executed in phases. |
| Repository | Place where Maven artifacts are stored and resolved. |
| `.gitignore` | Prevents generated or local-only files from being tracked. |

An answer about Maven should not describe it as a continuous-integration framework.
It can be used inside CI pipelines, but Maven itself is the build/dependency tool.

---

## 3. Docker and Containerization

### The deployment problem

A Java web application needs compatible versions of Java, Tomcat, PostgreSQL,
libraries, configuration files, and environment variables. Maven can create the WAR,
but it does not guarantee the runtime environment.

![[docker-webapp-lifecycle.jpg|520]]

*Figure 7: Build and deployment flow from development to Maven WAR and Tomcat runtime*

> [!important] Definition - Containerization
> Containerization packages an application and its runtime dependencies into an
> isolated environment that behaves consistently across machines.

### Containers vs virtual machines

![[docker-containers-stack.jpg|420]]

*Figure 8: Docker container execution stack sharing the host operating-system kernel*

![[docker-vm-stack.jpg|420]]

*Figure 9: Virtual-machine execution stack with hypervisor and separate guest operating systems*

| Aspect | Container | Virtual machine |
|---|---|---|
| Isolation | Process-level isolation, shared host kernel | Full guest OS through hypervisor |
| Startup | Fast | Slower |
| Size | Lightweight | Heavy |
| Portability | High, if Docker is available | Lower, full VM image needed |

### Docker objects

| Object | Role |
|---|---|
| Dockerfile | Recipe for building an image. |
| Image | Immutable, layered, read-only template. |
| Container | Runtime instance of an image with a writable layer. |
| Volume | Persistent storage outside the container writable layer. |
| Network | Private communication channel between containers. |
| Service | Logical application component, e.g. `web` or `db`. |

```dockerfile
FROM tomcat:10
COPY target/app.war /usr/local/tomcat/webapps/app.war
EXPOSE 8080
```

The Dockerfile is declarative: start from a Tomcat image, add the WAR, expose the
port. In a real project, each instruction contributes to image layers.

### Docker Compose

Docker Compose manages multi-container applications through `docker-compose.yml`.

![[docker-compose-webapp-architecture.jpg|520]]

*Figure 10: Docker Compose architecture with Tomcat web service and PostgreSQL database service*

```yaml
services:
  web:
    image: tomcat:10
    ports:
      - "8080:8080"
    depends_on:
      db:
        condition: service_healthy
    volumes:
      - ./crane.war:/usr/local/tomcat/webapps/crane.war

  db:
    image: postgres
    environment:
      - POSTGRES_PASSWORD=postgres
      - POSTGRES_USER=postgres
    volumes:
      - ./crane.sql:/docker-entrypoint-initdb.d/init.sql
      - ./data/db:/var/lib/postgresql/data
    healthcheck:
      test: [ "CMD-SHELL", "pg_isready -U postgres" ]
      interval: 5s
      timeout: 10s
      retries: 50
```

Explanation:
- `web` and `db` are service names. Inside the Compose network, services can use
  those names as hostnames.
- `"8080:8080"` maps host port 8080 to container port 8080.
- The WAR is mounted into Tomcat from the host.
- The SQL script under `/docker-entrypoint-initdb.d/` initializes PostgreSQL on the
  first database creation.
- The DB data volume persists the database even if the container is removed.
- `depends_on` alone only waits for the container to start. The healthcheck waits
  until PostgreSQL is actually ready.

Essential commands:

```bash
docker-compose up
docker-compose down
docker ps
docker ps -a
docker exec <container-name> <command>
```

`docker-compose up` creates and starts the services. `docker-compose down` stops and
removes containers. `docker exec` is useful for debugging, for example to open a
`psql` shell inside the PostgreSQL container.

**Open-question focus:** explain why Docker solves environment mismatch, how image,
container, and volume differ, and why healthchecks matter in a Tomcat + PostgreSQL
setup.

### Extended study notes

The deployment environment problem is broader than "installing Tomcat". A Web
application depends on versions, configuration, ports, environment variables,
database initialization scripts, file-system paths, network visibility, and startup
order. Maven produces an artifact, usually a WAR, but it does not say where the DBMS
runs or whether PostgreSQL is ready when Tomcat starts.

Docker moves that environment description closer to the project. A Docker image
contains the runtime filesystem needed by an application component. A container is a
running instance of that image. The image is immutable; the container has a writable
layer on top. If a container is removed, data in that writable layer disappears unless
it was stored in a volume.

This distinction is very important for databases. PostgreSQL data must be persistent,
so it belongs in a volume or bind mount. A Tomcat container running a WAR can often
be recreated from the image and mounted artifact. Database state cannot be recreated
unless it is only test data generated from initialization scripts.

The Dockerfile describes how to build an image. Docker Compose describes how several
containers form one application. In the course example, Tomcat and PostgreSQL are
separate services because they are separate application components with different
lifecycles and persistent-state requirements.

Port mapping can be misunderstood. This line:

```yaml
ports:
  - "8080:8080"
```

means host port 8080 is forwarded to container port 8080. It is used to reach Tomcat
from the host browser. It is not how containers normally talk to each other inside
the Compose network. Inside the network, `web` can reach `db` by service name.

The PostgreSQL initialization convention is also relevant:

```yaml
volumes:
  - ./crane.sql:/docker-entrypoint-initdb.d/init.sql
```

Scripts in `/docker-entrypoint-initdb.d/` run when the database storage is initialized
for the first time. If the data directory already exists, those scripts are not
automatically re-run. This is why deleting or preserving the DB volume changes the
behavior of subsequent starts.

`depends_on` controls startup dependency, but by itself it only means "start this
container after that one". A container may be running while the application inside it
is still initializing. For databases this is common: PostgreSQL may need several
seconds before accepting connections.

The healthcheck fixes that:

```yaml
healthcheck:
  test: [ "CMD-SHELL", "pg_isready -U postgres" ]
  interval: 5s
  timeout: 10s
  retries: 50
```

`pg_isready` checks whether PostgreSQL can accept connections. Combined with:

```yaml
depends_on:
  db:
    condition: service_healthy
```

Tomcat starts only after the database is declared healthy.

Container vs VM exam answer:

| Point | Container | Virtual machine |
|---|---|---|
| Kernel | Shared host kernel. | Separate guest OS kernel. |
| Isolation cost | Lower. | Higher. |
| Startup | Fast. | Slower. |
| Typical use | Package services and dependencies. | Full OS isolation. |

Do not say containers are "less isolated" as if they are not isolated at all. They
are isolated processes with their own filesystem, network namespace, and runtime
configuration, but they do not emulate a complete computer.

---

## 4. Java Servlets

### Browser-server architecture

![[servlet-browser-server-architecture.jpg|520]]

*Figure 11: Browser-server architecture for a servlet-based Web application*

The browser renders HTML/CSS, executes JavaScript, maintains the DOM, and sends HTTP
requests. The web server parses requests, performs access control, dispatches to
static or dynamic resources, logs activity, and sends responses.

### Jakarta EE and Tomcat

**Jakarta EE** is the standardized platform for enterprise web applications.
**Tomcat** is a web container: it implements the servlet/JSP part of the platform and
executes web components.

Package naming matters:
- Tomcat 9 uses Java EE style `javax.*`.
- Tomcat 10+ uses Jakarta EE style `jakarta.*`.

### Servlet definition and lifecycle

> [!important] Definition - Servlet
> A servlet is a Java-based web component, managed by a web container, that generates
> dynamic content in response to requests.

Servlets usually extend `HttpServlet`. The container controls the lifecycle:

1. `init(ServletConfig)` runs once after servlet creation.
2. `service(req, res)` runs for each request.
3. `service()` dispatches to `doGet`, `doPost`, `doPut`, `doDelete`, etc.
4. `destroy()` runs once before the servlet is taken out of service.

Servlets are **not automatically thread-safe**. Several concurrent requests may use
the same servlet instance. Request-specific data must stay in local variables, not in
shared instance fields.

![[servlet-sequence-diagram.jpg|520]]

*Figure 12: First servlet request sequence from browser request to generated HTML response*

### `web.xml` mapping

```xml
<servlet>
  <servlet-name>HelloWorld</servlet-name>
  <servlet-class>it.unipd.dei.webapp.HelloWorldServlet</servlet-class>
</servlet>

<servlet-mapping>
  <servlet-name>HelloWorld</servlet-name>
  <url-pattern>/hello</url-pattern>
</servlet-mapping>
```

Explanation: the container maps `/hello` to `HelloWorldServlet`. A servlet can have
multiple URL patterns.

`WEB-INF/` is not directly accessible from the browser. It contains private web app
configuration such as `web.xml`, libraries, and compiled classes.

### Minimal servlet response

```java
public class HelloWorldServlet extends HttpServlet {
    public void doGet(HttpServletRequest req, HttpServletResponse res)
            throws ServletException, IOException {

        res.setContentType("text/html; charset=utf-8");

        PrintWriter out = res.getWriter();
        out.printf("<!DOCTYPE html>%n");
        out.printf("<html lang=\"en\">%n");
        out.printf("<body>%n");
        out.printf("<p>Hello, world!</p>%n");
        out.printf("</body>%n");
        out.printf("</html>%n");
        out.flush();
        out.close();
    }
}
```

Explanation:
- `setContentType` sets the MIME type and character encoding.
- `getWriter` obtains the response body writer.
- The servlet manually writes HTML.
- The writer is flushed and closed after writing.

Manual HTML generation works for tiny examples, but becomes hard to maintain. This
is why JSP and MVC are introduced later.

### Logging with Log4J

Log4J separates:

| Concept | Role |
|---|---|
| Logger | Emits log messages. |
| Appender | Destination: console, file, rolling file, etc. |
| Layout | Format of the log line. |
| Level | Filters messages: `TRACE < DEBUG < INFO < WARN < ERROR < FATAL`. |

`ThreadContext` / MDC stores request-scoped metadata such as IP, user, action, and
resource. The pattern is:

```java
LogContext.setIPAddress(req.getRemoteAddr());
LogContext.setAction("CREATE_EMPLOYEE");
try {
    // process request
    LOGGER.info("Request served.");
} finally {
    LogContext.removeIPAddress();
    LogContext.removeAction();
}
```

The `finally` cleanup matters because servlet containers reuse threads. If MDC data
is not removed, the next request handled by the same thread could inherit the wrong
logging context.

### GET and POST forms

```html
<form method="GET" action="../helloworld-get">
  <input name="helloName" type="text">
  <button type="submit">Submit</button>
</form>

<form method="POST" action="../helloworld-post">
  <input name="helloName" type="text">
  <button type="submit">Submit</button>
</form>
```

GET puts parameters in the URL query string. POST sends them in the request body.
In servlets, both can be read with:

```java
String name = req.getParameter("helloName");
```

**Open-question focus:** know servlet lifecycle, `HttpServletRequest` vs
`HttpServletResponse`, `doGet` vs `doPost`, URL mapping, WAR packaging, and why
servlet instance variables are dangerous.

### Extended study notes

Servlets are the first server-side programming model in the course. The most
important idea is that the servlet code does not run as an ordinary `main()` program.
It runs inside a Web container. The container creates servlet instances, initializes
them, passes request and response objects, manages threads, and eventually destroys
the servlet.

The request object represents what the client sent. It exposes parameters, headers,
cookies, session information, body streams, remote address, method, and URI. The
response object represents what the server will send back. It lets the servlet set
status codes, headers, content type, character encoding, cookies, and body content.

`HttpServlet` already implements generic request dispatch. In ordinary servlet code,
developers override `doGet()` or `doPost()` rather than `service()`. REST dispatchers
are an exception because they need centralized method and path routing for several
HTTP methods.

GET and POST are not just "visible" vs "invisible". GET is intended for retrieving
information and should be safe. Parameters are in the query string and can be cached,
bookmarked, or logged. POST sends data in the body and is used for operations that
submit data, often creating or changing state.

The servlet response pattern is always similar:

```java
res.setStatus(HttpServletResponse.SC_OK);
res.setContentType("text/html; charset=utf-8");
try (PrintWriter out = res.getWriter()) {
    out.printf("<p>Hello</p>%n");
}
```

The course examples explicitly flush and close the writer. In modern Java,
try-with-resources is also a common way to ensure cleanup. The key theory point is
that the servlet is responsible for producing a valid HTTP response body and matching
`Content-Type`.

WAR packaging places files where the container expects them:

```text
webapp root
  html/, css/, js/, jsp/, media/
  WEB-INF/
    web.xml
    lib/
    classes/
```

Files under `WEB-INF` are private. A user can request `/html/page.html`, but not
`/WEB-INF/web.xml`. The container can read `WEB-INF`, but it does not expose it as a
static public directory.

Thread safety is a classic exam trap. The container may use one servlet instance for
many requests at the same time. This is bad:

```java
public class BadServlet extends HttpServlet {
    private String currentUser;

    public void doGet(HttpServletRequest req, HttpServletResponse res) {
        currentUser = req.getParameter("user");
    }
}
```

Two requests can overwrite `currentUser`. Use local variables:

```java
public void doGet(HttpServletRequest req, HttpServletResponse res) {
    String currentUser = req.getParameter("user");
}
```

Logging with MDC has the same concurrency concern. The context is thread-local, so
it must be cleared in `finally` before the container reuses that thread.

Servlet answer template:

```text
A servlet is a Java Web component managed by a Web container. The container calls
init once, service for each request, and destroy once at shutdown. In HTTP servlets,
service dispatches to doGet, doPost, doPut, and so on. The request object contains
client data; the response object is used to set status, headers, content type, and
body. Servlets must avoid request-specific instance variables because the same
servlet instance can serve concurrent requests.
```

---

## 5. Servlets and Database Access

### Application structure

The employee application is divided into layers:

| Layer | Classes / technologies |
|---|---|
| Interface/application logic | Servlets parse HTTP parameters, call DAOs, create responses. |
| Data logic | DAO classes contain SQL and JDBC operations. |
| Data layer | PostgreSQL stores `Employee` and `Manage` tables. |

### Resource classes

Resource classes are Java objects representing domain data.

```java
public class Employee {
    private final int badge;
    private final String surname;
    private final int age;
    private final int salary;

    public Employee(int badge, String surname, int age, int salary) {
        this.badge = badge;
        this.surname = surname;
        this.age = age;
        this.salary = salary;
    }

    public final int getBadge() { return badge; }
    public final String getSurname() { return surname; }
    public final int getAge() { return age; }
    public final int getSalary() { return salary; }
}
```

Fields are `final`, so the object is immutable after construction. This is safer in
request processing.

`Message` carries success or error information:

| Field | Meaning |
|---|---|
| `message` | Human-readable message. |
| `errorCode` | Application error code, such as `E100`. |
| `errorDetails` | Technical details. |
| `isError` | Distinguishes error and success messages. |

### DAO pattern

> [!important] Definition - DAO
> A Data Access Object encapsulates all logic needed to access a data source. Servlets
> should not contain SQL; they should call DAOs.

![[db-dao-interface.jpg|520]]

*Figure 13: DAO interface used to isolate database access from servlet logic*

```java
public interface DataAccessObject<T> {
    DataAccessObject<T> access() throws SQLException;
    T getOutputParam();
}
```

`access()` performs the database operation. `getOutputParam()` returns the result,
for example a `List<Employee>`.

```java
String sql = "SELECT badge, surname, age, salary FROM Employee WHERE salary > ?";
PreparedStatement pstmt = con.prepareStatement(sql);
pstmt.setInt(1, salary);
ResultSet rs = pstmt.executeQuery();
```

Explanation:
- The SQL structure is fixed.
- `?` is a placeholder.
- `setInt` binds the user value as data.
- The database cannot interpret that value as SQL syntax.

This is the core defense against SQL injection.

### Connection pool

Opening a new database connection for every request is expensive. Tomcat can manage
a connection pool exposed through JNDI.

```xml
<Resource name="jdbc/employee-ferro"
          auth="Container"
          type="javax.sql.DataSource"
          driverClassName="org.postgresql.Driver"
          url="jdbc:postgresql://localhost:5432/esami"
          username="ferro"
          password="ferro"
          maxActive="10"
          minIdle="5"
          validationQuery="SELECT 1" />
```

Servlets look up the `DataSource` once in `init()`:

```java
InitialContext cxt = new InitialContext();
ds = (DataSource) cxt.lookup("java:/comp/env/jdbc/employee-ferro");
```

Then each request borrows a connection with `ds.getConnection()`.

### Request flow

![[db-create-employee-sequence.jpg|520]]

*Figure 14: Create-employee sequence through servlet, DAO, and database*

Create Employee:
1. Browser submits `POST /create-employee`.
2. Servlet parses parameters.
3. Servlet builds an `Employee`.
4. Servlet gets a pooled DB connection.
5. `CreateEmployeeDAO.access()` performs the `INSERT`.
6. Servlet creates a `Message`.
7. Servlet returns an HTML response.

![[db-search-employee-sequence.jpg|500]]

*Figure 15: Search-employee-by-salary sequence returning a list of domain objects*

Search by salary:
1. Servlet parses the salary threshold.
2. `SearchEmployeeBySalaryDAO` executes `SELECT ... WHERE salary > ?`.
3. Rows are mapped into `Employee` objects.
4. The list becomes `outputParam`.
5. Servlet renders an HTML table.

**Open-question focus:** explain why DAO improves separation of concerns and security.
Be able to describe JNDI + connection pool + servlet + DAO as one flow.

### Extended study notes

The database chapter is where the course moves from "a servlet can answer a request"
to "a servlet participates in a layered application". The main design rule is that
SQL must be isolated from request-handling code. Servlets know HTTP. DAOs know SQL.
Resource classes carry domain data between the two.

The `Employee` class is intentionally simple. It is a value object: badge, surname,
age, salary. Making fields `final` means the object cannot silently change after it
has been created. In a multithreaded Web application, immutability reduces accidental
sharing bugs.

`Message` is not a database entity. It is a response helper. It lets the application
use one object for both success and failure cases. This makes servlet code cleaner:
the servlet can set a `Message` and later decide how to render it.

The DAO interface:

```java
DataAccessObject<T> access() throws SQLException;
T getOutputParam();
```

is deliberately generic. Some operations are commands and return no meaningful
domain data. Others are queries and return a list or single object. The type
parameter `T` lets both cases use the same pattern.

`AbstractDAO` centralizes cross-cutting database concerns:

| Concern | Why it belongs in `AbstractDAO` |
|---|---|
| Connection closing | Every DAO must release the JDBC connection. |
| Rollback on error | Failed operations must not leave partial transactions. |
| One-shot execution | A DAO instance should not accidentally execute twice. |
| Logging | DB failures should be recorded consistently. |

`CreateEmployeeDAO` and `SearchEmployeeBySalaryDAO` then implement only the specific
SQL operation. This is good object-oriented design because shared mechanics are not
duplicated in every DAO.

`PreparedStatement` is central:

```java
String sql = "INSERT INTO Employee (badge, surname, age, salary) VALUES (?, ?, ?, ?)";
PreparedStatement ps = con.prepareStatement(sql);
ps.setInt(1, employee.getBadge());
ps.setString(2, employee.getSurname());
ps.setInt(3, employee.getAge());
ps.setInt(4, employee.getSalary());
ps.execute();
```

The SQL template is fixed before user data is inserted. The values are sent as typed
parameters. Even if the surname contains quotes or SQL-looking text, it remains a
string value, not executable SQL.

Connection pooling is a performance and resource-management mechanism. Without a
pool, each request would pay the cost of opening a TCP connection, authenticating,
and initializing the JDBC session. With a pool, Tomcat maintains ready connections
and the servlet borrows one for the duration of the request.

The moving parts fit together like this:

```text
context.xml
  defines DataSource as jdbc/employee-ferro

web.xml
  declares resource-ref for the application

AbstractDatabaseServlet.init()
  performs JNDI lookup with java:/comp/env/jdbc/employee-ferro

Concrete servlet.doPost()
  calls getConnection()
  creates DAO
  calls access()
```

`InitialContext` is the JNDI lookup API. It is not the same thing as
`ServletContext`. `ServletContext` represents the Web application context; JNDI is a
naming service used to find resources such as the connection pool.

Error handling in the employee example has semantic meaning:

| Code | Meaning |
|---|---|
| `E100` | Input format error, such as non-integer badge, age, or salary. |
| `E200` | Unexpected SQL/database error. |
| `E300` | Duplicate key, identified by PostgreSQL SQLState `23505`. |

A strong open answer should mention both architecture and security: DAO separates
servlet logic from persistence, and prepared statements prevent SQL injection by
separating SQL code from user data.

---

## 6. JSP and MVC

### Why JSP

Writing HTML with `out.printf` inside servlets is fragile and unreadable. JSP lets
developers write mostly HTML, with controlled dynamic parts.

> [!important] Definition - JSP
> A JavaServer Page is a template-based server-side view. On first request, the
> container translates the `.jsp` file into a servlet, compiles it, and executes it.

![[Pasted image 20260512115326.png|420]]

*Figure 16: JSP translation and execution flow from JSP source to servlet class and HTML response*

First invocation: `hello.jsp -> hello_jsp.java -> hello_jsp.class -> response`.
Later invocations reuse the compiled servlet class.

### JSP components

| Component | Syntax | Role |
|---|---|---|
| Template text | HTML | Static output. |
| Page directive | `<%@ page ... %>` | Page-level settings, such as content type. |
| Taglib directive | `<%@ taglib ... %>` | Makes JSTL/custom tags available. |
| Standard action | `<jsp:useBean>` | JSP standard operations. |
| JSTL tag | `<c:if>`, `<c:forEach>` | View logic without Java scriptlets. |
| Expression Language | `${employee.badge}` | Access beans, scopes, params. |
| Scriptlet | `<% ... %>` | Raw Java in JSP; avoid. |

```jsp
<%@ page contentType="text/html;charset=UTF-8" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>

<c:choose>
  <c:when test="${empty param.helloName}">
    <div>Please, enter your name!</div>
  </c:when>
  <c:otherwise>
    <div>Hello, <c:out value="${param.helloName}"/>!</div>
  </c:otherwise>
</c:choose>
```

Explanation:
- `${param.helloName}` reads request parameter `helloName`.
- `empty` checks null or empty string.
- `<c:out>` escapes HTML/XML characters, so it is safer than raw output.

### JavaBeans and EL

JavaBeans expose properties through methods like `getBadge()` and `isError()`.
Expression Language resolves:

```jsp
${employee.badge}
```

as a call to:

```java
employee.getBadge()
```

### MVC

> [!important] Definition - MVC
> Model-View-Controller separates application state and logic (Model), rendering
> (View), and input handling / flow control (Controller).

![[jsp-mvc-layers-employee.jpg|480]]

*Figure 17: Mapping of MVC roles to servlet controllers, JSP views, DAOs, and resource classes*

| MVC role | Java web technology |
|---|---|
| Model | Java resource classes and DAOs. |
| View | JSP pages. |
| Controller | Servlets. |

The servlet no longer writes all HTML. It sets request attributes and forwards to a
JSP.

```java
req.setAttribute("employee", e);
req.setAttribute("message", m);
req.getRequestDispatcher("/jsp/create-employee-result.jsp").forward(req, res);
```

Then the JSP reads the model:

```jsp
<c:out value="${employee.badge}"/>
<c:out value="${message.message}"/>
```

`forward()` is server-side: the browser still receives a single HTTP response.

### Result JSP example

```jsp
<c:import url="/jsp/include/show-message.jsp"/>

<c:if test="${not empty employee && !message.error}">
  <ul>
    <li>badge: <c:out value="${employee.badge}"/></li>
    <li>surname: <c:out value="${employee.surname}"/></li>
    <li>age: <c:out value="${employee.age}"/></li>
    <li>salary: <c:out value="${employee.salary}"/></li>
  </ul>
</c:if>
```

Explanation:
- `<c:import>` dynamically includes a shared JSP fragment.
- `<c:if>` conditionally renders a block.
- `<c:out>` escapes user-controlled data and prevents simple XSS.

JSTL must be bundled in the WAR; Tomcat does not provide it by default. Servlet API
is usually `provided`, JSTL is not.

**Open-question focus:** explain the JSP execution model, why scriptlets are bad,
how EL resolves bean properties, and how MVC changes the servlet-only architecture.

### Extended study notes

JSP should be understood as a view technology, not as a replacement for all server
logic. Technically, a JSP becomes a servlet. Architecturally, it should be used to
render a response, not to contain database access or business logic.

The first request to a JSP is slower because the container must translate and compile
the page. After that, the generated servlet class can be reused. This explains the
exam statement: JSP is preprocessed into a servlet and then the servlet processes the
request.

Scriptlets are discouraged because they mix Java control logic with HTML structure.
For example:

```jsp
<% if (message.isError()) { %>
  <p>Error</p>
<% } %>
```

This works, but it is hard to read, test, and maintain. The JSTL version keeps view
logic in tag form:

```jsp
<c:if test="${message.error}">
  <p>Error</p>
</c:if>
```

The important difference is not only syntax. JSTL and EL encourage a cleaner
separation: the servlet prepares objects; the JSP renders them.

EL property access depends on naming conventions:

| EL expression | Java method called |
|---|---|
| `${employee.badge}` | `employee.getBadge()` |
| `${message.error}` | `message.isError()` |
| `${param.salary}` | request parameter named `salary` |
| `${sessionScope.user}` | session attribute named `user` |

The course resource classes are "almost JavaBeans": they have getters, but no
no-argument constructor and no setters because they are immutable. EL can still read
their properties because getter names are present.

`<c:out>` matters for security. This:

```jsp
<c:out value="${employee.surname}"/>
```

escapes special characters. If the surname contains `<script>`, it is displayed as
text rather than executed as markup. Bare `${employee.surname}` can be dangerous when
rendering user-controlled data.

`<c:url>` matters for portability:

```jsp
<form method="POST" action="<c:url value="/create-employee"/>">
```

The application may be deployed under different context paths. Hard-coding
`/create-employee` may point to the server root, not the application root. `<c:url>`
adds the correct context path and can also handle URL rewriting for sessions.

MVC flow in the employee app:

```text
form JSP
  -> POST request
  -> servlet controller
  -> DAO/model operation
  -> request attributes
  -> RequestDispatcher.forward()
  -> result JSP
  -> HTML response
```

The servlet is the Controller because it interprets the request and decides what to
do. The DAO/resource objects are the Model because they represent data and operations.
The JSP is the View because it renders output.

Forward vs redirect:

| Mechanism | Where it happens | Browser sees new request? | Request attributes preserved? |
|---|---|---|---|
| `forward()` | Server-side | No | Yes |
| redirect | Client-side through 3xx response | Yes | No |

The notes use `forward()` because the servlet wants to pass model objects to the JSP
in request scope. A redirect would lose those request attributes unless the data were
stored somewhere else.

JSTL dependencies must be packaged in the WAR. Marking JSTL as `provided` would be a
mistake unless the runtime container supplies it. In the course setup, Tomcat
provides the servlet API, not JSTL.

Open-answer template:

```text
JSP pages solve the problem of writing HTML inside Java strings. At runtime a JSP is
translated into a servlet, compiled, and executed by the container. In MVC, servlets
act as controllers: they parse input, call model/DAO code, set request attributes,
and forward to JSP views. JSP pages use EL and JSTL to render data without Java
scriptlets. This separates controller logic from presentation and makes the Web
application easier to maintain.
```

---

## 7. REST Web Services

### REST principles

> [!important] Definition - REST
> REST, Representational State Transfer, is an architectural style that applies Web
> principles to services. Data is modeled as resources, resources are identified by
> URIs, and HTTP methods form a uniform interface.

![[Pasted image 20260512123223.png|420]]

*Figure 18: REST model based on resources, representations, and state transitions*

A **resource** is anything with identity and state. A resource has a URI and can be
transferred as a representation: JSON, XML, HTML, etc.

| HTTP method | CRUD meaning | Example |
|---|---|---|
| GET | Read | `GET /student/123456` |
| POST | Create subordinate resource | `POST /student` |
| PUT | Create or replace resource | `PUT /student/123456` |
| DELETE | Delete | `DELETE /student/123456` |

REST is stateless: each request must carry all information needed to process it.

A **Web service** is a software system designed to support interoperable
machine-to-machine interaction over a network using standard Web technologies. REST
is one way to design such services.

### Representations and content negotiation

The same resource can have different representations:

```http
GET /student/123456 HTTP/1.1
Accept: application/json
```

```json
{
  "student": {
    "badge": 123456,
    "name": "Mario",
    "surname": "Rossi"
  }
}
```

The `Accept` header says which response media types the client can process.
For POST/PUT, `Content-Type` says what media type the request body has.

### Employee REST API

| URI | Method | Meaning |
|---|---|---|
| `/rest/employee` | GET | List all employees. |
| `/rest/employee` | POST | Create an employee. |
| `/rest/employee/{badge}` | GET | Read one employee. |
| `/rest/employee/{badge}` | PUT | Update one employee. |
| `/rest/employee/{badge}` | DELETE | Delete one employee. |
| `/rest/employee/salary/{salary}` | GET | Search by salary threshold. |

```json
{
  "employee": {
    "badge": 7309,
    "surname": "Rossi",
    "age": 34,
    "salary": 45
  }
}
```

Error responses are also JSON resources:

```json
{
  "message": {
    "message": "Unsupported operation.",
    "error-code": "E500",
    "error-details": "OPTIONS"
  }
}
```

### API documentation

REST APIs must be documented precisely. The notes mention two approaches:

| Format | Description |
|---|---|
| WADL | XML description for HTTP-based services; W3C submission, not a dominant standard. |
| OpenAPI | YAML/JSON description of servers, paths, methods, parameters, schemas, and responses; modern de-facto standard. |

OpenAPI is more relevant in practice because it is widely supported by tooling for
documentation, validation, and client generation.

### REST implementation pattern

![[rest-employee-class-diagram.jpg|420]]

*Figure 19: REST employee application class structure with resources, REST handlers, DAOs, and dispatcher*

Key classes:

| Component | Responsibility |
|---|---|
| `Resource` | Anything serializable to JSON through `toJSON(OutputStream)`. |
| `AbstractResource` | Shared JSON factory and template method. |
| `Employee` | Domain resource; can write/read JSON. |
| `Message` | Error/info JSON resource. |
| `ResourceList<T>` | JSON list of resources. |
| `RestResource` | Handler with `serve()`. |
| `AbstractRR` | Checks media types, wraps errors, delegates to `doServe()`. |
| `RestDispatcherServlet` | Front controller for `/rest/*`. |

```java
public interface Resource {
    void toJSON(OutputStream out) throws IOException;
}
```

Writing JSON with Jackson:

```java
JsonGenerator jg = JSON_FACTORY.createGenerator(out);
jg.writeStartObject();
jg.writeFieldName("employee");
jg.writeStartObject();
jg.writeNumberField("badge", badge);
jg.writeStringField("surname", surname);
jg.writeNumberField("age", age);
jg.writeNumberField("salary", salary);
jg.writeEndObject();
jg.writeEndObject();
jg.flush();
```

Explanation: the generator writes tokens in order. `flush()` sends buffered data to
the servlet response stream. The code disables Jackson auto-close so it does not
close the servlet's stream unexpectedly.

### Header validation

`checkMethodMediaType()` validates REST requests:

| Case | Error |
|---|---|
| Missing `Accept` | `E4A1`, 400 |
| Unsupported `Accept` | `E4A2`, 406 |
| Missing `Content-Type` on POST/PUT | `E4A3`, 400 |
| Unsupported input media type | `E4A4`, 415 |
| Unsupported HTTP method | `E4A5`, 405 |
| Unknown resource | `E4A6`, 404 |

### REST dispatcher

`RestDispatcherServlet` overrides `service()` because it must support `GET`, `POST`,
`PUT`, `DELETE`, and dispatch by both URI and method.

```xml
<servlet-mapping>
  <servlet-name>RestManagerServlet</servlet-name>
  <url-pattern>/rest/*</url-pattern>
</servlet-mapping>
```

**Open-question focus:** explain REST resources, URIs, methods, representations,
`Accept` vs `Content-Type`, error status codes, and why a REST front controller
dispatches all `/rest/*` requests.

### Extended study notes

REST is often reduced to "JSON over HTTP", but that is incomplete. JSON is only one
possible representation. The real REST ideas are resource identification, uniform
interface, stateless communication, and representation transfer.

A URI should identify a resource, not an operation name. Prefer:

```text
GET /rest/employee/7309
DELETE /rest/employee/7309
```

over:

```text
GET /deleteEmployee?badge=7309
```

The operation is expressed by the HTTP method. The URI identifies the target
resource. This is the uniform interface principle.

Collection resource vs item resource:

| Resource kind | Example URI | Meaning |
|---|---|---|
| Collection | `/rest/employee` | The set of employees. |
| Item | `/rest/employee/7309` | Employee with badge 7309. |
| Filtered collection | `/rest/employee/salary/45` | Employees satisfying a salary filter. |

`Accept` and `Content-Type` are different:

| Header | Direction | Question answered |
|---|---|---|
| `Accept` | client -> server | What response formats can I accept? |
| `Content-Type` | sender -> receiver | What is the format of this body? |

For a `GET`, there is usually no request body, so `Content-Type` is often irrelevant.
For a `POST` or `PUT` with JSON body, `Content-Type: application/json` is essential.

Status codes should match the failure:

| Situation | Typical status |
|---|---|
| Created new resource | `201 Created` |
| Successful normal response | `200 OK` |
| No body to return | `204 No Content` |
| Malformed request | `400 Bad Request` |
| Unsupported method | `405 Method Not Allowed` |
| Unsupported response media type | `406 Not Acceptable` |
| Conflict, duplicate resource | `409 Conflict` |
| Unsupported request body media type | `415 Unsupported Media Type` |
| Unexpected server failure | `500 Internal Server Error` |

The REST implementation mirrors the layered architecture:

```text
RestDispatcherServlet
  routes URI and method
  obtains DB connection
  creates concrete RestResource

AbstractRR
  validates headers and method
  catches unexpected errors
  delegates to doServe()

Concrete RR
  parses JSON if needed
  calls DAO
  writes Resource JSON response
```

`Resource.toJSON(OutputStream)` is a useful abstraction because every response
object can serialize itself. `Employee`, `Message`, and `ResourceList` all become
writeable resources. This avoids having each servlet manually build JSON strings.

Jackson streaming generation is verbose but controlled. It reduces mistakes such as
missing quotes, wrong commas, or invalid escaping. Streaming parsing also avoids
loading an entire JSON object model if only some tokens are needed.

`Employee.fromJSON()` is the inverse of `toJSON()`. It reads the request body and
constructs a domain object. If the JSON does not contain an `"employee"` object, the
REST layer returns a client error because the client supplied the wrong resource
format.

`RestDispatcherServlet` overrides `service()` because a REST endpoint must dispatch
multiple methods. A normal servlet example can use `doGet()` and `doPost()`, but a
front controller receives all `/rest/*` requests and must route them based on both
the method and the path.

OpenAPI vs WADL is a documentation question. Both describe HTTP APIs, but OpenAPI is
the modern practical standard. It can describe paths, path parameters, query
parameters, request bodies, response schemas, and reusable components.

Open-answer template:

```text
In REST, the application exposes resources identified by URIs. Clients operate on
those resources through the uniform HTTP interface: GET for reading, POST for
creating, PUT for replacing/updating, DELETE for deleting. A resource can have
multiple representations, such as JSON or XML, negotiated through Accept. Requests
are stateless, so every request must contain the information needed to process it.
The employee API follows this model with collection, item, and filtered collection
URIs under /rest/employee.
```

---

## 8. HTTP and Surroundings

### Four Web pillars

| Standard | Role |
|---|---|
| HTML | Markup language for web pages. |
| HTTP | Application-layer request/response protocol. |
| MIME | Media type and encoding of exchanged information. |
| URL | Locates resources on the Web. |

### URI, URL, URN, IRI

> [!important] Definition - URI
> A URI is a compact sequence of characters that identifies an abstract or physical
> resource.

| Term | Meaning | Example |
|---|---|---|
| URI | Generic identifier | any valid identifier syntax |
| URL | URI that also gives a location/access mechanism | `https://example.org/page` |
| URN | Persistent name using `urn:` scheme | `urn:isbn:978-951-0-18435-6` |
| IRI | URI extended with Unicode characters | URL with non-ASCII characters |

General syntax:

```text
scheme:[//[user[:password]@]host[:port]][/path][?query][#fragment]
```

`path` identifies hierarchical resource location, `query` carries name/value
parameters, and `fragment` identifies a secondary resource inside the representation.

### Percent-encoding and character encoding

Percent-encoding writes an octet as `%XX` in hexadecimal. It is used for reserved
characters and non-ASCII characters in URIs.

| Character | Encoding |
|---|---|
| space | `%20` |
| `?` | `%3F` |
| `&` | `%26` |
| `#` | `%23` |

ASCII uses 7 bits and covers 128 characters. Extended ASCII uses 8 bits but creates
country-specific incompatibilities. Unicode provides a universal character set.
UTF-8 is the dominant Web encoding and is backward-compatible with ASCII for the
first 128 characters.

### MIME

> [!important] Definition - MIME
> MIME defines media types and transfer encodings for email and the Web.

Important headers:

| Header | Meaning |
|---|---|
| `Content-Type` | Media type of body, e.g. `text/html; charset=utf-8`. |
| `Content-Encoding` | Compression applied to body, e.g. `gzip`. |
| `Content-Disposition` | Suggested handling, e.g. attachment filename. |
| `Content-Transfer-Encoding` | Encoding for binary transport, e.g. Base64. |

### Multipart and form encodings

`multipart/form-data` is used for file uploads. Each field or file is a separate MIME
part separated by a boundary.

```http
Content-Type: multipart/form-data; boundary=AaB03x

--AaB03x
Content-Disposition: form-data; name="submit-name"

Nicola
--AaB03x
Content-Disposition: form-data; name="files"; filename="file.pdf"
Content-Type: application/pdf

...binary content...
--AaB03x--
```

`application/x-www-form-urlencoded` is simpler and used for normal fields:

```text
submit-name=Nicola&submit-surname=Ferro
```

Servlet file upload uses the `Part` API:

```java
for (Part p : req.getParts()) {
    String name = p.getName();
    String contentType = p.getContentType();
    InputStream in = p.getInputStream();
}
```

Always validate file type server-side. The HTML `accept` attribute is only a client
hint and can be bypassed.

The extended employee example combines multipart upload and email:

1. The JSP form uses `method="POST"` and `enctype="multipart/form-data"`.
2. The servlet iterates over `req.getParts()`.
3. Text fields are read from part input streams.
4. The photo part is checked with `p.getContentType()`.
5. Photo bytes and media type are stored in the DB.
6. A confirmation email is sent with Jakarta Mail.
7. A separate servlet can stream the photo back with the original MIME type.

```java
if (e.hasPhoto()) {
    res.setContentType(e.getPhotoMediaType());
    res.getOutputStream().write(e.getPhoto());
} else {
    res.setStatus(HttpServletResponse.SC_NO_CONTENT);
}
```

Jakarta Mail models messages through `Session`, `MimeMessage`, `Transport`,
`MimeMultipart`, and `MimeBodyPart`. An email with an attachment is
`multipart/mixed`: one body part for the HTML/text message and one body part for the
binary attachment.

### HTTP

![[http-proxy-architecture.jpg|420]]

*Figure 20: HTTP request-response chain with browser, proxies, and origin web server*

HTTP is textual, request-response based, and stateless. Statelessness simplifies
scalability because each request can be handled independently.

| Method | Meaning | Safe | Idempotent |
|---|---|---|---|
| GET | Retrieve resource | yes | yes |
| HEAD | GET without response body | yes | yes |
| POST | Submit data/create subordinate resource | no | no |
| PUT | Store/replace resource | no | yes |
| DELETE | Delete resource | no | yes |
| OPTIONS | Communication options | yes | yes |

**Safe** means no intended server-side side effects. **Idempotent** means repeating
the same request has the same effect as doing it once.

Status code classes:

| Class | Meaning |
|---|---|
| 1xx | Informational. |
| 2xx | Success, e.g. `200 OK`, `201 Created`, `204 No Content`. |
| 3xx | Redirection, often with `Location`. |
| 4xx | Client error, e.g. `400`, `401`, `404`, `405`, `409`, `415`. |
| 5xx | Server error, e.g. `500`. |

### Authentication

HTTP Basic authentication:

```http
Authorization: Basic bmljb2xhOmZlcnJv
```

The value is Base64 of `username:password`. Base64 is encoding, not encryption.
Basic auth must be used with HTTPS.

If credentials are missing or wrong, the server answers:

```http
HTTP/1.1 401 Unauthorized
WWW-Authenticate: Basic realm="Webapp"
```

### Filters and sessions

A Servlet `Filter` can protect paths before requests reach servlets/JSPs.

```java
HttpSession session = req.getSession(false);
if (session == null) {
    if (!authenticateUser(req, res)) return;
}
chain.doFilter(req, res);
```

Explanation:
- `getSession(false)` does not create a new session.
- If no valid session exists, the filter tries Basic authentication.
- If authentication succeeds, it stores the user in `HttpSession`.
- `chain.doFilter` lets the request continue.

**Open-question focus:** URI vs URL, percent-encoding, MIME multipart boundaries,
safe/idempotent HTTP methods, status code classes, Basic auth, and filter/session
authentication are all high-value theory topics.

### Extended study notes

The HTTP chapter is dense because it contains several definitions that look similar.
For an open question, definitions must be clean and examples help a lot.

URI is the broad concept. URL is a URI that also tells how to locate the resource.
URN is a URI intended as a persistent name. IRI generalizes URI syntax to
international characters. Therefore, every URL is a URI, but not every URI is a URL.

The fragment part of a URI is not sent to the server in an ordinary HTTP request. It
is interpreted by the client to identify a secondary resource inside the returned
representation. For example:

```text
https://example.org/page.html#bottom
```

identifies the `bottom` fragment in the page.

Percent-encoding is about bytes, not "random replacement". A character is first
encoded into bytes, commonly UTF-8, and then each byte can be written as `%XX`.
This is why accented letters may become several percent-encoded bytes.

MIME is needed because HTTP bodies are just sequences of bytes. The receiver needs
metadata to know how to interpret those bytes:

```http
Content-Type: text/html; charset=utf-8
Content-Encoding: gzip
Content-Length: 1200
```

`Content-Type` says what the representation is. `Content-Encoding` says whether an
additional encoding such as compression was applied. These are often confused in
multiple-choice questions.

Multipart bodies rely on a boundary that must not appear inside the parts. Each part
has its own headers and content. The final boundary has an extra `--` suffix. This
mechanism is used both in email attachments and HTML file-upload forms.

`application/x-www-form-urlencoded` is simpler than multipart. It is appropriate
when the form contains only ordinary fields. File upload needs `multipart/form-data`
because binary files and metadata must be transmitted as separate parts.

Safe and idempotent are independent concepts:

| Method | Safe? | Idempotent? | Reason |
|---|---|---|---|
| GET | yes | yes | Repeated reads should not change server state. |
| POST | no | no | Repeating may create multiple resources. |
| PUT | no | yes | Repeating same replacement leaves same final state. |
| DELETE | no | yes | After resource is deleted, repeating keeps it deleted. |

This is why retry logic can safely repeat idempotent requests after a network failure,
but repeating a POST may duplicate an operation.

HTTP Basic authentication flow:

```text
Client requests protected resource without credentials.
Server responds 401 + WWW-Authenticate.
Browser asks user for username/password.
Browser sends Authorization: Basic base64(username:password).
Server verifies credentials.
Browser repeats Authorization automatically for same realm.
```

Base64 is reversible. Anyone who sees the header can decode it. HTTPS is required
for confidentiality.

The session-based filter adds application-level state on top of stateless HTTP. The
session identifier is usually stored in a cookie. The server keeps a map from session
ID to attributes, such as the authenticated username.

The protected-resource filter combines Basic auth and sessions:

1. If a valid session with user exists, continue.
2. Otherwise read `Authorization`.
3. Decode credentials.
4. Validate them through a DAO.
5. On success, create session and store user.
6. On failure, send `401` and `WWW-Authenticate`.

`chain.doFilter(req, res)` is the point where the request is allowed to continue to
the target servlet or JSP. If authentication fails and the filter returns before
calling the chain, the protected resource is never reached.

Open-answer template:

```text
HTTP is a stateless textual request-response protocol. Requests contain a method,
URI, headers, and optional body; responses contain a status code, headers, and
optional body. MIME headers such as Content-Type describe the body representation.
Methods have properties: GET is safe and idempotent, POST is neither, PUT and DELETE
are idempotent but not safe. Authentication can be implemented with Basic auth, but
because Base64 is not encryption it must be protected with HTTPS.
```

---

## 9. Markup Languages, XML, and JSON

### Markup types

> [!important] Definition - Markup
> Markup is not the content itself; it is information about the content.

| Type | Meaning | Example |
|---|---|---|
| Punctuational | Syntactic separators | `.`, `,`, `?` |
| Presentational | Layout information | line breaks, page breaks |
| Procedural | Commands describing how to format | "make this red" |
| Descriptive | Describes role or meaning | `<h1>`, `<blockquote>` |
| Referential | Refers to external/replacement entities | `&amp;`, `&copy;` |
| Meta-markup | Defines markup languages | SGML, DTD, XML Schema |

Modern Web design prefers descriptive markup plus CSS presentation.

### SGML, HTML, XML

**SGML** is a meta-markup language and ancestor of HTML and XML. It introduced DTDs.

HTML4 mixed structure and presentation. Example: `<font color="red">` is procedural
because it says how text should look. HTML5 improves separation by using semantic
elements and CSS for presentation.

> [!important] Definition - XML
> XML is a markup language for representing and exchanging semi-structured
> information. It is designed for interoperability among distributed systems.

![[markup-xml-tree.jpg|520]]

*Figure 21: XML document represented as a hierarchical tree of elements, attributes, and text nodes*

XML nodes:

| Node | Meaning |
|---|---|
| Element | Logical grouping, e.g. `<channel>...</channel>`. |
| Attribute | Property in opening tag, e.g. `version="2.0"`. |
| Text | Literal character data. |
| Comment | Ignored content, `<!-- comment -->`. |
| Processing instruction | Instruction to processor, `<?target value?>`. |
| Root | Whole tree. |

### Well-formed vs valid XML

Well-formed XML is syntactically correct:
- matching opening and closing tags,
- properly nested elements,
- quoted attribute values,
- exactly one root element.

Valid XML also satisfies a DTD or XML Schema.

### DOM, SAX, StAX

![[markup-dom-interfaces.jpg|520]]

*Figure 22: DOM interface hierarchy rooted in the generic Node abstraction*

| Parser | Model | Memory | Direction | Good for |
|---|---|---|---|---|
| DOM | In-memory tree | higher | bidirectional | random access, modification |
| SAX | Push streaming callbacks | low | forward only | large read-only XML |
| StAX | Pull streaming | low | forward only | application-controlled parsing |

DOM is the model browsers use for HTML and JavaScript manipulation.

### DTD, namespaces, XSD

DTD defines element and attribute structure:

```xml
<!ELEMENT channel (title, link, description, item+)>
<!ELEMENT title (#PCDATA)>
<!ATTLIST guid isPermaLink (true | false) "false">
```

Operators:
- `,` sequence,
- `|` choice,
- `?` zero or one,
- `*` zero or more,
- `+` one or more.

DTD limitations: no rich data types, non-XML syntax, no namespaces.

XML namespaces prevent name clashes:

```xml
<rss xmlns:html="http://www.w3.org/TR/html4"
     xmlns="http://www.rssboard.org">
  <html:html>...</html:html>
</rss>
```

The URI is used as a unique identifier; it is not necessarily dereferenced.

XML Schema (XSD) uses XML syntax and supports data types:

```xml
<xs:element name="link" type="xs:anyURI"/>
<xs:element name="guid">
  <xs:complexType>
    <xs:simpleContent>
      <xs:extension base="xs:ID">
        <xs:attribute name="isPermaLink" type="xs:boolean" default="false"/>
      </xs:extension>
    </xs:simpleContent>
  </xs:complexType>
</xs:element>
```

### JSON and Jackson

> [!important] Definition - JSON
> JSON is a lightweight, language-independent data interchange format based on
> objects, arrays, strings, numbers, booleans, and null.

![[markup-json-object-syntax.jpg|520]]

*Figure 23: JSON object syntax showing name-value pairs enclosed in braces*

```json
{
  "employee": {
    "badge": 7309,
    "surname": "Rossi",
    "age": 34,
    "salary": 45
  }
}
```

JSON is usually more compact than XML because it has no closing tags and maps
naturally to JavaScript objects.

Jackson streaming parser pattern:

```java
JsonParser jp = JSON_FACTORY.createParser(in);
while (jp.getCurrentToken() != JsonToken.FIELD_NAME
        || !"employee".equals(jp.getCurrentName())) {
    if (jp.nextToken() == null) throw new EOFException("No Employee object found.");
}
```

Explanation: the parser pulls one token at a time, like StAX for XML. This is useful
for streaming large inputs without building a full object tree first.

**Open-question focus:** procedural vs descriptive markup, XML well-formed vs valid,
DOM/SAX/StAX differences, DTD vs XSD, namespaces, JSON vs XML, and Jackson streaming.

### Extended study notes

Markup languages are useful because they add structure to otherwise plain text.
For the exam, the important point is not just that markup uses tags, but that tags
turn a document into something that software can process. A browser can render an
HTML document, an XML parser can build a tree, a validator can compare a document
against a grammar, and an application can extract specific fields without guessing
from visual layout.

The difference between procedural and descriptive markup is a good open-question
topic. Procedural markup gives instructions about presentation or processing. It
tells a program what to do. Descriptive markup identifies the role of a piece of
content. It tells a program what the content is. HTML, especially modern semantic
HTML, should be descriptive: a `<nav>` element describes navigation, while CSS
decides how that navigation looks.

| Aspect | Procedural markup | Descriptive markup |
|---|---|---|
| Main idea | Instruction to process or render content. | Description of the logical role of content. |
| Typical question | "How should this appear?" | "What is this element?" |
| Example | "make this bold" | "this is a heading" |
| Web relevance | Older/presentational style. | Modern HTML and XML data exchange. |

XML is stricter than HTML. In HTML, browsers often recover from errors because
human-facing pages should remain visible. In XML, a single structural error can make
the document not well-formed, so a parser must reject it. This strictness is useful
when XML is used for data interchange: the receiver should not silently guess the
meaning of malformed data.

A complete answer on XML should separate three levels:

1. **Well-formed XML** means that the syntax rules of XML are respected.
2. **Valid XML** means that the document also respects a declared grammar such as a
   DTD or an XML Schema.
3. **Application-level correctness** means that the values make sense for the
   application, even beyond what the grammar can express.

Example of well-formed XML:

```xml
<employee id="42">
  <name>Ada</name>
  <department>Research</department>
</employee>
```

Example of not well-formed XML:

```xml
<employee id="42">
  <name>Ada</department>
</employee>
```

The second example is wrong because the closing tag does not match the opening tag.
A DTD or XSD is not even needed to reject it.

DTD and XSD both define allowed structure, but they belong to different generations
of XML tooling. DTD is older and compact, but it has weak typing and a syntax that
is not XML. XSD is more verbose, but it is itself XML and supports data types,
namespaces, cardinality constraints, and richer validation.

| Feature | DTD | XML Schema (XSD) |
|---|---|---|
| Syntax | Custom non-XML syntax. | XML syntax. |
| Data types | Very limited. | Rich built-in types such as `xs:date`, `xs:int`, `xs:anyURI`. |
| Namespaces | Poor support. | Designed to work with namespaces. |
| Expressiveness | Good for simple document shape. | Better for typed data exchange. |
| Readability | Shorter. | More verbose. |

Namespaces solve collisions between element names from different vocabularies. For
example, `<title>` can mean the title of a book, the title of an HTML page, or the
title of an RSS item. A namespace URI qualifies the vocabulary, so processors can
distinguish names that look the same locally.

```xml
<book xmlns:dc="http://purl.org/dc/elements/1.1/">
  <title>Web Applications</title>
  <dc:title>Course metadata title</dc:title>
</book>
```

The exam may ask about DOM, SAX, and StAX. The clean way to compare them is by
memory usage and control flow:

| Parser model | How it works | Advantages | Disadvantages |
|---|---|---|---|
| DOM | Builds a complete tree in memory. | Easy navigation and modification. | High memory cost for large documents. |
| SAX | Parser pushes events to callbacks. | Low memory cost. | Harder because control is inverted. |
| StAX | Application pulls events from parser. | Low memory and explicit control. | More manual than DOM. |

If a program needs random access to many parts of a small document, DOM is often
comfortable. If the file is huge and the program only needs a few fields, SAX or
StAX is more appropriate.

JSON is not a markup language in the same sense as XML. It does not annotate text
with tags; it represents data as nested objects and arrays. Its advantage in Web
applications is that it maps naturally to JavaScript and is compact. Its weakness is
that it does not carry a standard schema mechanism inside the core format, although
JSON Schema exists as a separate specification.

Compare the same data in XML and JSON:

```xml
<employee>
  <badge>7309</badge>
  <surname>Rossi</surname>
  <active>true</active>
</employee>
```

```json
{
  "badge": 7309,
  "surname": "Rossi",
  "active": true
}
```

The JSON version is shorter and directly usable in JavaScript. The XML version can
be validated with XML tools, can mix vocabularies through namespaces, and can
represent document-like structures with attributes and ordered text nodes.

An open answer about Jackson should mention that streaming parsing avoids loading a
whole JSON document into memory. This is similar in spirit to StAX. The application
asks for the next token, checks whether it is a field name, object start, string,
number, and so on, then decides what to do.

Short answer template:

```text
Markup adds machine-processable structure to text. XML is strict and can be
well-formed or valid. Well-formedness is about XML syntax; validity is about a
grammar such as DTD or XSD. DTD is older and less typed, while XSD is XML-based and
supports namespaces and data types. XML can be parsed with DOM, SAX, or StAX,
depending on memory and control-flow needs. JSON is a compact data format based on
objects and arrays; it is common in Web APIs because it maps naturally to
JavaScript, but it has less built-in validation machinery than XML.
```

---

## 10. HTML5

### Base structure

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>This is the Title of the Page</title>
  </head>
  <body>
    <h1>Main content</h1>
  </body>
</html>
```

Key elements:
- `<!DOCTYPE html>` triggers standards mode.
- `<html>` is the root.
- `<head>` contains metadata, not visible page content.
- `<title>` appears in the browser tab.
- `<body>` contains visible content.
- `<meta charset="utf-8">` declares character encoding.

### Semantic HTML

HTML tags should be chosen for meaning, not visual appearance. Use CSS for visual
style.

Example: do not use `<h1>` only to make text large. Use `<h1>` when the text is the
main heading.

![[html5-block-inline.jpg|520]]

*Figure 24: Difference between block elements and inline elements in normal HTML flow*

| Element type | Behavior | Examples |
|---|---|---|
| Block | Starts on a new line, takes available width | `<p>`, `<h1>`, `<ul>`, `<li>`, `<div>` |
| Inline | Stays inside text flow | `<a>`, `<em>`, `<img>`, `<span>` |

Semantic text:

```html
<strong>important</strong>
<em>emphasized</em>
```

Prefer these over purely presentational `<b>` and `<i>`.

### Links, images, tables, forms

```html
<a href="https://example.org/page.html#bottom">Go to section</a>
<a href="mailto:user@example.org">Email</a>
<a href="tel:+18005551212">Call</a>
```

`href` is the destination. A `#fragment` points to an element with matching `id`.

```html
<figure>
  <img src="figure/quokka.jpg" alt="A family of quokka">
  <figcaption>The quokka is an Australian marsupial.</figcaption>
</figure>
```

`alt` is required for accessibility and fallback. `<figure>` and `<figcaption>`
associate media with its caption.

```html
<form action="/create-employee" method="post">
  <input type="text" name="surname">
  <input type="email" name="email">
  <button type="submit">Submit</button>
</form>
```

`name` is the server-side parameter name. `id` is unique in the page and used by CSS
or JavaScript. Radio buttons share the same `name` to form one group.

### HTML5 semantic layout

![[html5-layout-comparison.jpg|520]]

*Figure 25: Comparison between generic HTML4 div-based layout and semantic HTML5 layout*

| Element | Meaning |
|---|---|
| `<header>` | Header of page or section. |
| `<footer>` | Footer of page or section. |
| `<nav>` | Major navigation block. |
| `<article>` | Self-contained piece of content. |
| `<section>` | Thematic grouping, often with heading. |
| `<aside>` | Related but non-essential content. |

HTML5 layout is clearer than generic `<div id="header">` patterns. It helps
developers, accessibility tools, and search engines.

HTML5 also standardizes APIs that previously required plug-ins or custom solutions:
Media API, Session History, Offline Web Applications, Editing, Drag and Drop,
Canvas, Web Storage, Geolocation, Web Workers, and Web Sockets.

### Media and canvas

```html
<video controls>
  <source src="video.webm" type="video/webm">
  <source src="video.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>
```

Multiple `<source>` elements handle browser format differences.

```html
<canvas width="600" height="400" id="myCanvas">
  Your browser does not support canvas.
</canvas>
```

Canvas creates a drawable rectangle. Actual drawing is done through JavaScript.

**Open-question focus:** base structure, `title`, block vs inline, semantic vs
presentational tags, `id` vs `name`, forms, `<figure>`, semantic layout elements,
and native media/canvas.

### Extended study notes

HTML5 should be understood as both a markup language and a Web platform. As markup,
it defines elements used to structure a document. As a platform, it standardizes
native APIs such as media playback, canvas, storage, geolocation, workers, and
WebSockets. For a theory answer, start from the document structure and then connect
semantic elements to accessibility, search engines, and maintainability.

The minimal HTML5 page has a precise purpose for each part:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Course page</title>
  </head>
  <body>
    <main>
      <h1>Web Applications</h1>
      <p>Course material.</p>
    </main>
  </body>
</html>
```

`<!DOCTYPE html>` is not an HTML tag. It tells the browser to use standards mode
instead of old compatibility behavior. The `lang` attribute helps screen readers,
translation tools, and search engines. The `<title>` element is not a visible
heading; it is metadata shown in the browser tab and used by bookmarks/search
results. The visible page heading should be an `<h1>` inside the body.

Semantic HTML means choosing elements by meaning. This is important because many
agents consume a page: browsers, screen readers, crawlers, validators, CSS
selectors, JavaScript code, and future developers. A `<button>` is better than a
clickable `<div>` because it already has keyboard behavior, focus behavior, and
accessibility semantics.

Bad semantic choice:

```html
<div onclick="save()">Save</div>
```

Better semantic choice:

```html
<button type="button" id="save">Save</button>
```

Then JavaScript can attach behavior without mixing it into the markup:

```javascript
document.getElementById("save").addEventListener("click", save);
```

Block and inline elements are often tested because they affect document flow.
Block-level elements normally start on a new line and take the available width.
Inline elements flow inside text. Modern CSS can change visual display, but the
semantic role of the element should still be chosen correctly.

| Category | Examples | Typical role |
|---|---|---|
| Block / structural | `div`, `p`, `section`, `article`, `header`, `footer` | Page structure or text blocks. |
| Inline / phrasing | `span`, `a`, `em`, `strong`, `code` | Text-level meaning inside a line. |
| Replaced/media | `img`, `video`, `canvas`, `input` | Element whose content is external or special. |

`id` and `name` are different. `id` identifies one element in the document and is
used by CSS, JavaScript, fragment URLs, and labels. `name` is used mainly for form
submission: it becomes the key sent to the server.

```html
<label for="email">Email</label>
<input id="email" name="email" type="email" required>
```

Here `for="email"` points to the element with `id="email"`. When the form is sent,
the browser sends a parameter named `email` because of the `name` attribute.

Forms are the standard way to send user input from the browser to the server.

```html
<form method="post" action="/students">
  <label for="student-id">Student id</label>
  <input id="student-id" name="studentId" required>
  <button type="submit">Save</button>
</form>
```

`method="get"` appends parameters to the URL and is suitable for safe queries such
as search. `method="post"` sends data in the request body and is suitable for
operations that create or modify server state.

Tables should be used for tabular data, not for layout. A good table answer should
mention headings and structure:

```html
<table>
  <caption>Exam sessions</caption>
  <thead>
    <tr><th>Date</th><th>Room</th></tr>
  </thead>
  <tbody>
    <tr><td>June 18</td><td>Aula 1</td></tr>
  </tbody>
</table>
```

`<caption>` gives a human-readable title to the table. `<th>` marks header cells,
which helps accessibility tools associate values with headings.

`<figure>` and `<figcaption>` group media with a caption. In these notes, Obsidian
image embeds are followed by italic Markdown captions, but the HTML idea is the
same: the image and its explanation should stay together.

```html
<figure>
  <img src="architecture.png" alt="Three-tier Web architecture">
  <figcaption>Figure 1: Three-tier Web architecture.</figcaption>
</figure>
```

The `alt` attribute is not a decorative caption. It is fallback text for users who
cannot see the image or when the image cannot load. If the figure caption explains
the image fully, the `alt` text can be shorter, but it should still identify the
image.

HTML5 media elements replace many old plug-in based solutions. A `<video>` or
`<audio>` element can expose native controls, while multiple `<source>` tags let the
browser choose a supported format.

Canvas is different from normal HTML elements. It is a bitmap drawing surface. The
browser does not remember "there is a circle" as an accessible DOM node; JavaScript
draws pixels on a rectangle. This is powerful for games, charts, and custom graphics,
but less semantic than SVG or normal HTML.

Short answer template:

```text
HTML5 defines the structure of Web pages and adds native APIs. A correct document
uses doctype, html, head, metadata, title, and body. Semantic elements such as nav,
main, section, article, aside, header, and footer describe the role of content, not
its appearance. This improves accessibility, search, maintainability, and scripting.
Forms submit named controls to the server, usually with GET for safe queries and
POST for state changes. HTML5 also provides native media and canvas, where canvas is
a JavaScript-controlled bitmap drawing area.
```

---

## 11. Web Security

### CIA triad and attack surface

| Security goal | Meaning |
|---|---|
| Confidentiality | Information is available only to intended users. |
| Integrity | Information is not altered unexpectedly. |
| Availability | Information is accessible when needed. |

![[websec-scenario.jpg|480]]

*Figure 26: Web application attack surface involving users, web server, SQL queries, and database*

In web applications, attackers often have the same HTTP access as normal users. The
vulnerability appears when the application processes input incorrectly.

### SQL Injection

> [!important] Definition - SQL Injection
> SQL injection happens when untrusted user input is mixed with trusted SQL code and
> the database interprets attacker-controlled text as SQL syntax.

![[websec-sqli-flow.jpg|520]]

*Figure 27: SQL injection flow caused by mixing untrusted data with trusted SQL code*

Vulnerable pattern:

```php
$sql = "SELECT Name, Salary, SSN
        FROM employee
        WHERE eid = '$eid' and password = '$pwd'";
$conn->query($sql);
```

If `$eid` is:

```sql
' OR '1'='1' --
```

the password check can be commented out and bypassed.

Defense:

```php
$sql = "SELECT Name, Salary, SSN
        FROM employee
        WHERE eid = ? and password = ?";
$stmt = $conn->prepare($sql);
$stmt->bind_param("ss", $eid, $pwd);
$stmt->execute();
```

Prepared statements separate SQL code from data. The DB compiles the query structure
before parameter values are bound.

### XSS

> [!important] Definition - XSS
> Cross-Site Scripting lets an attacker inject malicious JavaScript into pages viewed
> by other users. The script executes in the victim's browser under the trusted site's
> origin.

Types:

| Type | Where payload lives |
|---|---|
| Stored XSS | Stored in server DB and served to many users. |
| Reflected XSS | Comes from a malicious URL and is reflected in the response. |
| DOM-based XSS | Client-side JavaScript inserts attacker-controlled data into DOM. |

![[websec-xss-stored-flow.jpg|480]]

*Figure 28: Stored XSS flow where malicious script is saved and later executed in victims' browsers*

Main defenses:
- output encoding before rendering user data,
- sanitization, e.g. DOMPurify for controlled HTML,
- avoid unsafe DOM APIs like `innerHTML` with untrusted data,
- use frameworks with built-in escaping.

`<c:out>` in JSP is important because it escapes output.

### CSRF

> [!important] Definition - CSRF
> Cross-Site Request Forgery tricks an authenticated user's browser into sending an
> unwanted request to a site where the user is already logged in.

![[websec-csrf-schema2.jpg|480]]

*Figure 29: CSRF attack flow where a malicious page triggers authenticated cross-site requests*

The attacker does not need to know the victim's cookie. The browser automatically
sends cookies for the target site.

Protection:

| Defense | Effect |
|---|---|
| `SameSite=Strict` cookie | Cookie not sent in cross-site requests. |
| CSRF token | Server accepts only requests containing a valid unpredictable token. |
| Method discipline | Avoid state-changing GET requests. |

**Open-question focus:** compare SQLi, XSS, and CSRF by target, root cause, attack
flow, and primary defenses. This is very suitable for an open question.

### Extended study notes

Security questions are usually best answered by separating the security property,
the vulnerability, the attack flow, and the defense. A common mistake is to list
attack names without explaining what trust boundary is broken. In Web applications,
the main boundary is between untrusted input from the network and trusted code,
queries, pages, sessions, and server-side state.

The CIA triad is a compact way to organize security goals:

| Goal | Web application example | Typical violation |
|---|---|---|
| Confidentiality | Only the owner can see private data. | SQL injection leaks salaries or passwords. |
| Integrity | A request changes only what it is allowed to change. | CSRF transfers money or changes email address. |
| Availability | The service remains usable. | Overload, crashes, or resource exhaustion. |

SQL injection attacks the database layer through the application layer. The root
cause is not "SQL is insecure"; the root cause is string concatenation that mixes
trusted query syntax with untrusted user data.

Vulnerable Java-style example:

```java
String sql = "SELECT * FROM users WHERE email = '" + email + "'";
Statement st = connection.createStatement();
ResultSet rs = st.executeQuery(sql);
```

If `email` contains SQL syntax, the database receives a different query from the one
the programmer intended. The defense is parameter binding:

```java
String sql = "SELECT * FROM users WHERE email = ?";
PreparedStatement ps = connection.prepareStatement(sql);
ps.setString(1, email);
ResultSet rs = ps.executeQuery();
```

The key concept is separation. The SQL structure is fixed first; values are sent as
values. Escaping strings manually is more fragile and should not be the main answer.

XSS attacks the browser of another user. The server may store or reflect attacker
input, but the damage happens when the victim's browser executes injected script in
the origin of the trusted site. Because the script runs under that origin, it can
read page content, send requests, modify the DOM, and interact with the application
as the victim.

Unsafe output:

```jsp
<p>${comment}</p>
```

Safer JSP output:

```jsp
<p><c:out value="${comment}"/></p>
```

`<c:out>` escapes characters such as `<`, `>`, and `&`, so a stored comment like
`<script>...</script>` is rendered as text instead of becoming executable code.

Encoding depends on context. HTML text, HTML attributes, JavaScript strings, CSS,
and URLs need different escaping rules. For exam purposes, the core idea is enough:
never insert untrusted data into executable or structural contexts without the
correct output encoding or sanitization.

CSRF is different from XSS. In CSRF, the attacker usually cannot read the response
because of the same-origin policy. The attack relies on the browser automatically
including authentication cookies with a request to the target site.

Example malicious page:

```html
<form action="https://bank.example/transfer" method="post">
  <input type="hidden" name="to" value="attacker">
  <input type="hidden" name="amount" value="1000">
</form>
<script>
  document.forms[0].submit();
</script>
```

If the victim is logged in and the bank accepts the request only based on cookies,
the transfer may be executed. A CSRF token prevents this because the attacker cannot
guess a fresh token embedded in the legitimate page.

| Attack | Main victim | Root cause | Main defense |
|---|---|---|---|
| SQL injection | Database/application data. | Concatenating untrusted input into SQL. | Prepared statements and least privilege. |
| XSS | Victim browser/session. | Rendering untrusted data as executable HTML/JS. | Output encoding, sanitization, safe DOM APIs. |
| CSRF | Authenticated server-side action. | Server trusts cookie-only cross-site request. | CSRF token, SameSite cookies, no state-changing GET. |

`SameSite` cookies reduce CSRF risk by controlling whether cookies are sent in
cross-site requests. `SameSite=Strict` is strongest but can be inconvenient for
normal navigation flows. `SameSite=Lax` is a common compromise. Tokens are still
important for sensitive actions.

Open questions may also expect a mention of defense in depth. Prepared statements do
not replace authorization checks. Output encoding does not replace authentication.
CSRF tokens do not protect against XSS, because an injected script may be able to
read the token from the page. Security controls should be layered.

Short answer template:

```text
SQL injection, XSS, and CSRF are different attacks because they break different
trust assumptions. SQL injection sends attacker-controlled syntax to the database
when the application builds queries by concatenation; prepared statements fix this
by separating code from data. XSS injects script into pages viewed by other users;
output encoding and sanitization prevent untrusted text from becoming executable
markup. CSRF tricks an authenticated browser into sending an unwanted request; CSRF
tokens, SameSite cookies, and avoiding state-changing GET requests reduce the risk.
```

---

## 12. CSS

### Role and attachment

CSS defines presentation. It keeps visual style separate from HTML structure.

Preferred attachment:

```html
<link rel="stylesheet" type="text/css" href="styles.css">
```

External stylesheets are cacheable and reusable across pages. Embedded `<style>` is
per-page. Inline `style="..."` is hard to maintain and has high specificity.

### Rules and selectors

```css
selector {
  property: value;
}
```

![[css-selectors-1.jpg|520]]

*Figure 30: CSS selector examples for type, class, and id-based targeting*

| Selector | Meaning |
|---|---|
| `p` | all `<p>` elements |
| `.note` | elements with class `note` |
| `p.note` | `<p>` elements with class `note` |
| `#intro` | element with id `intro` |
| `p a` | any `<a>` descendant inside a `<p>` |
| `p > a` | direct `<a>` children of `<p>` |
| `h1 + p` | first `<p>` immediately after `<h1>` |
| `h1 ~ p` | all following `<p>` siblings |

Pseudo-classes style state:

```css
a:link    { color: blue; }
a:visited { color: purple; }
a:focus   { outline: 2px solid black; }
a:hover   { color: red; }
a:active  { color: orange; }
```

Order matters: LVFHA (`link`, `visited`, `focus`, `hover`, `active`).

### Cascade and inheritance

Specificity priority:
1. inline style,
2. ID selector,
3. class / pseudo-class / attribute selector,
4. type selector,
5. universal selector.

If specificity is equal, the later rule wins. `!important` overrides ordinary
specificity; user `!important` rules outrank author rules for accessibility.

Text properties such as `font-family`, `font-size`, `color`, `line-height` inherit.
Box properties such as `margin`, `padding`, `border`, `width` do not.

### Colors and typography

CSS colors can be expressed in several equivalent formats:

```css
p { color: red; }
p { color: rgb(255, 0, 0); }
p { color: #ff0000; }
p { color: hsl(0, 100%, 50%); }
p { color: rgba(255, 0, 0, 0.5); }
```

`rgba()` and `hsla()` add alpha only to the specific color property. `opacity`
applies transparency to the whole element, including children.

```css
body {
  font-family: Georgia, "Times New Roman", serif;
  font-size: 16px;
  line-height: 1.5;
}
```

A font stack lists preferred fonts, then fallbacks, ending with a generic family
such as `serif`, `sans-serif`, or `monospace`.

### Box model

![[css-box-model.jpg|500]]

*Figure 31: CSS box model with content, padding, border, and margin areas*

Every element is a box:

```text
content -> padding -> border -> margin
```

In the standard box model, `width` means only content width. Total occupied width is:

```text
left margin + left border + left padding + width
+ right padding + right border + right margin
```

Padding shorthand follows top-right-bottom-left:

```css
p { padding: 10px 5px 20px 1px; }
```

So: top `10px`, right `5px`, bottom `20px`, left `1px`.

### Display, positioning, float

| Property | Effect |
|---|---|
| `display: none` | Element removed from layout. |
| `visibility: hidden` | Element invisible, space preserved. |
| `position: static` | Normal flow. |
| `position: relative` | Offset from normal position, original space kept. |
| `position: absolute` | Removed from flow, positioned relative to nearest non-static ancestor. |
| `position: fixed` | Removed from flow, positioned relative to viewport. |
| `float: left/right` | Element moves aside, following content wraps around. |

Floats can collapse parent height if all children float. A common fix is:

```css
.parent { overflow: auto; width: 100%; }
```

### Flexbox, Grid, responsive design

Flexbox is one-dimensional:

```css
.container {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
}
```

Grid is two-dimensional:

```css
.grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
}
```

![[css-grid-layout.jpg|520]]

*Figure 32: CSS Grid layout using rows, columns, and fractional space distribution*

Responsive design needs:

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

and media queries:

```css
/* mobile first */
.container { width: 100%; }

@media only screen and (min-width: 40em) {
  .container { width: 80%; margin: 0 auto; }
}
```

Breakpoints should be content-driven: add one when the layout starts to break, not
because of a specific device name.

**Open-question focus:** CSS selectors, specificity/cascade, inheritance, box model
formula, `display:none` vs `visibility:hidden`, positioning, flex vs grid, viewport
and media queries.

### Extended study notes

CSS is the language that assigns visual presentation to structured documents. In an
open answer, the most important idea is that CSS is rule-based and conflict-prone:
many rules can apply to the same element, so the browser needs a deterministic
algorithm to decide the final computed value of each property.

The cascade combines several inputs:

1. origin of the rule, such as browser default, user stylesheet, or author
   stylesheet,
2. importance, especially `!important`,
3. selector specificity,
4. source order when previous factors tie.

Specificity is commonly represented as a tuple. Inline styles are strongest among
normal author declarations, then IDs, then classes/attributes/pseudo-classes, then
type selectors and pseudo-elements.

```css
p { color: black; }                 /* type selector */
.note { color: blue; }              /* class selector */
#main .note { color: red; }         /* id + class */
```

For `<p id="x" class="note">`, `.note` beats `p`. For an element inside `#main`,
`#main .note` beats `.note` because ID specificity is higher. If two selectors have
the same specificity, the later rule wins.

Inheritance is separate from the cascade. Some properties, such as `color` and
`font-family`, naturally inherit from the parent. Others, such as `margin`, `border`,
and `width`, do not. If a property is not specified on an element, the browser may
inherit it or use its initial value depending on the property.

```css
body {
  color: #222;
  font-family: Arial, sans-serif;
}

.box {
  border: 1px solid #888;
}
```

The text color and font usually propagate to children. The border does not, because
otherwise every nested element would draw its own border.

The box model describes how much space an element occupies:

```text
total width = margin-left + border-left + padding-left
            + content width
            + padding-right + border-right + margin-right
```

With the default `box-sizing: content-box`, the declared `width` applies only to the
content area. With `box-sizing: border-box`, the declared width includes content,
padding, and border. Many modern layouts set border-box globally because it makes
component sizing easier.

```css
* {
  box-sizing: border-box;
}
```

`display: none` and `visibility: hidden` are a frequent exam contrast:

| Declaration | Visible? | Takes space? | In layout tree? |
|---|---|---|---|
| `display: none` | No. | No. | Removed from layout. |
| `visibility: hidden` | No. | Yes. | Space is preserved. |

Positioning changes how boxes are placed:

| Position | Meaning |
|---|---|
| `static` | Normal document flow. Offsets do not apply. |
| `relative` | Normal flow position is kept, then the box is visually offset. |
| `absolute` | Removed from normal flow, positioned relative to nearest positioned ancestor. |
| `fixed` | Positioned relative to viewport. |
| `sticky` | Behaves relative, then sticks when a scroll threshold is reached. |

Example:

```css
.card {
  position: relative;
}

.badge {
  position: absolute;
  top: 0;
  right: 0;
}
```

The badge is positioned relative to `.card` because `.card` is positioned. Without
that, the badge might be positioned relative to a more distant ancestor.

Floats were historically used for layouts, but their original purpose is text
wrapping around content such as images. Modern layout should use Flexbox for one
dimension and Grid for two dimensions.

Flexbox is useful for distributing items along a row or column:

```css
.toolbar {
  display: flex;
  gap: 0.75rem;
  align-items: center;
  justify-content: space-between;
}
```

Grid is useful when both rows and columns matter:

```css
.dashboard {
  display: grid;
  grid-template-columns: 240px 1fr;
  grid-template-rows: auto 1fr;
  min-height: 100vh;
}
```

Responsive Web Design has three core ingredients: fluid layouts, flexible media,
and media queries. The viewport meta tag is necessary on mobile because otherwise
the browser may render the page as if it had a wide desktop viewport and then scale
it down.

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

Media queries should react to layout needs:

```css
.notes {
  display: block;
}

@media (min-width: 48rem) {
  .notes {
    display: grid;
    grid-template-columns: 18rem 1fr;
  }
}
```

Short answer template:

```text
CSS separates presentation from HTML structure. A CSS rule has a selector and a set
of declarations. When many rules target the same element, the cascade decides the
final value using origin, importance, specificity, and source order. Some properties
inherit from parents, while others use initial values. The box model combines
content, padding, border, and margin. Layout can be controlled with display,
positioning, Flexbox, Grid, and responsive media queries together with the viewport
meta tag.
```

---

## 13. JavaScript

### Role in the web stack

| Technology | Responsibility |
|---|---|
| HTML | Structure. |
| CSS | Presentation. |
| JavaScript | Behavior and interactivity. |

JavaScript is high-level, dynamically typed, interpreted, and works with object-like
and functional styles. In the browser, it can modify the current page and react to
events, but same-origin restrictions protect other pages and origins.

External JS is preferred:

```html
<script src="my_script.js"></script>
```

Scripts execute in document order. A `<script>` pauses HTML parsing while it loads
and runs, so scripts are often placed at the end of `<body>`.

### Types and objects

Primitive types:

```text
number, string, boolean, null, undefined
```

Objects are dynamic associative arrays:

```javascript
var person = {
  firstName: "John",
  lastName: "Doe",
  fullName: function() {
    return this.firstName + " " + this.lastName;
  }
};
```

`this` refers to the object that owns the method call in this context.

Arrays are dynamic and heterogeneous:

```javascript
var misc = [1.1, true, "a", { x: 1 }];
misc.push("new");
misc.forEach(function(value, index, array) {
  console.log(index, value);
});
```

`forEach` calls a callback for each element with `(value, index, array)`.

### Browser objects and DOM

`window` is the global browser object. It exposes `document`, `location`, `history`,
`navigator`, `screen`, timers, dialogs, and the console.

Useful browser methods:

```javascript
alert("Message");                         // message, no return value
var ok = confirm("Proceed?");             // true for OK, false for Cancel
var name = prompt("What is your name?");  // string or null

setTimeout(function() { console.log("once"); }, 2000);
setInterval(function() { console.log("repeat"); }, 1000);
```

`confirm()` is often tested: it shows OK/Cancel and returns a boolean. Timers schedule
asynchronous callbacks; they do not block the whole browser while waiting.

![[js-dom-tree.jpg|520]]

*Figure 33: DOM tree generated from an HTML document and manipulated through JavaScript*

The DOM is the in-memory tree representation of the HTML page.

| Node type | Meaning |
|---|---|
| `Document` | Root of the tree. |
| `Element` | HTML tag node. |
| `Text` | Text inside elements. |
| `Comment` | HTML comment. |

Selection:

```javascript
var title = document.getElementById("main-title");
var warnings = document.getElementsByClassName("warning");
var links = document.querySelectorAll("p a");
```

DOM creation and insertion:

```javascript
var p = document.createElement("p");
var text = document.createTextNode("Hello, world!");
p.appendChild(text);
document.getElementById("container").appendChild(p);
```

Explanation:
- created nodes are not visible until inserted into the document,
- `appendChild` adds a node as last child,
- `createTextNode` avoids interpreting text as HTML.

### Events

An event has a type and a target: for example, a `"click"` event on a button.

Preferred registration:

```javascript
var b = document.getElementById("mybutton");
b.addEventListener("click", function(event) {
  alert("Thanks!");
});
```

Why `addEventListener`:
- supports multiple handlers,
- does not mix JS into HTML,
- works on DOM objects,
- can be paired with `removeEventListener`.

Form validation handlers often use:

```javascript
form.addEventListener("submit", function(event) {
  if (!valid) {
    event.preventDefault();
  }
});
```

`preventDefault()` blocks the browser's default form submission.

**Open-question focus:** JavaScript vs Java, primitive vs object, objects as
associative arrays, arrays and `forEach`, DOM tree and selection methods, node
creation, and `addEventListener`.

### Extended study notes

JavaScript is the behavior layer of the browser platform. It should not be confused
with Java: the names are historically related for marketing reasons, but the
languages have different type systems, object models, execution environments, and
typical uses. In this course, Java is mostly server-side, while JavaScript is mainly
client-side code executed by the browser.

Good open answers usually start from the three Web layers:

| Layer | Main language | Main responsibility |
|---|---|---|
| Structure | HTML | Describe content and controls. |
| Presentation | CSS | Define visual appearance and layout. |
| Behavior | JavaScript | React to events, update DOM, call servers. |

JavaScript is dynamically typed. A variable does not have a fixed declared type; the
value currently stored in it has a type.

```javascript
let value = 10;       // number
value = "ten";        // string
value = { n: 10 };    // object
```

This flexibility is convenient but can also hide errors. That is why careful naming,
small functions, and explicit checks are important in browser scripts.

Primitive values include numbers, strings, booleans, `null`, and `undefined`.
Objects are reference values. Objects can contain properties, and properties can be
functions.

```javascript
const course = {
  name: "Web Applications",
  credits: 6,
  describe: function() {
    return this.name + " (" + this.credits + " CFU)";
  }
};
```

In this example, `this` refers to the object before the dot when the method is
called as `course.describe()`. For an introductory exam answer, it is enough to say
that `this` depends on the call context, and that it commonly represents the object
owning the method call.

Objects also behave like associative arrays:

```javascript
course["name"] = "Web Applications";
course.teacher = "Professor";
```

Dot notation is shorter when the property name is known and is a valid identifier.
Bracket notation is useful when the property name is computed.

Arrays are objects specialized for ordered lists. They have a `length` property and
methods such as `push`, `pop`, `forEach`, `map`, and `filter`.

```javascript
const numbers = [1, 2, 3];

numbers.forEach(function(number, index) {
  console.log(index + ": " + number);
});
```

The callback receives the current value, the index, and the full array. This pattern
is useful when code must execute once per element without writing an explicit
counter loop.

The browser exposes a hierarchy of objects. `window` is the global object. It
contains `document`, which represents the current page as the DOM tree. The DOM is
not the source HTML file itself; it is the parsed, live, in-memory representation
that scripts can inspect and modify.

DOM selection methods are different in return type:

| Method | Returns |
|---|---|
| `getElementById` | One element or `null`. |
| `getElementsByClassName` | Live HTML collection. |
| `getElementsByTagName` | Live HTML collection. |
| `querySelector` | First matching element or `null`. |
| `querySelectorAll` | Static node list of all matches. |

Example:

```javascript
const list = document.querySelector("#students");
const item = document.createElement("li");
item.textContent = "Ada Lovelace";
list.appendChild(item);
```

`textContent` inserts text, not HTML. This is safer than assigning untrusted content
to `innerHTML`, because the browser will not interpret the string as markup.

Events are central to browser programming. The page loads, the user clicks, types,
submits forms, resizes the window, and receives asynchronous responses. JavaScript
registers callback functions to react to these events.

```javascript
const form = document.querySelector("form");

form.addEventListener("submit", function(event) {
  if (!form.checkValidity()) {
    event.preventDefault();
  }
});
```

The callback receives an event object. `event.target` is the element where the event
originated. `event.preventDefault()` cancels the default browser action, such as
submitting a form or following a link.

Inline event attributes are discouraged:

```html
<button onclick="save()">Save</button>
```

External registration is cleaner:

```javascript
document.querySelector("button").addEventListener("click", save);
```

This separates behavior from markup and allows multiple independent listeners on
the same element.

JavaScript in the browser is restricted by security rules. The same-origin policy
prevents a page from freely reading responses from another origin. An origin is
defined by scheme, host, and port. `https://example.com` and
`http://example.com` are different origins because the scheme is different.

Short answer template:

```text
JavaScript is the browser behavior language. It is dynamically typed, supports
primitive values and objects, and uses functions as first-class values. In Web
pages, JavaScript interacts mainly with the DOM, which is the live tree
representation of the document. Scripts select elements, create nodes, change text
or attributes, and register event listeners with addEventListener. Browser security
rules such as the same-origin policy limit what a script can read from other
origins.
```

---

## 14. Form Validation and AJAX

### Form validation

Validation checks user input before data is accepted.

| Validation type | Where | Purpose |
|---|---|---|
| Client-side | Browser | Fast feedback, better user experience. |
| Server-side | Server | Security and final correctness gate. |

Client-side validation is not enough: attackers can bypass it.

HTML5 built-in validation:

```html
<input id="choose" name="course"
       required
       pattern="Informatics|ICT|Cybersecurity">
```

```css
input:invalid { border: 2px dashed red; }
input:valid   { border: 2px solid black; }
```

Constraint Validation API:

```javascript
var email = document.getElementById("provide_email");

email.addEventListener("input", function () {
  if (email.validity.typeMismatch) {
    email.setCustomValidity("Please insert an email address!");
  } else {
    email.setCustomValidity("");
  }
});
```

`setCustomValidity("")` clears the error; any non-empty string marks the field as
invalid with that custom message.

Manual JavaScript validation uses event handlers, regular expressions, CSS classes,
and `event.preventDefault()` in the submit handler.

### AJAX

> [!important] Definition - AJAX
> AJAX is scripted HTTP from the browser. It lets a page exchange data with the
> server and update part of the DOM without reloading the whole page.

XHR request parts:
1. method,
2. URL,
3. optional headers,
4. optional body.

XHR response parts:
1. status code,
2. headers,
3. body.

```javascript
var request = new XMLHttpRequest();
request.onload = function() {
  if (request.readyState === XMLHttpRequest.DONE && request.status === 200) {
    console.log(request.responseText);
  }
};
request.open("GET", "test.html");
request.send();
```

`readyState` values:

| Value | Meaning |
|---|---|
| 0 | `open()` not called. |
| 1 | `open()` called. |
| 2 | response headers received. |
| 3 | response body downloading. |
| 4 | complete. |

### Encoding request bodies

Form encoding:

```javascript
request.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
request.send("find=pizza&zipcode=02134");
```

JSON encoding:

```javascript
request.setRequestHeader("Content-Type", "application/json");
request.send(JSON.stringify(dataObject));
```

### CORS

The same-origin policy normally blocks XHR responses from other origins. CORS is the
server's opt-in mechanism through headers such as `Access-Control-Allow-Origin`.

### JSON and Fetch

```javascript
var obj = JSON.parse(xhr.responseText);
var out = JSON.stringify(obj);
```

Never use `eval()` for JSON. Only parse JSON from trusted sources.

Modern Fetch:

```javascript
let response = await fetch(url);
if (response.ok) {
  let json = await response.json();
} else {
  alert("HTTP-Error: " + response.status);
}
```

Fetch returns a Promise. `await response.json()` parses the response body into a
JavaScript object.

**Open-question focus:** client vs server validation, HTML5 validation attributes,
Constraint Validation API, `preventDefault`, XHR lifecycle, CORS, JSON parse/stringify,
and Fetch vs XHR.

### Extended study notes

Form validation is a strong candidate for an open question because it connects HTML,
CSS, JavaScript, HTTP, and server-side security. The key thesis is simple:
client-side validation improves usability, but server-side validation is mandatory
for correctness and security.

Client-side validation can be bypassed by disabling JavaScript, editing HTML in the
browser developer tools, sending requests with curl/Postman, or directly calling an
API. Therefore it should never be the only protection for business rules, database
constraints, authentication, authorization, or security.

HTML5 validation attributes cover many common constraints:

| Attribute | Meaning |
|---|---|
| `required` | Field must not be empty. |
| `type="email"` | Value must look like an email address. |
| `type="number"` | Value must be numeric. |
| `min`, `max` | Numeric or date bounds. |
| `minlength`, `maxlength` | Text length bounds. |
| `pattern` | Regular expression constraint. |

Example:

```html
<input id="student-email"
       name="email"
       type="email"
       required
       maxlength="120">
```

CSS pseudo-classes can style validity:

```css
input:invalid {
  border-color: #c62828;
}

input:valid {
  border-color: #2e7d32;
}
```

The Constraint Validation API lets JavaScript inspect and customize validation.

```javascript
const password = document.getElementById("password");

password.addEventListener("input", function() {
  if (password.value.length < 8) {
    password.setCustomValidity("Password must contain at least 8 characters.");
  } else {
    password.setCustomValidity("");
  }
});
```

The empty string is important: it means "no custom error". Any non-empty message
makes the field invalid.

Manual validation often runs on the `submit` event:

```javascript
form.addEventListener("submit", function(event) {
  if (!isValid()) {
    event.preventDefault();
    showErrors();
  }
});
```

`preventDefault()` cancels the browser's normal submit behavior. Without it, the
form would be sent even if JavaScript found an error.

AJAX changes the interaction model. Instead of submitting a form and loading a new
page, JavaScript sends an HTTP request in the background and updates part of the DOM
when the response arrives. This produces faster interfaces, but it does not change
the fact that the server must validate all input.

The XMLHttpRequest lifecycle can be answered step by step:

```javascript
const xhr = new XMLHttpRequest();

xhr.onreadystatechange = function() {
  if (xhr.readyState === XMLHttpRequest.DONE) {
    if (xhr.status === 200) {
      document.getElementById("result").textContent = xhr.responseText;
    }
  }
};

xhr.open("GET", "/api/status");
xhr.send();
```

The request is configured with `open(method, url)`, optional headers are set, then
`send(body)` starts it. The browser later calls the callback as state changes. The
important final state is `DONE`, and the HTTP status tells whether the server
returned success or an error.

AJAX requests still use HTTP. The request can send query parameters, form-encoded
data, multipart data, or JSON. The server responds with text, HTML, XML, JSON, or
another media type. Modern APIs commonly exchange JSON:

```javascript
const payload = {
  title: "Exam registration",
  active: true
};

xhr.open("POST", "/api/forms");
xhr.setRequestHeader("Content-Type", "application/json");
xhr.send(JSON.stringify(payload));
```

`JSON.stringify` converts a JavaScript object into a JSON string. `JSON.parse`
converts a JSON string into a JavaScript value.

```javascript
const data = JSON.parse(xhr.responseText);
console.log(data.title);
```

`eval()` must not be used for JSON because it executes code. JSON parsing should
parse data, not run arbitrary script.

Fetch is a newer Promise-based API:

```javascript
const response = await fetch("/api/forms", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify(payload)
});

if (!response.ok) {
  throw new Error("Request failed: " + response.status);
}

const result = await response.json();
```

A common trap: `fetch()` only rejects the Promise for network-level failures. HTTP
errors such as 404 or 500 still produce a response object, so code must check
`response.ok` or `response.status`.

CORS appears when JavaScript tries to read a response from another origin. The
browser enforces the same-origin policy, and the server can opt into cross-origin
access with CORS headers. The policy is enforced by the browser, not by the server
alone.

Short answer template:

```text
Client-side validation improves usability by giving immediate feedback through
HTML5 attributes, CSS pseudo-classes, and JavaScript. It is not a security boundary
because users can bypass it, so the server must validate again. AJAX lets
JavaScript send HTTP requests without reloading the page. XMLHttpRequest uses
open, optional headers, send, readyState, and status; Fetch provides a more modern
Promise-based interface. JSON is commonly exchanged using JSON.stringify and
JSON.parse. Cross-origin AJAX is controlled by the same-origin policy and CORS.
```

---

## 15. jQuery and HTML5 Canvas

### jQuery

jQuery is a JavaScript library that simplifies DOM selection, manipulation, event
handling, and AJAX.

The `$()` function has several uses:

```javascript
$("p")                  // select all <p> elements
$(document)             // wrap a raw DOM object
$("<p>Hello</p>")       // create a new DOM element
```

A **jQuery object** is a set of zero or more DOM elements plus jQuery methods. It is
not the same as a raw DOM element.

```javascript
$("p").css("color", "red");
```

Explanation: `$("p")` returns all paragraphs as a jQuery object. `.css("color",
"red")` sets the CSS property on all matched elements.

Getter/setter pattern:

```javascript
$("#title").text();              // getter: returns text
$("#title").text("New title");   // setter: changes text and returns jQuery object
```

Setters support chaining; getters usually end the chain because they return a value.

Useful methods:

| Category | Methods |
|---|---|
| Attributes | `attr(name)`, `attr(name, value)` |
| CSS | `css(prop)`, `css(prop, value)` |
| Classes | `addClass`, `removeClass`, `toggleClass`, `hasClass` |
| Form values | `val()` |
| Content | `text()`, `html()` |
| Insert | `append`, `prepend`, `before`, `after`, `appendTo` |
| Delete | `empty`, `remove`, `detach`, `unwrap` |
| Events | `click`, `bind`, `unbind` |
| AJAX | `$.ajax`, `$.get`, `$.post`, `$.getJSON`, `.load` |

`text()` is safer for user content because it treats content as text. `html()` parses
HTML and can introduce XSS if used with untrusted data.

### Canvas

`<canvas>` is a fixed-size bitmap drawing surface. CSS resizing can distort it
because the internal bitmap size and visual size may differ.

```html
<canvas id="myCanvas" width="600" height="400">
  Your browser does not support canvas.
</canvas>
```

```javascript
const canvas = document.getElementById("myCanvas");
const ctx = canvas.getContext("2d");
```

![[Figures/slide-051-fig-01.jpg|520]]

*Figure 34: Canvas coordinate system with origin at the top-left corner and axes growing right and down*

Canvas coordinates start at top-left `(0,0)`. `x` grows to the right, `y` grows
downward. One canvas unit usually corresponds to one pixel.

Rectangles:

```javascript
ctx.fillRect(25, 25, 100, 100);   // filled rectangle
ctx.clearRect(45, 45, 60, 60);    // transparent hole
ctx.strokeRect(50, 50, 50, 50);   // outline
```

![[Figures/slide-052-fig-01.jpg|480]]

*Figure 35: Canvas rectangle operations showing filled, cleared, and stroked rectangles*

Paths:

```javascript
ctx.beginPath();
ctx.moveTo(20, 20);
ctx.lineTo(120, 20);
ctx.lineTo(120, 80);
ctx.closePath();
ctx.stroke();
```

`beginPath()` starts a new path. `moveTo()` moves the virtual pen without drawing.
`lineTo()` draws a segment. `stroke()` draws the outline; `fill()` fills the shape.

Arcs use radians:

```javascript
ctx.arc(x, y, radius, startAngle, endAngle, anticlockwise);
```

Images must be drawn after loading:

```javascript
const img = new Image();
img.onload = function() {
  ctx.drawImage(img, 0, 0);
};
img.src = "picture.png";
```

Without `onload`, drawing may happen before the image bytes exist.

State and transformations:

```javascript
ctx.save();
ctx.translate(100, 100);
ctx.rotate(Math.PI / 4);
// draw rotated object
ctx.restore();
```

`save()` and `restore()` avoid leaking transformations and styles into later drawing.
Use `requestAnimationFrame()` for smooth animations synchronized with browser repaint.

**Open-question focus:** jQuery object vs DOM element, getter/setter chaining,
`text` vs `html`, jQuery AJAX shortcuts, canvas coordinate system, paths, image
loading, state stack, and animation scheduling.

### Extended study notes

jQuery is less central in new projects than it used to be, but it remains important
for understanding many Web applications and for this course because it shows common
DOM and AJAX patterns in a compact form. The main idea is that jQuery wraps DOM
elements in a jQuery object that exposes convenience methods.

The `$` function can select, wrap, create, or run code after the DOM is ready:

```javascript
$("#main")              // select element with id main
$(".warning")           // select elements with class warning
$(document)             // wrap the document object
$("<li>New item</li>")  // create an element
$(function() {
  console.log("DOM ready");
});
```

A raw DOM element and a jQuery object are not interchangeable:

```javascript
const raw = document.getElementById("title");
raw.textContent = "Hello";

const wrapped = $("#title");
wrapped.text("Hello");
```

If you have a raw DOM element and want jQuery methods, wrap it:

```javascript
$(raw).addClass("highlight");
```

If you have a jQuery object and want the raw element, use indexing or `.get()`:

```javascript
const element = $("#title")[0];
```

jQuery methods often use the same method as getter and setter. With no argument,
they read. With an argument, they write and return the same jQuery object, enabling
chaining.

```javascript
const oldText = $("#message").text();

$("#message")
  .text("Saved")
  .addClass("success")
  .fadeIn();
```

`text()` and `html()` must be distinguished:

| Method | Meaning | Security note |
|---|---|---|
| `text()` | Reads/writes text content. | Safer for untrusted text. |
| `html()` | Reads/writes HTML markup. | Dangerous with untrusted input. |

Example:

```javascript
$("#output").text("<strong>Hello</strong>");
```

This displays the angle brackets as text. By contrast:

```javascript
$("#output").html("<strong>Hello</strong>");
```

This creates a real `<strong>` element. If the string came from an attacker, this
could become an XSS vulnerability.

jQuery groups DOM manipulation into readable methods:

```javascript
$("#list").append("<li>Last</li>");
$("#list").prepend("<li>First</li>");
$(".old").remove();
$(".item").attr("data-state", "selected");
$(".item").css("color", "red");
```

Event handling is also compact:

```javascript
$("#save").on("click", function(event) {
  event.preventDefault();
  saveForm();
});
```

Older jQuery code may use shortcuts such as `.click(handler)`, but `.on()` is the
more general method and supports delegated events:

```javascript
$("#list").on("click", "li", function() {
  $(this).toggleClass("selected");
});
```

Delegation attaches one listener to `#list`. Clicks from child `<li>` elements bubble
up, and jQuery checks whether the actual target matches `"li"`. This also works for
items added later.

jQuery AJAX hides some XMLHttpRequest boilerplate:

```javascript
$.getJSON("/api/students", function(students) {
  students.forEach(function(student) {
    $("#students").append($("<li>").text(student.name));
  });
});
```

The theory point is still HTTP: jQuery sends a request, receives a response, parses
data if needed, and calls callbacks.

Canvas is a different topic but fits the same JavaScript chapter because drawing is
performed through scripts. The `<canvas>` element creates a rectangular bitmap.
The 2D context exposes drawing operations:

```javascript
const canvas = document.getElementById("scene");
const ctx = canvas.getContext("2d");

ctx.fillStyle = "lightblue";
ctx.fillRect(10, 10, 120, 80);
```

Coordinates start at the top-left corner. `x` grows to the right, `y` grows
downward. This is different from the mathematical coordinate system usually drawn
on paper.

Canvas drawing is immediate-mode. After a rectangle or line is drawn, the canvas
does not keep a DOM object representing that shape. If the scene changes, the
program usually clears and redraws the frame.

```javascript
function draw(x) {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.fillRect(x, 40, 50, 50);
}
```

Paths collect drawing commands before they are stroked or filled:

```javascript
ctx.beginPath();
ctx.moveTo(50, 20);
ctx.lineTo(90, 90);
ctx.lineTo(10, 90);
ctx.closePath();
ctx.fill();
```

The state stack matters because drawing properties and transformations persist.

```javascript
ctx.save();
ctx.translate(100, 100);
ctx.rotate(Math.PI / 6);
ctx.fillRect(-25, -25, 50, 50);
ctx.restore();
```

After `restore()`, later drawings are not accidentally rotated or translated.

Animations should use `requestAnimationFrame()`:

```javascript
let x = 0;

function frame() {
  draw(x);
  x = (x + 2) % canvas.width;
  requestAnimationFrame(frame);
}

requestAnimationFrame(frame);
```

This lets the browser synchronize drawing with repaint cycles, which is smoother and
more efficient than a fixed `setInterval` for animation.

Short answer template:

```text
jQuery simplifies DOM selection, manipulation, events, effects, and AJAX. The $
function returns a jQuery object, which is a wrapper around zero or more DOM
elements. Many methods work as getters without arguments and setters with
arguments, returning the jQuery object for chaining. text() writes text safely,
while html() interprets markup and must not receive untrusted input. Canvas creates
a bitmap drawing surface controlled by JavaScript; drawing uses a 2D context,
coordinates, paths, images, transformations, save/restore, and animation frames.
```

---

## 16. Semantic Web and Linked Data

### Web of documents to Web of data

![[Figures/slide-003-fig-01.jpg|520]]

*Figure 36: Evolution from the Web of Documents to the Web of Data*

The Web of Documents links human-readable pages. The Web of Data links data entities
with typed relationships so machines can interpret what the links mean.

Raw data becomes information only when paired with schema/metadata.

![[Figures/slide-006-fig-01.jpg|520]]

*Figure 37: Raw data becoming information when interpreted through schema and metadata*

Example: `123`, `91`, `38.5`, `7` are just numbers. With labels, they become heart
rate, pressure, temperature, age, etc.

### Ontologies, RDF, knowledge graphs

| Layer | Technology | Meaning |
|---|---|---|
| Ontology | OWL | Classes, properties, constraints, abstract concepts. |
| Linked Data | RDF | Concrete facts about instances. |
| Knowledge graph/base | RDF + ontology | Connected graph of typed facts. |

### RDF

> [!important] Definition - RDF triple
> RDF represents facts as triples: `(subject, predicate, object)`.

```text
Subject   -> URI
Predicate -> URI
Object    -> URI or literal
```

![[Figures/slide-009-fig-01.jpg|520]]

*Figure 38: RDF document serializations representing an RDF graph of subject-predicate-object triples*

The predicate is a URI because relationships also need global identifiers. The object
can be another resource URI or a literal value.

![[Figures/slide-011-fig-01.jpg|560]]

*Figure 39: RDF graph connecting Bob, Alice, the Mona Lisa, typed literals, and external identifiers*

Example triples:

| Subject | Predicate | Object |
|---|---|---|
| `http://example.org/bob#me` | `rdf:type` | `foaf:Person` |
| `http://example.org/bob#me` | `foaf:knows` | `http://example.org/alice#me` |
| `http://example.org/bob#me` | `schema:birthDate` | `"1990-07-04"^^xsd:date` |
| `wd:Q12418` | `dcterms:title` | `"Mona Lisa"` |
| `wd:Q12418` | `dcterms:creator` | `dbpedia:Leonardo_da_Vinci` |

### RDF serializations

Same graph, different concrete syntaxes:

| Format | Best use |
|---|---|
| RDF/XML | XML ecosystem, but verbose. |
| JSON-LD | Web APIs and JavaScript-friendly linked data. |
| N-Triples | One triple per line, good for bulk/streaming. |
| Turtle | Compact and human-readable. |
| RDFa | RDF embedded inside HTML. |
| TriG | Named graphs. |

Turtle example:

```turtle
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX schema: <http://schema.org/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

<http://example.org/bob#me>
  a foaf:Person ;
  foaf:knows <http://example.org/alice#me> ;
  schema:birthDate "1990-07-04"^^xsd:date .
```

`;` continues statements for the same subject. `a` is shorthand for `rdf:type`.

### SPARQL

> [!important] Definition - SPARQL
> SPARQL is the standard query language for RDF graphs, analogous to SQL for
> relational databases.

```sparql
PREFIX foaf: <http://xmlns.com/foaf/0.1/>

SELECT ?name (COUNT(?friend) AS ?count)
WHERE {
  ?person foaf:name ?name .
  ?person foaf:knows ?friend .
}
GROUP BY ?person ?name
```

Explanation:
- variables start with `?`,
- `WHERE` contains graph patterns to match triples,
- `COUNT(?friend)` counts matched friends,
- `GROUP BY` groups by person/name before aggregation.

![[Figures/slide-016-fig-01.jpg|560]]

*Figure 40: SPARQL query and XML result format for counting friends in an RDF graph*

### Linked Data and FAIR

Tim Berners-Lee's four Linked Data principles:

1. Use URIs as names for things.
2. Use HTTP URIs so those names can be looked up.
3. When a URI is looked up, provide useful information using RDF/SPARQL.
4. Include links to other URIs so users and machines can discover more data.

Linked Open Data is Linked Data published under an open license.

![[Figures/slide-021-fig-01.jpg|560]]

*Figure 41: Linked Open Data cloud showing many interlinked datasets across domains*

The LOD cloud is huge, which creates a practical discovery problem: finding the
specific dataset and links you need is difficult.

FAIR principles:

| Principle | Meaning |
|---|---|
| Findable | Persistent identifiers, rich metadata, searchable indexes. |
| Accessible | Retrievable by standard protocols; metadata can remain available. |
| Interoperable | Formal representation and shared vocabularies. |
| Reusable | Clear license, provenance, accurate attributes, community standards. |

DBpedia extracts structured data from Wikipedia. Wikidata is a collaborative,
multilingual knowledge base with stable entity URIs.

![[Figures/slide-028-fig-01.jpg|540]]

*Figure 42: W3C One Web technology stack including Web applications, Semantic Web, Web services, and security*

The Semantic Web stack is part of the same "One Web" vision: it sits alongside Web
Applications, Web Services, Privacy/Security, and shared Web foundations such as URI,
HTTP, XML, RDF, DOM, and SPARQL.

**Open-question focus:** Web of Documents vs Web of Data, data vs information, RDF
triple model, URI/literal distinction, serialization formats, SPARQL graph matching,
Linked Data principles, LOD vs Linked Data, and FAIR.

### Extended study notes

The Semantic Web chapter is conceptual, so open answers should be built slowly. The
starting point is the limitation of the traditional Web: pages are connected by
links, but links usually do not tell machines what the relationship means. A human
can read a page and understand that "Leonardo da Vinci painted the Mona Lisa"; a
machine needs explicit structured statements to process that fact reliably.

The Web of Documents is centered on HTML documents and hyperlinks. The Web of Data
is centered on identifiable entities and typed relationships. The goal is not to
replace documents, but to add machine-readable data that can be linked, queried, and
combined across sources.

| Web of Documents | Web of Data |
|---|---|
| Main unit is a document. | Main unit is a resource/entity. |
| Links connect pages. | RDF triples connect things. |
| Meaning is mainly interpreted by humans. | Meaning is explicit through predicates and vocabularies. |
| HTML and URLs dominate. | URI, RDF, RDFS/OWL, SPARQL, JSON-LD/Turtle dominate. |

The difference between data and information is also important. Data are raw values.
Information is data interpreted through structure, context, and meaning. The value
`38.5` means little alone; with a schema saying it is body temperature in Celsius,
it becomes information.

Ontologies define shared vocabulary and meaning. They can describe classes,
properties, relationships, and constraints. RDF then represents concrete facts using
that vocabulary. A knowledge graph combines many facts into a connected graph.

Example:

```text
Class: Person
Property: knows
Instance: Bob
Fact: Bob knows Alice
```

In RDF, the fact becomes a triple:

```text
<http://example.org/bob#me> foaf:knows <http://example.org/alice#me> .
```

The subject is the thing being described. The predicate is the relationship. The
object is either another resource or a literal value. Predicates are URIs because
relationships themselves need global meaning. `foaf:knows` is not just the string
"knows"; it identifies a property from the FOAF vocabulary.

RDF objects can be resources or literals:

```turtle
<http://example.org/bob#me>
  foaf:knows <http://example.org/alice#me> ;
  foaf:name "Bob" ;
  schema:birthDate "1990-07-04"^^xsd:date .
```

`<http://example.org/alice#me>` is a URI resource. `"Bob"` is a plain literal.
`"1990-07-04"^^xsd:date` is a typed literal.

Prefixes are abbreviations, not different identifiers:

```turtle
PREFIX foaf: <http://xmlns.com/foaf/0.1/>

foaf:name
```

This expands to:

```text
http://xmlns.com/foaf/0.1/name
```

RDF is a data model, not one concrete syntax. Turtle, RDF/XML, JSON-LD, N-Triples,
RDFa, and TriG can serialize RDF graphs in different ways. This distinction is like
the difference between "table data" and "CSV/JSON/XML representation": the model and
the syntax are not the same thing.

SPARQL queries graph patterns. A `WHERE` clause describes triples to match, and
variables collect the matching parts.

```sparql
PREFIX foaf: <http://xmlns.com/foaf/0.1/>

SELECT ?person ?name
WHERE {
  ?person a foaf:Person .
  ?person foaf:name ?name .
}
```

This means: find resources that are persons and have a FOAF name. Return the
resource and the name. The query does not require knowing all person URIs in
advance; it discovers them by matching graph patterns.

Aggregation works after grouping:

```sparql
PREFIX foaf: <http://xmlns.com/foaf/0.1/>

SELECT ?person (COUNT(?friend) AS ?numberOfFriends)
WHERE {
  ?person foaf:knows ?friend .
}
GROUP BY ?person
```

This counts how many `foaf:knows` relationships each person has.

Linked Data principles explain how RDF data should be published on the Web. The
principles are practical:

1. Use URIs to name things, so entities can be referenced globally.
2. Use HTTP URIs, so clients can look them up.
3. Return useful information, preferably RDF and SPARQL access.
4. Link to other URIs, so datasets become connected rather than isolated.

Linked Open Data adds the open-license requirement. Data can be Linked Data without
being open, for example inside a company. It becomes Linked Open Data when it is
published under terms that allow reuse.

FAIR is related but broader. It is not only about RDF; it is a set of principles for
scientific and data management quality:

| FAIR principle | Practical meaning |
|---|---|
| Findable | Data has persistent identifiers and rich metadata. |
| Accessible | Data/metadata can be retrieved through standard protocols. |
| Interoperable | Data uses formal languages, shared vocabularies, and links. |
| Reusable | Data has license, provenance, and enough context for reuse. |

DBpedia and Wikidata are useful examples. DBpedia extracts structured facts from
Wikipedia, while Wikidata is a collaborative knowledge base designed around
entities, properties, statements, references, and multilingual labels. Both provide
stable identifiers that can be linked from other datasets.

A strong final connection is that Semantic Web technologies reuse general Web
foundations. URIs identify resources, HTTP retrieves representations, RDF models
facts, SPARQL queries graphs, and vocabularies/ontologies define shared meaning.

Short answer template:

```text
The Semantic Web extends the Web of Documents into a Web of Data. Instead of only
linking pages for humans, it identifies entities with URIs and connects them through
typed RDF triples. A triple has subject, predicate, and object; the object may be
another URI resource or a literal. RDF is a graph data model and can be serialized
as Turtle, RDF/XML, JSON-LD, and other formats. SPARQL queries RDF graphs by
matching triple patterns. Linked Data principles say to use HTTP URIs, provide
useful RDF information, and link to other URIs. FAIR describes data that is
findable, accessible, interoperable, and reusable.
```

---

## High-Yield Open Questions to Practice

1. Explain the three-tier architecture of a Web application and map each tier to the
   technologies used in the course.
2. Compare servlet-only response generation with JSP/MVC response generation.
3. Explain how a servlet obtains a pooled database connection through Tomcat, JNDI,
   and `DataSource`.
4. Describe the DAO pattern and explain how `PreparedStatement` prevents SQL
   injection.
5. Explain REST as an architectural style, including resources, URIs, HTTP methods,
   representations, and statelessness.
6. Compare URI, URL, URN, IRI, percent-encoding, and MIME media types.
7. Explain safe and idempotent HTTP methods, with examples.
8. Compare XML and JSON for Web data exchange, including schema mechanisms and
   parsing approaches.
9. Explain HTML5 semantic layout and why tags should be chosen for meaning rather
   than visual appearance.
10. Explain the CSS cascade: specificity, inheritance, source order, and
    `!important`.
11. Explain JavaScript's role in the browser: DOM manipulation, event handling, and
    security restrictions.
12. Compare HTML5 validation, Constraint Validation API, JavaScript validation, and
    server-side validation.
13. Explain the AJAX request/response lifecycle using `XMLHttpRequest`, then compare
    it with Fetch.
14. Compare SQL Injection, XSS, and CSRF by target, root cause, attack flow, and
    defenses.
15. Explain jQuery objects, getter/setter methods, DOM manipulation, event handling,
    and AJAX shortcuts.
16. Explain how Canvas drawing works: coordinate system, rectangles, paths, images,
    transformations, and animation.
17. Explain RDF triples, RDF graphs, SPARQL queries, Linked Data principles, and FAIR
    data.
