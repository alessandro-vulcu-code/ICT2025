# Web Applications 25-26 - Exam Questions, Answers, and Code Practice

Main source: [[Web Applications 25-26 - Theory Summary]].

Purpose: prepare for an exam that can contain both conceptual questions and code-writing questions. Each chapter contains exam-style questions with model answers. Chapters with implementation material also include code templates that can be adapted during an exam.

Use this document in two passes:

1. First pass: explain each concept without looking at the answer.
2. Second pass: rewrite each code answer from memory, then compare structure and details.

---

# Exam Answer Strategy

## Question 0.1 - How should a conceptual answer be structured?

**Answer.** Start with a precise definition, then add purpose, context, and one concrete example. If the question asks for a comparison, answer by criteria: responsibility, where it runs, advantages, disadvantages, and typical technologies. Avoid listing words without explaining their role.

For example, if asked "What is HTML?", do not only say "a markup language". A complete answer is: HTML is the standard markup language used to structure Web pages. It describes the meaning and organization of content through elements such as headings, paragraphs, links, images, forms, and semantic layout elements. It should describe structure and meaning, while CSS should define presentation and JavaScript behavior.

## Question 0.2 - How should a code-writing answer be structured?

**Answer.** Write minimal but complete code. Include imports only when useful, choose clear class and method names, and show the key API calls. For Java Web code, the examiner usually wants the pattern more than every small project-specific detail.

For code answers, always check:

- where the data comes from;
- which object owns the responsibility;
- which method is called by the framework or container;
- how user input is validated or bound safely;
- which resources must be closed;
- which object is returned, forwarded, or serialized.

---

# 1. Introduction to Web Applications

Likely conceptual themes: Web history, Web phases, Deep Web vs Dark Web, three logical layers, single-tier/two-tier/three-tier architecture, and HTTP in the network stack.

## Question 1.1 - What is hypertext, and how did it lead to the Web?

**Answer.** Hypertext is text connected by links, allowing the reader to move non-linearly between related pieces of information. The Web did not appear from nowhere: it evolved from previous ideas about linked knowledge. Vannevar Bush's Memex imagined associative information retrieval. Ted Nelson coined "hypertext" and imagined Xanadu, with bidirectional links and versioning. Douglas Engelbart's NLS introduced early hyperlinks, mouse interaction, windows, and collaborative editing.

Tim Berners-Lee made the idea practical at CERN by combining simple hypertext with the Internet. The World Wide Web used resources identified by URLs, transferred by HTTP, and represented mainly with HTML. The first popular graphical browser was Mosaic in 1993.

## Question 1.2 - Compare Web 1.0, Web 2.0, Web 3.0, and Web3.

**Answer.** Web 1.0 is the "Read Web": producers publish pages and users mostly read. Its core technologies are HTTP, HTML, MIME, and URL. Web 2.0 is the "Read/Write Web": users also create content and applications become more interactive. It uses technologies such as XML, AJAX, JSON, Web services, and REST.

Web 3.0, in this course, means the Semantic Web or Web of Data. Its goal is to make data machine-readable through explicit semantics, using RDF, OWL, and SPARQL. Web3 is a different concept related to decentralization, blockchain, crypto, DeFi, and NFTs. It must not be confused with Web 3.0 as Semantic Web.

## Question 1.3 - Explain Deep Web and Dark Web.

**Answer.** The Deep Web is the part of the Web not indexed by ordinary search engines. It includes private databases, login-protected resources, dynamically generated pages, and pages hidden behind forms or access control. The Dark Web is content accessed through anonymous networks such as Tor or I2P.

The key distinction is: Deep Web means not indexed; Dark Web means anonymous access. The Dark Web can be part of the Deep Web, but the two terms are not equivalent.

## Question 1.4 - Explain the three logical layers of a Web application.

**Answer.** A Web application can be described through presentation logic, application logic, and data logic. Presentation logic handles user interface, input/output format, and first validation. Application logic controls the flow of operations, business rules, and constraints. Data logic manages persistent storage, retrieval, and consistency.

A frequent exam trap is the application logic layer. Its purpose is not to display data and not to store data. Its purpose is to define and control the operations performed by the application.

## Question 1.5 - Compare single-tier, two-tier, and three-tier architecture.

**Answer.** In a single-tier architecture, all layers run on one machine, for example a mainframe with dumb terminals. It is simple, but it concentrates load and scales poorly.

In a two-tier fat-client architecture, presentation and application logic run on the client, while data logic runs on the server. The client does much work, but maintenance becomes difficult. In a two-tier fat-server architecture, presentation runs on the client, while application and data logic are centralized on the server.

In a three-tier architecture, the client handles presentation, the application server handles application logic, and the database server handles data. A typical Web application maps naturally to this model: browser, Web/application server, and DBMS. The advantages are scalability and separation of concerns; the disadvantage is greater implementation complexity.

---

# 2. Git and Maven

Likely conceptual themes: Git local areas, branches, pull requests, Maven lifecycle, phases/goals/plugins, POM, WAR packaging, and standard project layout.

## Question 2.1 - Explain Git working directory, index, and HEAD.

**Answer.** Git is a distributed version-control system. Each local copy is a complete repository with history, not only a checkout from a central server. The working directory contains files being edited. The index, or staging area, contains the snapshot prepared for the next commit. HEAD points to the last commit of the current branch.

`git add` copies selected changes from the working directory to the index. `git commit` records staged changes in local history. `git push` sends local commits to a remote repository.

## Question 2.2 - What is the difference between a pull request and `git pull`?

**Answer.** `git pull` is a command that fetches changes from a remote repository and integrates them into the current local branch. A pull request is a review request on a platform such as GitHub or Bitbucket. It proposes merging one branch into another and allows discussion, code review, and checks before integration.

## Question 2.3 - Explain Maven lifecycle, phase, goal, plugin, and POM.

**Answer.** Maven is a Java project-management tool for building, packaging, dependency resolution, documentation, and deployment. A lifecycle is an ordered build process, such as `clean`, `default`, or `site`. A phase is a step in a lifecycle, such as `compile`, `test`, or `package`. A goal is a concrete operation implemented by a plugin. A plugin contains one or more goals.

The POM, `pom.xml`, is the declarative project description. It contains coordinates, dependencies, plugins, and packaging. If a phase is invoked, Maven also executes the previous phases in that lifecycle. For example, `mvn package` validates, compiles, tests, and packages the project.

## Question 2.4 - Write a minimal Maven POM fragment for a Web application.

**Answer.** A Web application should use `war` packaging. The Servlet API is usually provided by Tomcat, so its dependency scope is `provided`.

```xml
<project>
  <modelVersion>4.0.0</modelVersion>

  <groupId>it.unipd.dei.webapp</groupId>
  <artifactId>employee-webapp</artifactId>
  <version>1.0.0</version>
  <packaging>war</packaging>

  <dependencies>
    <dependency>
      <groupId>jakarta.servlet</groupId>
      <artifactId>jakarta.servlet-api</artifactId>
      <version>6.0.0</version>
      <scope>provided</scope>
    </dependency>
  </dependencies>
</project>
```

Key points: `groupId`, `artifactId`, and `version` identify the artifact. `packaging` defines the output type. `target/` is generated output and should not be committed.

---

# 3. Docker and Containerization

Likely conceptual and code themes: deployment problem, container vs VM, image vs container, volume, network, Dockerfile, Docker Compose, and healthcheck.

## Question 3.1 - What problem does Docker solve for a Java Web application?

**Answer.** A Java Web application depends on more than source code and a WAR file. It needs compatible Java, Tomcat, PostgreSQL, libraries, configuration, ports, environment variables, and initial data. Docker packages the application and its runtime dependencies into isolated, repeatable environments. This reduces environment mismatch between development and deployment.

## Question 3.2 - Compare Docker image, container, volume, network, and service.

**Answer.** A Docker image is an immutable, layered template containing the filesystem and dependencies needed to run an application. A container is a running instance of an image with a writable layer. A volume is persistent storage outside the container layer. A network lets containers communicate privately. A service is a logical component of a Compose application, such as `web` or `db`.

## Question 3.3 - Write a Dockerfile for deploying a WAR on Tomcat.

**Answer.** A minimal Dockerfile starts from Tomcat, copies the WAR, and exposes the Tomcat port.

```dockerfile
FROM tomcat:10

COPY target/employee-webapp.war /usr/local/tomcat/webapps/employee.war

EXPOSE 8080
```

This is enough for a simple exam answer. In a real project, the WAR must be built before the image is built, usually through Maven.

## Question 3.4 - Write a Docker Compose file for Tomcat and PostgreSQL.

**Answer.** Compose is used for multi-container applications. The Web service depends on the database service. The database should have a healthcheck, because `depends_on` alone does not guarantee that PostgreSQL is ready to accept connections.

```yaml
services:
  web:
    image: tomcat:10
    ports:
      - "8080:8080"
    volumes:
      - ./target/employee-webapp.war:/usr/local/tomcat/webapps/employee.war
    depends_on:
      db:
        condition: service_healthy

  db:
    image: postgres:16
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: employee
    volumes:
      - ./employee.sql:/docker-entrypoint-initdb.d/init.sql
      - ./data/db:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
      timeout: 10s
      retries: 20
```

Inside the Compose network, the Web container can use `db` as database hostname.

---

# 4. Java Servlets

Likely conceptual and code themes: servlet definition, lifecycle, `init`, `service`, `doGet`, `doPost`, thread safety, URL mapping, `WEB-INF`, response generation, forms, and request/response objects.

## Question 4.1 - What is a servlet, and what is its lifecycle?

**Answer.** A servlet is a Java-based server-side Web component managed by a Web container. It generates dynamic content in response to requests. In this course, servlets usually extend `HttpServlet`, and Tomcat acts as the Web container.

The container calls `init()` once after creating the servlet, calls `service()` for each request, and calls `destroy()` once before removing the servlet. `service()` dispatches HTTP requests to methods such as `doGet`, `doPost`, `doPut`, and `doDelete`.

## Question 4.2 - Why are servlet instance fields dangerous?

**Answer.** The same servlet instance may serve multiple concurrent requests. If request-specific data is stored in instance fields, two requests can overwrite each other's data. Request-specific values must stay in local variables, request attributes, or properly scoped objects. Shared fields are acceptable only for immutable configuration or thread-safe shared resources.

## Question 4.3 - Write a minimal servlet that returns HTML.

**Answer.** This is the standard pattern: extend `HttpServlet`, override `doGet`, set content type, obtain a writer, and write the response.

```java
package it.unipd.dei.webapp.servlet;

import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;
import java.io.PrintWriter;

public final class HelloServlet extends HttpServlet {

    @Override
    protected void doGet(final HttpServletRequest req,
                         final HttpServletResponse res)
            throws ServletException, IOException {

        res.setContentType("text/html; charset=utf-8");

        try (PrintWriter out = res.getWriter()) {
            out.println("<!DOCTYPE html>");
            out.println("<html lang=\"en\">");
            out.println("<head><title>Hello</title></head>");
            out.println("<body>");
            out.println("<p>Hello, world!</p>");
            out.println("</body>");
            out.println("</html>");
        }
    }
}
```

Manual HTML generation is fine for small examples, but JSP/MVC is better for real views.

## Question 4.4 - Write a servlet that reads a form parameter.

**Answer.** GET parameters are sent in the URL query string. POST parameters are sent in the request body. In both cases, a servlet can read them with `getParameter`.

```java
public final class HelloNameServlet extends HttpServlet {

    @Override
    protected void doPost(final HttpServletRequest req,
                          final HttpServletResponse res)
            throws ServletException, IOException {

        final String name = req.getParameter("helloName");

        res.setContentType("text/html; charset=utf-8");

        try (PrintWriter out = res.getWriter()) {
            out.println("<!DOCTYPE html>");
            out.println("<html lang=\"en\">");
            out.println("<body>");
            out.printf("<p>Hello, %s!</p>%n", name);
            out.println("</body>");
            out.println("</html>");
        }
    }
}
```

Security note: this direct output is intentionally minimal. In real code, escape user input or render through JSP with `<c:out>`.

## Question 4.5 - Write a `web.xml` mapping for a servlet.

**Answer.** `web.xml` maps a servlet class to one or more URL patterns. Files under `WEB-INF/` are private and cannot be directly requested by the browser.

```xml
<web-app>
  <servlet>
    <servlet-name>HelloServlet</servlet-name>
    <servlet-class>it.unipd.dei.webapp.servlet.HelloServlet</servlet-class>
  </servlet>

  <servlet-mapping>
    <servlet-name>HelloServlet</servlet-name>
    <url-pattern>/hello</url-pattern>
  </servlet-mapping>
</web-app>
```

## Question 4.6 - Write a Log4J MDC cleanup pattern for a servlet.

**Answer.** Servlet containers reuse threads, so request-specific logging context must be removed in `finally`.

```java
protected void doPost(final HttpServletRequest req,
                      final HttpServletResponse res)
        throws ServletException, IOException {

    LogContext.setIPAddress(req.getRemoteAddr());
    LogContext.setAction("CREATE_EMPLOYEE");

    try {
        // Process request here.
        LOGGER.info("Request served.");
    } finally {
        LogContext.removeIPAddress();
        LogContext.removeAction();
    }
}
```

Without cleanup, the next request served by the same thread may inherit wrong metadata.

---

# 5. Servlets and Database Access

Likely conceptual and code themes: resource classes, DAO pattern, `PreparedStatement`, SQL Injection prevention, JNDI, `DataSource`, connection pool, and servlet-to-DAO flow.

## Question 5.1 - What is a DAO, and why should servlets use it?

**Answer.** A DAO, Data Access Object, encapsulates database access logic. Servlets should not contain SQL directly. A servlet should parse and validate HTTP input, obtain a database connection, call a DAO, and prepare the response. The DAO should contain SQL, JDBC code, and mapping between database rows and resource objects.

This improves separation of concerns and security. It also makes the code easier to test and maintain. When SQL is isolated in DAOs, changes to database access do not spread through every servlet.

## Question 5.2 - Write an immutable `Employee` resource class.

**Answer.** A resource class represents domain data. Fields are often `final`, so the object cannot change after construction.

```java
package it.unipd.dei.webapp.resource;

public final class Employee {

    private final int badge;
    private final String surname;
    private final int age;
    private final int salary;

    public Employee(final int badge, final String surname,
                    final int age, final int salary) {
        this.badge = badge;
        this.surname = surname;
        this.age = age;
        this.salary = salary;
    }

    public int getBadge() {
        return badge;
    }

    public String getSurname() {
        return surname;
    }

    public int getAge() {
        return age;
    }

    public int getSalary() {
        return salary;
    }
}
```

## Question 5.3 - Write a generic DAO interface like the one used in the course.

**Answer.** The course pattern uses `access()` to execute the operation and `getOutputParam()` to return the result.

```java
package it.unipd.dei.webapp.dao;

import java.sql.SQLException;

public interface DataAccessObject<T> {

    DataAccessObject<T> access() throws SQLException;

    T getOutputParam();
}
```

Some implementations return themselves from `access()` with a more specific return type, which is allowed through covariant return types.

## Question 5.4 - Write a DAO that searches employees by salary.

**Answer.** This is one of the most likely code-writing tasks. The DAO stores the connection and input parameter, uses `PreparedStatement`, maps rows to `Employee` objects, stores the list in `outputParam`, and returns it through `getOutputParam()`.

```java
package it.unipd.dei.webapp.dao;

import it.unipd.dei.webapp.resource.Employee;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

public final class SearchEmployeeBySalaryDAO implements DataAccessObject<List<Employee>> {
    private static final String STATEMENT =
            "SELECT badge, surname, age, salary " +
            "FROM Employee " +
            "WHERE salary > ?";

    private final Connection con;
    private final int salary;

    private List<Employee> outputParam;

    public SearchEmployeeBySalaryDAO(final Connection con, final int salary) {
        this.con = con;
        this.salary = salary;
    }

    @Override
    public SearchEmployeeBySalaryDAO access() throws SQLException {
        final List<Employee> employees = new ArrayList<>();

        try (PreparedStatement pstmt = con.prepareStatement(STATEMENT)) {
            pstmt.setInt(1, salary);

            try (ResultSet rs = pstmt.executeQuery()) {
                while (rs.next()) {
                    employees.add(new Employee(
                            rs.getInt("badge"),
                            rs.getString("surname"),
                            rs.getInt("age"),
                            rs.getInt("salary")));
                }
            }
        }

        outputParam = employees;
        return this;
    }

    @Override
    public List<Employee> getOutputParam() {
        return outputParam;
    }
}
```

Key exam details: `?` prevents SQL structure manipulation; `setInt` binds the value as data; `executeQuery()` is used for `SELECT`; `try-with-resources` closes statement and result set. The DAO does not open the connection; it receives it from the servlet.

## Question 5.5 - Write a DAO that inserts an employee.

**Answer.** Insert/update/delete operations use `executeUpdate()`. The result is the number of affected rows.

```java
package it.unipd.dei.webapp.dao;

import it.unipd.dei.webapp.resource.Employee;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public final class CreateEmployeeDAO
        implements DataAccessObject<Employee> {

    private static final String STATEMENT =
            "INSERT INTO Employee (badge, surname, age, salary) " +
            "VALUES (?, ?, ?, ?)";

    private final Connection con;
    private final Employee employee;

    private Employee outputParam;

    public CreateEmployeeDAO(final Connection con,
                             final Employee employee) {
        this.con = con;
        this.employee = employee;
    }

    @Override
    public CreateEmployeeDAO access() throws SQLException {
        try (PreparedStatement pstmt = con.prepareStatement(STATEMENT)) {
            pstmt.setInt(1, employee.getBadge());
            pstmt.setString(2, employee.getSurname());
            pstmt.setInt(3, employee.getAge());
            pstmt.setInt(4, employee.getSalary());

            final int affectedRows = pstmt.executeUpdate();

            if (affectedRows == 1) {
                outputParam = employee;
            }
        }

        return this;
    }

    @Override
    public Employee getOutputParam() {
        return outputParam;
    }
}
```

If `affectedRows` is zero, the insert did not create a row. In a full project, the DAO or servlet would turn this into a `Message` error.

## Question 5.6 - Write servlet code that obtains a pooled connection through JNDI.

**Answer.** The servlet should look up the `DataSource` once in `init()`. Each request borrows a connection with `ds.getConnection()`.

```java
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServlet;
import javax.naming.InitialContext;
import javax.naming.NamingException;
import javax.sql.DataSource;

public abstract class AbstractDatabaseServlet extends HttpServlet {

    protected DataSource ds;

    @Override
    public void init() throws ServletException {
        try {
            final InitialContext ctx = new InitialContext();
            ds = (DataSource) ctx.lookup(
                    "java:/comp/env/jdbc/employee-ferro");
        } catch (NamingException e) {
            throw new ServletException("Cannot look up DataSource.", e);
        }
    }
}
```

`context.xml` defines the Tomcat resource. `web.xml` declares that the application uses it through a `<resource-ref>`.

## Question 5.7 - Write a servlet that calls a DAO and forwards to JSP.

**Answer.** This combines servlet, connection pool, DAO, model object, request attributes, and MVC forwarding.

```java
public final class SearchEmployeeServlet extends AbstractDatabaseServlet {

    @Override
    protected void doGet(final HttpServletRequest req,
                         final HttpServletResponse res)
            throws ServletException, IOException {

        final int salary = Integer.parseInt(req.getParameter("salary"));

        try (Connection con = ds.getConnection()) {
            final SearchEmployeeBySalaryDAO dao =
                    new SearchEmployeeBySalaryDAO(con, salary);

            final List<Employee> employees =
                    dao.access().getOutputParam();

            req.setAttribute("employees", employees);
            req.getRequestDispatcher("/jsp/search-result.jsp")
                    .forward(req, res);
        } catch (SQLException e) {
            throw new ServletException("Database error.", e);
        }
    }
}
```

The servlet controls flow. The DAO handles SQL. The JSP handles rendering.

## Question 5.8 - Explain how `PreparedStatement` prevents SQL Injection.

**Answer.** SQL Injection happens when untrusted input is concatenated into SQL and the database interprets it as syntax. With `PreparedStatement`, SQL structure and user values are separated. The query contains `?` placeholders; values are bound with methods such as `setInt` or `setString`.

The database treats bound values as data, not as SQL syntax. Therefore an input such as `' OR '1'='1' --` cannot change the structure of the query. Prepared statements must be combined with validation and least privilege, but they are the core JDBC defense.

---

# 6. JSP and MVC

Likely conceptual and code themes: JSP translation into servlet, JSP components, JSTL, EL, JavaBeans, `<c:out>`, scriptlets, MVC, request attributes, and server-side forward.

## Question 6.1 - How does JSP technology work?

**Answer.** A JSP is a server-side template-based view. On first request, the container translates the `.jsp` file into a servlet, compiles it, and executes it. Later requests reuse the compiled servlet unless the JSP changes.

JSP lets the developer write mostly HTML and use tags or EL for dynamic parts. It avoids writing large HTML pages with `out.println` inside servlets.

## Question 6.2 - Explain Model, View, and Controller in Java Web MVC.

**Answer.** In this course, the Model is made of resource classes and DAOs. The View is made of JSP pages. The Controller is made of servlets. The servlet reads input, validates it, calls DAOs, stores model objects in request attributes, and forwards to a JSP. The JSP reads the attributes and renders HTML.

`forward()` is server-side. The browser receives a single response and does not need to know which JSP was used internally.

## Question 6.3 - Write a JSP that displays a message and one employee.

**Answer.** Use JSTL and EL. Use `<c:out>` for user-controlled values because it escapes HTML/XML characters.

```jsp
<%@ page contentType="text/html;charset=UTF-8" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>

<!DOCTYPE html>
<html lang="en">
<head>
  <title>Employee result</title>
</head>
<body>
  <c:if test="${not empty message}">
    <p><c:out value="${message.message}"/></p>
  </c:if>

  <c:if test="${not empty employee}">
    <ul>
      <li>Badge: <c:out value="${employee.badge}"/></li>
      <li>Surname: <c:out value="${employee.surname}"/></li>
      <li>Age: <c:out value="${employee.age}"/></li>
      <li>Salary: <c:out value="${employee.salary}"/></li>
    </ul>
  </c:if>
</body>
</html>
```

`${employee.badge}` calls `getBadge()` on the JavaBean-style object.

## Question 6.4 - Write a JSP that displays a list of employees.

**Answer.** Use `<c:forEach>` for iteration and `<c:out>` for escaped output.

```jsp
<%@ page contentType="text/html;charset=UTF-8" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>

<table>
  <thead>
    <tr>
      <th>Badge</th>
      <th>Surname</th>
      <th>Age</th>
      <th>Salary</th>
    </tr>
  </thead>
  <tbody>
    <c:forEach var="employee" items="${employees}">
      <tr>
        <td><c:out value="${employee.badge}"/></td>
        <td><c:out value="${employee.surname}"/></td>
        <td><c:out value="${employee.age}"/></td>
        <td><c:out value="${employee.salary}"/></td>
      </tr>
    </c:forEach>
  </tbody>
</table>
```

This is the expected view-side counterpart of a servlet that sets `req.setAttribute("employees", employees)`.

## Question 6.5 - Why are scriptlets bad in JSP?

**Answer.** Scriptlets mix Java logic with HTML, making the page hard to read and maintain. They also blur MVC responsibilities: business logic should not be in the view. JSTL and EL are preferred for limited view logic, such as conditions, loops, and safe output. Complex logic belongs in servlets, DAOs, or resource classes.

---

# 7. REST Web Services

Likely conceptual and code themes: REST resources, URIs, representations, methods, statelessness, `Accept`, `Content-Type`, JSON resources, Jackson, error statuses, and REST dispatcher.

## Question 7.1 - Explain REST as an architectural style.

**Answer.** REST models application data as resources. Each resource has identity and is identified by a URI. Clients and servers exchange representations of resources, such as JSON or XML. HTTP methods form a uniform interface: `GET` reads, `POST` creates or submits, `PUT` replaces or updates, and `DELETE` deletes.

REST is stateless. Each request must contain all information needed to process it. The server should not rely on previous requests to understand the current one.

## Question 7.2 - Explain `Accept` and `Content-Type`.

**Answer.** `Accept` is sent by the client to say which response media types it can process. Example: `Accept: application/json`. `Content-Type` says which media type is actually contained in the request or response body. For `POST` and `PUT`, `Content-Type` is essential because the server must know how to parse the request body.

Missing or unsupported media types should produce correct HTTP errors: 400 for malformed or missing required headers, 406 for unacceptable response type, and 415 for unsupported input media type.

## Question 7.3 - Write a REST resource method that serializes `Employee` to JSON.

**Answer.** The course pattern uses a `Resource` interface with `toJSON(OutputStream)`. Jackson `JsonGenerator` writes JSON tokens in order.

```java
public final class Employee implements Resource {

    private final int badge;
    private final String surname;
    private final int age;
    private final int salary;

    @Override
    public void toJSON(final OutputStream out) throws IOException {
        final JsonGenerator jg = JSON_FACTORY.createGenerator(out);

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
    }
}
```

Do not close the servlet output stream accidentally. In the course code, Jackson auto-close is disabled for that reason.

## Question 7.4 - Write a simple REST handler for `GET /rest/employee/{badge}`.

**Answer.** The handler should read the path parameter, call a DAO, set status and content type, and serialize the resource.

```java
public final class ReadEmployeeRR extends AbstractRR {

    private final HttpServletRequest req;
    private final HttpServletResponse res;
    private final Connection con;
    private final int badge;

    public ReadEmployeeRR(final HttpServletRequest req,
                          final HttpServletResponse res,
                          final Connection con,
                          final int badge) {
        this.req = req;
        this.res = res;
        this.con = con;
        this.badge = badge;
    }

    @Override
    protected void doServe() throws IOException, SQLException {
        final Employee employee =
                new ReadEmployeeDAO(con, badge).access().getOutputParam();

        if (employee == null) {
            res.setStatus(HttpServletResponse.SC_NOT_FOUND);
            new Message("Employee not found.", "E404", null)
                    .toJSON(res.getOutputStream());
            return;
        }

        res.setStatus(HttpServletResponse.SC_OK);
        res.setContentType("application/json");
        employee.toJSON(res.getOutputStream());
    }
}
```

This is a model answer for structure. Project-specific constructors and message classes may differ.

## Question 7.5 - Write a `web.xml` mapping for a REST dispatcher.

**Answer.** A REST front controller can receive all `/rest/*` requests and dispatch by method and URI.

```xml
<servlet>
  <servlet-name>RestManagerServlet</servlet-name>
  <servlet-class>
    it.unipd.dei.webapp.rest.RestDispatcherServlet
  </servlet-class>
</servlet>

<servlet-mapping>
  <servlet-name>RestManagerServlet</servlet-name>
  <url-pattern>/rest/*</url-pattern>
</servlet-mapping>
```

The dispatcher often overrides `service()` so it can handle `GET`, `POST`, `PUT`, and `DELETE` in one routing point.

## Question 7.6 - Map REST methods to an employee API.

**Answer.** Typical mapping:

| Method | URI | Meaning |
|---|---|---|
| `GET` | `/rest/employee` | List employees |
| `POST` | `/rest/employee` | Create employee |
| `GET` | `/rest/employee/{badge}` | Read one employee |
| `PUT` | `/rest/employee/{badge}` | Replace or update employee |
| `DELETE` | `/rest/employee/{badge}` | Delete employee |
| `GET` | `/rest/employee/salary/{salary}` | Search by salary |

Use JSON representations and meaningful HTTP status codes.

---

# 8. HTTP and Surroundings

Likely conceptual and code themes: four Web pillars, URI/URL/URN/IRI, percent-encoding, MIME, multipart/form-data, safe/idempotent methods, status codes, Basic authentication, filters, and sessions.

## Question 8.1 - Explain URI, URL, URN, and IRI.

**Answer.** A URI identifies a resource. A URL is a URI that also provides a location or access mechanism, such as `https://example.org/page`. A URN is a persistent name using the `urn:` scheme, such as `urn:isbn:...`. An IRI extends URI by allowing Unicode characters.

URI syntax can include scheme, authority, host, port, path, query, and fragment. The path identifies the resource location, query carries parameters, and fragment identifies a secondary resource inside the representation.

## Question 8.2 - Explain percent-encoding and character encoding.

**Answer.** Percent-encoding represents an octet as `%XX`, where `XX` is hexadecimal. It is used in URIs for reserved characters and non-plain-ASCII characters. For example, space is `%20`, `?` is `%3F`, `&` is `%26`, and `#` is `%23`.

ASCII uses 7 bits. Extended ASCII uses 8 bits but creates country-specific compatibility problems. Unicode defines a common character set. UTF-8 is the dominant Web encoding and is compatible with ASCII for the first 128 characters.

## Question 8.3 - Explain MIME and multipart/form-data.

**Answer.** MIME defines media types and transfer encodings for email and the Web. `Content-Type` gives the media type of the body, such as `text/html; charset=utf-8`. `Content-Encoding` says whether compression such as `gzip` was applied. `Content-Disposition` can suggest attachment handling and filename.

`multipart/form-data` combines multiple body parts into one request, especially for file uploads. Parts are separated by a boundary: an arbitrary sequence of characters that must not appear inside the parts. Ordinary form fields often use `application/x-www-form-urlencoded`.

## Question 8.4 - Compare safe and idempotent HTTP methods.

**Answer.** A safe method has no intended server-side side effects. `GET`, `HEAD`, and `OPTIONS` are safe. An idempotent method has the same effect if repeated once or many times. `GET`, `HEAD`, `PUT`, `DELETE`, and `OPTIONS` are idempotent. `POST` is usually not idempotent.

`GET` retrieves. `POST` submits data or creates a subordinate resource. `PUT` stores or replaces the resource identified by the URI. `DELETE` removes the resource.

## Question 8.5 - Write the Basic authentication header for `user:secret`.

**Answer.** Basic authentication sends Base64 of `username:password` in the `Authorization` header.

```http
Authorization: Basic dXNlcjpzZWNyZXQ=
```

Base64 is encoding, not encryption. Basic authentication must be used over HTTPS.

## Question 8.6 - Write a servlet filter that protects a private path.

**Answer.** A filter can check whether a session already exists. `getSession(false)` does not create a new session.

```java
public final class AuthenticationFilter implements Filter {

    @Override
    public void doFilter(final ServletRequest request,
                         final ServletResponse response,
                         final FilterChain chain)
            throws IOException, ServletException {

        final HttpServletRequest req = (HttpServletRequest) request;
        final HttpServletResponse res = (HttpServletResponse) response;

        final HttpSession session = req.getSession(false);

        if (session == null || session.getAttribute("user") == null) {
            res.setHeader("WWW-Authenticate", "Basic realm=\"Webapp\"");
            res.sendError(HttpServletResponse.SC_UNAUTHORIZED);
            return;
        }

        chain.doFilter(request, response);
    }
}
```

In a full implementation, the filter would parse `Authorization`, validate credentials, and create a session after successful authentication.

---

# 9. Markup Languages, XML, and JSON

Likely conceptual and code themes: markup types, XML nodes, well-formed vs valid XML, DOM/SAX/StAX, DTD, namespaces, XSD, JSON, JSON Schema, and Jackson parsing.

## Question 9.1 - Explain descriptive and procedural markup.

**Answer.** Descriptive markup describes the role or meaning of content. For example, `<h1>` means "main heading" and `<blockquote>` means quoted content. Procedural markup contains instructions about how content should be formatted, such as "make this red". Modern Web documents should prefer descriptive markup and leave presentation to CSS.

## Question 9.2 - Explain well-formed and valid XML.

**Answer.** Well-formed XML follows XML syntax: matching tags, proper nesting, quoted attribute values, and exactly one root element. Valid XML is well-formed and also satisfies a DTD or XML Schema. Therefore validity is stronger than well-formedness.

## Question 9.3 - Compare DOM, SAX, and StAX.

**Answer.** DOM builds an in-memory tree and supports bidirectional access and modification. SAX is a push streaming API: the parser calls callbacks while reading forward. StAX is a pull streaming API: the application asks for the next event. DOM is easy for random access; SAX and StAX are better for large documents.

## Question 9.4 - Write a small DTD fragment.

**Answer.** DTD defines allowed elements and attributes.

```xml
<!ELEMENT channel (title, link, description, item+)>
<!ELEMENT title (#PCDATA)>
<!ELEMENT link (#PCDATA)>
<!ELEMENT description (#PCDATA)>
<!ELEMENT item (title, link, description)>
<!ATTLIST guid isPermaLink (true | false) "false">
```

Operators: `,` means sequence, `|` choice, `?` zero or one, `*` zero or more, and `+` one or more.

## Question 9.5 - Write a small JSON representation of an employee.

**Answer.**

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

JSON is usually more compact than XML and maps naturally to JavaScript objects.

## Question 9.6 - Write Jackson code that reads an `Employee` object from JSON.

**Answer.** This example uses the tree model for readability. A streaming solution is also valid if it reads tokens carefully.

```java
public static Employee fromJSON(final InputStream in)
        throws IOException {

    final ObjectMapper mapper = new ObjectMapper();
    final JsonNode root = mapper.readTree(in);
    final JsonNode node = root.get("employee");

    if (node == null || node.isMissingNode()) {
        throw new EOFException("No employee object found.");
    }

    return new Employee(
            node.get("badge").asInt(),
            node.get("surname").asText(),
            node.get("age").asInt(),
            node.get("salary").asInt());
}
```

If the course expects streaming Jackson, mention that `JsonParser` reads one token at a time, like StAX for XML.

---

# 10. HTML5

Likely conceptual and code themes: base structure, doctype, semantic HTML, block vs inline, links, figures, forms, `id` vs `name`, radio buttons, semantic layout, media, and canvas.

## Question 10.1 - What is HTML?

**Answer.** HTML is the standard markup language for structuring Web pages. It uses elements to describe headings, paragraphs, links, images, tables, forms, and semantic page areas. HTML should express structure and meaning. CSS should handle presentation, and JavaScript should handle behavior.

## Question 10.2 - Write a minimal valid HTML5 page.

**Answer.**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Employee page</title>
</head>
<body>
  <h1>Employee page</h1>
</body>
</html>
```

`<!DOCTYPE html>` triggers standards mode. `<title>` appears in the browser tab.

## Question 10.3 - Explain block and inline elements.

**Answer.** Block elements start on a new line and take the available width. Examples: `<p>`, `<h1>`, `<ul>`, `<li>`, and `<div>`. Inline elements stay inside the text flow. Examples: `<a>`, `<em>`, `<img>`, and `<span>`.

## Question 10.4 - Write HTML for a figure with image and caption.

**Answer.**

```html
<figure>
  <img src="figure/quokka.jpg" alt="A family of quokka">
  <figcaption>The quokka is an Australian marsupial.</figcaption>
</figure>
```

`alt` is needed for accessibility and fallback. `<figure>` groups media and caption.

## Question 10.5 - Write a form with text input, email input, and radio buttons.

**Answer.**

```html
<form action="/create-employee" method="post">
  <label for="surname">Surname</label>
  <input id="surname" name="surname" type="text" required>

  <label for="email">Email</label>
  <input id="email" name="email" type="email" required>

  <fieldset>
    <legend>Gender</legend>
    <label>
      <input type="radio" name="gender" value="male" checked>
      Male
    </label>
    <label>
      <input type="radio" name="gender" value="female">
      Female
    </label>
    <label>
      <input type="radio" name="gender" value="other">
      Other
    </label>
  </fieldset>

  <button type="submit">Submit</button>
</form>
```

`name` is the parameter sent to the server. `id` identifies an element inside the page. Radio buttons in the same group must have the same `name` and different `value`.

## Question 10.6 - Write semantic layout using HTML5 elements.

**Answer.**

```html
<header>
  <h1>Employee application</h1>
</header>

<nav>
  <a href="/employees">Employees</a>
  <a href="/create">Create</a>
</nav>

<main>
  <article>
    <h2>Employee result</h2>
    <p>Employee successfully created.</p>
  </article>

  <aside>
    <p>Related actions</p>
  </aside>
</main>

<footer>
  <p>Web Applications course</p>
</footer>
```

Semantic elements make page structure clearer for developers, browsers, accessibility tools, and search engines.

---

# 11. Web Security

Likely conceptual and code themes: CIA triad, SQL Injection, XSS, CSRF, prepared statements, escaping with `<c:out>`, safe DOM APIs, tokens, and `SameSite`.

## Question 11.1 - Compare SQL Injection, XSS, and CSRF.

**Answer.** SQL Injection targets the database. It happens when untrusted input is mixed with SQL code and interpreted as SQL syntax. The main defense is prepared statements.

XSS targets the victim's browser. It happens when attacker-controlled content is rendered as HTML or JavaScript in a trusted page. Defenses include output escaping, sanitization, and safe DOM APIs.

CSRF targets authenticated actions. It tricks the victim's browser into sending a request to a site where the victim is already authenticated. Defenses include CSRF tokens, `SameSite` cookies, and avoiding state-changing GET requests.

## Question 11.2 - Fix vulnerable SQL code.

**Answer.** Vulnerable pattern:

```java
String sql = "SELECT * FROM Employee WHERE surname = '" + surname + "'";
Statement st = con.createStatement();
ResultSet rs = st.executeQuery(sql);
```

Safe pattern:

```java
String sql = "SELECT * FROM Employee WHERE surname = ?";

try (PreparedStatement pstmt = con.prepareStatement(sql)) {
    pstmt.setString(1, surname);

    try (ResultSet rs = pstmt.executeQuery()) {
        while (rs.next()) {
            // Map rows here.
        }
    }
}
```

The safe version separates SQL structure from user data.

## Question 11.3 - Fix an XSS-prone JSP output.

**Answer.** Unsafe output:

```jsp
<p>${param.comment}</p>
```

Safer output with escaping:

```jsp
<p><c:out value="${param.comment}"/></p>
```

`<c:out>` escapes HTML/XML characters, so a string such as `<script>...</script>` is displayed as text instead of executed as code.

## Question 11.4 - Fix unsafe DOM insertion in JavaScript.

**Answer.** Unsafe code:

```javascript
output.innerHTML = userComment;
```

Safer code:

```javascript
output.textContent = userComment;
```

`innerHTML` parses the string as HTML. `textContent` inserts it as text.

## Question 11.5 - Show the idea of a CSRF token in a form.

**Answer.** The server generates an unpredictable token, stores it in the session, and puts it in the form. On submission, the server accepts the request only if the submitted token matches the session token.

```jsp
<form action="/transfer" method="post">
  <input type="hidden" name="csrfToken" value="${csrfToken}">
  <input name="amount" type="number" min="1" required>
  <button type="submit">Transfer</button>
</form>
```

The token must be checked server-side. Client-side validation is not enough.

---

# 12. CSS

Likely conceptual and code themes: CSS attachment, selectors, cascade, specificity, inheritance, colors, typography, box model, display, positioning, float, Flexbox, Grid, viewport, and media queries.

## Question 12.1 - What is CSS, and how should it be attached?

**Answer.** CSS defines presentation: colors, typography, spacing, layout, and visual style. HTML should describe structure and meaning. The preferred attachment method is an external stylesheet linked in the `<head>`:

```html
<link rel="stylesheet" type="text/css" href="styles.css">
```

Use `href`, not `src`. External stylesheets are reusable and cacheable.

## Question 12.2 - Explain CSS selectors and specificity.

**Answer.** `p` selects all paragraphs. `.note` selects elements with class `note`. `p.note` selects paragraphs with class `note`. `#intro` selects the element with that id. `p a` selects all links inside paragraphs. `p > a` selects only direct child links.

Specificity priority is: inline style, ID selector, class/pseudo-class/attribute selector, type selector, and universal selector. If specificity is equal, later source order wins. `!important` overrides normal declarations, but should be used carefully.

## Question 12.3 - Explain the box model.

**Answer.** Every element is a box: content, padding, border, and margin. In the standard box model, `width` is content width only. Total occupied width includes left and right margin, border, padding, and content width.

Padding shorthand follows top-right-bottom-left order:

```css
p {
  padding: 10px 5px 20px 1px;
}
```

This means top `10px`, right `5px`, bottom `20px`, and left `1px`.

## Question 12.4 - Compare `display:none` and `visibility:hidden`.

**Answer.** `display: none` removes the element from layout. It is not visible and takes no space. `visibility: hidden` makes the element invisible but preserves its layout space.

## Question 12.5 - Write a responsive Flexbox layout.

**Answer.**

```css
.toolbar {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

@media only screen and (min-width: 40em) {
  .toolbar {
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
  }
}
```

Flexbox is one-dimensional. It arranges items along one main axis.

## Question 12.6 - Write a simple CSS Grid layout.

**Answer.**

```css
.employee-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1rem;
}

@media only screen and (min-width: 48em) {
  .employee-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}
```

Grid is two-dimensional: it manages rows and columns. Responsive design also needs:

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

---

# 13. JavaScript

Likely conceptual and code themes: JavaScript role, primitive types, objects, arrays, `forEach`, browser objects, DOM, node creation, events, `addEventListener`, and `preventDefault`.

## Question 13.1 - What is JavaScript's role in the Web stack?

**Answer.** HTML defines structure, CSS defines presentation, and JavaScript defines behavior and interactivity. In the browser, JavaScript can modify the DOM, react to events, schedule timers, show dialogs, and make scripted HTTP requests. Same-origin restrictions limit access to other origins.

## Question 13.2 - Explain JavaScript objects and arrays.

**Answer.** JavaScript objects are dynamic collections of properties, similar to associative arrays. A property can contain a value or a function. In a method call, `this` refers to the object receiving the call. Arrays are dynamic and heterogeneous: they can contain values of different types and can grow with methods such as `push`.

## Question 13.3 - Write JavaScript that creates and inserts a DOM node.

**Answer.**

```javascript
const container = document.getElementById("container");

const p = document.createElement("p");
const text = document.createTextNode("Employee created.");

p.appendChild(text);
container.appendChild(p);
```

The node is not visible until it is inserted into the document. `createTextNode` avoids parsing user text as HTML.

## Question 13.4 - Write a form event handler that blocks invalid submission.

**Answer.**

```javascript
const form = document.getElementById("employee-form");
const salary = document.getElementById("salary");

form.addEventListener("submit", function (event) {
  const value = Number(salary.value);

  if (!Number.isInteger(value) || value <= 0) {
    event.preventDefault();
    alert("Salary must be a positive integer.");
  }
});
```

`addEventListener` is preferred because it supports multiple handlers and keeps JavaScript separate from HTML. `preventDefault()` blocks the default form submission.

## Question 13.5 - Explain `confirm()`, `setTimeout`, and `setInterval`.

**Answer.** `confirm()` shows a dialog with OK and Cancel and returns a boolean. `setTimeout` schedules a callback once after a delay. `setInterval` schedules a callback repeatedly. Timers are asynchronous; they do not block the whole browser while waiting.

---

# 14. Form Validation and AJAX

Likely conceptual and code themes: client-side vs server-side validation, HTML5 validation attributes, Constraint Validation API, XHR lifecycle, request body encoding, CORS, JSON parsing/stringifying, and Fetch.

## Question 14.1 - Compare client-side and server-side validation.

**Answer.** Client-side validation gives fast feedback and improves user experience. It can be implemented with HTML5 attributes, CSS pseudo-classes, and JavaScript. Server-side validation is mandatory for security and correctness, because attackers can bypass the browser. Client-side validation helps usability; server-side validation is the authoritative gate.

## Question 14.2 - Write HTML5 validation attributes.

**Answer.**

```html
<input id="course"
       name="course"
       required
       pattern="Informatics|ICT|Cybersecurity">
```

`required` makes the field mandatory. `pattern` restricts accepted values.

## Question 14.3 - Write Constraint Validation API code.

**Answer.**

```javascript
const email = document.getElementById("email");

email.addEventListener("input", function () {
  if (email.validity.typeMismatch) {
    email.setCustomValidity("Please insert a valid email address.");
  } else {
    email.setCustomValidity("");
  }
});
```

A non-empty custom validity string marks the field invalid. An empty string clears the custom error.

## Question 14.4 - Write an `XMLHttpRequest` GET request.

**Answer.**

```javascript
const request = new XMLHttpRequest();

request.onload = function () {
  if (request.readyState === XMLHttpRequest.DONE &&
      request.status === 200) {
    console.log(request.responseText);
  }
};

request.open("GET", "employees.json");
request.send();
```

`readyState === 4` means complete. `status === 200` means successful HTTP response.

## Question 14.5 - Write a Fetch request that sends JSON.

**Answer.**

```javascript
const employee = {
  employee: {
    badge: 7309,
    surname: "Rossi",
    age: 34,
    salary: 45
  }
};

const response = await fetch("/rest/employee", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "Accept": "application/json"
  },
  body: JSON.stringify(employee)
});

if (response.ok) {
  const json = await response.json();
  console.log(json);
} else {
  console.error("HTTP error: " + response.status);
}
```

Use `JSON.stringify` to send JSON. Use `response.json()` to parse JSON. Do not use `eval()` for JSON.

## Question 14.6 - Explain CORS.

**Answer.** The same-origin policy normally prevents a script from reading responses from another origin. CORS lets the server explicitly allow cross-origin access through headers such as `Access-Control-Allow-Origin`. CORS is controlled by the server, not by the client alone.

---

# 15. jQuery and HTML5 Canvas

Likely conceptual and code themes: jQuery object, `$()`, getter/setter methods, chaining, `text()` vs `html()`, jQuery AJAX, canvas coordinates, rectangles, paths, images, transformations, and animation.

## Question 15.1 - What is a jQuery object?

**Answer.** A jQuery object is a set of zero or more DOM elements plus jQuery methods. It is not the same thing as a raw DOM element. `$()` can select existing elements, wrap DOM objects, or create new elements.

## Question 15.2 - Write jQuery code that changes all paragraphs to red.

**Answer.**

```javascript
$("p").css("color", "red");
```

`.css("color", "red")` is the correct setter. Setters usually return the jQuery object, so they support chaining.

## Question 15.3 - Compare `text()` and `html()` in jQuery.

**Answer.** `text()` treats content as text and is safer for user input. `html()` parses the string as HTML and can introduce XSS if the string is untrusted.

```javascript
$("#output").text(userInput);
```

This is safer than:

```javascript
$("#output").html(userInput);
```

## Question 15.4 - Write a jQuery AJAX request.

**Answer.**

```javascript
$.ajax({
  url: "/rest/employee",
  method: "GET",
  dataType: "json",
  success: function (data) {
    console.log(data);
  },
  error: function (xhr) {
    console.error("HTTP error: " + xhr.status);
  }
});
```

Shortcuts include `$.get`, `$.post`, `$.getJSON`, and `.load`.

## Question 15.5 - Write Canvas code that draws a rectangle and a path.

**Answer.**

```javascript
const canvas = document.getElementById("myCanvas");
const ctx = canvas.getContext("2d");

ctx.fillStyle = "lightblue";
ctx.fillRect(25, 25, 100, 80);

ctx.beginPath();
ctx.moveTo(160, 30);
ctx.lineTo(240, 30);
ctx.lineTo(240, 100);
ctx.closePath();
ctx.stroke();
```

Canvas coordinates start at the top-left corner. `x` grows right; `y` grows downward.

## Question 15.6 - Write Canvas image-loading and animation code.

**Answer.** Images must be drawn after loading. Animations should use `requestAnimationFrame`.

```javascript
const img = new Image();
let x = 0;

img.onload = function () {
  requestAnimationFrame(draw);
};

img.src = "picture.png";

function draw() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.drawImage(img, x, 20);
  x = (x + 2) % canvas.width;
  requestAnimationFrame(draw);
}
```

Use `save()` and `restore()` when transformations or styles should not affect later drawings.

---

# 16. Semantic Web and Linked Data

Likely conceptual and code themes: Web of Documents vs Web of Data, ontology, RDF, triples, URI vs literal, RDF serializations, Turtle, SPARQL, Linked Data principles, Linked Open Data, DBpedia, Wikidata, and FAIR.

## Question 16.1 - What is the Semantic Web?

**Answer.** The Semantic Web is the Web of Data: resources are connected through typed links so machines can interpret what data means. It extends the Web of Documents, where links mostly connect human-readable pages. Technologies include RDF, OWL, and SPARQL.

## Question 16.2 - Explain an RDF triple.

**Answer.** An RDF triple is a statement of the form `(subject, predicate, object)`. The subject is a URI identifying the resource being described. The predicate is a URI identifying the relationship. The object can be another URI or a literal value.

Example: Bob knows Alice can be represented as:

```text
<http://example.org/bob#me>
  <http://xmlns.com/foaf/0.1/knows>
  <http://example.org/alice#me>
```

## Question 16.3 - Write RDF data in Turtle.

**Answer.**

```turtle
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX schema: <http://schema.org/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

<http://example.org/bob#me>
  a foaf:Person ;
  foaf:name "Bob" ;
  foaf:knows <http://example.org/alice#me> ;
  schema:birthDate "1990-07-04"^^xsd:date .
```

In Turtle, `a` means `rdf:type`. Semicolon continues statements for the same subject.

## Question 16.4 - Write a SPARQL query that counts friends.

**Answer.**

```sparql
PREFIX foaf: <http://xmlns.com/foaf/0.1/>

SELECT ?name (COUNT(?friend) AS ?count)
WHERE {
  ?person foaf:name ?name .
  ?person foaf:knows ?friend .
}
GROUP BY ?person ?name
```

Variables start with `?`. The `WHERE` clause contains graph patterns. `GROUP BY` groups solutions before aggregation.

## Question 16.5 - Explain Linked Data and FAIR.

**Answer.** Linked Data principles are: use URIs as names for things; use HTTP URIs so they can be looked up; provide useful information using RDF/SPARQL when a URI is looked up; and include links to other URIs. Linked Open Data is Linked Data published under an open license.

FAIR means Findable, Accessible, Interoperable, and Reusable. Findable data has persistent identifiers and rich metadata. Accessible data can be retrieved through standard protocols. Interoperable data uses formal representations and shared vocabularies. Reusable data has clear licenses, provenance, and accurate attributes.

---

# Final Code Checklist

## Question C.1 - What must a DAO answer contain?

**Answer.** A strong DAO code answer contains:

- `Connection` received from outside, not opened inside the DAO;
- SQL stored in a constant;
- `PreparedStatement`, never string concatenation with user input;
- parameter binding with `setInt`, `setString`, and similar methods;
- `executeQuery()` for `SELECT`;
- `executeUpdate()` for `INSERT`, `UPDATE`, and `DELETE`;
- `ResultSet` mapping into resource objects;
- `try-with-resources` for statement and result set;
- `outputParam` plus `getOutputParam()`.

## Question C.2 - What must a servlet answer contain?

**Answer.** A strong servlet code answer contains:

- class extending `HttpServlet`;
- override of `doGet` or `doPost`;
- request parameters read from `HttpServletRequest`;
- response status/content type set on `HttpServletResponse`;
- local variables for request-specific data;
- no unsafe shared instance fields;
- DAO call or forward when needed;
- exceptions handled or wrapped in `ServletException`.

## Question C.3 - What must a JSP answer contain?

**Answer.** A strong JSP code answer contains:

- page directive with UTF-8 content type;
- JSTL taglib directive if using `<c:...>` tags;
- EL expressions reading request attributes or parameters;
- `<c:out>` for user-controlled output;
- no Java scriptlets;
- only view logic, not database logic.

## Question C.4 - What must a REST answer contain?

**Answer.** A strong REST answer contains:

- resource identified by URI;
- correct HTTP method;
- `Accept` and `Content-Type` distinction;
- JSON or XML representation;
- appropriate status code;
- stateless request handling;
- error response as structured resource when relevant.
