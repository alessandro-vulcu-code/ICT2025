# Web Applications 25-26 - Theory Summary

This summary is based on `Notes/Web Applications 25-26.md` and is meant for theory study, especially for open-ended exam questions. It keeps the same order as the course notes and focuses on definitions, concepts, differences, architectural flows, and small code snippets when they clarify the idea.

Older exam questions often ask for precise definitions, such as "What is a URI?", "What is Maven?", "How does JSP work?", "What does idempotent mean?", "What is XSS?", or "What is the purpose of the application logic layer?". For open questions, the expected answer is usually not just a definition: explain the concept, place it in the architecture, give one example, and mention the main tradeoff or risk.

## 1. Introduction to Web Applications

### Web Evolution

| Era | Main idea | Technologies | Key point |
|---|---|---|---|
| Web 1.0 | Read Web | HTTP, HTML, MIME, URL | Mostly static or server-generated pages, users consume content |
| Web 2.0 | Read/Write Web | XML, AJAX, JSON, REST | Users create content, applications become interactive |
| Web 3.0 | Semantic Web | RDF, OWL, SPARQL | Data is machine-readable and linked by typed relations |
| Web3 | Decentralized Web | Blockchain | User-controlled data, decentralized finance, NFTs |

**Semantic Web** is the Web of data: resources are connected by typed links so that their structure and meaning can be processed by machines. An **RDF triple** is a statement of the form **subject, predicate, object**.

**Deep Web** is content not indexed by normal search engines. **Dark Web** is a part of the Web that requires specific tools and is designed to provide anonymity.

### Distributed Applications

A distributed application separates responsibilities into logical layers:

| Layer | Also called | Responsibility |
|---|---|---|
| Presentation logic | Interface/User logic | Manages user interaction, input, output format, visualization |
| Application logic | Business logic | Defines and controls the flow of operations and business rules |
| Data logic | Persistence logic | Stores, searches, retrieves, and maintains data consistency |

Exam-style point: **application logic** is not the UI and not the database. It controls the operations of the application.

### Architectures

| Architecture | Distribution | Pros | Cons |
|---|---|---|---|
| Single-tier | Everything on one machine, e.g. dumb terminal/mainframe | Easy to implement, no client management | Mainframe is bottleneck and single point of failure |
| Two-tier, fat client | Presentation + application on client, data on server | Simple, some load balancing | Client maintenance, limited scalability |
| Two-tier, fat server | Presentation on client, application + data on server | Simpler clients | Scalability and maintenance limits |
| Three-tier | Client, application server, database server | Scalable, easier client maintenance, load balancing | More complex implementation |

![[intro-three-tier.jpg|520]]

**Web applications are a special case of three-tier architecture**:

- Browser = thin client / presentation tier
- Web server and application server = application logic tier
- Database server = data tier

Advantages: no client installation, standard technologies, ubiquitous browsers, desktop and mobile access, familiar interaction patterns.

HTTP is the application-layer protocol used by Web applications. It runs over the TCP/IP stack:

```text
Application: HTTP
Transport:   TCP / UDP
Network:     IP
Physical:    link technology
```

## 2. Git and Maven

### Git

**Git** is a distributed version control system. It manages revisions of files and directories, concurrent modifications, conflicts, branches, tags, and merges.

| Approach | Meaning |
|---|---|
| Centralized, e.g. CVS/SVN | One central repository stores history; clients synchronize with it |
| Distributed, e.g. Git | Every local copy is a complete repository; synchronization happens by exchanging patches |

Git models development as a directed graph. Branches are alternative development lines; tags mark stable versions.

![[git-workflow-three-trees.jpg|520]]

Git local areas:

1. **Working directory**: actual files.
2. **Index/Stage**: selected changes ready to commit.
3. **HEAD**: last committed version.

Essential commands:

```bash
git init
git clone <url>
git add <file>
git commit -m "Message"
git push origin <branch>
git pull origin <branch>
git checkout -b <branch-name>
git merge <branch-name>
```

A **pull request** is a collaboration mechanism provided by platforms such as GitHub or Bitbucket. It is a request to review and merge changes. It is not the same as `git pull`.

`.gitignore` lists files and directories that should not be tracked, such as generated packages, compiled classes, logs, IDE files, and `target/`.

### Maven

**Maven** is a tool for managing Java software projects. It supports build, dependency management, packaging, deployment, collaboration, and documentation.

Advantages:

- Consistency across projects
- Reuse of build configurations
- Simpler dependency and packaging management
- Easier maintenance than custom scripts

Core concepts:

| Concept | Meaning |
|---|---|
| Lifecycle | Sequence of phases used to build a project |
| Phase | A step in the lifecycle |
| Goal | A concrete operation executed in a phase |
| Plugin | Implements one or more goals |
| POM | `pom.xml`, declarative project description |

If you invoke a Maven phase, all previous phases in that lifecycle are also executed. Example: `mvn package` runs validation, compilation, tests, and packaging steps needed before `package`.

Important lifecycles:

- `clean`: removes generated files.
- `default`: main build lifecycle.
- `site`: generates project documentation.

Main `default` phases:

```text
validate -> compile -> test -> package -> verify -> install -> deploy
```

POM coordinates identify an artifact:

```xml
<groupId>it.unipd.dei.webapp</groupId>
<artifactId>employee-webapp</artifactId>
<version>1.00</version>
<packaging>war</packaging>
```

For web applications, `packaging` is usually `war`, because Tomcat deploys Web ARchive files.

Maven repositories:

- Local repository: `~/.m2/repository`
- Remote repositories: Maven Central, Sonatype, custom repositories
- If a dependency is missing locally, Maven downloads it from a remote repository.

Standard Maven structure:

```text
project/
  src/main/java/
  src/main/resources/
  src/main/webapp/
  src/test/
  pom.xml
  target/
```

Exam focus:

- Define Maven as a Java build/dependency management tool.
- Explain lifecycle, phase, goal, plugin, and POM.
- Explain why `mvn package` also runs previous phases.
- Explain what dependency coordinates are.

## 3. Docker and Containerization

### Deployment Environment Problem

A web application depends on several components: Java, Tomcat, PostgreSQL, libraries, configuration files, OS packages, and versions. Maven builds the application, but it does not guarantee that the target runtime environment is compatible.

Classic problem: "it works on my machine". The application works locally, but fails on another server because Java, Tomcat, DB, or dependencies differ.

### Containerization

**Containerization** packages an application with the libraries and runtime dependencies it needs, inside an isolated execution environment. It improves portability and reproducibility.

**Docker** is a platform for developing, distributing, and running applications in containers.

### Containers vs Virtual Machines

| Aspect | Container | Virtual Machine |
|---|---|---|
| Isolation | Process-level isolation | Full machine isolation |
| OS | Shares host kernel | Has guest OS |
| Startup | Fast | Slower |
| Size | Lightweight | Heavy |
| Portability | High | Lower |
| Resource use | Efficient | More expensive |

![[docker-containers-stack.jpg|420]]

### Docker Objects

| Object | Definition |
|---|---|
| Dockerfile | Text file describing how to build an image |
| Image | Read-only template used to create containers |
| Container | Runtime instance created from an image |
| Volume | Persistent data storage outside container writable layer |
| Network | Virtual network for container communication |
| Service | Application component, often managed by Compose |

**Docker image** is immutable and layered. Each instruction in a Dockerfile adds a layer.

Minimal Dockerfile idea:

```dockerfile
FROM tomcat:10
COPY target/app.war /usr/local/tomcat/webapps/app.war
EXPOSE 8080
```

### Docker Compose

**Docker Compose** manages multi-container applications through a YAML file. In the course example, one service runs Tomcat and another runs PostgreSQL.

![[docker-compose-webapp-architecture.jpg|520]]

Key ideas:

- Compose automatically creates a private network.
- Services can communicate using service names as hostnames.
- Volumes persist data and mount files from host to container.
- `depends_on` controls startup order, but alone does not guarantee readiness.
- `healthcheck` verifies that a service is actually ready.

Essential example:

```yaml
services:
  web:
    image: tomcat:10
    ports:
      - "8080:8080"
    volumes:
      - ./crane.war:/usr/local/tomcat/webapps/crane.war
    depends_on:
      db:
        condition: service_healthy

  db:
    image: postgres
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
    volumes:
      - ./crane.sql:/docker-entrypoint-initdb.d/init.sql
      - ./data/db:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
```

Useful commands:

```bash
docker-compose up
docker-compose down
docker ps
docker ps -a
docker exec <container> <command>
docker build .
```

Exam focus:

- Docker image = read-only template/snapshot of dependencies and instructions.
- Container = isolated runtime instance created from an image.
- Volume = persistent data outside container lifecycle.
- Compose = orchestrates multi-container apps.
- Container vs VM: containers share host kernel; VMs include guest OS.

## 4. Java Servlets

### Web Application Technologies

Browser-side components:

- User interface
- Rendering engine
- DOM
- JavaScript engine
- HTML/CSS parser
- Networking

Server-side components:

- Request analysis
- Access control
- Resource dispatch
- Static resources
- Dynamic resources
- Logging
- Networking

Communication is HTTP request/response.

### Jakarta EE and Tomcat

**Jakarta EE** is a standardized platform for multi-tier enterprise applications. It defines APIs such as Servlet, JSP, and REST support.

**Web container** is the runtime that implements the web part of Jakarta EE and executes web components. **Tomcat** is a web container.

Package migration:

| Version family | Package prefix |
|---|---|
| Java EE / Jakarta EE 8 and before | `javax.*` |
| Jakarta EE 9+ | `jakarta.*` |

Tomcat 9 uses `javax.*`; Tomcat 10+ uses `jakarta.*`.

### Servlet Definition

A **Java servlet** is a Java-based server-side web component, managed by a container, that generates dynamic web content.

Properties:

- Platform-independent Java class compiled to bytecode.
- Loaded and executed by a Java-enabled web server/container.
- Handles HTTP requests and produces HTTP responses.
- Not thread-safe by default: multiple requests may access the same servlet instance concurrently.

Exam-style answer: a servlet is server-side technology that dynamically generates web content.

### Main Servlet Classes

| Class/Interface | Role |
|---|---|
| `Servlet` | Base interface every servlet implements |
| `ServletRequest` | Generic request information |
| `ServletResponse` | Generic response output |
| `ServletConfig` | Servlet initialization parameters |
| `ServletContext` | Application-wide context and container communication |
| `HttpServlet` | Base class for HTTP servlets |
| `HttpServletRequest` | HTTP-specific request object |
| `HttpServletResponse` | HTTP-specific response object |
| `Cookie` | Small server-created value stored by the browser |
| `HttpSession` | Per-user state across requests |
| `Part` | One part of a multipart upload |
| `Filter` | Intercepts requests/responses before/after servlets |

### Servlet Lifecycle

![[servlet-sequence-diagram.jpg|520]]

Lifecycle:

1. `init(ServletConfig)` is called once after instantiation, before serving requests. It is used to allocate resources.
2. `service(ServletRequest, ServletResponse)` is called for every request.
3. In `HttpServlet`, `service()` dispatches to `doGet()`, `doPost()`, `doPut()`, `doDelete()`, etc.
4. `destroy()` is called once before the servlet is removed, after active requests finish.

```text
init() -> service() many times -> destroy()
```

Important thread-safety rule: do not store request-specific state in servlet instance variables. Use local variables, request attributes, or session attributes where appropriate.

### web.xml and WAR

`WEB-INF/web.xml` is the deployment descriptor. It declares servlets and maps URL patterns to them. `WEB-INF` is not directly accessible from the browser.

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

A web application is packaged as a WAR:

```xml
<packaging>war</packaging>
```

The Servlet API dependency is usually `provided` because Tomcat already provides it:

```xml
<dependency>
  <groupId>jakarta.servlet</groupId>
  <artifactId>jakarta.servlet-api</artifactId>
  <scope>provided</scope>
</dependency>
```

### Minimal Servlet Pattern

```java
public class HelloWorldServlet extends HttpServlet {
  protected void doGet(HttpServletRequest req, HttpServletResponse res)
      throws IOException {
    res.setContentType("text/html; charset=utf-8");
    PrintWriter out = res.getWriter();
    out.printf("<!DOCTYPE html>%n");
    out.printf("<html><body><p>Hello, world!</p></body></html>%n");
    out.flush();
    out.close();
  }
}
```

Key steps: set response MIME type, get writer/output stream, write response body, flush/close.

### GET and POST Forms

`GET` sends form parameters in the query string. It is suitable for retrieval and bookmarkable requests. `POST` sends data in the request body. It is suitable for creating or submitting data.

```html
<form method="POST" action="../create-employee">
  <input name="badge" type="text">
  <button type="submit">Submit</button>
</form>
```

Servlets read parameters with:

```java
String badge = req.getParameter("badge");
```

## 5. Servlets and Database Access

### Application Structure

The employee application uses:

- Resource classes: domain objects such as `Employee` and `Message`
- DAO classes: database access logic
- Servlet classes: HTTP controllers
- Tomcat connection pool: database connection management
- PostgreSQL: persistence layer

Logical layers:

| Layer | Course implementation |
|---|---|
| Interface/Application logic | Servlets parse requests, call DAOs, prepare responses |
| Data logic | DAO classes contain SQL |
| Data layer | PostgreSQL |

### Resource Classes

`Employee` represents a domain entity. In the notes it is immutable:

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

  public int getBadge() { return badge; }
}
```

`Message` represents success or error information:

- message text
- optional error code
- optional error details
- boolean `isError`

### DAO Pattern

**Data Access Object (DAO)** abstracts and encapsulates all access to a data source.

Benefits:

- Servlets do not contain SQL.
- Persistence logic is separated from business/application logic.
- Each DAO handles one operation or one resource type.
- DAOs expose a uniform interface.

Core interface:

```java
public interface DataAccessObject<T> {
  DataAccessObject<T> access() throws SQLException;
  T getOutputParam();
}
```

Typical flow:

```text
Servlet -> creates DAO -> dao.access() -> SQL execution -> dao.getOutputParam()
```

### Connection Pool

Opening a new database connection for every request is expensive. A **connection pool** keeps reusable database connections ready.

Tomcat exposes the pool as a `DataSource` through JNDI:

```java
InitialContext ctx = new InitialContext();
DataSource ds = (DataSource) ctx.lookup("java:/comp/env/jdbc/employee-ferro");
Connection con = ds.getConnection();
```

`context.xml` defines the pool, while `web.xml` declares a `resource-ref`.

### AbstractDatabaseServlet

Common pattern:

- `init()` runs once and obtains the connection pool.
- `getConnection()` returns a pooled connection for each request.
- `destroy()` releases the reference.

```java
public abstract class AbstractDatabaseServlet extends HttpServlet {
  private DataSource ds;

  public void init(ServletConfig config) throws ServletException {
    ds = (DataSource) new InitialContext()
      .lookup("java:/comp/env/jdbc/employee-ferro");
  }

  protected final Connection getConnection() throws SQLException {
    return ds.getConnection();
  }
}
```

### SQL Injection

**SQL Injection** occurs when untrusted user input is concatenated into SQL code, allowing the attacker to change the query structure.

Vulnerable:

```java
String q = "SELECT * FROM Employee WHERE salary > "
         + req.getParameter("salary");
Statement s = con.createStatement();
ResultSet rs = s.executeQuery(q);
```

Attack input such as `0 OR 1=1` may change the intended query.

Safe:

```java
String q = "SELECT * FROM Employee WHERE salary > ?";
PreparedStatement ps = con.prepareStatement(q);
ps.setInt(1, salary);
ResultSet rs = ps.executeQuery();
```

**PreparedStatement** separates SQL structure from data values. The database treats bound parameters as data, not executable SQL syntax.

### Sequence

![[db-create-employee-sequence.jpg|520]]

Create employee flow:

1. Browser sends POST form.
2. Servlet parses parameters.
3. Servlet creates `Employee`.
4. Servlet obtains DB connection.
5. Servlet creates DAO.
6. DAO executes prepared `INSERT`.
7. Servlet creates `Message`.
8. Servlet renders or forwards response.

Exam focus:

- Define DAO and explain why SQL belongs in DAO classes.
- Explain connection pooling and JNDI.
- Explain SQL injection and prepared statements.
- Explain why servlets must avoid shared request state.

## 6. JSP and MVC

### Why JSP

Writing HTML from a servlet using `PrintWriter` is cumbersome and hard to maintain. JSP solves this by letting developers write HTML-like template pages with dynamic parts.

**JSP** stands for JavaServer Pages. It is a server-side view technology for creating dynamic web responses.

### JSP Execution Model

On first request:

```text
JSP file -> translated into servlet Java source -> compiled -> executed
```

On later requests, the compiled servlet class is reused.

Exam-style answer: JSP is not interpreted like PHP; a preprocessor translates JSP into a servlet, and then the servlet processes the request.

### JSP Components

| Component | Syntax | Purpose |
|---|---|---|
| Template text | HTML | Static output |
| Page directive | `<%@ page ... %>` | Page configuration |
| Taglib directive | `<%@ taglib ... %>` | Imports custom tag library |
| Standard action | `<jsp:useBean>` | Standard JSP operation |
| JSTL tag | `<c:if>`, `<c:forEach>` | Common logic without Java scriptlets |
| Expression Language | `${employee.badge}` | Access attributes, beans, params |
| Scriptlet | `<% ... %>` | Raw Java in JSP, should be avoided |

Minimal JSP:

```jsp
<%@ page contentType="text/html;charset=UTF-8" %>
<!DOCTYPE html>
<html>
<body>
  <p>Hello, world!</p>
</body>
</html>
```

### JavaBeans and EL

JavaBeans convention:

- no-argument constructor
- properties accessed through `getXXX()` and `setXXX()`
- boolean properties can use `isXXX()`

Expression Language uses getters:

```jsp
${employee.badge}
```

This resolves to:

```java
employee.getBadge()
```

### JSTL

JSTL is the JSP Standard Tag Library. It provides reusable tags for conditions, loops, formatting, URLs, and functions.

Important core tags:

| Tag | Meaning |
|---|---|
| `<c:out>` | Outputs a value with XML/HTML escaping |
| `<c:if>` | Conditional rendering |
| `<c:choose>` | Multi-branch conditional |
| `<c:forEach>` | Loop over collection |
| `<c:url>` | Builds context-aware URL |
| `<c:import>` | Includes another resource |

Always use `<c:out>` for user-controlled content:

```jsp
<c:out value="${employee.surname}"/>
```

This helps prevent XSS because it escapes special characters.

JSTL must be bundled in the WAR unless the container provides it:

```xml
<dependency>
  <groupId>jakarta.servlet.jsp.jstl</groupId>
  <artifactId>jakarta.servlet.jsp.jstl-api</artifactId>
</dependency>
```

### MVC

**Model-View-Controller (MVC)** separates an application into:

| Role | Responsibility | Java Web implementation |
|---|---|---|
| Model | Data and business/domain state | JavaBeans, resources, DAOs |
| View | Renders output | JSP |
| Controller | Handles input and coordinates flow | Servlet |

Typical Java Web MVC:

```text
Browser -> Servlet controller -> DAO/model -> request attributes -> JSP view -> HTML
```

![[jsp-mvc-layers-employee.jpg|520]]

The servlet does not write HTML directly. It sets request attributes and forwards:

```java
req.setAttribute("employee", e);
req.setAttribute("message", m);
req.getRequestDispatcher("/jsp/create-employee-result.jsp")
   .forward(req, res);
```

The JSP reads attributes:

```jsp
<c:if test="${not empty employee && !message.error}">
  <c:out value="${employee.badge}"/>
</c:if>
```

`forward()` is server-side: the browser receives one response and does not know that control moved from servlet to JSP.

Exam focus:

- JSP is translated into a servlet.
- In MVC with Java Web: JavaBeans/DAOs = Model, JSP = View, Servlets = Controller.
- `RequestDispatcher.forward()` is server-side delegation to the view.
- Use JSTL/EL instead of scriptlets.

## 7. REST Web Services

### REST Definition

**REST** means REpresentational State Transfer. It is an architectural style that applies Web principles to Web services.

Core ideas:

- Everything is a **resource**.
- Every resource has a **URI**.
- The client transfers representations of resource state.
- HTTP provides a uniform interface through methods.
- Communication is stateless.

### Resources and URIs

A resource is anything with identity: a student, an employee, a collection, an exam result, a photo.

Example URI templates:

```text
/student
/student/{badge}
/student/{badge}/exam/{id}
```

### HTTP Methods and CRUD

| HTTP method | CRUD | Meaning |
|---|---|---|
| GET | Read | Retrieve a resource or collection |
| POST | Create | Create a new resource under a collection |
| PUT | Update/Replace | Store or replace resource at URI |
| DELETE | Delete | Remove resource |

REST design principles:

1. Identify resources.
2. Assign URI to each resource.
3. Decide allowed HTTP methods.
4. Link resources.
5. Decide representations, usually JSON or XML.
6. Document the API.

### Representations

The same resource can be represented as JSON, XML, or HTML. The client states preferred response types through `Accept`, and POST/PUT bodies declare their type with `Content-Type`.

JSON employee example:

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

### API Documentation

| Tool | Format | Status |
|---|---|---|
| WADL | XML | Older, W3C submission, not widely standardized |
| OpenAPI | YAML/JSON | De-facto modern standard for REST API description |

### Employee REST API

| URI | Method | Meaning |
|---|---|---|
| `/rest/employee` | GET | List employees |
| `/rest/employee` | POST | Create employee |
| `/rest/employee/{badge}` | GET | Read employee |
| `/rest/employee/{badge}` | PUT | Update employee |
| `/rest/employee/{badge}` | DELETE | Delete employee |
| `/rest/employee/salary/{salary}` | GET | Search by salary |

### REST Implementation Architecture

Important classes:

| Component | Role |
|---|---|
| `Resource` | Interface for JSON-serializable resources |
| `AbstractResource` | Common JSON serialization machinery |
| `Employee` | Domain resource, can serialize/parse JSON |
| `Message` | JSON error/info response |
| `ResourceList<T>` | JSON collection wrapper |
| `RestResource` | Interface for a REST request handler |
| `AbstractRR` | Common REST request validation and error handling |
| `RestDispatcherServlet` | Front controller for `/rest/*` |

`Resource` interface:

```java
public interface Resource {
  void toJSON(OutputStream out) throws IOException;
}
```

REST resources validate method and media types:

```text
Accept missing -> 400
Accept not JSON or */* -> 406
POST/PUT Content-Type missing -> 400
POST/PUT Content-Type not JSON -> 415
Unsupported method -> 405
Unknown resource -> 404
```

`RestDispatcherServlet` overrides `service()` instead of only `doGet()` or `doPost()` because REST must handle several HTTP methods, including PUT and DELETE.

`web.xml` maps all REST requests:

```xml
<servlet-mapping>
  <servlet-name>RestManagerServlet</servlet-name>
  <url-pattern>/rest/*</url-pattern>
</servlet-mapping>
```

Exam focus:

- REST is resource-oriented, stateless, and uses HTTP methods as a uniform interface.
- `POST` creates, `GET` reads, `PUT` updates/replaces, `DELETE` removes.
- URI should identify resources, not actions.
- `Accept` is for response media type; `Content-Type` is for request body media type.

## 8. HTTP and Surroundings

### Four Pillars of the Web

| Standard | Role |
|---|---|
| HTML | Markup language for web pages |
| HTTP | Application-layer protocol for client/server communication |
| MIME | Media type and encoding of exchanged information |
| URL | Locates web resources |

### URI, URL, URN, IRI

**URI** is a compact sequence of characters that identifies an abstract or physical resource.

| Term | Meaning |
|---|---|
| URI | Generic resource identifier |
| URL | URI that also gives a location/access mechanism |
| URN | URI with `urn:` scheme, used as persistent name |
| IRI | Internationalized URI, allows Unicode characters |

URI syntax:

```text
scheme:[//[user[:password]@]host[:port]][/path][?query][#fragment]
```

Example:

```text
https://example.com:8080/rest/employee/7309?format=json#details
```

### Percent-Encoding

Percent-encoding represents reserved or non-ASCII characters in a URI using `%` plus hexadecimal octets.

Examples:

| Character | Encoded |
|---|---|
| space | `%20` |
| `?` | `%3F` |
| `&` | `%26` |
| `#` | `%23` |

Exam-style answer: percent encoding escapes reserved and non-plain ASCII characters in URI using `%XX`.

### Character Encoding

| Encoding | Key point |
|---|---|
| ASCII | 7-bit, 128 characters, English-oriented |
| Extended ASCII | 8-bit, 256 characters, many incompatible variants |
| Unicode | Universal character set for many languages and symbols |
| UTF-8 | Variable-width Unicode encoding, backward-compatible with ASCII |

Extended ASCII problem: different national code tables use the upper 128 values differently, causing incompatibilities.

### MIME

**MIME** means Multipurpose Internet Mail Extensions. It is an Internet standard for encoding information in email and the Web. It defines media types such as:

```text
text/html
text/plain
application/json
application/xml
image/png
multipart/form-data
```

Important headers:

| Header | Purpose |
|---|---|
| `Content-Type` | MIME type of body |
| `Content-Encoding` | Compression/encoding of body, e.g. gzip |
| `Content-Length` | Body size |
| `Content-Disposition` | How to display/download content |

### Multipart and Form Encoding

`multipart` combines several body parts separated by a boundary string that does not appear in any part.

```text
Content-Type: multipart/form-data; boundary=AaB03x

--AaB03x
Content-Disposition: form-data; name="submit-name"

Nicola
--AaB03x
Content-Disposition: form-data; name="files"; filename="file.pdf"
Content-Type: application/pdf

...
--AaB03x--
```

| Encoding | Use |
|---|---|
| `multipart/form-data` | File upload plus form fields |
| `application/x-www-form-urlencoded` | Form fields only, encoded as `name=value&name2=value2` |

### File Upload

For multipart upload:

```html
<form method="POST" enctype="multipart/form-data">
  <input name="photo" type="file" accept="image/png, image/jpeg">
</form>
```

Servlet API:

```java
for (Part p : req.getParts()) {
  String name = p.getName();
  String type = p.getContentType();
  InputStream in = p.getInputStream();
}
```

Client-side `accept` is not security. Server must validate MIME type and size.

### HTTP/1.1

**HTTP** is a textual, stateless, request-response protocol. Stateless means each request is independent; this improves scalability but requires explicit mechanisms for state, such as cookies or sessions.

HTTP request parts:

1. Request line
2. Headers
3. Optional body

HTTP response parts:

1. Status line
2. Headers
3. Optional body

### HTTP Methods

| Method | Meaning | Safe | Idempotent |
|---|---|---|---|
| GET | Retrieve resource | Yes | Yes |
| HEAD | Like GET, headers only | Yes | Yes |
| POST | Submit/create subordinate resource | No | No |
| PUT | Store/replace resource | No | Yes |
| DELETE | Delete resource | No | Yes |
| OPTIONS | Communication options | Yes | Yes |

**Safe** means no intended side effects on server state. **Idempotent** means repeating the same request has the same effect as performing it once.

### Status Codes

| Class | Meaning | Examples |
|---|---|---|
| 1xx | Informational | 101 |
| 2xx | Success | 200 OK, 201 Created, 204 No Content |
| 3xx | Redirection | 301 Moved Permanently |
| 4xx | Client error | 400, 401, 404, 405, 409, 415 |
| 5xx | Server error | 500 |

### Authentication

HTTP Basic Authentication:

1. Server replies `401 Unauthorized`.
2. Server sends `WWW-Authenticate: Basic realm="Employee"`.
3. Browser asks credentials.
4. Client sends `Authorization: Basic <base64>`.
5. `<base64>` encodes `username:password`.

```text
Authorization: Basic bmljb2xhOmZlcnJv
```

Important: Base64 is encoding, not encryption. Basic Authentication must be used over HTTPS.

### Sessions and Filters

A **cookie** is a way for the server to store state information in the client. Browser sends it back in later requests.

`HttpSession` is a server-side key-value store associated with a user session.

`Filter` lifecycle:

```text
init() -> doFilter() many times -> destroy()
```

`doFilter()` can block a request or pass it forward:

```java
chain.doFilter(req, res);
```

Authentication filter flow:

1. Check if session exists.
2. If session has authenticated user, continue.
3. Otherwise read `Authorization` header.
4. Decode Basic credentials.
5. Verify with DAO.
6. If valid, create session and store user.
7. If invalid, send `401` challenge.

## 9. Markup Languages

### Markup

Markup is information added to text that tells us something about the text. It is not the content itself.

Types:

| Type | Meaning |
|---|---|
| Punctuational | Separators such as commas and periods |
| Presentational | Layout information |
| Procedural | Commands saying how to format content |
| Descriptive | Describes the role/type of content |
| Referential | Refers to external or special entities |
| Meta-markup | Defines markup languages or their vocabulary |

Exam definitions:

- **Procedural markup** says how to format content.
- **Descriptive markup** defines the type or class of content to indicate intended use.
- **Referential markup** refers to entities external to the document.
- **Meta-markup** provides means to define or extend markup languages.

### SGML, HTML, HTML5

**SGML** is a meta-markup language. HTML and XML are historically derived from SGML ideas.

**HTML4** mixed structure/content with presentation. This caused problems:

- loose parsing and browser heuristics
- weak separation of content and presentation
- limited semantic description
- difficult reuse across devices

**HTML5** redesigns HTML to separate:

```text
HTML = structure/content
CSS = presentation
JavaScript = behavior
```

HTML5 adds semantic elements such as `<header>`, `<nav>`, `<article>`, `<section>`, `<footer>`, media elements, canvas, and richer input types.

### XML

**XML** is a markup language for representing and exchanging semi-structured data, especially among distributed systems.

It is:

- descriptive
- referential
- meta-markup
- semi-structured
- extensible

XML document is a tree of nodes:

![[markup-xml-tree.jpg|520]]

XML node types:

| Node | Meaning |
|---|---|
| Text | Unstructured textual information |
| Element | Logical grouping of child nodes |
| Attribute | Property of an element, written in opening tag |
| Comment | Ignored text |
| Processing instruction | Directive for processor |
| Root | Implicit root of the tree |

**Well-formed XML**:

- tags are properly nested
- opening and closing tags match
- there is exactly one root element
- attributes are quoted

**Valid XML** also satisfies a DTD or XML Schema.

### DOM, SAX, StAX

| Parser | Type | Key point |
|---|---|---|
| DOM | In-memory tree | Easy random access, higher memory |
| SAX | Streaming push | Low memory, parser calls callbacks |
| StAX | Streaming pull | Low memory, application pulls events |

**DOM API** creates an in-memory representation of XML/HTML. Browsers use DOM to represent HTML pages.

Exam-style answer: DOM's main feature is that it builds an in-memory tree representation of the document.

### DTD and XML Schema

**DTD** defines allowed XML structure, elements, attributes, and content models. It uses a non-XML syntax and has limitations: no rich data types, no namespace support, limited contextual constraints.

**XML Schema (XSD)** defines XML structure using XML syntax. It supports data types, namespaces, occurrence constraints, simple/complex types.

### JSON

**JSON** means JavaScript Object Notation. It is a lightweight text format for data interchange.

Built on:

- objects: unordered name/value pairs
- arrays: ordered lists of values

```json
{
  "employee": {
    "badge": 7309,
    "surname": "Rossi",
    "age": 34
  }
}
```

JSON types:

```text
object, array, string, number, boolean, null
```

Compared with XML, JSON is usually more compact and maps naturally to JavaScript objects. XML is more verbose but has mature schema and namespace mechanisms.

### JSON in Java

Jackson is a Java library for JSON processing. It uses a pull streaming API similar to StAX:

| Class | Role |
|---|---|
| `JsonFactory` | Creates parser/generator |
| `JsonParser` | Reads JSON tokens |
| `JsonGenerator` | Writes JSON tokens |
| `JsonToken` | Token enum |

## 10. HTML5

### Base Structure

Correct HTML5 doctype:

```html
<!DOCTYPE html>
```

Basic page:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Page title</title>
</head>
<body>
  <h1>Main heading</h1>
</body>
</html>
```

`<head>` contains metadata not displayed directly. `<title>` defines the browser tab title. `<body>` contains visible content.

### Semantic vs Presentational Markup

Use tags for meaning, not visual appearance:

- Use `<h1>` because content is a main heading.
- Use `<strong>` because content is important.
- Use CSS for visual styling.

This improves accessibility, search indexing, and maintainability.

### Block and Inline

| Type | Behavior | Examples |
|---|---|---|
| Block | Starts on new line, takes full width | `<p>`, `<h1>`, `<div>`, `<ul>`, `<table>` |
| Inline | Flows inside text | `<a>`, `<span>`, `<img>`, `<em>` |

### Links and Images

Links:

```html
<a href="https://example.com/page.html#section">Example</a>
<a href="mailto:user@example.com">Email</a>
<a href="tel:+18005551212">Call</a>
```

Fragment links use an `id`:

```html
<h2 id="details">Details</h2>
<a href="#details">Go to details</a>
```

Images:

```html
<img src="figure/quokka.jpg" alt="A family of quokka">
```

`alt` is important for accessibility and fallback.

HTML5 associates image and caption with:

```html
<figure>
  <img src="figure/quokka.jpg" alt="A family of quokka">
  <figcaption>The quokka is an Australian marsupial.</figcaption>
</figure>
```

### Forms

Form controls must usually have `name`, because the submitted data is sent as name/value pairs.

```html
<form action="/create-employee" method="post">
  <input name="surname" type="text">
  <input name="email" type="email">
  <button type="submit">Submit</button>
</form>
```

`id` is unique in the page and useful for CSS/JavaScript. `name` identifies values sent to the server and may be shared by radio buttons.

Correct radio group pattern:

```html
<input type="radio" name="gender" value="male" checked> Male
<input type="radio" name="gender" value="female"> Female
<input type="radio" name="gender" value="other"> Other
```

### HTML5 Semantic Layout

![[html5-layout-comparison.jpg|520]]

| Element | Meaning |
|---|---|
| `<header>` | Header of page/section |
| `<footer>` | Footer of page/section |
| `<nav>` | Major navigation |
| `<article>` | Self-contained content |
| `<section>` | Thematic section |
| `<aside>` | Related secondary content |
| `<figure>` | Media with optional caption |
| `<figcaption>` | Caption |

### HTML5 APIs and Media

HTML5 includes APIs for:

- media playback
- canvas drawing
- web storage
- geolocation
- web workers
- web sockets
- drag and drop

Canvas:

```html
<canvas id="c" width="600" height="400"></canvas>
```

```javascript
const ctx = document.getElementById("c").getContext("2d");
ctx.fillStyle = "#ff0000";
ctx.fillRect(0, 0, 150, 75);
```

Exam-style answer: `<canvas>` is an HTML5 element that allows drawing graphics using JavaScript.

## 11. Web Security

### CIA Triad

| Property | Meaning |
|---|---|
| Confidentiality | Information is available only to intended users |
| Integrity | Information is not altered improperly |
| Availability | Information remains accessible when needed |

Web security studies attacks and defenses for websites and web applications.

OWASP Top Ten is a standard awareness document listing important web application security risks. Injection remains a recurring major risk.

### SQL Injection

SQL Injection is code injection against the database. Root cause: user input and SQL code are mixed into the same string.

Vulnerable:

```sql
SELECT Name, Salary
FROM employee
WHERE eid = '$eid' AND password = '$pwd'
```

Attack:

```text
' OR '1'='1' --
```

Effect: condition always true, password check commented out.

Defense: prepared statements.

```java
PreparedStatement ps = con.prepareStatement(
  "SELECT Name, Salary FROM employee WHERE eid = ? AND password = ?"
);
ps.setString(1, eid);
ps.setString(2, pwd);
```

### XSS

**Cross-Site Scripting (XSS)** allows attackers to inject malicious JavaScript into pages viewed by other users. The script executes in the victim browser with the privileges of the trusted site.

Types:

| Type | Mechanism |
|---|---|
| Stored XSS | Malicious script stored in DB and later rendered |
| Reflected XSS | Script in URL/request is reflected in response |
| DOM-based XSS | Client-side JavaScript inserts attacker-controlled content into DOM |

Stored XSS flow:

![[websec-xss-stored-flow.jpg|520]]

Defense:

- output encoding
- sanitize HTML with libraries such as DOMPurify
- avoid dangerous DOM APIs such as unsafe `innerHTML`
- use frameworks with automatic escaping
- never render user input as HTML unless sanitized

JSP note:

```jsp
<c:out value="${userInput}"/>
```

is safer than raw `${userInput}` because it escapes XML/HTML characters.

### CSRF

**Cross-Site Request Forgery (CSRF)** tricks an authenticated user's browser into sending an unauthorized request to a site where the user is logged in. The browser automatically attaches cookies for the target site.

Key difference:

- XSS executes attacker code in the trusted site context.
- CSRF sends forged requests using the victim's existing authentication.

CSRF flow:

![[websec-csrf-schema1.jpg|420]]

Defense in notes:

| Defense | Idea |
|---|---|
| `SameSite=Strict` cookie | Browser does not send cookie on cross-site requests |

`SameSite=Lax` is weaker; `Strict` prevents cookies from being attached to cross-site requests.

Exam focus:

- SQLi targets database queries.
- XSS targets other users' browsers.
- CSRF targets authenticated sessions by abusing automatic cookie sending.
- Prepared statements defend against SQLi.
- Output encoding/sanitization defends against XSS.
- SameSite cookies defend against CSRF.

## 12. CSS

### CSS Definition

**CSS** means Cascading Style Sheets. It defines presentation for HTML/XML documents and separates visual appearance from content structure.

CSS recipe:

1. Mark up content with HTML.
2. Write style rules for selected elements.
3. Attach the rules to the document.

### Attaching CSS

Preferred: external stylesheet.

```html
<link rel="stylesheet" href="styles.css">
```

Other methods:

- embedded `<style>` inside `<head>`
- inline `style` attribute, least maintainable

### CSS Rules and Selectors

Rule structure:

```css
selector {
  property: value;
}
```

Important selectors:

| Selector | Meaning |
|---|---|
| `*` | Universal |
| `p` | Type selector |
| `.note` | Class selector |
| `#intro` | ID selector |
| `p a` | Any `<a>` descendant of `<p>` |
| `p > a` | Direct `<a>` child of `<p>` |
| `h1 + p` | First `<p>` immediately after `h1` |
| `h1 ~ p` | All following sibling `<p>` elements |

Exam recurring point: `p a` selects any `<a>` element inside a `<p>` element, at any depth.

Pseudo-classes:

```css
a:link {}
a:visited {}
a:focus {}
a:hover {}
a:active {}
```

Order: LVFHA, link -> visited -> focus -> hover -> active.

### Cascade, Specificity, Inheritance

Cascade resolves conflicts among rules.

Specificity order:

1. Inline styles
2. ID selectors
3. Class, pseudo-class, attribute selectors
4. Type selectors
5. Universal selector

If specificity is equal, later rule wins. `!important` overrides normal specificity, with user `!important` rules having highest priority.

Inherited properties: text-related, such as `font-family`, `font-size`, `color`, `line-height`.

Non-inherited properties: box-related, such as `margin`, `padding`, `border`, `width`, `height`.

### Box Model

Every element is a box:

```text
content -> padding -> border -> margin
```

![[css-box-model.jpg|460]]

Total occupied width:

```text
left margin + left border + left padding + width
+ right padding + right border + right margin
```

`width` applies only to content by default.

### Display, Positioning, Float

| Property/value | Meaning |
|---|---|
| `display: block` | Starts new line, full width |
| `display: inline` | Flows inside line |
| `display: none` | Removed from layout |
| `visibility: hidden` | Invisible but space preserved |
| `position: relative` | Offset from normal position; space preserved |
| `position: absolute` | Removed from flow; relative to nearest positioned ancestor |
| `position: fixed` | Removed from flow; relative to viewport |

Float:

```css
img { float: left; }
.after { clear: both; }
```

`float` moves an element left/right and lets following content wrap around it. `clear` prevents an element from appearing next to a floated element and forces it below the float.

### Flexbox and Grid

**Flexbox** is one-dimensional: row or column.

```css
.container {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}
```

**Grid** is two-dimensional: rows and columns.

```css
.grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
}
```

Use Grid for page-level layout; Flexbox for alignment within a row/column or component.

### Responsive Web Design

Responsive design uses one codebase that adapts to different viewport sizes.

Viewport meta tag:

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

Media query:

```css
@media only screen and (min-width: 40em) {
  nav { display: block; }
}
```

Mobile-first approach: define simple mobile layout first, then add complexity for larger screens.

Breakpoints should be based on content, not specific devices.

## 13. JavaScript

### JavaScript Role

In the Web stack:

```text
HTML = structure
CSS = presentation
JavaScript = behavior/interactivity
```

JavaScript is high-level, dynamically typed, interpreted, and traditionally client-side. It can also be used server-side with Node.js.

JavaScript is not Java. The name is historical/marketing; the languages have different type systems, object models, and runtimes.

### What JavaScript Can and Cannot Do

Can:

- modify HTML elements, attributes, and text
- react to events
- validate forms
- update pages using AJAX
- manipulate the DOM

Cannot, due to browser security:

- freely access other tabs/windows
- bypass same-origin policy
- close arbitrary windows
- open windows except under browser restrictions

### Syntax Essentials

JavaScript is case-sensitive; HTML is not.

Types:

| Category | Types |
|---|---|
| Primitive | number, string, boolean, null, undefined |
| Object | objects, arrays, functions |

`undefined` means variable declared but not assigned, or missing property. `null` means explicit absence of value.

Always use explicit semicolons to avoid automatic semicolon insertion surprises.

### Objects and Arrays

Objects are associative arrays:

```javascript
var person = {
  firstName: "John",
  lastName: "Doe",
  fullName: function() {
    return this.firstName + " " + this.lastName;
  }
};
```

Property access:

```javascript
person.firstName
person["firstName"]
```

Arrays are dynamic and heterogeneous:

```javascript
var data = [1, true, "hello"];
data.push(42);
```

`forEach()`:

```javascript
data.forEach(function(value, index, array) {
  console.log(index, value);
});
```

Exam-style answer: `forEach()` iterates through an array and invokes a function for each element.

### Window and Browser Objects

`window` represents the browser window. Global variables are properties of `window`.

Important members:

| Member | Role |
|---|---|
| `alert()` | Message dialog |
| `confirm()` | OK/cancel dialog returning boolean |
| `prompt()` | Input dialog |
| `setTimeout()` | One delayed execution |
| `setInterval()` | Repeated execution |
| `location` | Current URL/navigation |
| `history` | Browser history |
| `navigator` | Browser information |
| `screen` | Display information |
| `document` | DOM root |

### DOM

**DOM** is the in-memory tree representation of an HTML/XML document and the API used to manipulate it.

![[js-dom-tree.jpg|520]]

Node types:

| Node | nodeType |
|---|---|
| Document | 9 |
| Element | 1 |
| Text | 3 |
| Comment | 8 |

Selecting elements:

```javascript
document.getElementById("id")
document.getElementsByName("name")
document.getElementsByTagName("span")
document.getElementsByClassName("warning")
document.querySelectorAll(".sidebar p")
```

Manipulating:

```javascript
var p = document.createElement("p");
var t = document.createTextNode("Hello");
p.appendChild(t);
document.body.appendChild(p);
```

Attributes:

```javascript
element.getAttribute("src");
element.setAttribute("src", "new.jpg");
element.removeAttribute("title");
```

### Events

JavaScript execution phases:

1. Browser parses HTML and builds document.
2. Scripts execute synchronously when encountered.
3. Document completes and `load` event fires.
4. Event-driven phase begins.

Event concepts:

| Concept | Meaning |
|---|---|
| Event | Something the browser reports |
| Event type | String like `click`, `keydown`, `load` |
| Event target | Object where event occurred |
| Event handler | Function registered to respond |

Preferred registration:

```javascript
button.addEventListener("click", function(event) {
  console.log(event.target);
});
```

Avoid inline HTML handlers:

```html
<!-- avoid -->
<button onclick="alert('hi')">
```

`addEventListener()` supports multiple handlers and keeps HTML separate from behavior.

## 14. Form Validation and AJAX

### Form Validation

Form validation checks that user input is correct before it is accepted.

Reasons:

1. Correct data and format.
2. User account security.
3. Protection from malicious input.

| Type | Where | Purpose |
|---|---|---|
| Client-side | Browser | Fast feedback, better UX |
| Server-side | Server | Mandatory security check |

Client-side validation is not enough because users can disable/bypass it. Server-side validation is always required.

### HTML5 Built-in Validation

Attributes:

```html
<input name="email" type="email" required>
<input name="course" pattern="Informatics|ICT|Cybersecurity">
<input name="age" type="number" min="0" max="120">
```

CSS states:

```css
input:invalid { border: 2px dashed red; }
input:valid   { border: 2px solid black; }
```

Constraint Validation API:

```javascript
email.addEventListener("input", function () {
  if (email.validity.typeMismatch) {
    email.setCustomValidity("Please insert an email address!");
  } else {
    email.setCustomValidity("");
  }
});
```

Plain JavaScript validation can use `preventDefault()`:

```javascript
form.addEventListener("submit", function(event) {
  if (!valid) {
    event.preventDefault();
  }
});
```

### AJAX

**AJAX** originally meant Asynchronous JavaScript And XML. Today it means using scripted HTTP from the browser to exchange data with a server without reloading the whole page.

AJAX is client-side technology that programmatically issues HTTP requests.

Use cases:

- live search
- partial page updates
- username availability checks
- shopping cart updates
- REST API calls

### Synchronous vs Asynchronous

Synchronous processing blocks the browser while waiting. Asynchronous processing lets the browser continue; a callback runs when the response arrives.

### XMLHttpRequest

XHR wraps HTTP in a JavaScript API.

HTTP request parts:

1. method
2. URL
3. optional headers
4. optional body

HTTP response parts:

1. status code
2. headers
3. body

Basic XHR:

```javascript
var request = new XMLHttpRequest();
request.open("GET", "data.json");
request.onload = function() {
  if (request.status === 200) {
    var obj = JSON.parse(request.responseText);
  }
};
request.send();
```

For POST JSON:

```javascript
request.open("POST", "/api/employee");
request.setRequestHeader("Content-Type", "application/json");
request.send(JSON.stringify(employee));
```

Ready states:

| Value | Meaning |
|---|---|
| 0 | Object created, `open()` not called |
| 1 | `open()` called |
| 2 | Response headers received |
| 3 | Response body downloading |
| 4 | Complete |

Always check both completion and status before processing:

```javascript
if (request.readyState === XMLHttpRequest.DONE && request.status === 200) {
  // process response
}
```

### CORS

Same-origin policy normally restricts XHR/fetch to the same origin that served the page. An origin is scheme + host + port.

**CORS** lets servers opt in to cross-origin access using headers such as:

```text
Access-Control-Allow-Origin: https://example.com
```

### Response Formats

| Format | Pros | Cons |
|---|---|---|
| HTML | Easy to insert into page | Low portability, server must produce page-ready markup |
| XML | Structured and portable | Verbose, more processing |
| JSON | Concise, natural in JS | Must parse safely, strict syntax |

JSON:

```javascript
var obj = JSON.parse(xhr.responseText);
var text = JSON.stringify(obj);
```

Avoid `eval()` on JSON.

### Fetch API

Fetch is a modern Promise-based alternative to XHR.

```javascript
let response = await fetch(url);

if (response.ok) {
  let json = await response.json();
} else {
  alert("HTTP error: " + response.status);
}
```

Two-step pattern:

1. Check response status.
2. Parse body with `response.json()` or `response.text()`.

## High-Yield Open Question Patterns

Use these to rehearse answers in 5-8 sentences each.

1. Explain why a web application is a three-tier architecture. Mention browser, web/application server, database, and the three logical layers.
2. Explain Maven's lifecycle model and how phases, goals, plugins, and the POM relate.
3. Compare Docker containers and virtual machines, and explain why Docker helps deployment.
4. Define servlet and explain its lifecycle, including `init`, `service`, `doGet/doPost`, and `destroy`.
5. Explain why servlets are not thread-safe and give an example of bad shared state.
6. Explain the DAO pattern and why it helps separate persistence logic from servlet logic.
7. Explain SQL Injection and how prepared statements prevent it.
8. Explain how JSP works internally and how JSP fits MVC.
9. Explain Java Web MVC: Model, View, Controller, request attributes, and forward.
10. Explain REST as an architectural style: resources, URIs, representations, statelessness, and HTTP methods.
11. Compare `GET`, `POST`, `PUT`, and `DELETE`, including safe/idempotent properties.
12. Explain URI, URL, percent encoding, MIME, and `Content-Type`.
13. Explain multipart/form-data and why boundaries are needed.
14. Explain HTTP Basic Authentication and why HTTPS is required.
15. Explain XML well-formedness vs validity; compare DOM, SAX, and StAX.
16. Compare XML and JSON for data interchange.
17. Explain HTML5 semantic elements and why semantic markup matters.
18. Explain the CSS cascade, specificity, inheritance, and box model.
19. Compare Flexbox and Grid; explain responsive design and media queries.
20. Explain the DOM API and how JavaScript manipulates HTML.
21. Explain event handling and why `addEventListener` is preferred.
22. Explain client-side vs server-side form validation.
23. Explain AJAX/XHR/fetch and how they update a page without reload.
24. Compare SQL Injection, XSS, and CSRF: target, mechanism, root cause, defense.
