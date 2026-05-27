# 1. Introduction to Web Applications

## Historical foundations

The Web grew out of earlier work on linked information.

| Person / System                | Main contribution                                                       |
| ------------------------------ | ----------------------------------------------------------------------- |
| Vannevar Bush, Memex (1945)    | Vision of a machine for storing and retrieving linked information.      |
| Ted Nelson, Hypertext / Xanadu | Coined "hypertext"; imagined bidirectional links and versioning.        |
| Douglas Engelbart, NLS         | Early system with mouse, windows, hyperlinks, collaborative editing.    |
| NoteCards                      | Hypertext system for organizing information into cards and links.       |
| Tim Berners-Lee, WWW           | Practical Web architecture at CERN: simple hypertext over the Internet. |

> [!important] Definition - Hypertext
> Hypertext is text connected by links, so the reader can move non-linearly between related pieces of information.

The first popular graphical browser was **Mosaic** (1993). Later browsers include Netscape Navigator, Internet Explorer, Firefox, Safari, Chrome, and Edge.

## Evolution of the Web

![[intro-web10.jpg|520]]

*Figure 1: Diagram of Web 1.0 as an informative read-only Web*

| Phase | Informal name | Core technologies | Main idea |
|---|---|---|---|
| Web 1.0 | Read Web | HTTP, HTML, MIME, URL | Producers publish, users mostly read. |
| Web 2.0 | Read/Write Web | XML, AJAX, JSON, Web services, REST | Users also create content and services interact. |
| Web 3.0 | Web of Data / Semantic Web | RDF, OWL, SPARQL | Data has explicit semantics and machine-readable links. |
| Web3 | Decentralized Web | Blockchain, crypto, DeFi, NFT | User-controlled data and decentralized infrastructure. |

**Deep Web** means content not indexed by ordinary search engines: private databases, login-protected systems, dynamically generated pages. **Dark Web** means anonymous access through systems such as Tor or I2P. They are not the same thing.

## Application layers and architectures

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

A typical Web application follows a **three-tier structure**: the browser handles presentation, the web/application server runs the application logic, and the DBMS stores the data. Browser and server communicate through HTTP over the network stack.

Network stack mapping:

| Layer | Typical protocol in Web applications |
|---|---|
| Application | HTTP / HTTPS |
| Transport | TCP, or UDP for some newer protocols |
| Network | IP |
| Host / physical | Ethernet, Wi-Fi, mobile networks |

For the exam, remember that HTTP is an application-layer request/response protocol carried by the lower Internet layers.

**For open questions:** explain the three logical layers, then map them onto single-tier, two-tier, and three-tier architectures. Keep the distinction clear: the application layer controls the operation flow, while the data layer manages persistent data.

---

# 2. Git and Maven

## Git

**Git** is a distributed version control system. Each local copy is a complete repository, rather than just a checkout from a central server.

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

What to notice:
- `git add` copies selected changes from the working directory to the index.
- `git commit` records staged changes into local history.
- `git push` sends local commits to a remote branch.

Branches are independent lines of development. A feature branch can diverge from `main` and later be merged back.

![[git-branch-merge.jpg|520]]

*Figure 5: Feature branch diverging from and merging back into the main branch*

A **pull request** is different from `git pull`. On platforms such as GitHub or Bitbucket, it is a review request for a branch before it is merged.

## Maven

**Maven** is a Java project management tool. It standardizes building, packaging, dependency resolution, documentation, and deployment.

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

Invoking a Maven phase also executes all previous phases in that lifecycle. For example, `mvn package` validates, compiles, tests, and then packages.

```xml
<groupId>it.unipd.dei.webapp</groupId>
<artifactId>employee-webapp</artifactId>
<version>1.00</version>
<packaging>war</packaging>
```

These are Maven **coordinates**: they identify the artifact. `packaging` says what Maven produces, for example `jar` for ordinary Java archives or `war` for web applications.

Maven uses remote repositories, such as Maven Central, and a local cache under `~/.m2/repository`. If a dependency is missing locally, Maven downloads it.

Maven also expects a standard project layout. This is the "convention over configuration" idea:

| Path | Meaning |
|---|---|
| `src/main/java` | Java source code. |
| `src/main/resources` | Application resources and configuration files. |
| `src/main/webapp` | Web files for a WAR project, such as JSP, HTML, CSS, JS, and `WEB-INF`. |
| `src/test` | Test code and test resources. |
| `target` | Generated build output; it should not be committed. |
| `pom.xml` | Project configuration, dependencies, plugins, and artifact coordinates. |

The file `~/.m2/settings.xml` contains user-level Maven configuration: local repository path, repository mirrors, credentials, proxy settings. It complements the project `pom.xml`: the POM describes the project; `settings.xml` describes the user's Maven environment.

**For open questions:** connect lifecycle -> phase -> goal -> plugin, and explain why the POM is declarative. Also know why generated files such as `target/` do not belong in Git.

---

# 3. Docker and Containerization

## The deployment problem

A Java web application needs compatible versions of Java, Tomcat, PostgreSQL, libraries, configuration files, and environment variables. Maven can create the WAR, but it does not guarantee the runtime environment.

![[docker-webapp-lifecycle.jpg|520]]

*Figure 7: Build and deployment flow from development to Maven WAR and Tomcat runtime*

> [!important] Definition - Containerization
> Containerization packages an application and its runtime dependencies into an isolated environment that behaves consistently across machines.

## Containers vs virtual machines

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

## Docker objects

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

The Dockerfile is declarative: start from a Tomcat image, add the WAR, expose the port. In a real project, each instruction contributes to image layers.

## Docker Compose

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

What to notice:
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

`docker-compose up` creates and starts the services. `docker-compose down` stops and removes containers. `docker exec` is handy for debugging, for example to open a `psql` shell inside the PostgreSQL container.

**For open questions:** explain why Docker solves environment mismatch, how image, container, and volume differ, and why healthchecks matter in a Tomcat + PostgreSQL setup.

---

# 4. Java Servlets

## Browser-server architecture

![[servlet-browser-server-architecture.jpg|520]]

*Figure 11: Browser-server architecture for a servlet-based Web application*

The browser renders HTML/CSS, executes JavaScript, maintains the DOM, and sends HTTP requests. The web server parses requests, performs access control, dispatches to static or dynamic resources, logs activity, and sends responses.

## Jakarta EE and Tomcat

**Jakarta EE** is the standardized platform for enterprise web applications. **Tomcat** is a web container: it implements the servlet/JSP part of the platform and executes web components.

Package names matter:
- Tomcat 9 uses Java EE style `javax.*`.
- Tomcat 10+ uses Jakarta EE style `jakarta.*`.

## Servlet definition and lifecycle

> [!important] Definition - Servlet
> A servlet is a Java-based web component, managed by a web container, that generates dynamic content in response to requests.

Servlets usually extend `HttpServlet`. The container controls the lifecycle:

1. `init(ServletConfig)` runs once after servlet creation.
2. `service(req, res)` runs for each request.
3. `service()` dispatches to `doGet`, `doPost`, `doPut`, `doDelete`, etc.
4. `destroy()` runs once before the servlet is taken out of service.

Servlets are **not automatically thread-safe**. Several concurrent requests may use the same servlet instance. Request-specific data must stay in local variables, not in shared instance fields.

![[servlet-sequence-diagram.jpg|520]]

*Figure 12: First servlet request sequence from browser request to generated HTML response*

## `web.xml` mapping

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

The container maps `/hello` to `HelloWorldServlet`. A servlet can have multiple URL patterns.

`WEB-INF/` is not directly accessible from the browser. It contains private web app configuration such as `web.xml`, libraries, and compiled classes.

## Minimal servlet response

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

What to notice:
- `setContentType` sets the MIME type and character encoding.
- `getWriter` obtains the response body writer.
- The servlet manually writes HTML.
- The writer is flushed and closed after writing.

Manual HTML generation is fine for tiny examples, but it becomes painful quickly. JSP and MVC are introduced to avoid this style in real pages.

## Logging with Log4J

Log4J separates:

| Concept | Role |
|---|---|
| Logger | Emits log messages. |
| Appender | Destination: console, file, rolling file, etc. |
| Layout | Format of the log line. |
| Level | Filters messages: `TRACE < DEBUG < INFO < WARN < ERROR < FATAL`. |

`ThreadContext` / MDC stores request-scoped metadata such as IP, user, action, and resource. The pattern is:

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

The `finally` cleanup matters because servlet containers reuse threads. If MDC data is left behind, the next request handled by the same thread may inherit the wrong logging context.

## GET and POST forms

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

GET puts parameters in the URL query string. POST sends them in the request body. In servlets, both can be read with:

```java
String name = req.getParameter("helloName");
```

**For open questions:** know servlet lifecycle, `HttpServletRequest` vs `HttpServletResponse`, `doGet` vs `doPost`, URL mapping, WAR packaging, and why servlet instance variables are dangerous.

---

# 5. Servlets and Database Access

## Application structure

The employee application is divided into layers:

| Layer | Classes / technologies |
|---|---|
| Interface/application logic | Servlets parse HTTP parameters, call DAOs, create responses. |
| Data logic | DAO classes contain SQL and JDBC operations. |
| Data layer | PostgreSQL stores `Employee` and `Manage` tables. |

## Resource classes

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

Fields are `final`, so the object cannot change after construction. That is safer during request processing.

`Message` carries success or error information:

| Field | Meaning |
|---|---|
| `message` | Human-readable message. |
| `errorCode` | Application error code, such as `E100`. |
| `errorDetails` | Technical details. |
| `isError` | Distinguishes error and success messages. |

## DAO pattern

> [!important] Definition - DAO
> A Data Access Object encapsulates all logic needed to access a data source. Servlets should not contain SQL; they should call DAOs.

![[db-dao-interface.jpg|520]]

*Figure 13: DAO interface used to isolate database access from servlet logic*

```java
public interface DataAccessObject<T> {
    DataAccessObject<T> access() throws SQLException;
    T getOutputParam();
}
```

`access()` performs the database operation. `getOutputParam()` returns the result, for example a `List<Employee>`.

```java
String sql = "SELECT badge, surname, age, salary FROM Employee WHERE salary > ?";
PreparedStatement pstmt = con.prepareStatement(sql);
pstmt.setInt(1, salary);
ResultSet rs = pstmt.executeQuery();
```

What to notice:
- The SQL structure is fixed.
- `?` is a placeholder.
- `setInt` binds the user value as data.
- The database cannot interpret that value as SQL syntax.

That is the main defense against SQL injection.

## Connection pool

Opening a new database connection for every request is expensive. Tomcat can manage a connection pool exposed through JNDI.

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

In the course setup, this pool is declared in `src/main/webapp/META-INF/context.xml`, then exposed to the web application through a `web.xml` resource reference:

```xml
<resource-ref>
  <res-ref-name>jdbc/employee-ferro</res-ref-name>
  <res-type>javax.sql.DataSource</res-type>
  <res-auth>Container</res-auth>
</resource-ref>
```

`context.xml` defines the Tomcat resource; `web.xml` declares that the application wants to use it.

Servlets look up the `DataSource` once in `init()`:

```java
InitialContext cxt = new InitialContext();
ds = (DataSource) cxt.lookup("java:/comp/env/jdbc/employee-ferro");
```

Each request then borrows a connection with `ds.getConnection()`.

## Request flow

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

**For open questions:** explain why DAO improves separation of concerns and security. Be able to describe JNDI + connection pool + servlet + DAO as one flow.

---

# 6. JSP and MVC

## Why JSP

Writing HTML with `out.printf` inside servlets gets messy fast. JSP lets developers write mostly HTML and keep the dynamic parts controlled.

> [!important] Definition - JSP
> A JavaServer Page is a template-based server-side view. On first request, the container translates the `.jsp` file into a servlet, compiles it, and executes it.

![[Pasted image 20260512115326.png|420]]

*Figure 16: JSP translation and execution flow from JSP source to servlet class and HTML response*

First invocation: `hello.jsp -> hello_jsp.java -> hello_jsp.class -> response`. Later invocations reuse the compiled servlet class.

## JSP components

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

What to notice:
- `${param.helloName}` reads request parameter `helloName`.
- `empty` checks null or empty string.
- `<c:out>` escapes HTML/XML characters, so it is safer than raw output.

JSTL is divided into tag libraries:

| Prefix | Purpose |
|---|---|
| `c` | Core control flow, output, URLs, imports, redirects. |
| `fmt` | Locale, message bundles, date and number formatting. |
| `fn` | Functions, especially string utilities such as length, contains, replace, split. |

Shared JSP fragments can be included with actions such as `<c:import>`. Use them for repeated parts like headers, footers, menus, or message blocks.

## JavaBeans and EL

JavaBeans expose properties through methods like `getBadge()` and `isError()`. Expression Language resolves:

```jsp
${employee.badge}
```

as a call to:

```java
employee.getBadge()
```

## MVC

> [!important] Definition - MVC
> Model-View-Controller separates application state and logic (Model), rendering (View), and input handling / flow control (Controller).

![[jsp-mvc-layers-employee.jpg|480]]

*Figure 17: Mapping of MVC roles to servlet controllers, JSP views, DAOs, and resource classes*

| MVC role | Java web technology |
|---|---|
| Model | Java resource classes and DAOs. |
| View | JSP pages. |
| Controller | Servlets. |

The servlet no longer writes all HTML. It sets request attributes and forwards to a JSP.

```java
req.setAttribute("employee", e);
req.setAttribute("message", m);
req.getRequestDispatcher("/jsp/create-employee-result.jsp").forward(req, res);
```

The JSP then reads the model:

```jsp
<c:out value="${employee.badge}"/>
<c:out value="${message.message}"/>
```

`forward()` is server-side: the browser still receives a single HTTP response.

## Result JSP example

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

What to notice:
- `<c:import>` dynamically includes a shared JSP fragment.
- `<c:if>` conditionally renders a block.
- `<c:out>` escapes user-controlled data and prevents simple XSS.

JSTL must be bundled in the WAR; Tomcat does not provide it by default. The Servlet API is usually marked as `provided`, but JSTL is not.

**For open questions:** explain the JSP execution model, why scriptlets are bad, how EL resolves bean properties, and how MVC changes the servlet-only architecture.

---

# 7. REST Web Services

## REST principles

> [!important] Definition - REST
> REST, Representational State Transfer, is an architectural style that applies Web principles to services. Data is modeled as resources, resources are identified by URIs, and HTTP methods form a uniform interface.

![[Pasted image 20260512123223.png|420]]

*Figure 18: REST model based on resources, representations, and state transitions*

A **resource** is anything with identity and state. It has a URI and can be transferred as a representation: JSON, XML, HTML, and so on.

| HTTP method | CRUD meaning | Example |
|---|---|---|
| GET | Read | `GET /student/123456` |
| POST | Create subordinate resource | `POST /student` |
| PUT | Create or replace resource | `PUT /student/123456` |
| DELETE | Delete | `DELETE /student/123456` |

REST is stateless: each request must carry all information needed to process it.

A **Web service** is a software system for interoperable machine-to-machine interaction over a network, using standard Web technologies. REST is one way to design such services.

## Representations and content negotiation

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

The `Accept` header says which response media types the client can process. For POST/PUT, `Content-Type` says what media type the request body has.

## Employee REST API

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

## API documentation

REST APIs need precise documentation. The notes mention two approaches:

| Format | Description |
|---|---|
| WADL | XML description for HTTP-based services; W3C submission, not a dominant standard. |
| OpenAPI | YAML/JSON description of servers, paths, methods, parameters, schemas, and responses; modern de-facto standard. |

OpenAPI is the one you are more likely to see in practice, because many tools can generate documentation, validators, and clients from it.

## REST implementation pattern

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

The generator writes tokens in order. `flush()` sends buffered data to the servlet response stream. The code disables Jackson auto-close so Jackson does not close the servlet stream by accident.

## Header validation

`checkMethodMediaType()` validates REST requests:

| Case | Error |
|---|---|
| Missing `Accept` | `E4A1`, 400 |
| Unsupported `Accept` | `E4A2`, 406 |
| Missing `Content-Type` on POST/PUT | `E4A3`, 400 |
| Unsupported input media type | `E4A4`, 415 |
| Unsupported HTTP method | `E4A5`, 405 |
| Unknown resource | `E4A6`, 404 |

## REST dispatcher

`RestDispatcherServlet` overrides `service()` so it can support `GET`, `POST`, `PUT`, `DELETE`, and dispatch by both URI and method.

```xml
<servlet-mapping>
  <servlet-name>RestManagerServlet</servlet-name>
  <url-pattern>/rest/*</url-pattern>
</servlet-mapping>
```

**For open questions:** explain REST resources, URIs, methods, representations, `Accept` vs `Content-Type`, error status codes, and why a REST front controller dispatches all `/rest/*` requests.

---

# 8. HTTP and Surroundings

## Four Web pillars

| Standard | Role |
|---|---|
| HTML | Markup language for web pages. |
| HTTP | Application-layer request/response protocol. |
| MIME | Media type and encoding of exchanged information. |
| URL | Locates resources on the Web. |

## URI, URL, URN, IRI

> [!important] Definition - URI
> A URI is a compact sequence of characters that identifies an abstract or physical resource.

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

`path` identifies hierarchical resource location, `query` carries name/value parameters, and `fragment` identifies a secondary resource inside the representation.

## Percent-encoding and character encoding

Percent-encoding writes an octet as `%XX` in hexadecimal. It is used for reserved characters and non-ASCII characters in URIs.

| Character | Encoding |
|---|---|
| space | `%20` |
| `?` | `%3F` |
| `&` | `%26` |
| `#` | `%23` |

ASCII uses 7 bits and covers 128 characters. Extended ASCII uses 8 bits but creates country-specific incompatibilities. Unicode gives a common character set. UTF-8 is the dominant Web encoding and stays compatible with ASCII for the first 128 characters.

## MIME

> [!important] Definition - MIME
> MIME defines media types and transfer encodings for email and the Web.

Important headers:

| Header | Meaning |
|---|---|
| `Content-Type` | Media type of body, e.g. `text/html; charset=utf-8`. |
| `Content-Encoding` | Compression applied to body, e.g. `gzip`. |
| `Content-Disposition` | Suggested handling, e.g. attachment filename. |
| `Content-Transfer-Encoding` | Encoding for binary transport, e.g. Base64. |

## Multipart and form encodings

`multipart/form-data` is used for file uploads. Each field or file is a separate MIME part separated by a boundary.

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

Always validate file type server-side. The HTML `accept` attribute is only a client hint and can be bypassed.

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

Jakarta Mail represents messages with `Session`, `MimeMessage`, `Transport`, `MimeMultipart`, and `MimeBodyPart`. An email with an attachment is `multipart/mixed`: one body part for the HTML/text message and one for the binary attachment.

## HTTP

![[http-proxy-architecture.jpg|420]]

*Figure 20: HTTP request-response chain with browser, proxies, and origin web server*

HTTP is textual, request-response based, and stateless. Statelessness helps scalability because each request can be handled independently.

| Method | Meaning | Safe | Idempotent |
|---|---|---|---|
| GET | Retrieve resource | yes | yes |
| HEAD | GET without response body | yes | yes |
| POST | Submit data/create subordinate resource | no | no |
| PUT | Store/replace resource | no | yes |
| DELETE | Delete resource | no | yes |
| OPTIONS | Communication options | yes | yes |

**Safe** means no intended server-side side effects. **Idempotent** means repeating the same request has the same effect as doing it once.

Status code classes:

| Class | Meaning |
|---|---|
| 1xx | Informational. |
| 2xx | Success, e.g. `200 OK`, `201 Created`, `204 No Content`. |
| 3xx | Redirection, often with `Location`. |
| 4xx | Client error, e.g. `400`, `401`, `404`, `405`, `409`, `415`. |
| 5xx | Server error, e.g. `500`. |

## Authentication

HTTP Basic authentication:

```http
Authorization: Basic bmljb2xhOmZlcnJv
```

The value is Base64 of `username:password`. Base64 is encoding, not encryption. Basic auth must be used with HTTPS.

If credentials are missing or wrong, the server answers:

```http
HTTP/1.1 401 Unauthorized
WWW-Authenticate: Basic realm="Webapp"
```

## Filters and sessions

A Servlet `Filter` can protect paths before requests reach servlets/JSPs.

```java
HttpSession session = req.getSession(false);
if (session == null) {
    if (!authenticateUser(req, res)) return;
}
chain.doFilter(req, res);
```

What to notice:
- `getSession(false)` does not create a new session.
- If no valid session exists, the filter tries Basic authentication.
- If authentication succeeds, it stores the user in `HttpSession`.
- `chain.doFilter` lets the request continue.

**For open questions:** URI vs URL, percent-encoding, MIME multipart boundaries, safe/idempotent HTTP methods, status code classes, Basic auth, and filter/session authentication are likely exam material.

---

# 9. Markup Languages, XML, and JSON

## Markup types

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

Modern Web pages should use descriptive markup and leave presentation to CSS.

## SGML, HTML, XML

**SGML** is a meta-markup language and ancestor of HTML and XML. It introduced DTDs.

HTML4 often mixed structure and presentation. Example: `<font color="red">` is procedural because it says how text should look. HTML5 separates the two more cleanly, using semantic elements for meaning and CSS for presentation.

> [!important] Definition - XML
> XML is a markup language for representing and exchanging semi-structured information. It is designed for interoperability among distributed systems.

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

## Well-formed vs valid XML

Well-formed XML is syntactically correct:
- matching opening and closing tags,
- properly nested elements,
- quoted attribute values,
- exactly one root element.

Valid XML also satisfies a DTD or XML Schema.

## DOM, SAX, StAX

![[markup-dom-interfaces.jpg|520]]

*Figure 22: DOM interface hierarchy rooted in the generic Node abstraction*

| Parser | Model | Memory | Direction | Good for |
|---|---|---|---|---|
| DOM | In-memory tree | higher | bidirectional | random access, modification |
| SAX | Push streaming callbacks | low | forward only | large read-only XML |
| StAX | Pull streaming | low | forward only | application-controlled parsing |

DOM is the model browsers use for HTML and JavaScript manipulation.

## DTD, namespaces, XSD

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

The URI works as a unique identifier; it does not necessarily have to be dereferenced.

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

## JSON and Jackson

> [!important] Definition - JSON
> JSON is a lightweight, language-independent data interchange format based on objects, arrays, strings, numbers, booleans, and null.

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

JSON is usually more compact than XML because it has no closing tags and maps naturally to JavaScript objects.

**JSON Schema** defines the expected structure of JSON data: object properties, required fields, value types, formats, and constraints. It does roughly the same job for JSON that XML Schema does for XML, although it is not part of the core JSON syntax.

Jackson streaming parser pattern:

```java
JsonParser jp = JSON_FACTORY.createParser(in);
while (jp.getCurrentToken() != JsonToken.FIELD_NAME
        || !"employee".equals(jp.getCurrentName())) {
    if (jp.nextToken() == null) throw new EOFException("No Employee object found.");
}
```

The parser pulls one token at a time, like StAX for XML. This helps with large inputs because the program does not need to build the whole object tree first.

**For open questions:** procedural vs descriptive markup, XML well-formed vs valid, DOM/SAX/StAX differences, DTD vs XSD, namespaces, JSON vs XML, and Jackson streaming.

---

# 10. HTML5

## Base structure

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

## Semantic HTML

Choose HTML tags for meaning, not for visual appearance. Use CSS for visual style.

Example: do not use `<h1>` just to make text large. Use `<h1>` when the text is the main heading.

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

## Links, images, tables, forms

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

`alt` is required for accessibility and fallback. `<figure>` and `<figcaption>` associate media with its caption.

```html
<form action="/create-employee" method="post">
  <input type="text" name="surname">
  <input type="email" name="email">
  <button type="submit">Submit</button>
</form>
```

`name` is the server-side parameter name. `id` is unique in the page and used by CSS or JavaScript. Radio buttons share the same `name` to form one group.

## HTML5 semantic layout

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

HTML5 layout is clearer than generic `<div id="header">` patterns. Developers, accessibility tools, and search engines can read the structure more easily.

HTML5 also standardizes APIs that previously required plug-ins or custom solutions: Media API, Session History, Offline Web Applications, Editing, Drag and Drop, Canvas, Web Storage, Geolocation, Web Workers, and Web Sockets.

## Media and canvas

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

Canvas creates a drawable rectangle; JavaScript performs the actual drawing.

**For open questions:** base structure, `title`, block vs inline, semantic vs presentational tags, `id` vs `name`, forms, `<figure>`, semantic layout elements, and native media/canvas.

---

# 11. Web Security

## CIA triad and attack surface

| Security goal | Meaning |
|---|---|
| Confidentiality | Information is available only to intended users. |
| Integrity | Information is not altered unexpectedly. |
| Availability | Information is accessible when needed. |

![[websec-scenario.jpg|480]]

*Figure 26: Web application attack surface involving users, web server, SQL queries, and database*

In web applications, attackers often have the same HTTP access as normal users. The bug appears when the application processes that input incorrectly.

**OWASP Top Ten** is a reference document for common Web application security risks. In this course, the lecture focuses especially on SQL Injection, Cross-Site Scripting, and Cross-Site Request Forgery. OWASP gives the context; an exam answer still needs the concrete attack flow and the defense.

## SQL Injection

> [!important] Definition - SQL Injection
> SQL injection happens when untrusted user input is mixed with trusted SQL code and the database interprets attacker-controlled text as SQL syntax.

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

Prepared statements separate SQL code from data. The DB compiles the query structure before parameter values are bound.

## XSS

> [!important] Definition - XSS
> Cross-Site Scripting lets an attacker inject malicious JavaScript into pages viewed by other users. The script executes in the victim's browser under the trusted site's origin.

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

In JSP, `<c:out>` matters because it escapes output.

## CSRF

> [!important] Definition - CSRF
> Cross-Site Request Forgery tricks an authenticated user's browser into sending an unwanted request to a site where the user is already logged in.

![[websec-csrf-schema2.jpg|480]]

*Figure 29: CSRF attack flow where a malicious page triggers authenticated cross-site requests*

The attacker does not need to know the victim's cookie. The browser automatically sends cookies for the target site.

Protection:

| Defense | Effect |
|---|---|
| `SameSite=Strict` cookie | Cookie not sent in cross-site requests. |
| CSRF token | Server accepts only requests containing a valid unpredictable token. |
| Method discipline | Avoid state-changing GET requests. |

**For open questions:** compare SQLi, XSS, and CSRF by target, root cause, attack flow, and primary defenses. This comparison is very likely to work as an open-answer question.

---

# 12. CSS

## Role and attachment

CSS defines presentation. It keeps visual style separate from HTML structure.

Preferred attachment:

```html
<link rel="stylesheet" type="text/css" href="styles.css">
```

External stylesheets are cacheable and reusable across pages. Embedded `<style>` applies only to one page. Inline `style="..."` is hard to maintain and has high specificity.

## Rules and selectors

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

## Cascade and inheritance

Specificity priority:
1. inline style,
2. ID selector,
3. class / pseudo-class / attribute selector,
4. type selector,
5. universal selector.

If specificity is equal, the later rule wins. `!important` overrides ordinary specificity; user `!important` rules outrank author rules, which matters for accessibility.

Text properties such as `font-family`, `font-size`, `color`, `line-height` inherit. Box properties such as `margin`, `padding`, `border`, `width` do not.

## Colors and typography

CSS colors can be expressed in several equivalent formats:

```css
p { color: red; }
p { color: rgb(255, 0, 0); }
p { color: #ff0000; }
p { color: hsl(0, 100%, 50%); }
p { color: rgba(255, 0, 0, 0.5); }
```

`rgba()` and `hsla()` add alpha only to the specific color property. `opacity` applies transparency to the whole element, including children.

```css
body {
  font-family: Georgia, "Times New Roman", serif;
  font-size: 16px;
  line-height: 1.5;
}
```

A font stack lists preferred fonts first, then fallbacks, ending with a generic family such as `serif`, `sans-serif`, or `monospace`.

## Box model

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

## Display, positioning, float

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

## Flexbox, Grid, responsive design

Before modern responsive layouts, many pages used either fixed or liquid layouts:

| Layout | Unit style | Advantage | Risk |
|---|---|---|---|
| Fixed | Pixel-based widths | Precise visual control. | Does not adapt well to different screens. |
| Liquid | Percentage-based widths | Adapts to available width. | Can create overly long lines or unstable layouts. |

Responsive Web Design combines flexible measurements, media queries, flexible media, and the viewport meta tag. A related strategy is **progressive enhancement**: start from a simple baseline that works everywhere, then add layout and behavior where the browser or screen can support it. Mobile-first CSS is a common form of this approach.

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

Breakpoints should come from the content: add one when the layout starts to break, not because of a specific device name.

**For open questions:** CSS selectors, specificity/cascade, inheritance, box model formula, `display:none` vs `visibility:hidden`, positioning, flex vs grid, viewport and media queries.

---

# 13. JavaScript

## Role in the web stack

| Technology | Responsibility |
|---|---|
| HTML | Structure. |
| CSS | Presentation. |
| JavaScript | Behavior and interactivity. |

JavaScript is high-level, dynamically typed, interpreted, and supports both object-like and functional styles. In the browser, it can modify the current page and react to events, but same-origin restrictions protect other pages and origins.

Prefer external JavaScript:

```html
<script src="my_script.js"></script>
```

Scripts execute in document order. A `<script>` pauses HTML parsing while it loads and runs, so scripts are often placed at the end of `<body>`.

## Types and objects

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

Here, `this` refers to the object that owns the method call.

Constructor functions create multiple objects with the same structure when they are called with `new`:

```javascript
function Person(firstName, lastName) {
  this.firstName = firstName;
  this.lastName = lastName;
  this.fullName = function() {
    return this.firstName + " " + this.lastName;
  };
}

var ada = new Person("Ada", "Lovelace");
```

Inside the constructor, `this` refers to the new object being initialized.

Arrays are dynamic and heterogeneous:

```javascript
var misc = [1.1, true, "a", { x: 1 }];
misc.push("new");
misc.forEach(function(value, index, array) {
  console.log(index, value);
});
```

`forEach` calls a callback for each element with `(value, index, array)`.

## Browser objects and DOM

`window` is the global browser object. It exposes `document`, `location`, `history`, `navigator`, `screen`, timers, dialogs, and the console.

Useful browser methods:

```javascript
alert("Message");                         // message, no return value
var ok = confirm("Proceed?");             // true for OK, false for Cancel
var name = prompt("What is your name?");  // string or null

setTimeout(function() { console.log("once"); }, 2000);
setInterval(function() { console.log("repeat"); }, 1000);
```

`confirm()` is often tested: it shows OK/Cancel and returns a boolean. Timers schedule asynchronous callbacks; they do not block the whole browser while waiting.

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

What to notice:
- created nodes are not visible until inserted into the document,
- `appendChild` adds a node as last child,
- `createTextNode` avoids interpreting text as HTML.

## Events

An event has a type and a target: for example, a `"click"` event on a button.

Preferred registration:

```javascript
var b = document.getElementById("mybutton");
b.addEventListener("click", function(event) {
  alert("Thanks!");
});
```

Why `addEventListener` is preferred:
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

**For open questions:** JavaScript vs Java, primitive vs object, objects as associative arrays, arrays and `forEach`, DOM tree and selection methods, node creation, and `addEventListener`.

---

# 14. Form Validation and AJAX

## Form validation

Validation checks user input before the application accepts it.

| Validation type | Where | Purpose |
|---|---|---|
| Client-side | Browser | Fast feedback, better user experience. |
| Server-side | Server | Security and final correctness gate. |

Client-side validation is not enough, because attackers can bypass it.

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

`setCustomValidity("")` clears the error; any non-empty string marks the field as invalid with that custom message.

Manual JavaScript validation usually uses event handlers, regular expressions, CSS classes, and `event.preventDefault()` in the submit handler.

## AJAX

> [!important] Definition - AJAX
> AJAX is scripted HTTP from the browser. It lets a page exchange data with the server and update part of the DOM without reloading the whole page.

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

## Encoding request bodies

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

## CORS

The same-origin policy normally blocks XHR responses from other origins. CORS is how the server opts in, using headers such as `Access-Control-Allow-Origin`.

## JSON and Fetch

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

Fetch returns a Promise. `await response.json()` parses the response body into a JavaScript object.

**For open questions:** client vs server validation, HTML5 validation attributes, Constraint Validation API, `preventDefault`, XHR lifecycle, CORS, JSON parse/stringify, and Fetch vs XHR.

---

# 15. jQuery and HTML5 Canvas

## jQuery

jQuery is a JavaScript library for shorter DOM selection, DOM manipulation, event handling, and AJAX.

The `$()` function has several uses:

```javascript
$("p")                  // select all <p> elements
$(document)             // wrap a raw DOM object
$("<p>Hello</p>")       // create a new DOM element
```

A **jQuery object** is a set of zero or more DOM elements plus jQuery methods. It is not the same as a raw DOM element.

```javascript
$("p").css("color", "red");
```

`$("p")` returns all paragraphs as a jQuery object. `.css("color", "red")` sets the CSS property on all matched elements.

Getter/setter pattern:

```javascript
$("#title").text();              // getter: returns text
$("#title").text("New title");   // setter: changes text and returns jQuery object
```

Setters support chaining. Getters usually end the chain because they return a value.

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

`text()` is safer for user content because it treats the value as text. `html()` parses HTML and can introduce XSS if the value is untrusted.

## Canvas

`<canvas>` is a fixed-size bitmap drawing surface. CSS resizing can distort it because the internal bitmap size and visual size may differ.

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

Canvas coordinates start at top-left `(0,0)`. `x` grows to the right, `y` grows downward. One canvas unit usually corresponds to one pixel.

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

`beginPath()` starts a new path. `moveTo()` moves the virtual pen without drawing. `lineTo()` draws a segment. `stroke()` draws the outline; `fill()` fills the shape.

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

Without `onload`, the drawing code may run before the image bytes are available.

State and transformations:

```javascript
ctx.save();
ctx.translate(100, 100);
ctx.rotate(Math.PI / 4);
// draw rotated object
ctx.restore();
```

`save()` and `restore()` prevent transformations and styles from leaking into later drawing. Use `requestAnimationFrame()` for animations synchronized with browser repaint.

**For open questions:** jQuery object vs DOM element, getter/setter chaining, `text` vs `html`, jQuery AJAX shortcuts, canvas coordinate system, paths, image loading, state stack, and animation scheduling.

---

# 16. Semantic Web and Linked Data

## Web of documents to Web of data

![[Figures/slide-003-fig-01.jpg|520]]

*Figure 36: Evolution from the Web of Documents to the Web of Data*

The Web of Documents links human-readable pages. The Web of Data links data entities with typed relationships, so machines can interpret what the links mean.

Raw data becomes information when schema or metadata gives it meaning.

![[Figures/slide-006-fig-01.jpg|520]]

*Figure 37: Raw data becoming information when interpreted through schema and metadata*

Example: `123`, `91`, `38.5`, `7` are just numbers. With labels, they become heart rate, pressure, temperature, age, etc.

## Ontologies, RDF, knowledge graphs

| Layer | Technology | Meaning |
|---|---|---|
| Ontology | OWL | Classes, properties, constraints, abstract concepts. |
| Linked Data | RDF | Concrete facts about instances. |
| Knowledge graph/base | RDF + ontology | Connected graph of typed facts. |

## RDF

> [!important] Definition - RDF triple
> RDF represents facts as triples: `(subject, predicate, object)`.

```text
Subject   -> URI
Predicate -> URI
Object    -> URI or literal
```

![[Figures/slide-009-fig-01.jpg|520]]

*Figure 38: RDF document serializations representing an RDF graph of subject-predicate-object triples*

The predicate is a URI because relationships need global identifiers too. The object can be another resource URI or a literal value.

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

## RDF serializations

Same graph, different syntaxes:

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

## SPARQL

> [!important] Definition - SPARQL
> SPARQL is the standard query language for RDF graphs, analogous to SQL for relational databases.

```sparql
PREFIX foaf: <http://xmlns.com/foaf/0.1/>

SELECT ?name (COUNT(?friend) AS ?count)
WHERE {
  ?person foaf:name ?name .
  ?person foaf:knows ?friend .
}
GROUP BY ?person ?name
```

What to notice:
- variables start with `?`,
- `WHERE` contains graph patterns to match triples,
- `COUNT(?friend)` counts matched friends,
- `GROUP BY` groups by person/name before aggregation.

![[Figures/slide-016-fig-01.jpg|560]]

*Figure 40: SPARQL query and XML result format for counting friends in an RDF graph*

## Linked Data and FAIR

Tim Berners-Lee's four Linked Data principles:

1. Use URIs as names for things.
2. Use HTTP URIs so those names can be looked up.
3. When a URI is looked up, provide useful information using RDF/SPARQL.
4. Include links to other URIs so users and machines can discover more data.

Linked Open Data is Linked Data published under an open license.

![[Figures/slide-021-fig-01.jpg|560]]

*Figure 41: Linked Open Data cloud showing many interlinked datasets across domains*

The LOD cloud is large, so discovery becomes a practical problem: it can be hard to find the dataset and links you actually need.

FAIR principles:

| Principle | Meaning |
|---|---|
| Findable | Persistent identifiers, rich metadata, searchable indexes. |
| Accessible | Retrievable by standard protocols; metadata can remain available. |
| Interoperable | Formal representation and shared vocabularies. |
| Reusable | Clear license, provenance, accurate attributes, community standards. |

DBpedia extracts structured data from Wikipedia. Wikidata is a collaborative, multilingual knowledge base with stable entity URIs.

![[Figures/slide-028-fig-01.jpg|540]]

*Figure 42: W3C One Web technology stack including Web applications, Semantic Web, Web services, and security*

The Semantic Web stack belongs to the same "One Web" view: it sits alongside Web Applications, Web Services, Privacy/Security, and shared Web foundations such as URI, HTTP, XML, RDF, DOM, and SPARQL.

**For open questions:** Web of Documents vs Web of Data, data vs information, RDF triple model, URI/literal distinction, serialization formats, SPARQL graph matching, Linked Data principles, LOD vs Linked Data, and FAIR.

---

# High-Yield Open Questions to Practice

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
