# Web Applications 2025-26 - exam questions and model answers

Source note: [[Web Applications 25-26]].

Study bank for a 1-hour written exam with 3-4 questions. Each macro-topic has possible theory questions and paper-code questions, with compact model answers. Use it for rehearsal: definitions, code skeletons, and links between topics.

## How to study

- For theory questions, answer with: definition, role in the system, main mechanism, example.
- For code questions, write the essential structure first: class or method signature, main API calls, error handling, produced response or output.
- For architecture questions, sketch the layers and label responsibilities before writing prose.
- For security questions, state root cause and mitigation.

---

## 1. Introduction to web applications

### Q1. Why are web applications considered a special case of three-tier architecture?

**Answer.**  
A web application separates responsibilities into three logical tiers:

- Presentation tier: the browser renders HTML/CSS and executes JavaScript.
- Application tier: the web/application server handles HTTP requests, runs servlets/JSP/REST logic, validates input, and coordinates operations.
- Data tier: the database stores persistent application data.

It is a special case of three-tier architecture because the browser acts as a universal thin client. Users do not install application-specific client software: they only need a browser. The server side can be updated centrally, while data remains isolated in the database tier.

### Q2. Compare Web 1.0, Web 2.0, Web 3.0, and Web3.

**Answer.**  
Web 1.0 was mostly a read-only web based on static or simple dynamic pages. Main technologies were HTML, HTTP, MIME, and URLs. Users mainly consumed content.

Web 2.0 introduced read/write interaction: social networks, user-generated content, AJAX, JSON, XML, REST APIs, and web services. Users became content producers.

Web 3.0 is the Semantic Web idea: data is machine-readable and linked through technologies such as RDF, OWL, and SPARQL. The goal is data integration that software can interpret more directly.

Web3 is a newer blockchain-based idea: decentralization, smart contracts, DeFi, NFTs, and user-controlled assets. It should not be confused with the Semantic Web.

### Q3. What is the difference between Deep Web and Dark Web?

**Answer.**  
The **Deep Web** is all web content not indexed by standard search engines: private databases, university portals, email inboxes, cloud documents, banking areas, and dynamically generated pages.

The **Dark Web** is a smaller part of the Deep Web that requires special software or protocols, such as Tor, and is intentionally hidden. Confusing them is wrong because most Deep Web content is normal private or restricted content, not hidden criminal infrastructure.

### Q4. What are presentation logic, application logic, and data logic?

**Answer.**  
Presentation logic controls how data is shown to users and how users interact with the interface. In web apps, this includes HTML, CSS, JavaScript, and JSP views.

Application logic implements use cases: request handling, validation, workflow, authorization, and coordination between components. Servlets and REST resources often live here.

Data logic manages persistent data: SQL queries, transactions, database access, and mapping rows to objects. DAO classes implement this layer in the notes.

### Q5. How does HTTP fit into the TCP/IP stack?

**Answer.**  
HTTP is an application-layer protocol. It defines request and response messages exchanged between clients and servers. It relies on lower layers for delivery: TCP provides reliable transport, IP provides addressing and routing, and the link layer handles local network transmission. HTTP does not manage packets directly; it defines web-level semantics such as methods, headers, status codes, and bodies.

### Q6. How does application load distribution change from single-tier to two-tier and three-tier architectures?

**Answer.**  
In a single-tier architecture, all logic runs on one machine, so scaling is limited. In a two-tier architecture, the client and server share responsibilities. In a fat-client model, presentation and application logic live on the client, causing maintenance problems. In a fat-server model, the client is thinner and the server handles more logic. In a three-tier architecture, presentation, application, and data logic are separated, so each tier can be scaled, maintained, and secured more independently.

### Q7. Why were graphical browsers such as Mosaic important for Web adoption?

**Answer.**  
Graphical browsers made the Web usable for non-specialists by integrating text, links, and images in one visual interface. Mosaic helped move the Web from a technical hypertext system to a mainstream information platform. Later browsers continued this evolution by improving standards support, scripting, performance, and developer tools.

---

## 2. Git and Maven

### Q1. Explain Git's three local areas: working directory, Index/Stage, and HEAD.

**Answer.**  
The **working directory** contains the files currently visible and editable by the developer. The **Index** or **Stage** contains the changes selected for the next commit. **HEAD** points to the latest committed snapshot of the current branch.

`git add` moves changes from the working directory to the Index. `git commit` records the staged changes into the repository and updates HEAD. `git push` sends committed changes to a remote repository.

### Q2. What is the difference between a centralized and a distributed version control system?

**Answer.**  
In a centralized system, there is one main repository and developers usually need the central server for most operations. In a distributed system like Git, every clone contains the full repository history. Developers can commit, branch, inspect history, and merge locally, then synchronize with remotes later. This makes offline work and branch-heavy workflows much easier.

### Q3. How are Maven lifecycles, phases, goals, and plugins related?

**Answer.**  
A **lifecycle** is an ordered build process. The default lifecycle includes phases such as `validate`, `compile`, `test`, `package`, `install`, and `deploy`.

A **phase** is a step in that lifecycle. When a phase is executed, all previous phases are executed too. For example, `mvn package` also compiles and tests before creating the artifact.

A **goal** is a concrete operation implemented by a **plugin**, such as compiling Java sources or packaging a WAR. The POM coordinates plugins, dependencies, project metadata, and packaging.

### Q4. Why is the servlet API usually marked as `provided` in Maven?

**Answer.**  
The servlet API is needed at compile time because servlet classes use types such as `HttpServlet`, `HttpServletRequest`, and `HttpServletResponse`. At runtime, Tomcat already provides the servlet API. Therefore, the dependency should not be bundled inside the WAR.

For Tomcat 9 / Java EE style projects:

```xml
<!-- Maven dependency: compile against the Servlet API, but let Tomcat provide it at runtime. -->
<dependency>
  <groupId>javax.servlet</groupId>
  <artifactId>javax.servlet-api</artifactId>
  <version>4.0.0</version>
  <scope>provided</scope>
</dependency>
```

For Tomcat 10+ / Jakarta EE style projects, including the course note's Tomcat 11 context, the package prefix changes from `javax.*` to `jakarta.*`:

```xml
<!-- Jakarta EE dependency for Tomcat 10+/11 projects; still provided by the container. -->
<dependency>
  <groupId>jakarta.servlet</groupId>
  <artifactId>jakarta.servlet-api</artifactId>
  <version>6.1.0</version>
  <scope>provided</scope>
</dependency>
```

Libraries not provided by Tomcat, such as Log4J, Jackson, PostgreSQL driver, or JSTL, must be packaged in the WAR unless the container explicitly provides them.

### Q5. Write basic Git commands for creating a branch, committing, and pushing it.

**Answer.**

```bash
# Create a new branch, stage current changes, commit them, and publish the branch.
git checkout -b feature-name
git add .
git commit -m "Implement feature"
git push origin feature-name
```

To merge the branch back:

```bash
# Update main, merge the feature branch into it, and publish the merged history.
git checkout main
git pull origin main
git merge feature-name
git push origin main
```

### Q6. What is the role of Maven local and remote repositories?

**Answer.**  
Maven downloads dependencies and plugins from remote repositories, then stores them in the local repository, usually `~/.m2/repository`. Future builds reuse the local cache instead of downloading the same artifacts again. Project artifacts can also be installed locally with `mvn install` or deployed to a remote repository with `mvn deploy`.

### Q7. What is `settings.xml` used for?

**Answer.**  
`settings.xml` is Maven's user-level or global configuration file. It can define repository mirrors, credentials, proxies, profiles, and plugin groups. It is not the same as `pom.xml`: the POM describes one project, while `settings.xml` configures the Maven environment.

### Q8. What is the standard Maven project directory structure?

**Answer.**  
The standard structure follows convention over configuration:

```text
Standard Maven layout: source, resources, web files, tests, generated output, project descriptor.
src/main/java       Java source code
src/main/resources  application resources
src/main/webapp     web application files
src/test/java       test source code
target/             generated build output
pom.xml             Maven project configuration
```

Maven plugins expect this structure by default, reducing explicit configuration.

---

## 3. Docker and containerization

### Q1. Why does a Maven WAR not fully solve the deployment environment problem?

**Answer.**  
A WAR packages the web application, but it does not fully package the execution environment. The application can still depend on a specific Java version, Tomcat version, database server, environment variables, network configuration, file paths, and libraries available on the host machine. Docker solves more of the deployment problem by packaging the application with a reproducible runtime environment.

### Q2. Compare Docker containers and virtual machines.

**Answer.**  
A virtual machine includes a full guest operating system running on a hypervisor. This gives strong isolation but costs more disk, memory, and startup time.

A Docker container shares the host OS kernel and isolates processes, filesystem, network, and resources. It is lighter and starts faster. Containers are suitable for packaging services such as Tomcat, PostgreSQL, and web apps in reproducible units.

### Q3. Explain Dockerfile, image, container, and volume.

**Answer.**  
A **Dockerfile** is a text recipe that describes how to build an image. An **image** is an immutable layered template. A **container** is a runtime instance of an image with its own writable layer. A **volume** stores persistent data outside the container writable layer, so data can survive container deletion.

Example: a PostgreSQL database should store its data in a volume; the database container can be recreated, but the data should persist.

### Q4. Write a minimal `docker-compose.yml` with Tomcat and PostgreSQL.

**Answer.**

```yaml
# Compose application: PostgreSQL stores data in a volume; Tomcat waits for DB health.
services:
  db:
    image: postgres:16
    environment:
      POSTGRES_DB: esami
      POSTGRES_USER: ferro
      POSTGRES_PASSWORD: ferro
    volumes:
      - pgdata:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ferro -d esami"]
      interval: 10s
      timeout: 5s
      retries: 5

  web:
    image: tomcat:10
    ports:
      - "8080:8080"
    depends_on:
      db:
        condition: service_healthy
    volumes:
      - ./target/app.war:/usr/local/tomcat/webapps/app.war

volumes:
  pgdata:
```

### Q5. Why is `depends_on` alone not enough when Tomcat depends on PostgreSQL?

**Answer.**  
`depends_on` can ensure startup order, but startup order does not mean the database is ready to accept connections. PostgreSQL may still be initializing, applying scripts, or waiting for authentication setup. A healthcheck verifies readiness, and `condition: service_healthy` lets Tomcat start only after the database is actually usable.

### Q6. What is the relationship between a Dockerfile instruction and an image layer?

**Answer.**  
A Dockerfile contains ordered instructions such as `FROM`, `COPY`, `RUN`, `ENV`, and `CMD`. During build, Docker creates image layers from these instructions. Layers are cached and reused when unchanged, making rebuilds faster. The final image is an immutable layered template used to create containers.

### Q7. Write a minimal Dockerfile that deploys a WAR to Tomcat.

**Answer.**

```dockerfile
# Build a custom Tomcat image that deploys the WAR at container startup.
FROM tomcat:10
COPY target/employee.war /usr/local/tomcat/webapps/employee.war
EXPOSE 8080
```

For development, mounting the WAR with Docker Compose is convenient. For deployment, copying the WAR into a custom image is usually cleaner.

### Q8. Which Docker commands are useful while debugging a Compose application?

**Answer.**

```bash
# Common debugging commands for a Docker Compose / Docker container setup.
docker-compose up
docker-compose down
docker ps
docker ps -a
docker exec -it container-name bash
docker logs container-name
```

`up` starts services, `down` stops and removes containers, `ps` lists containers, `exec` runs commands inside a container, and `logs` inspects service output.

---

## 4. Java servlet

### Q1. What is a servlet?

**Answer.**  
A servlet is a Java server-side web component that handles requests and generates dynamic responses, usually HTTP responses. A typical servlet extends `HttpServlet` and overrides `doGet()` or `doPost()`. The web container, such as Tomcat, creates servlet instances, calls lifecycle methods, and dispatches requests to them.

### Q2. Explain the servlet lifecycle.

**Answer.**  
The container controls the lifecycle:

1. It creates the servlet instance.
2. It calls `init()` once, usually on first request or startup.
3. For each request, it calls `service()`.
4. `HttpServlet.service()` dispatches to `doGet()`, `doPost()`, `doPut()`, etc., according to the HTTP method.
5. Before removing the servlet, the container calls `destroy()`.

Because the same servlet instance can serve many requests, request-specific data must be stored in local variables, not instance fields.

### Q3. Why is `WEB-INF/` not directly accessible from the browser?

**Answer.**  
`WEB-INF/` contains private web application resources: `web.xml`, compiled classes, libraries, and internal configuration. The container blocks direct browser access to this directory. This protects implementation details and forces access through declared servlets, JSP forwarding, or other controlled server-side mechanisms.

### Q4. Write a minimal `HelloWorldServlet`.

**Answer.**

```java
/**
 * Minimal servlet that handles GET requests and writes an HTML response.
 */
public class HelloWorldServlet extends HttpServlet {

    @Override
    public void doGet(HttpServletRequest req, HttpServletResponse res)
            throws ServletException, IOException {

        // Tell the browser that the response body is UTF-8 HTML.
        res.setContentType("text/html; charset=utf-8");

        // Write the complete HTML document to the HTTP response body.
        PrintWriter out = res.getWriter();
        out.printf("<!DOCTYPE html>%n");
        out.printf("<html lang=\"en\">%n");
        out.printf("<head><meta charset=\"utf-8\"><title>Hello</title></head>%n");
        out.printf("<body>%n");
        out.printf("<h1>Hello, world!</h1>%n");
        out.printf("</body>%n");
        out.printf("</html>%n");

        // Flush buffered characters and close the response writer.
        out.flush();
        out.close();
    }
}
```

Important steps: set the MIME type, obtain the writer, write the response body, flush, and close.

### Q5. Write a `web.xml` mapping for a servlet.

**Answer.**

```xml
<!-- Declare the servlet class under a logical name used by mappings below. -->
<servlet>
  <servlet-name>HelloWorld</servlet-name>
  <servlet-class>it.unipd.dei.webapp.HelloWorldServlet</servlet-class>
</servlet>

<!-- Route requests for /hello to the HelloWorld servlet. -->
<servlet-mapping>
  <servlet-name>HelloWorld</servlet-name>
  <url-pattern>/hello</url-pattern>
</servlet-mapping>
```

The servlet declaration gives the container the class name. The servlet mapping connects a URL pattern to that servlet name.

### Q6. Why does the `javax.*` to `jakarta.*` package rename matter?

**Answer.**  
Tomcat 9 uses Java EE / Servlet 4 style packages such as `javax.servlet.*`. Tomcat 10+ uses Jakarta EE packages such as `jakarta.servlet.*`. Mixing Tomcat 10/11 with `javax.servlet.*` code, or Tomcat 9 with `jakarta.servlet.*` code, causes compatibility problems. The course notes mention Tomcat 11, so Jakarta package names are the current target, even if some older code examples use `javax`.

### Q7. How does Log4J `ThreadContext` improve servlet logging?

**Answer.**  
`ThreadContext` stores request-specific key-value data such as IP address, user, action, and resource. Log4J layouts can include these values in every log line. Since servlet containers reuse threads, the context must be removed in a `finally` block to avoid leaking one request's metadata into another request.

```java
// Set request-specific logging context before processing.
try {
    LogContext.setIPAddress(req.getRemoteAddr());
    LogContext.setAction("CREATE_EMPLOYEE");
    // process request
} finally {
    // Always clear ThreadContext values because servlet threads are reused.
    LogContext.removeIPAddress();
    LogContext.removeAction();
}
```

### Q8. What is a servlet `Filter`?

**Answer.**  
A filter intercepts requests and responses before and/or after a servlet or JSP. It implements `init()`, `doFilter()`, and `destroy()`. In `doFilter()`, it can block the request or call `chain.doFilter(req, res)` to pass control onward. Filters are useful for authentication, logging, compression, authorization, and request preprocessing.

---

## 5. Java servlets and database access

### Q1. What is the DAO pattern?

**Answer.**  
DAO means **Data Access Object**. It is a pattern that encapsulates all database access logic inside dedicated classes. Servlets should not write SQL directly. Instead, a servlet creates a DAO, calls `access()`, and reads possible output with `getOutputParam()`.

Benefits:

- Separates application logic from persistence logic.
- Makes SQL code easier to test and reuse.
- Centralizes error handling and connection management.
- Pushes prepared-statement usage into one place.

### Q2. Why are `Employee` and `Message` useful resource classes?

**Answer.**  
`Employee` represents domain data: badge, surname, age, salary. It lets the application pass employee information as a Java object instead of loose parameters.

`Message` represents success or error information. It can carry a readable message, an error code, error details, and a boolean flag. This makes servlet and JSP output easier to handle.

Immutable fields and getters make these classes safer in request processing because values cannot change unexpectedly after construction.

### Q3. Write the `DataAccessObject<T>` interface.

**Answer.**

```java
/**
 * Common DAO contract: run a DB operation and optionally expose its result.
 */
public interface DataAccessObject<T> {

    /** Executes the database access and returns this DAO for chaining. */
    DataAccessObject<T> access() throws SQLException;

    /** Returns the output produced by access(), or null for command-only DAOs. */
    T getOutputParam();
}
```

`access()` performs the database operation and returns the DAO itself, enabling chaining. `getOutputParam()` returns the operation result, such as `List<Employee>`, `Employee`, `Boolean`, or `null`.

### Q4. Write a DAO method that inserts an employee safely.

**Answer.**

```java
/**
 * Command DAO that inserts one Employee row using a prepared statement.
 */
public final class CreateEmployeeDAO extends AbstractDAO {

    // Placeholders keep SQL structure separate from untrusted employee values.
    private static final String STATEMENT =
        "INSERT INTO Ferro.Employee (badge, surname, age, salary) VALUES (?, ?, ?, ?)";

    private final Employee employee;

    public CreateEmployeeDAO(Connection con, Employee employee) {
        super(con);
        this.employee = employee;
    }

    @Override
    protected void doAccess() throws SQLException {
        PreparedStatement pstmt = null;
        try {
            // Prepare once, then bind each Employee field by placeholder index.
            pstmt = con.prepareStatement(STATEMENT);
            pstmt.setInt(1, employee.getBadge());
            pstmt.setString(2, employee.getSurname());
            pstmt.setInt(3, employee.getAge());
            pstmt.setInt(4, employee.getSalary());
            pstmt.execute();
        } finally {
            // Close statement even if execution fails; AbstractDAO closes connection.
            if (pstmt != null) {
                pstmt.close();
            }
        }
    }
}
```

The point to remember is that SQL code and user data are separated by placeholders. The database treats bound values as data, not executable SQL. In the servlet-only notes, this DAO has no output parameter, so it extends `AbstractDAO` without a generic result type. In the REST version, the create DAO instead extends `AbstractDAO<Employee>` and uses `RETURNING *`.

### Q5. How do `context.xml`, `web.xml`, JNDI, and `AbstractDatabaseServlet` work together?

**Answer.**  
`context.xml` defines a Tomcat JDBC connection pool as a JNDI resource. `web.xml` declares a `<resource-ref>` so the web application can access that resource. In `AbstractDatabaseServlet.init()`, the servlet performs a JNDI lookup using `java:/comp/env/jdbc/employee-ferro` and stores the resulting `DataSource`. During each request, concrete servlets call `getConnection()` to borrow a pooled connection.

```java
/**
 * Servlet initialization: obtain the Tomcat-managed DataSource through JNDI.
 */
public void init(ServletConfig config) throws ServletException {
    try {
        InitialContext cxt = new InitialContext();
        // java:/comp/env/ is the mandatory prefix for web-app environment entries.
        ds = (DataSource) cxt.lookup("java:/comp/env/jdbc/employee-ferro");
    } catch (NamingException e) {
        throw new ServletException("Unable to acquire the connection pool.", e);
    }
}
```

### Q6. How does `SearchEmployeeBySalaryDAO` transform rows into objects?

**Answer.**  
It prepares a query with a salary placeholder, binds the salary parameter, executes the query, iterates the `ResultSet`, and creates one `Employee` object for each row. The list is stored as `outputParam`.

```java
// Query employees whose salary is above the submitted threshold.
PreparedStatement pstmt = con.prepareStatement(
    "SELECT badge, surname, age, salary FROM Ferro.Employee WHERE salary > ?");
pstmt.setInt(1, salary);
ResultSet rs = pstmt.executeQuery();

// Convert each ResultSet row into one immutable Employee object.
List<Employee> employees = new ArrayList<>();
while (rs.next()) {
    employees.add(new Employee(
        rs.getInt("badge"),
        rs.getString("surname"),
        rs.getInt("age"),
        rs.getInt("salary")
    ));
}
// Store DAO output so callers can retrieve it with getOutputParam().
outputParam = employees;
```

### Q7. Why does `AbstractDAO` use one-shot execution, rollback, and connection closing?

**Answer.**  
DAO objects are intended for one database operation. A one-shot guard prevents accidental reuse. If `doAccess()` fails, rollback keeps the database consistent. Closing the connection in `finally` returns it to the pool even on error, preventing connection leaks.

### Q8. What do common Tomcat pool parameters mean?

**Answer.**  
`testOnBorrow` validates a connection before lending it. `validationQuery` is the query used for validation, such as `SELECT 1`. `maxActive` limits active connections. `maxWait` limits how long a request waits for a connection. `removeAbandoned` reclaims connections not returned after a timeout.

---

## 6. JSP, JSTL, EL, and MVC

### Q1. What is JSP?

**Answer.**  
JSP means **JavaServer Pages**. It is a server-side view technology for writing dynamic pages using mostly HTML plus JSP directives, Expression Language, JSTL tags, and standard actions. A JSP is translated into a servlet, compiled, and then executed by the container. The first request is slower because translation and compilation may happen then; later requests reuse the generated servlet.

### Q2. Why are scriptlets discouraged in JSP?

**Answer.**  
Scriptlets mix Java code directly into the view. This makes pages harder to read, test, maintain, and split between designers and Java developers. Cleaner JSP style uses:

- EL for reading values: `${employee.badge}`
- JSTL for view logic: `<c:if>`, `<c:choose>`, `<c:forEach>`
- Servlet controllers for application logic
- DAO/model classes for data access

This keeps the JSP focused on presentation.

### Q3. How does MVC map to Java web technologies?

**Answer.**  
In the notes' employee application:

- Model: resource classes such as `Employee` and `Message`, plus DAO classes for persistence.
- View: JSP pages that render HTML.
- Controller: servlets that parse requests, validate input, call DAOs, create model objects, and forward to JSPs.

The controller does not print full HTML. It sets request attributes and forwards to the view.

### Q4. Write a servlet controller that forwards to a JSP.

**Answer.**

```java
/**
 * Controller servlet for create-employee form submissions in the MVC version.
 */
public final class CreateEmployeeServlet extends AbstractDatabaseServlet {

    @Override
    public void doPost(HttpServletRequest req, HttpServletResponse res)
            throws ServletException, IOException {

        Employee employee = null;
        Message message = null;

        try {
            // Parse request parameters sent by the HTML/JSP form.
            int badge = Integer.parseInt(req.getParameter("badge"));
            String surname = req.getParameter("surname");
            int age = Integer.parseInt(req.getParameter("age"));
            int salary = Integer.parseInt(req.getParameter("salary"));

            // Build model object, persist it through the DAO, and prepare feedback.
            employee = new Employee(badge, surname, age, salary);
            new CreateEmployeeDAO(getConnection(), employee).access();
            message = new Message("Employee successfully created.");
        } catch (NumberFormatException e) {
            // User submitted a non-integer value for numeric fields.
            message = new Message("Invalid numeric parameter.", "E100", e.getMessage());
        } catch (SQLException e) {
            // Database layer failed; a real implementation can inspect SQLState.
            message = new Message("Database error.", "E200", e.getMessage());
        }

        // Pass model objects to the JSP view and let the view render HTML.
        req.setAttribute("employee", employee);
        req.setAttribute("message", message);
        req.getRequestDispatcher("/jsp/create-employee-result.jsp").forward(req, res);
    }
}
```

### Q5. Write a JSP fragment that displays a message and a list of employees.

**Answer.**

```jsp
<%-- JSP view: render a Message and, when present, a table of Employee objects. --%>
<%@ page contentType="text/html;charset=utf-8" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>

<%-- Choose error or success rendering based on the Message bean. --%>
<c:choose>
  <c:when test="${message.error}">
    <p>Error: <c:out value="${message.message}"/></p>
    <p>Code: <c:out value="${message.errorCode}"/></p>
  </c:when>
  <c:otherwise>
    <p><c:out value="${message.message}"/></p>
  </c:otherwise>
</c:choose>

<%-- Iterate request-scope employeeList and escape every displayed property. --%>
<c:if test="${not empty employeeList}">
  <table>
    <thead>
      <tr><th>Badge</th><th>Surname</th><th>Age</th><th>Salary</th></tr>
    </thead>
    <tbody>
      <c:forEach var="employee" items="${employeeList}">
        <tr>
          <td><c:out value="${employee.badge}"/></td>
          <td><c:out value="${employee.surname}"/></td>
          <td><c:out value="${employee.age}"/></td>
          <td><c:out value="${employee.salary}"/></td>
        </tr>
      </c:forEach>
    </tbody>
  </table>
</c:if>
```

`<c:out>` escapes output, so user-controlled values are not inserted as raw HTML.

### Q6. Why should JSP pages use `<c:url>` for links, images, and form actions?

**Answer.**  
`<c:url>` builds URLs relative to the web application context path and can support URL rewriting. This avoids broken links when the application is deployed under a context path such as `/employee-webapp` instead of the server root.

```jsp
<%-- Build a context-aware form action URL for the create-employee controller. --%>
<form method="POST" action="<c:url value="/create-employee"/>">
```

### Q7. What are common EL implicit variables?

**Answer.**  
`param` accesses request parameters. `requestScope` accesses request attributes. `sessionScope` accesses session attributes. `cookie` accesses cookies. These maps let JSP pages read web data without Java scriptlets.

### Q8. What is the purpose of shared JSP includes?

**Answer.**  
Shared includes keep repeated page fragments in one place, such as head metadata, CSS links, scripts, and footer markup. In the notes, `<c:import>` includes fragments at request time, so the same markup is not copied across JSP pages.

---

## 7. REST web services and AJAX example

### Q1. What is REST?

**Answer.**  
REST is an architectural style where application data is modeled as **resources** identified by **URIs**. Clients manipulate resources through a uniform interface, usually HTTP methods:

- `GET`: read a resource.
- `POST`: create a subordinate resource.
- `PUT`: create or replace a resource at a known URI.
- `DELETE`: remove a resource.

REST services should be stateless: each request carries the information needed to process it.

### Q2. What is the role of `Accept` and `Content-Type` in a REST API?

**Answer.**  
`Accept` tells the server which response media types the client can handle, for example `application/json`. `Content-Type` tells the server the media type of the request body, for example JSON in a `POST` or `PUT`.

If `Accept` is missing or incompatible, the server can return `400 Bad Request` or `406 Not Acceptable`. If `Content-Type` is missing or unsupported for a request with body, the server can return `400 Bad Request` or `415 Unsupported Media Type`.

### Q3. Write the `Resource` interface and `AbstractResource` idea.

**Answer.**

```java
/**
 * REST resources implement this contract to serialize themselves as JSON.
 */
public interface Resource {
    /** Writes this resource as JSON to the provided output stream. */
    void toJSON(OutputStream out) throws IOException;
}
```

```java
/**
 * Base class for JSON resources using Jackson streaming APIs.
 */
public abstract class AbstractResource implements Resource {

    protected static final JsonFactory JSON_FACTORY = new JsonFactory();

    static {
        // The servlet container owns request/response streams; Jackson must not close them.
        JSON_FACTORY.disable(JsonGenerator.Feature.AUTO_CLOSE_TARGET);
        JSON_FACTORY.disable(JsonParser.Feature.AUTO_CLOSE_SOURCE);
    }

    @Override
    public final void toJSON(OutputStream out) throws IOException {
        if (out == null) {
            throw new IOException("Output stream cannot be null.");
        }
        try {
            // Delegate resource-specific fields to the template method.
            writeJSON(out);
        } catch (Exception e) {
            throw new IOException("Unable to serialize resource.", e);
        }
    }

    /** Subclasses write their concrete JSON structure here. */
    protected abstract void writeJSON(OutputStream out) throws Exception;
}
```

Auto-close is disabled because Jackson must not close servlet request or response streams owned by the container.

### Q4. Write a REST resource skeleton with `serve()`.

**Answer.**

```java
/**
 * Base REST handler: validate request metadata, run endpoint logic, return JSON errors.
 */
public abstract class AbstractRR implements RestResource {

    protected final HttpServletRequest req;
    protected final HttpServletResponse res;
    protected final Connection con;
    private final String action;

    protected AbstractRR(String action, HttpServletRequest req, HttpServletResponse res, Connection con) {
        this.action = action;
        // Add action name to Log4J ThreadContext for request-scoped logging.
        LogContext.setAction(action);
        this.req = req;
        this.res = res;
        this.con = con;
    }

    @Override
    public final void serve() throws IOException {
        try {
            // Reject unsupported HTTP methods or media types before business logic.
            if (!checkMethodMediaType(req, res)) {
                return;
            }
            doServe();
        } catch (Throwable t) {
            // Convert unexpected failures into a structured REST error response.
            Message m = new Message(
                "Unable to serve REST request: " + action + ".", "E5A1", t.getMessage());
            res.setStatus(HttpServletResponse.SC_INTERNAL_SERVER_ERROR);
            m.toJSON(res.getOutputStream());
        } finally {
            // Clear per-thread log context because servlet threads are reused.
            LogContext.removeAction();
            LogContext.removeResource();
        }
    }

    /** Endpoint-specific behavior implemented by concrete REST resources. */
    protected abstract void doServe() throws IOException;
}
```

`AbstractRR` centralizes validation, error handling, and common request/response/database fields. Concrete classes implement endpoint-specific behavior.

### Q5. Explain the AJAX flow in the REST employee example.

**Answer.**  
The browser page contains an input field, a button, a result container, and a JavaScript file. JavaScript registers a click listener on the button. When clicked, it reads the salary value, builds a REST URL, creates an `XMLHttpRequest`, and sends an asynchronous request. When the response arrives, the callback checks `readyState` and `status`, parses JSON with `JSON.parse()`, creates DOM elements such as table rows and cells, and appends them to the result container without reloading the whole page.

### Q6. What are the main REST error codes used in the notes?

**Answer.**  
Client errors include `E4A1` for missing `Accept`, `E4A2` for unacceptable response type, `E4A3` for missing `Content-Type`, `E4A4` for unsupported input type, `E4A5` for unsupported method, `E4A6` for unknown resource, `E4A7` for wrong URI format, and `E4A8` for malformed resource body. Server-side errors include `E5A1` unexpected server error, `E5A2` resource already exists, `E5A3` resource not found, and `E5A4` conflict caused by dependent resources.

### Q7. How does `RestDispatcherServlet` route employee requests?

**Answer.**  
It maps `/rest/*` to one dispatcher servlet and overrides `service()` so it can handle all HTTP methods. It checks whether the URI belongs to `/rest/employee`, then dispatches by method and remaining path. Examples: `GET /rest/employee` lists employees, `POST /rest/employee` creates one, `GET /rest/employee/{badge}` reads one, `PUT /rest/employee/{badge}` updates one, `DELETE /rest/employee/{badge}` deletes one, and `GET /rest/employee/salary/{salary}` searches by salary.

### Q8. Why does `Employee.fromJSON()` throw `EOFException`?

**Answer.**  
`Employee.fromJSON()` scans the request body until it finds the `"employee"` field. If the parser reaches end of input before finding that object, the JSON body is missing the expected resource. The REST layer catches this as a bad request, represented in the notes by `E4A8`.

---

## 8. HTTP and surroundings

### Q1. Distinguish URI, URL, URN, and IRI.

**Answer.**  
A **URI** is a generic identifier for a resource. A **URL** is a URI that also gives a way to locate the resource, usually by network access, such as `https://example.com/page.html`. A **URN** is a URI that names a resource persistently using the `urn:` scheme, without necessarily locating it. An **IRI** extends URI syntax with Unicode characters.

### Q2. What is percent-encoding and why is it needed?

**Answer.**  
Percent-encoding represents reserved or non-ASCII characters using `%` followed by hexadecimal bytes. It is needed because some characters have special meanings in URI syntax, such as `?`, `&`, `/`, `#`, or spaces. Encoding lets data be safely transmitted inside URI components without being misinterpreted as URI syntax.

### Q3. Compare `multipart/form-data` and `application/x-www-form-urlencoded`.

**Answer.**  
`application/x-www-form-urlencoded` represents form data as name-value pairs in a compact text format, such as `name=Alice&age=20`. It is suitable for normal text fields.

`multipart/form-data` splits the request body into separate parts, each with its own headers and content. It is required for file uploads because binary file bytes and textual fields can be sent together.

### Q4. Write a multipart form for employee creation with photo upload.

**Answer.**

```jsp
<%-- Multipart JSP form: sends text fields plus a file part to CreateEmployeeServlet. --%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>

<%-- enctype is required for file bytes to appear as request Parts. --%>
<form method="POST" enctype="multipart/form-data"
      action="<c:url value="/create-employee"/>">
  <input id="badgeID" name="badge" type="text">
  <input id="surnameID" name="surname" type="text">
  <input id="ageID" name="age" type="text">
  <input id="salaryID" name="salary" type="text">
  <input id="emailID" name="email" type="text">
  <%-- accept helps the UI, but the servlet must still validate MIME type. --%>
  <input id="photoID" name="photo" type="file"
         accept="image/png, image/jpeg, .jpg, .jpeg, .png">
  <button type="submit">Submit</button>
</form>
```

The `accept` attribute makes client-side file selection nicer, but it is not a security control. The servlet must validate the uploaded MIME type server-side.

### Q5. How does Basic Authentication work and why does it need HTTPS?

**Answer.**  
With HTTP Basic Authentication, the client sends an `Authorization` header containing `Basic ` plus Base64 encoding of `username:password`. If credentials are missing or invalid, the server responds with `401 Unauthorized` and a `WWW-Authenticate` challenge with a realm.

Base64 is encoding, not encryption. Anyone who intercepts plain HTTP traffic can decode the credentials. Therefore Basic Authentication must be used only over HTTPS/TLS.

### Q6. Compare safe, idempotent, and cacheable HTTP methods.

**Answer.**  
Safe methods are intended not to change server state, such as `GET`, `HEAD`, and `OPTIONS`. Idempotent methods have the same server-side effect if repeated, such as `GET`, `PUT`, `DELETE`, `HEAD`, and `OPTIONS`. `POST` is not idempotent because repeating it can create multiple subordinate resources. Cacheable responses may be stored and reused according to HTTP caching rules, especially for safe requests.

### Q7. What do common HTTP status code classes mean?

**Answer.**  
`2xx` means success, such as `200 OK`, `201 Created`, and `204 No Content`. `3xx` means redirection. `4xx` means client error, such as bad syntax, unauthorized access, missing resource, wrong method, conflict, or unsupported media type. `5xx` means server error while processing a valid request.

### Q8. How does `MailManager` send an email with an attachment?

**Answer.**  
It creates a `MimeMessage`, creates a `MimeMultipart`, adds one `MimeBodyPart` for the message body, adds another `MimeBodyPart` with a `DataHandler` for the attachment bytes and MIME type, sets the multipart content on the message, and sends it with `Transport.send()`. This represents the email as `multipart/mixed`.

---

## 9. Markup languages, XML, and JSON

### Q1. What does markup mean?

**Answer.**  
Markup is information added to text to describe structure, meaning, presentation, references, or processing instructions. It is not the textual content itself; it tells software how to interpret or display the content. HTML marks up web documents, XML marks up structured data, and CSS separates visual presentation from structural markup.

### Q2. What is the difference between well-formed and valid XML?

**Answer.**  
A **well-formed** XML document follows basic XML syntax rules: one root element, properly nested tags, closed elements, quoted attribute values, and correct entity usage.

A **valid** XML document is well-formed and also conforms to a declared structure such as a DTD or XML Schema. Validity checks whether elements, attributes, order, cardinality, and data types match the schema rules.

### Q3. Compare DOM, SAX, and StAX.

**Answer.**  
DOM loads the whole document into an in-memory tree. It allows navigation and modification in both directions, but uses more memory.

SAX is event-based push parsing. The parser reads the document and calls callbacks. It uses little memory but the application has less control.

StAX is pull parsing. The application asks the parser for the next event. It also uses low memory, but gives the application more control than SAX.

### Q4. Why were XML Schema and namespaces introduced?

**Answer.**  
DTD has limitations: it uses non-XML syntax, has weak data typing, and has limited namespace support. XML Schema uses XML syntax, supports richer data types, and works better with namespaces. Namespaces prevent element-name collisions when multiple XML vocabularies are combined in the same document.

### Q5. Write a JSON object equivalent to an employee XML element.

**Answer.**

XML:

```xml
<!-- XML representation of one employee resource. -->
<employee>
  <badge>7309</badge>
  <surname>Rossi</surname>
  <age>34</age>
  <salary>45</salary>
</employee>
```

JSON:

The `_comment` field below is only a study note inserted to explain the block; omit it in a real API response.

```json
{
  "_comment": "JSON representation of the same employee resource.",
  "employee": {
    "badge": 7309,
    "surname": "Rossi",
    "age": 34,
    "salary": 45
  }
}
```

JSON is usually more compact because it does not repeat closing tags and maps directly to JavaScript objects and arrays.

### Q6. What do DTD operators `,`, `|`, `?`, `*`, and `+` mean?

**Answer.**  
`,` means sequence, `|` means choice, `?` means optional zero or one, `*` means zero or more, and `+` means one or more. They define allowed XML element structure and cardinality.

### Q7. Why are XML namespaces useful?

**Answer.**  
Namespaces prevent name collisions when elements from different vocabularies appear in the same XML document. A prefix is bound to a URI, so two elements with the same local name can still have different meanings.

### Q8. What can JSON Schema validate?

**Answer.**  
JSON Schema can validate object structure, required properties, primitive types, arrays, numeric constraints, string formats or patterns, and nested schemas. It is useful for checking API input and output contracts.

---

## 10. HTML5

### Q1. Why does an HTML document start with `<!DOCTYPE html>`?

**Answer.**  
The `DOCTYPE` tells the browser which rendering mode to use. In HTML5, `<!DOCTYPE html>` triggers standards mode and avoids older quirks-mode behavior. The HTML5 declaration is simpler than older HTML4/XHTML declarations because it does not require a long DTD reference.

### Q2. What is the difference between `id` and `name`?

**Answer.**  
`id` uniquely identifies one element in the document. It is used by CSS, JavaScript, labels, and fragment links. It should not be repeated in the same page.

`name` identifies form controls when a form is submitted. The server receives name-value pairs. Multiple controls can share the same `name`, especially radio buttons, where the shared name defines a group and each button has a different `value`.

### Q3. Write a minimal HTML5 page with semantic layout.

**Answer.**

```html
<!-- Complete HTML5 document with metadata and semantic page regions. -->
<!DOCTYPE html>
<html lang="en">
<head>
  <!-- UTF-8 supports Web text; viewport enables responsive mobile layout. -->
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Employee App</title>
</head>
<body>
  <!-- Semantic elements describe page structure better than generic divs. -->
  <header>
    <h1>Employee App</h1>
  </header>
  <nav>
    <a href="/employees">Employees</a>
  </nav>
  <main>
    <section>
      <h2>Create Employee</h2>
      <p>Employee form goes here.</p>
    </section>
  </main>
  <footer>
    <p>Web Applications 2025-26</p>
  </footer>
</body>
</html>
```

### Q4. Write a form with common HTML5 input types.

**Answer.**

```html
<!-- POST form: name attributes become request parameters on the server. -->
<form method="POST" action="/create-employee">
  <label for="badge">Badge</label>
  <input id="badge" name="badge" type="number" required>

  <label for="email">Email</label>
  <input id="email" name="email" type="email" required>

  <label for="birth">Birth date</label>
  <input id="birth" name="birth" type="date">

  <!-- Radio buttons share the same name so the browser submits one selected role. -->
  <fieldset>
    <legend>Role</legend>
    <input id="dev" name="role" type="radio" value="developer">
    <label for="dev">Developer</label>
    <input id="mgr" name="role" type="radio" value="manager">
    <label for="mgr">Manager</label>
  </fieldset>

  <!-- File input lets the browser send an uploaded photo. -->
  <label for="photo">Photo</label>
  <input id="photo" name="photo" type="file" accept="image/png, image/jpeg">

  <button type="submit">Submit</button>
</form>
```

### Q5. When should semantic elements be preferred over `div` and `span`?

**Answer.**  
Use semantic elements when the content has a real page role: `header`, `nav`, `main`, `section`, `article`, `aside`, and `footer`. They make the document easier to read, parse, and expose to assistive technologies. `div` and `span` are generic containers; use them when no more specific semantic element fits.

### Q6. How should an accessible table be structured?

**Answer.**  
Use `table`, `thead`, `tbody`, `tr`, `th`, and `td`. Header cells should use `th`, and `scope` can clarify whether the header applies to a row or column. `colspan` and `rowspan` merge cells when needed, but should not be abused because complex tables are harder to read and make accessible.

### Q7. Why do `<video>` and `<audio>` often contain multiple `<source>` elements?

**Answer.**  
Different browsers may support different media formats. Multiple `<source>` elements let the browser choose the first compatible format. Fallback text can be shown if the browser does not support the media element.

### Q8. What is `<canvas>` used for?

**Answer.**  
`<canvas>` creates a drawable region in the page. JavaScript uses the Canvas API to draw shapes, text, images, charts, or games. The element provides the drawing surface; JavaScript provides the behavior.

---

## 11. Web security

### Q1. What is SQL Injection?

**Answer.**  
SQL Injection is a code injection attack against the interface between a web application and its database. The root cause is mixing untrusted user input with trusted SQL code in a single string. The database parser cannot distinguish intended SQL from injected SQL, so attacker input may change query structure.

Example attack:

```sql
-- Attack payload: closes the string, adds an always-true condition, comments out the rest.
' OR '1'='1' --
```

This can turn a login condition into an always-true condition and comment out the password check.

### Q2. How do prepared statements prevent SQL Injection?

**Answer.**  
Prepared statements separate SQL code from user data. The SQL structure is compiled with placeholders, and values are bound later as parameters. Injected SQL characters inside parameters are treated as data, not as executable SQL.

```java
// SQL text contains placeholders; user values are bound separately.
String sql = "SELECT * FROM Employee WHERE badge = ? AND surname = ?";
PreparedStatement pstmt = con.prepareStatement(sql);
// Parameters are treated as data, not as executable SQL code.
pstmt.setInt(1, badge);
pstmt.setString(2, surname);
ResultSet rs = pstmt.executeQuery();
```

Manual filtering can help, but it is easier to get wrong. Prepared statements are the primary defense.

### Q3. What is XSS and what are its main types?

**Answer.**  
XSS, or Cross-Site Scripting, lets an attacker inject JavaScript into pages viewed by other users. The script executes in the victim's browser with the privileges of the trusted site.

Main types:

- Stored XSS: malicious script is stored in the database and later shown to users.
- Reflected XSS: malicious input is reflected immediately in a response, often through a crafted URL.
- DOM-based XSS: vulnerable client-side JavaScript inserts attacker-controlled data into the DOM.

Main defenses are output encoding, input validation, safe DOM APIs, sanitization such as DOMPurify, and framework escaping.

### Q4. What is CSRF?

**Answer.**  
CSRF, or Cross-Site Request Forgery, tricks an authenticated user's browser into sending an unwanted request to a site where the user is logged in. The browser automatically attaches cookies for the target site, so the server may treat the forged request as legitimate.

`SameSite=Strict` works here because it prevents cookies from being sent with cross-site requests. Without the victim's session cookie, the forged request is not authenticated.

### Q5. Identify and fix this vulnerable SQL pattern.

**Question code.**

```php
// Vulnerable example: user input is concatenated directly into SQL.
$sql = "SELECT Name FROM employee WHERE eid = '$eid' and password = '$pwd'";
$result = $conn->query($sql);
```

**Answer.**  
The code is vulnerable because `$eid` and `$pwd` are concatenated directly into SQL. An attacker can inject SQL syntax.

Safe version:

```php
// Safe version: query structure uses placeholders and values are bound as strings.
$sql = "SELECT Name FROM employee WHERE eid = ? and password = ?";
$stmt = $conn->prepare($sql);
$stmt->bind_param("ss", $eid, $pwd);
$stmt->execute();
$stmt->bind_result($name);
```

### Q6. What are confidentiality, integrity, and availability?

**Answer.**  
Confidentiality means information is not disclosed to unauthorized users. Integrity means data is not modified improperly. Availability means systems and data remain accessible when needed. Web security controls usually protect one or more of these goals.

### Q7. What is OWASP Top Ten?

**Answer.**  
OWASP Top Ten is a widely used list of common web application security risk categories, such as injection, broken access control, authentication issues, and XSS. It gives developers a shortlist of risks to check first.

### Q8. Why is defense-in-depth necessary?

**Answer.**  
No single defense is perfect. A well-built web application combines server-side validation, prepared statements, output encoding, sanitization, safe DOM APIs, secure cookies, authentication checks, upload limits, logging, and least-privilege database access.

---

## 12. CSS

### Q1. What is the cascade in CSS?

**Answer.**  
The cascade is the mechanism that decides which CSS declaration applies when multiple rules target the same element and property. The main factors are origin, importance, specificity, and source order.

In simplified author CSS:

1. More specific selectors win.
2. If specificity is equal, later rules win.
3. `!important` overrides normal declarations.
4. User `!important` rules can override author rules for accessibility.

### Q2. Explain the CSS box model.

**Answer.**  
Every element is represented as a rectangular box with:

- content area
- padding
- border
- margin

In the standard box model, `width` applies only to the content area. Total horizontal occupied space is:

```text
Formula: total horizontal space occupied by a standard CSS box.
left margin + left border + left padding + width
+ right padding + right border + right margin
```

For example, `width: 500px`, `padding: 20px`, `border: 2px`, and `margin: 20px` gives total occupied width `584px`.

### Q3. Compare `display: none` and `visibility: hidden`.

**Answer.**  
`display: none` removes the element from the layout. It is not visible and does not reserve space.

`visibility: hidden` makes the element invisible but keeps its layout space. Other elements behave as if the hidden element were still there.

### Q4. Write a mobile-first responsive CSS example.

**Answer.**

```css
/* Mobile-first base layout: full width content and hidden navigation. */
.container {
  width: 100%;
}

nav {
  display: none;
}

/* Tablet and wider: constrain content and show navigation. */
@media only screen and (min-width: 40em) {
  .container {
    width: 80%;
    margin: 0 auto;
  }

  nav {
    display: block;
  }
}

/* Desktop and wider: use a fixed readable content width. */
@media only screen and (min-width: 64em) {
  .container {
    width: 960px;
  }
}
```

Mobile-first CSS starts with the simplest layout and adds complexity for larger screens.

### Q5. When should Flexbox and Grid be used?

**Answer.**  
Flexbox is one-dimensional: it arranges items along a row or a column. It is good for navigation bars, toolbars, card rows, and aligning content inside components.

Grid is two-dimensional: it controls rows and columns together. It is good for page-level layout and complex alignment. They can be combined: Grid for the outer page structure, Flexbox inside grid cells.

### Q6. How do CSS selectors differ?

**Answer.**  
Type selectors target elements by tag name, class selectors target reusable class names, ID selectors target one unique element, descendant selectors target nested elements at any depth, child selectors target direct children, adjacent sibling selectors target the immediately following sibling, and general sibling selectors target later siblings with the same parent.

### Q7. Which CSS properties are inherited by default?

**Answer.**  
Text-related properties such as `font-family`, `font-size`, `color`, `line-height`, and `text-align` commonly inherit. Box-related properties such as `margin`, `padding`, `border`, `width`, `height`, and `background-color` generally do not inherit. The `inherit` keyword can force inheritance.

### Q8. Why can floats collapse a parent element?

**Answer.**  
Floated children are taken out of normal flow. If all children are floated, the parent may have no normal-flow content and collapse to zero height. One fix from the notes is:

```css
/* Keep a parent from collapsing when all children are floated. */
.parent {
  overflow: auto;
  width: 100%;
}
```

---

## 13. JavaScript

### Q1. What is the role of JavaScript in the web stack?

**Answer.**  
HTML defines structure, CSS defines presentation, and JavaScript defines behavior. JavaScript can inspect and modify the DOM, react to events, validate forms, call APIs with AJAX/fetch, update parts of a page without reload, and interact with browser objects such as `window`, `document`, `location`, `history`, timers, and console.

### Q2. Explain the DOM.

**Answer.**  
The DOM, or Document Object Model, is the in-memory tree representation of an HTML or XML document. The root is a `Document` object. HTML tags become `Element` nodes, text becomes `Text` nodes, and all of them inherit from `Node`. JavaScript uses DOM APIs to select, create, insert, remove, replace, and modify nodes. Changes to the DOM are reflected in the rendered page.

### Q3. Why is `addEventListener()` preferred?

**Answer.**  
`addEventListener()` is preferred because it separates JavaScript from HTML, allows multiple handlers for the same event on the same target, works on many DOM objects, and supports event phases. HTML event attributes mix behavior with markup, and assigning `onclick` directly allows only one handler per event property.

```javascript
// Select the button and register a click listener without using inline HTML handlers.
var button = document.getElementById("save");

button.addEventListener("click", function (event) {
  console.log("Clicked");
});
```

### Q4. Write JavaScript that creates and inserts a paragraph.

**Answer.**

```javascript
// Create a paragraph node and insert it into the existing results container.
var container = document.getElementById("results");
var paragraph = document.createElement("p");
var text = document.createTextNode("Employee created successfully.");

// Text goes inside the paragraph; paragraph goes inside the page.
paragraph.appendChild(text);
container.appendChild(paragraph);
```

The new nodes are floating until they are appended to an existing node in the document.

### Q5. Write a submit handler that blocks invalid input.

**Answer.**

```javascript
// Read form fields used for validation and feedback.
var form = document.getElementById("employee-form");
var salary = document.getElementById("salary");
var error = document.getElementById("salary-error");

// Final validation gate: stop submission if salary is invalid.
form.addEventListener("submit", function (event) {
  var value = Number(salary.value);

  if (!Number.isInteger(value) || value < 0) {
    error.textContent = "Salary must be a non-negative integer.";
    event.preventDefault();
  } else {
    error.textContent = "";
  }
});
```

`event.preventDefault()` cancels the browser's default form submission.

### Q6. Why are JavaScript objects described as associative arrays?

**Answer.**  
JavaScript objects store name-value pairs. Properties can be accessed with dot notation or bracket notation. Bracket notation is useful when property names are computed dynamically.

```javascript
// Bracket notation reads a property whose name is stored in a variable.
var employee = { badge: 7309, surname: "Rossi" };
var key = "surname";
console.log(employee[key]);
```

### Q7. What is the JavaScript execution timeline in a page?

**Answer.**  
The browser parses HTML and builds the document. When it encounters synchronous scripts, parsing pauses while the script downloads and executes. After the document and resources finish loading, the `load` event fires. Then the page enters the event-driven phase, where handlers run in response to clicks, keyboard events, timers, network responses, and other events.

### Q8. What are common browser objects?

**Answer.**  
`window` is the global browser window object. `document` is the DOM root. `location` represents the current URL. `history` represents browser navigation history. `navigator` contains browser information. `screen` describes display properties. `console` provides debugging output.

---

## 14. Form validation and AJAX

### Q1. Why are both client-side and server-side validation needed?

**Answer.**  
Client-side validation gives immediate feedback. It can use HTML5 attributes, CSS pseudo-classes, the Constraint Validation API, or custom JavaScript.

Server-side validation is mandatory for security because clients can disable JavaScript, bypass forms, modify requests, or send malicious data directly. The server is the final trusted validation point before database writes or sensitive operations.

### Q2. What does the Constraint Validation API provide?

**Answer.**  
It exposes validation state and lets JavaScript customize validation messages. `element.validity` contains boolean flags such as `valueMissing`, `typeMismatch`, and `patternMismatch`. `setCustomValidity(message)` sets a custom error; passing an empty string clears it.

```javascript
// Use the Constraint Validation API to customize the email error message.
var email = document.getElementById("email");

email.addEventListener("input", function () {
  if (email.validity.typeMismatch) {
    email.setCustomValidity("Please enter a valid email address.");
  } else {
    email.setCustomValidity("");
  }
});
```

### Q3. Explain the `XMLHttpRequest` request/response cycle.

**Answer.**  
An XHR request has method, URL, optional headers, and optional body. The response has status code, headers, and body. The JavaScript code creates an `XMLHttpRequest`, configures it with `open()`, optionally sets headers with `setRequestHeader()`, registers a callback, and sends it with `send()`. The callback checks that the request is complete and successful before processing data.

### Q4. Write an XHR GET that parses JSON.

**Answer.**

```javascript
// Create one asynchronous HTTP request object.
var xhr = new XMLHttpRequest();

xhr.onreadystatechange = function () {
  // Ignore intermediate states; process only when the response is complete.
  if (xhr.readyState !== XMLHttpRequest.DONE) {
    return;
  }

  if (xhr.status === 200) {
    // Convert JSON response text into a JavaScript object.
    var data = JSON.parse(xhr.responseText);
    console.log(data);
  } else {
    console.error("Request failed: " + xhr.status);
  }
};

// Configure and send an asynchronous GET request asking for JSON.
xhr.open("GET", "rest/employee/salary/45", true);
xhr.setRequestHeader("Accept", "application/json");
xhr.send();
```

### Q5. Rewrite the same idea with Fetch.

**Answer.**

```javascript
// Fetch version of the same REST call, written with async/await.
async function loadEmployees() {
  var response = await fetch("rest/employee/salary/45", {
    headers: {
      "Accept": "application/json"
    }
  });

  // Fetch resolves for HTTP errors, so status must be checked explicitly.
  if (!response.ok) {
    throw new Error("HTTP error: " + response.status);
  }

  // Parse response body as JSON after successful status check.
  var data = await response.json();
  console.log(data);
}
```

`fetch()` returns a Promise. `await` makes asynchronous code easier to read, but status must still be checked explicitly.

### Q6. How do URL-encoded and JSON POST bodies differ?

**Answer.**  
URL-encoded bodies serialize pairs as `name=value&name2=value2` and use `Content-Type: application/x-www-form-urlencoded`. JSON bodies serialize structured objects with `JSON.stringify()` and use `Content-Type: application/json`. The server must parse the body according to the declared content type.

### Q7. What is CORS?

**Answer.**  
CORS, or Cross-Origin Resource Sharing, is a controlled relaxation of the same-origin policy. Browsers normally restrict AJAX requests to the same origin. A server can allow selected cross-origin access by sending headers such as `Access-Control-Allow-Origin`.

### Q8. Compare HTML, XML, and JSON as AJAX response formats.

**Answer.**  
HTML is easy to insert into a page but is not portable as data. XML is structured and platform-independent but verbose and requires DOM-style processing. JSON is concise and maps naturally to JavaScript objects, but untrusted JSON-derived content must still be handled safely before rendering.

---

## 15. jQuery and HTML5 canvas

### Q1. What is jQuery and what does the `$()` function return?

**Answer.**  
jQuery is a JavaScript library that gives a compact, cross-browser API for selecting elements, manipulating the DOM, registering events, and making AJAX requests. The global function `jQuery()` is usually used through the alias `$()`.

When `$()` receives a CSS selector, it returns a jQuery object containing all matched elements. The object is array-like: it has `length`, indexed elements, and many jQuery methods. If it contains one DOM node, it is still not the same thing as the raw DOM element.

```javascript
// Select all div elements and keep them inside a jQuery object.
var divs = $("div");

// Read the number of matched elements.
console.log(divs.length);

// Extract the first raw DOM element from the jQuery object.
var firstDiv = divs[0];
```

### Q2. How do jQuery getters, setters, and method chaining work?

**Answer.**  
Many jQuery methods work both as setters and getters. When a value is passed, the method sets that value on every matched element and returns the same jQuery object, so calls can be chained. When no value is passed, the method usually reads a value from the first matched element and returns a plain value, so the chain ends there.

```javascript
// Setter calls return the jQuery object, so they can be chained.
$("p.details")
  .css("background-color", "yellow")
  .attr("title", "Important details")
  .show("fast");

// Getter call returns a string, not a jQuery object, so it normally ends the chain.
var title = $("p.details").attr("title");
```

Common dual-role methods are `attr()`, `css()`, `val()`, `text()`, and `html()`.

### Q3. Compare `text()`, `html()`, `val()`, and class methods.

**Answer.**  
`text()` reads or writes plain text. It is safer for user-controlled content because markup is escaped as text. `html()` reads or writes HTML markup and should not be used with untrusted input unless the HTML has been sanitized. `val()` reads or writes form-control values, including text inputs, radio buttons, checkboxes, and select elements. Class methods such as `addClass()`, `removeClass()`, and `toggleClass()` change styling through CSS classes instead of editing many inline CSS properties.

```javascript
// Trim every text input with class tags by computing a new value from the old one.
$("input[type=text].tags").val(function (index, value) {
  return value.trim();
});

// Add a CSS class instead of setting many presentation properties by hand.
$("#message").addClass("success");

// Insert user-controlled content as text, not as raw HTML.
$("#message").text("Employee created successfully.");
```

### Q4. How do jQuery DOM insertion, copying, and deletion methods differ?

**Answer.**  
Insertion methods exist in two directions. Target-first methods put content relative to a target: `append()`, `prepend()`, `before()`, `after()`, and `replaceWith()`. Content-first methods do the same operation from the inserted content's point of view: `appendTo()`, `prependTo()`, `insertBefore()`, `insertAfter()`, and `replaceAll()`.

If an existing DOM node is inserted elsewhere, it is moved. To copy it, use `clone()`. For deletion, `empty()` removes children, `remove()` removes the matched elements and their jQuery data/events, `detach()` removes elements but keeps jQuery data/events for reinsertion, and `unwrap()` removes the parent while keeping the element.

```javascript
// Append a new list item at the end of the employee list.
$("<li/>", { text: "Rossi" }).appendTo("#employees");

// Copy a template row before inserting it, so the original stays in place.
var row = $("#employee-template").clone();
row.removeAttr("id").appendTo("#employee-table tbody");

// Temporarily remove a panel while keeping jQuery data and event handlers.
var panel = $("#filters").detach();
panel.appendTo("#sidebar");
```

### Q5. How does jQuery handle events?

**Answer.**  
jQuery can register handlers on every matched element in one call. Shortcut methods such as `click()` cover common events, while `bind()` and `unbind()` register and remove named handlers. Inside a normal function handler, `this` refers to the raw DOM element that received the event, so `$(this)` wraps it as a jQuery object.

```javascript
// Register one click handler on every matched button.
$(".delete-button").click(function (event) {
  event.preventDefault();

  // Wrap the clicked raw DOM element to use jQuery methods on it.
  $(this).closest("tr").remove();
});

// Register the same handler for two mouse events.
$("a.preview").bind("mouseenter mouseleave", function () {
  $(this).toggleClass("hovered");
});
```

### Q6. Compare `$.ajax()`, `$.get()`, `$.post()`, `$.getJSON()`, `$.getScript()`, and `.load()`.

**Answer.**  
`$.ajax()` is the low-level function and gives the most control over method, URL, data, headers, and callbacks. `$.get()` and `$.post()` are shortcuts for simple GET and POST requests. `$.getJSON()` performs a GET request and parses JSON automatically. `$.getScript()` downloads and executes a JavaScript file. `.load()` fetches HTML and injects it into matched elements; it can also load only a selector fragment from the remote HTML.

```javascript
// Full-control jQuery AJAX request. Object data is serialized as form data.
$.ajax({
  method: "POST",
  url: "create-employee.jsp",
  data: {
    badge: 7309,
    surname: "Rossi"
  }
}).done(function (html) {
  // Insert server response HTML into the result area.
  $("#result").html(html);
});
```

```javascript
// Load JSON and build list items after jQuery has parsed the response.
$.getJSON("rest/employee/salary/45", function (data) {
  var list = $("<ul/>");

  $.each(data.employees, function (index, employee) {
    // Use text to avoid inserting untrusted values as raw HTML.
    $("<li/>", { text: employee.surname }).appendTo(list);
  });

  $("#employees").empty().append(list);
});
```

### Q7. What is the HTML5 `<canvas>` element?

**Answer.**  
`<canvas>` is a fixed-size bitmap drawing surface controlled by JavaScript. It has no `src` or `alt` like an image. If `width` and `height` are omitted, the default size is 300 by 150 pixels. CSS can resize the displayed element, but that scales the bitmap and may distort the drawing if the aspect ratio changes.

To draw, JavaScript obtains a rendering context, usually `"2d"`.

```html
<!-- Minimal canvas page: JavaScript obtains the 2D context after page load. -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Canvas example</title>
  <script>
    // Initialize drawing only after the canvas element exists in the DOM.
    function draw() {
      var canvas = document.getElementById("tutorial");

      if (canvas.getContext) {
        var ctx = canvas.getContext("2d");
        ctx.fillRect(25, 25, 100, 100);
      }
    }
  </script>
</head>
<body onload="draw();">
  <canvas id="tutorial" width="150" height="150"></canvas>
</body>
</html>
```

### Q8. How do the canvas coordinate system and rectangle functions work?

**Answer.**  
The canvas origin `(0, 0)` is in the top-left corner. The `x` axis grows to the right and the `y` axis grows downward. By default, one canvas unit corresponds to one pixel. Rectangle methods are the only native primitive shapes: `fillRect()` draws a filled rectangle, `strokeRect()` draws an outline, and `clearRect()` clears pixels to transparency.

```javascript
// Draw a black square, clear a hole, then draw an outline inside the hole.
var canvas = document.getElementById("tutorial");
var ctx = canvas.getContext("2d");

ctx.fillRect(25, 25, 100, 100);
ctx.clearRect(45, 45, 60, 60);
ctx.strokeRect(50, 50, 50, 50);
```

### Q9. How are paths, lines, and arcs drawn on canvas?

**Answer.**  
All non-rectangle shapes are drawn with paths. A path starts with `beginPath()`, moves the virtual pen with `moveTo()`, adds segments with methods such as `lineTo()` or `arc()`, and is finally rendered with `stroke()` or `fill()`. `closePath()` can draw a straight line back to the path start.

Arcs use radians, not degrees. `arc(x, y, radius, startAngle, endAngle, anticlockwise)` draws an arc around a center point.

```javascript
// Draw a simple smiley face with one outer circle, one mouth arc, and two eyes.
var canvas = document.getElementById("tutorial");
var ctx = canvas.getContext("2d");

ctx.beginPath();
ctx.arc(75, 75, 50, 0, Math.PI * 2, true);
ctx.moveTo(110, 75);
ctx.arc(75, 75, 35, 0, Math.PI, false);
ctx.moveTo(65, 65);
ctx.arc(60, 65, 5, 0, Math.PI * 2, true);
ctx.moveTo(95, 65);
ctx.arc(90, 65, 5, 0, Math.PI * 2, true);
ctx.stroke();
```

### Q10. Why are `img.onload`, `save()`, `restore()`, transformations, and `requestAnimationFrame()` useful?

**Answer.**  
Images must be drawn after `img.onload` because loading is asynchronous. Calling `drawImage()` too early can draw nothing because the image bytes are not ready. `save()` and `restore()` manage canvas state as a stack, including styles, transformations, and clipping. `translate()` moves the origin, while `rotate()` rotates around the current origin. `requestAnimationFrame()` is preferred for animation because it runs before repaint and is synchronized with the browser.

```javascript
// Load an image, then draw it and overlay a path only after it is available.
var img = new Image();

img.onload = function () {
  ctx.drawImage(img, 0, 0);
  ctx.beginPath();
  ctx.moveTo(30, 96);
  ctx.lineTo(70, 66);
  ctx.lineTo(103, 76);
  ctx.stroke();
};

img.src = "backdrop.png";
```

```javascript
// Animation loop: clear old frame, isolate transform state, draw, then schedule next frame.
var angle = 0;

function animate() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  ctx.save();
  ctx.translate(75, 75);
  ctx.rotate(angle);
  ctx.fillRect(-20, -20, 40, 40);
  ctx.restore();

  angle += 0.05;
  requestAnimationFrame(animate);
}

requestAnimationFrame(animate);
```

---

## 16. Semantic Web and Linked Data

### Q1. What changes from the Web of Documents to the Web of Data?

**Answer.**  
The Web of Documents links human-readable resources such as HTML pages, images, and files. The Web of Data also links data entities: people, places, works, measurements, datasets, and concepts. The difference is that links become typed and machine-readable, so software can interpret what a relationship means instead of only following a hyperlink.

Raw values are not enough. `123`, `91`, and `38.5` become information only when metadata says what they represent, such as heartbeat, pressure, or temperature. This is why the Semantic Web needs explicit schemas, identifiers, and machine-readable representations.

### Q2. Compare ontology, Linked Data, knowledge graph, and knowledge base.

**Answer.**  
An ontology describes abstract concepts and relationships, for example the concept of `Person`, `Artwork`, or `createdBy`. OWL is used to define classes, properties, constraints, and axioms.

Linked Data describes concrete instances using RDF, for example Bob, Alice, the Mona Lisa, or Leonardo da Vinci. A knowledge graph is the graph of facts connecting these instances through typed relationships. A knowledge base combines the graph, the vocabulary/ontology, and the stored facts used by applications.

### Q3. Explain the RDF triple model.

**Answer.**  
RDF represents facts as triples:

- Subject: the resource being described, usually a URI.
- Predicate: the relationship, also usually a URI.
- Object: another resource URI or a literal value.

A set of triples forms an RDF graph. Nodes are subjects or objects; directed edges are predicates. Objects can be literals when the fact points to a value, such as a date or title, and URIs when the fact points to another resource.

```turtle
# Prefixes shorten long URIs so triples remain readable.
PREFIX foaf:    <http://xmlns.com/foaf/0.1/>
PREFIX schema:  <http://schema.org/>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX wd:      <http://www.wikidata.org/entity/>
PREFIX xsd:     <http://www.w3.org/2001/XMLSchema#>

# Bob is a person, knows Alice, has a typed birth date, and is interested in Mona Lisa.
<http://example.org/bob#me>
  a foaf:Person ;
  foaf:knows <http://example.org/alice#me> ;
  schema:birthDate "1990-07-04"^^xsd:date ;
  foaf:topic_interest wd:Q12418 .

# Mona Lisa is linked to its title and creator.
wd:Q12418
  dcterms:title "Mona Lisa" ;
  dcterms:creator <http://dbpedia.org/resource/Leonardo_da_Vinci> .
```

### Q4. Compare RDF/XML, Turtle, N-Triples, JSON-LD, RDFa, and TriG.

**Answer.**  
All of these formats can serialize RDF, but they suit different contexts. RDF/XML fits XML-based systems but is verbose. Turtle is compact and good for humans. N-Triples writes one triple per line, so it is simple and useful for bulk exchange or streaming. JSON-LD fits web APIs and JavaScript applications. RDFa embeds RDF annotations inside HTML. TriG extends Turtle-style syntax with named graphs.

Example in RDF/XML:

```xml
<!-- RDF/XML representation of Bob as a described resource. -->
<rdf:RDF
  xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
  xmlns:foaf="http://xmlns.com/foaf/0.1/"
  xmlns:schema="http://schema.org/">
  <rdf:Description rdf:about="http://example.org/bob#me">
    <rdf:type rdf:resource="http://xmlns.com/foaf/0.1/Person"/>
    <foaf:knows rdf:resource="http://example.org/alice#me"/>
    <schema:birthDate rdf:datatype="http://www.w3.org/2001/XMLSchema#date">1990-07-04</schema:birthDate>
  </rdf:Description>
</rdf:RDF>
```

Example in JSON-LD. The `_comment` field is only a study note; omit it in real JSON-LD data.

```json
{
  "_comment": "JSON-LD representation of Bob with context, id, type, and linked properties.",
  "@context": "example-context.json",
  "@id": "http://example.org/bob#me",
  "@type": "Person",
  "birthdate": "1990-07-04",
  "knows": "http://example.org/alice#me",
  "interest": {
    "@id": "http://www.wikidata.org/entity/Q12418",
    "title": "Mona Lisa",
    "creator": "http://dbpedia.org/resource/Leonardo_da_Vinci"
  }
}
```

### Q5. What is SPARQL and how does a `SELECT` query work?

**Answer.**  
SPARQL is the W3C query language for RDF graphs, similar in role to SQL for relational databases. A `SELECT` query binds variables by matching graph patterns in the `WHERE` clause. Variables start with `?`. Aggregation works with operators such as `COUNT()` and grouping with `GROUP BY`.

```sparql
# Query each person's name and count how many foaf:knows links they have.
PREFIX foaf: <http://xmlns.com/foaf/0.1/>

SELECT ?name (COUNT(?friend) AS ?count)
WHERE {
  ?person foaf:name ?name .
  ?person foaf:knows ?friend .
}
GROUP BY ?person ?name
```

`?person foaf:name ?name` binds a person to a name. `?person foaf:knows ?friend` binds each friend. `GROUP BY` groups rows by person and name, then `COUNT(?friend)` returns the number of friends per person.

### Q6. What are Tim Berners-Lee's four Linked Data principles?

**Answer.**  
The four principles are:

1. Use URIs as names for things, not only for documents.
2. Use HTTP URIs, so those names can be looked up.
3. When a URI is looked up, provide useful information using standards such as RDF and SPARQL.
4. Include links to other URIs, so clients can discover related resources.

Dereferencing matters because an HTTP URI can identify a thing and also lead clients to a description of that thing. In Linked Data, RDF links are typed links between data resources, not just clickable HTML links between pages.

### Q7. What are the FAIR principles?

**Answer.**  
FAIR means Findable, Accessible, Interoperable, and Reusable.

Findable data has persistent identifiers and rich metadata registered in searchable resources. Accessible data can be retrieved through standard protocols, possibly with authentication or authorization. Interoperable data uses formal representation languages, shared vocabularies, and qualified references to other data. Reusable data has clear licenses, provenance, accurate metadata, and domain standards.

Metadata can remain useful even if the original data disappears, because it still records what the data was, who produced it, and how it could be cited or understood.

### Q8. Why are DBpedia, Wikidata, and the LOD Cloud important examples?

**Answer.**  
DBpedia extracts structured data from Wikipedia and publishes it as Linked Data. It became a central hub because many datasets link to DBpedia URIs as shared references.

Wikidata is a collaborative, multilingual knowledge base. It gives entities stable URIs, such as the URI for the Mona Lisa, and provides machine-readable statements used by Wikipedia and external datasets.

The Linked Open Data Cloud shows many open datasets connected by RDF links. Its size is useful, but it also creates a discovery problem: users and systems must find which datasets contain the specific data they need.

---

## High-probability cross-topic questions

### Q1. Compare servlet-only, JSP/MVC, and REST implementations.

**Answer.**  
In a servlet-only implementation, the servlet parses the request, calls the model/DAO, and writes HTML directly with `PrintWriter`. This works for small examples but becomes hard to maintain.

In JSP/MVC, the servlet is the controller. It parses input, calls DAOs, creates model objects, stores them in request attributes, and forwards to JSP. JSP is the view and renders HTML with EL/JSTL.

In REST, the server returns resources, usually JSON, instead of HTML pages. A dispatcher routes requests to REST resource classes. Client-side JavaScript or another client consumes the JSON.

### Q2. Trace a create-employee request in MVC.

**Answer.**  
The browser submits a POST form to `/create-employee`. Tomcat routes the request to `CreateEmployeeServlet`. The servlet reads parameters, validates/parses them, creates an `Employee`, calls `CreateEmployeeDAO`, and receives success or catches errors. It creates a `Message`, stores `employee` and `message` as request attributes, and forwards to `create-employee-result.jsp`. The JSP reads attributes with EL and renders HTML using JSTL. The browser receives one HTTP response.

### Q3. Trace a create-employee request in REST.

**Answer.**  
The client sends `POST /rest/employee` with `Content-Type: application/json` and `Accept: application/json`. `RestDispatcherServlet` routes the request to `CreateEmployeeRR`. `AbstractRR` validates method and media types. `CreateEmployeeRR` parses the request body with Jackson, creates an `Employee`, calls `CreateEmployeeDAO`, and returns either `201 Created` with employee JSON or an error status such as `400`, `409`, or `500` with a `Message` JSON body.

### Q4. Connect validation, SQL injection, XSS, CSRF, and upload security.

**Answer.**  
All of these topics point to the same rule: client input cannot be trusted. HTML5 and JavaScript validation give quick feedback but can be bypassed. Server-side validation is mandatory. SQL injection is prevented primarily with prepared statements. XSS is mitigated with output encoding, sanitization, and safe DOM APIs. CSRF is mitigated with cookie policies such as `SameSite=Strict` and other anti-CSRF controls. File uploads require server-side MIME/type validation and size limits because client-side `accept` can be bypassed.

### Q5. Connect jQuery AJAX with the servlet, JSP, and REST approaches.

**Answer.**  
jQuery AJAX can call servlet/JSP endpoints that return HTML fragments, or REST endpoints that return JSON. With `.load()`, the browser fetches HTML and injects it into the page, so server-side rendering remains central. With `$.getJSON()` or `$.ajax()` against REST, the browser receives structured data and builds the DOM client-side. The first approach is closer to JSP/MVC; the second is closer to REST plus JavaScript UI logic.

### Q6. Connect Semantic Web concepts with XML, JSON, URI, and REST.

**Answer.**  
Semantic Web technologies reuse web foundations. URI/IRI identifies resources. HTTP makes those identifiers dereferenceable. XML, RDF/XML, Turtle, JSON-LD, and other formats serialize data. REST can expose resources and representations, while RDF adds typed relationships between resources. SPARQL then queries RDF graphs in a way similar to how SQL queries relational tables.

---

## One-hour exam simulations

### Simulation 1

1. Explain why web applications are a special case of three-tier architecture.
2. Write a minimal servlet and its `web.xml` mapping.
3. Explain Maven WAR packaging and `scope=provided`.
4. Compare GET and POST form submission.

### Simulation 2

1. Define the DAO pattern and explain why servlets should not contain SQL.
2. Write `CreateEmployeeDAO` with `PreparedStatement`.
3. Explain Tomcat connection pool with `context.xml`, `web.xml`, and JNDI lookup.
4. Explain SQL Injection and its mitigation.

### Simulation 3

1. Explain JSP execution model and why scriptlets are discouraged.
2. Write a servlet controller that forwards to a JSP.
3. Write a JSP using `<c:out>`, `<c:if>`, and `<c:forEach>`.
4. Explain MVC roles in the employee application.

### Simulation 4

1. Define REST, resource, URI, representation, and statelessness.
2. Write the `Resource` interface and explain JSON serialization.
3. Explain `Accept`, `Content-Type`, and REST status codes.
4. Describe AJAX flow from button click to DOM update.

### Simulation 5

1. Distinguish URI, URL, URN, and IRI.
2. Explain MIME and multipart file upload.
3. Write a multipart form and explain `Part` processing.
4. Explain Basic Authentication and why HTTPS is required.

### Simulation 6

1. Explain well-formed vs valid XML.
2. Compare DOM, SAX, and StAX.
3. Convert XML employee data to JSON.
4. Explain JSON parsing/serialization in REST.

### Simulation 7

1. Write a semantic HTML5 page.
2. Explain `id` vs `name` in forms.
3. Explain CSS cascade and specificity.
4. Write mobile-first CSS with media queries.

### Simulation 8

1. Explain the DOM and JavaScript event handling.
2. Write DOM creation code for a dynamic result table.
3. Write form validation with `preventDefault()`.
4. Write XHR or Fetch code that loads JSON.

### Simulation 9

1. Explain SQL Injection, XSS, and CSRF.
2. Fix vulnerable SQL concatenation with prepared statements.
3. Explain why `innerHTML` with untrusted data is dangerous.
4. Explain `SameSite=Strict`.

### Simulation 10

1. Explain Docker image, container, volume, network, and service.
2. Write a Compose file for Tomcat and PostgreSQL.
3. Explain healthcheck and why startup order is not readiness.
4. Write Docker Compose debugging commands.

### Simulation 11

1. Explain what a jQuery object is and how it differs from a raw DOM element.
2. Write jQuery code that registers an event handler and updates the DOM.
3. Compare `$.ajax()`, `$.getJSON()`, and `.load()`.
4. Write canvas code that draws rectangles, paths, or an animation frame.

### Simulation 12

1. Explain Web of Documents vs Web of Data.
2. Convert a small Bob/Alice/Mona Lisa example into RDF triples.
3. Compare Turtle, RDF/XML, JSON-LD, and N-Triples.
4. Write a SPARQL query with variables and explain how `GROUP BY` works.
