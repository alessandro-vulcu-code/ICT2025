# 08 — REST Web Services

_Source: `08-Webapp-2025-26-REST.pdf` — Web Applications, Master Degree, A.Y. 2025/2026, Prof. Nicola Ferro_

---

## Table of Contents

- [[#REST — The Architectural Paradigm|REST — The Architectural Paradigm]]
  - [[#Resources and URIs|Resources and URIs]]
  - [[#HTTP and REST — Uniform Interface|HTTP and REST — Uniform Interface]]
  - [[#Representations — XML, JSON, HTML|Representations — XML, JSON, HTML]]
  - [[#REST Design Principles|REST Design Principles]]
  - [[#API Documentation — WADL and OpenAPI|API Documentation — WADL and OpenAPI]]
- [[#Employee REST API|Employee REST API]]
  - [[#API Endpoints|API Endpoints]]
  - [[#JSON Resource Format|JSON Resource Format]]
  - [[#Error Codes|Error Codes]]
- [[#Implementation — Class Architecture|Implementation — Class Architecture]]
  - [[#Resource Interface and AbstractResource|Resource Interface and AbstractResource]]
  - [[#Employee — toJSON and fromJSON|Employee — toJSON and fromJSON]]
  - [[#ResourceList|ResourceList]]
  - [[#RestResource Interface and AbstractRR|RestResource Interface and AbstractRR]]
  - [[#checkMethodMediaType|checkMethodMediaType]]
  - [[#CreateEmployeeRR|CreateEmployeeRR]]
  - [[#CreateEmployeeDAO|CreateEmployeeDAO]]
  - [[#RestDispatcherServlet|RestDispatcherServlet]]
  - [[#AbstractDatabaseServlet|AbstractDatabaseServlet]]
  - [[#web.xml and Maven POM|web.xml and Maven POM]]
- [[#AJAX|AJAX]]
  - [[#XMLHttpRequest Pattern|XMLHttpRequest Pattern]]
  - [[#AJAX Employee JS Code|AJAX Employee JS Code]]
- [[#Summary Table|Summary Table]]

---

## REST — The Architectural Paradigm

> [!Important] REST: REpresentational State Transfer
> **REST** is an architectural paradigm that applies the architectural principles of the Web to Web services.
> - Network of **Web resources** where users proceed by following **links** (state transitions)
> - Each link provides the **representation** of the next resource (new state)
> - Features: **simplicity**, **statelessness**, **scalability**
> **Intuition:** REST treats everything as a resource accessible via URL; HTTP methods are the only operations.
![[Pasted image 20260512123223.png]]
### Resources and URIs

> [!Important] Resource
> - A **resource** is whatever has identity
> - Resources have a **state** that can change over time
> - Resources have a **URI** — unique and global identifier
> - Resources can transfer a **representation** of their state upon request
![[Pasted image 20260512123137.png]]

> [!Important] URI Templates
> REST uses URI templates to specify resource identification patterns:
> ```
> /student/{badge}/exam/{id}
> ```
> | Resource | URI |
> |----------|-----|
> | List of students | `/student` |
> | Student badge 123456 | `/student/123456` |
> | Exam "webapp" for student 123456 | `/student/123456/exam/webapp` |

### HTTP and REST — Uniform Interface

> [!Important] HTTP as REST's Uniform Interface
> - HTTP is **stateless** — each request must be self-explaining
> - HTTP provides a **uniform interface** via well-defined methods: `GET`, `POST`, `PUT`, `DELETE`
> - HTTP headers/body carry all needed information (no session state on server)

| HTTP Method | CRUD Operation | Example                                    |
| ----------- | -------------- | ------------------------------------------ |
| `POST`      | Create         | `POST /student` — creates new student      |
| `GET`       | Read           | `GET /student/123456` — reads student data |
| `PUT`       | Update         | `PUT /student/123456` — updates student    |
| `DELETE`    | Delete         | `DELETE /student/123456` — deletes student |

### Representations — XML, JSON, HTML

Same resource, multiple representations negotiated via `Accept` header:

> [!Example] XML Representation — GET /student
> ```
> GET /student HTTP/1.1
> Accept: application/xml
> ```
> ```xml
> <?xml version="1.0"?>
> <students xmlns:xlink="http://www.w3.org/1999/xlink">
>   <student badge="123456" xlink:href="http://.../student/123456" />
>   <student badge="123457" xlink:href="http://.../student/123457" />
> </students>
> ```

> [!Example] JSON Representation — GET /student/123456
> ```
> GET /student/123456 HTTP/1.1
> Accept: application/json
> ```
> ```json
> {
>    "student": {
>       "badge": 123456,
>       "name": "Mario",
>       "surname": "Rossi",
>       "exams": [
>          { "exam": { "id": "webapp", "link": "http://.../student/123456/exam/webapp" } },
>          { "exam": { "id": "dbms",   "link": "http://.../student/123456/exam/dbms" } }
>       ]
>    }
> }
> ```

> [!Example] HTML Representation — GET /student HTTP/1.1 Accept: text/html
> Returns an HTML table with badge + hyperlinks to each student's URI.

### REST Design Principles

1. Identify all **resources** to expose
2. Create a **URI** for each resource (prefer nouns, not verbs)
3. Determine which **HTTP methods** are needed for each resource
4. **Link** resources — unveil information by following links
5. Specify the **representation format** (possibly with a schema)
6. **Accurately document** all services

### API Documentation — WADL and OpenAPI

> [!Important] WADL — Web Application Description Language
> - Machine-readable **XML** description of HTTP-based (REST) web services
> - Submitted to W3C by Sun Microsystems on 31 August 2009
> - W3C has **no current plans to standardise** it
> ```xml
> <resources base="http://api.search.yahoo.com/NewsSearchService/V1/">
>   <resource path="newsSearch">
>     <method name="GET" id="search">
>       <request>
>         <param name="appid" type="xsd:string" style="query" required="true" />
>         <param name="query" type="xsd:string" style="query" required="true" />
>       </request>
>       <response status="200">
>         <representation mediatype="application/xml" element="yn:ResultSet" />
>       </response>
>     </method>
>   </resource>
> </resources>
> ```
> Reference: Hadley, M. (2009). *WADL — W3C Member Submission 31 August 2009*

> [!Important] OAI — OpenAPI Initiative
> - **YAML-based** description standard for REST APIs
> - Created by a consortium of industries under the **Linux Foundation**
> - Supersedes/competes with WADL as the de-facto standard
> ```yaml
> openapi: "3.0.0"
> info:
>   version: 1.0.0
>   title: Swagger Petstore
> paths:
>   /pets:
>     get:
>       summary: List all pets
>       operationId: listPets
>       responses:
>         '200':
>           description: An paged array of pets
>           content:
>             application/json:
>               schema:
>                 $ref: "#/components/schemas/Pets"
>   /pets/{petId}:
>     get:
>       summary: Info for a specific pet
>       parameters:
>         - name: petId
>           in: path
>           required: true
>           schema:
>             type: string
> ```

---

## Employee REST API

### API Endpoints

| URI | Method | Description |
|-----|--------|-------------|
| `/rest/employee` | `GET` | List all employees |
| `/rest/employee` | `POST` | Create a new employee |
| `/rest/employee/{badge}` | `GET` | Read employee by badge |
| `/rest/employee/{badge}` | `PUT` | Update employee by badge |
| `/rest/employee/{badge}` | `DELETE` | Delete employee by badge |
| `/rest/employee/salary/{salary}` | `GET` | Search employees with salary above threshold |

### JSON Resource Format

Three JSON resource types used across the API:

> [!Example] Employee Resource
> ```json
> {
>    "employee": {
>       "badge": 7309,
>       "surname": "Rossi",
>       "age": 34,
>       "salary": 45
>    }
> }
> ```

> [!Example] Message Resource (error/info response)
> ```json
> {
>    "message": {
>       "message": "Unsupported operation.",
>       "error-code": "E500",
>       "error-details": "OPTIONS"
>    }
> }
> ```

> [!Example] ResourceList (collection of employees)
> ```json
> {
>    "resource-list": [
>       { "employee": { "badge": 7309, "surname": "Rossi", "age": 34, "salary": 45 } },
>       { "employee": { "badge": 4076, "surname": "Mori",  "age": 45, "salary": 50 } }
>    ]
> }
> ```

### Error Codes

**Client-side errors (4xx):**

| Error Code | HTTP Status | Status Text | Cause |
|------------|-------------|-------------|-------|
| `E4A1` | 400 | Bad Request | `Accept` header missing (output media type not specified) |
| `E4A2` | 406 | Not Acceptable | Unsupported output media type |
| `E4A3` | 400 | Bad Request | `Content-Type` header missing (input media type not specified) |
| `E4A4` | 415 | Unsupported Media Type | Unsupported input media type |
| `E4A5` | 405 | Method Not Allowed | Unsupported HTTP operation |
| `E4A6` | 404 | Not Found | Unknown resource requested |
| `E4A7` | 400 | Bad Request | Wrong URI format |
| `E4A8` | 400 | Bad Request | Wrong resource provided (e.g., malformed JSON body) |

**Server-side errors (5xx):**

| Error Code | HTTP Status | Status Text | Cause |
|------------|-------------|-------------|-------|
| `E5A1` | 500 | Internal Server Error | Unexpected error while processing resource |
| `E5A2` | 409 | Conflict | Resource already exists (PostgreSQL SQLState `23505`) |
| `E5A3` | 404 | Not Found | Resource not found |
| `E5A4` | 409 | Conflict | Cannot modify — other resources depend on it |

---

## Implementation — Class Architecture

![[rest-employee-class-diagram.jpg]]

*Figure: Full UML class diagram — Resource hierarchy, RR hierarchy, DAO hierarchy, RestDispatcherServlet.*

![[rest-create-employee-sequence.jpg]]

*Figure: CREATE sequence — `POST /rest/employee` → `RestDispatcherServlet` → `CreateEmployeeRR` → `CreateEmployeeDAO` → DB → JSON response.*

### Resource Interface and AbstractResource

![[rest-resource-interface.jpg]]

*Figure: `Resource` interface — single method `void toJSON(OutputStream out) throws IOException`.*

> [!Important] Resource Interface
> ```java
> public interface Resource {
>     void toJSON(OutputStream out) throws IOException;
> }
> ```
> All JSON-serialisable domain objects implement `Resource`. `toJSON()` writes JSON to any `OutputStream` (e.g., `res.getOutputStream()`).

> [!Example] AbstractResource — JSON Factory Setup
> ```java
> public abstract class AbstractResource implements Resource {
>
>     protected static final JsonFactory JSON_FACTORY;
>
>     static {
>         JSON_FACTORY = new JsonFactory();
>         JSON_FACTORY.disable(JsonGenerator.Feature.AUTO_CLOSE_TARGET);
>         JSON_FACTORY.disable(JsonParser.Feature.AUTO_CLOSE_SOURCE);
>     }
>
>     @Override
>     public void toJSON(final OutputStream out) throws IOException {
>         if (out == null) throw new IOException("The output stream cannot be null.");
>         try {
>             writeJSON(out);
>         } catch (Exception e) {
>             throw new IOException("Unable to serialize the resource to JSON.", e);
>         }
>     }
>
>     protected abstract void writeJSON(OutputStream out) throws Exception;
> }
> ```
> **Key points:**
> - `AUTO_CLOSE_TARGET` disabled — factory does not close the servlet's response stream
> - `AUTO_CLOSE_SOURCE` disabled — factory does not close the request's input stream
> - `writeJSON()` is the template method subclasses implement

### Employee — toJSON and fromJSON

> [!Example] Employee.writeJSON — serialise to JSON
> Subclass of `AbstractResource`. `writeJSON()` creates a `JsonGenerator` and writes fields step-by-step:
> ```java
> final JsonGenerator jg = JSON_FACTORY.createGenerator(out);
> jg.writeStartObject();
> jg.writeFieldName("employee");
> jg.writeStartObject();
> jg.writeNumberField("badge",   badge);
> jg.writeStringField("surname", surname);
> jg.writeNumberField("age",     age);
> jg.writeNumberField("salary",  salary);
> jg.writeEndObject();
> jg.writeEndObject();
> jg.flush();
> ```

> [!Example] Employee.fromJSON — parse from request body
> Static factory method; uses `JsonParser` to read the incoming request `InputStream`:
> ```java
> public static Employee fromJSON(final InputStream in) throws IOException {
>     int jBadge = -1; String jSurname = null; int jAge = -1; int jSalary = -1;
>
>     final JsonParser jp = JSON_FACTORY.createParser(in);
>
>     // advance until "employee" field name
>     while (jp.getCurrentToken() != JsonToken.FIELD_NAME || !"employee".equals(jp.getCurrentName())) {
>         if (jp.nextToken() == null)
>             throw new EOFException("Unable to parse JSON: no Employee object found.");
>     }
>
>     // read fields inside employee object
>     while (jp.nextToken() != JsonToken.END_OBJECT) {
>         if (jp.getCurrentToken() == JsonToken.FIELD_NAME) {
>             switch (jp.getCurrentName()) {
>                 case "badge":   jp.nextToken(); jBadge   = jp.getIntValue();  break;
>                 case "surname": jp.nextToken(); jSurname = jp.getText();       break;
>                 case "age":     jp.nextToken(); jAge     = jp.getIntValue();  break;
>                 case "salary":  jp.nextToken(); jSalary  = jp.getIntValue();  break;
>             }
>         }
>     }
>     return new Employee(jBadge, jSurname, jAge, jSalary);
> }
> ```
> **Note:** `EOFException` thrown when the `"employee"` token is never found — caught in `CreateEmployeeRR` as `E4A8`.

### ResourceList

> [!Example] ResourceList — generic collection serialiser
> ```java
> public final class ResourceList<T extends Resource> extends AbstractResource {
>
>     private final Iterable<T> list;
>
>     @Override
>     protected void writeJSON(final OutputStream out) throws IOException {
>         final JsonGenerator jg = JSON_FACTORY.createGenerator(out);
>         jg.writeStartObject();
>         jg.writeFieldName("resource-list");
>         jg.writeStartArray();
>         jg.flush();
>
>         boolean firstElement = true;
>         for (final Resource r : list) {
>             if (firstElement) {
>                 r.toJSON(out); jg.flush();
>                 firstElement = false;
>             } else {
>                 jg.writeRaw(','); jg.flush();
>                 r.toJSON(out);   jg.flush();
>             }
>         }
>
>         jg.writeEndArray();
>         jg.writeEndObject();
>         jg.flush();
>     }
> }
> ```
> **Note:** Each resource writes itself via `toJSON(out)` directly; `jg.writeRaw(',')` manually injects array separators because each element uses its own generator instance flushing to the same stream.

### RestResource Interface and AbstractRR

![[rest-restresource-interface.jpg]]

*Figure: `RestResource` interface — single method `void serve() throws IOException`.*

> [!Important] RestResource Interface
> ```java
> public interface RestResource {
>     void serve() throws IOException;
> }
> ```
> Each concrete REST resource (RR) handles one or more HTTP methods for one API endpoint.

> [!Example] AbstractRR — constructor and serve()
> ```java
> public abstract class AbstractRR implements RestResource {
>
>     protected static final String JSON_MEDIA_TYPE      = "application/json";
>     protected static final String JSON_UTF_8_MEDIA_TYPE = "application/json; charset=utf-8";
>     protected static final String ALL_MEDIA_TYPE        = "*/*";
>
>     protected final HttpServletRequest  req;
>     protected final HttpServletResponse res;
>     protected final Connection          con;
>     private   final String              action;
>
>     protected AbstractRR(String action, HttpServletRequest req, HttpServletResponse res, Connection con) {
>         this.action = action;
>         LogContext.setAction(action);
>         this.req = req; this.res = res; this.con = con;
>     }
>
>     @Override
>     public void serve() throws IOException {
>         try {
>             if (!checkMethodMediaType(req, res)) return;
>             doServe();
>         } catch (Throwable t) {
>             final Message m = new Message(
>                 String.format("Unable to serve the REST request: %s.", action), "E5A1", t.getMessage());
>             res.setStatus(HttpServletResponse.SC_INTERNAL_SERVER_ERROR);
>             m.toJSON(res.getOutputStream());
>         } finally {
>             LogContext.removeAction();
>             LogContext.removeResource();
>         }
>     }
>
>     protected abstract void doServe() throws IOException;
> }
> ```

### checkMethodMediaType

> [!Important] checkMethodMediaType — validation logic
> Called at start of every `serve()`. Validates `Accept` and `Content-Type` headers, returns `false` (and writes error JSON) if invalid.
> ```
> Accept header missing?          → E4A1, 400
> Accept not JSON or */*?         → E4A2, 406
> Method = GET or DELETE:         → OK (no body expected)
> Method = POST or PUT:
>   Content-Type missing?         → E4A3, 400
>   Content-Type not JSON?        → E4A4, 415
> Method = anything else:         → E4A5, 405
> ```
> Subclasses may override `checkMethodMediaType` to implement method-specific behaviour.

### CreateEmployeeRR

> [!Example] CreateEmployeeRR.doServe()
> ```java
> public final class CreateEmployeeRR extends AbstractRR {
>
>     public CreateEmployeeRR(HttpServletRequest req, HttpServletResponse res, Connection con) {
>         super(Actions.CREATE_EMPLOYEE, req, res, con);
>     }
>
>     @Override
>     protected void doServe() throws IOException {
>         Employee e = null; Message m = null;
>         try {
>             final Employee employee = Employee.fromJSON(req.getInputStream());
>             LogContext.setResource(Integer.toString(employee.getBadge()));
>
>             e = new CreateEmployeeDAO(con, employee).access().getOutputParam();
>
>             if (e != null) {
>                 res.setStatus(HttpServletResponse.SC_CREATED);   // 201
>                 e.toJSON(res.getOutputStream());
>             } else {
>                 m = new Message("Cannot create the employee: unexpected error.", "E5A1", null);
>                 res.setStatus(HttpServletResponse.SC_INTERNAL_SERVER_ERROR);
>                 m.toJSON(res.getOutputStream());
>             }
>         } catch (EOFException ex) {
>             m = new Message("Cannot create the employee: no Employee JSON object found in the request.",
>                             "E4A8", ex.getMessage());
>             res.setStatus(HttpServletResponse.SC_BAD_REQUEST);
>             m.toJSON(res.getOutputStream());
>         } catch (SQLException ex) {
>             if ("23505".equals(ex.getSQLState())) {
>                 m = new Message("Cannot create the employee: it already exists.", "E5A2", ex.getMessage());
>                 res.setStatus(HttpServletResponse.SC_CONFLICT);  // 409
>             } else {
>                 m = new Message("Cannot create the employee: unexpected database error.", "E5A1", ex.getMessage());
>                 res.setStatus(HttpServletResponse.SC_INTERNAL_SERVER_ERROR);
>             }
>             m.toJSON(res.getOutputStream());
>         }
>     }
> }
> ```
> **SQLState `23505`** = PostgreSQL unique constraint violation → resource already exists → `E5A2 / 409`.

### CreateEmployeeDAO

> [!Example] CreateEmployeeDAO — INSERT with RETURNING *
> ```java
> public final class CreateEmployeeDAO extends AbstractDAO<Employee> {
>
>     private static final String STATEMENT =
>         "INSERT INTO Ferro.Employee (badge, surname, age, salary) VALUES (?, ?, ?, ?) RETURNING *";
>
>     private final Employee employee;
>
>     public CreateEmployeeDAO(Connection con, Employee employee) {
>         super(con);
>         this.employee = employee;
>     }
>
>     @Override
>     protected final void doAccess() throws SQLException {
>         PreparedStatement pstmt = null;
>         Employee e = null;
>         try {
>             pstmt = con.prepareStatement(STATEMENT);
>             pstmt.setInt(1,    employee.getBadge());
>             pstmt.setString(2, employee.getSurname());
>             pstmt.setInt(3,    employee.getAge());
>             pstmt.setInt(4,    employee.getSalary());
>
>             ResultSet rs = pstmt.executeQuery();
>             if (rs.next()) {
>                 e = new Employee(rs.getInt("badge"), rs.getString("surname"),
>                                  rs.getInt("age"),   rs.getInt("salary"));
>             }
>         } finally {
>             if (pstmt != null) pstmt.close();
>         }
>         outputParam = e;
>     }
> }
> ```

> [!Important] PostgreSQL `RETURNING *`
> `RETURNING *` is a **PostgreSQL extension** to standard SQL. It returns the inserted row as a `ResultSet` immediately after the `INSERT`, allowing the application to read the stored state (e.g., DB-generated defaults) without a second SELECT.
> - `executeQuery()` used (not `executeUpdate()`) because `RETURNING` produces a result set
> - The created `Employee` is set as `outputParam` → retrieved via `dao.getOutputParam()`

### RestDispatcherServlet

![[rest-dispatcher-service-code.jpg]]

*Figure: `RestDispatcherServlet.service()` — overrides `service()` (not `doGet/doPost`) to handle all HTTP methods; routes to `processEmployee()`, or returns `E4A6` for unknown resources.*

![[rest-process-employee-routing.jpg]]

*Figure: `processEmployee()` — matches URI patterns against `/rest/employee` variants; delegates to the appropriate RR (e.g., `ListEmployeeRR`, `CreateEmployeeRR`). Returns if no pattern matched.*

> [!Important] RestDispatcherServlet — design
> - Extends `AbstractDatabaseServlet` (inherits JNDI connection pool)
> - **Overrides `service()`** instead of `doGet/doPost` — necessary to handle `PUT`, `DELETE`, and other methods
> - Routing logic:
>   1. Check if URI is under `/rest/employee` → call `processEmployee(req, res)`
>   2. If no route matched → write `E4A6 / 404` (unknown resource)
>   3. Always flush and close response output stream in `finally`
> - `processEmployee()` matches URI patterns in priority order:
>   - `GET /rest/employee` → `ListEmployeeRR`
>   - `POST /rest/employee` → `CreateEmployeeRR`
>   - `GET /rest/employee/{badge}` → `ReadEmployeeRR`
>   - `PUT /rest/employee/{badge}` → `UpdateEmployeeRR`
>   - `DELETE /rest/employee/{badge}` → `DeleteEmployeeRR`
>   - `GET /rest/employee/salary/{salary}` → `SearchEmployeeBySalaryRR`
> - Each RR instantiated with `(req, res, con)` and `.serve()` called

### AbstractDatabaseServlet

> [!Example] AbstractDatabaseServlet (same as servlet-database lecture)
> ```java
> public abstract class AbstractDatabaseServlet extends HttpServlet {
>     private DataSource ds;
>
>     public void init(ServletConfig config) throws ServletException {
>         try {
>             InitialContext cxt = new InitialContext();
>             ds = (DataSource) cxt.lookup("java:/comp/env/jdbc/employee-ferro");
>         } catch (NamingException e) {
>             ds = null;
>             throw new ServletException("Unable to acquire the connection pool to the database", e);
>         }
>     }
>
>     public void destroy() { ds = null; }
>
>     protected final Connection getConnection() throws SQLException {
>         return ds.getConnection();
>     }
> }
> ```

### web.xml and Maven POM

> [!Example] web.xml — route all /rest/* to RestDispatcherServlet
> Every request under `/rest` is forwarded to `RestDispatcherServlet`:
> ```xml
> <servlet>
>   <servlet-name>RestDispatcherServlet</servlet-name>
>   <servlet-class>it.unipd.dei.webapp.rest.RestDispatcherServlet</servlet-class>
> </servlet>
> <servlet-mapping>
>   <servlet-name>RestDispatcherServlet</servlet-name>
>   <url-pattern>/rest/*</url-pattern>
> </servlet-mapping>
> ```

> [!Example] Maven POM — Jackson dependency
> Jackson must NOT have `provided` scope (it is not bundled with Tomcat):
> ```xml
> <dependency>
>     <groupId>com.fasterxml.jackson.core</groupId>
>     <artifactId>jackson-core</artifactId>
>     <version>2.x.x</version>
>     <!-- no <scope>provided</scope> -->
> </dependency>
> ```

---

## AJAX

> [!Important] AJAX — Asynchronous JavaScript and XML
> **AJAX** allows web pages to send HTTP requests and update the DOM without full page reloads.
> - Uses `XMLHttpRequest` (XHR) object
> - Response body parsed with `JSON.parse()`
> - DOM updated programmatically via `document.createElement()` / `appendChild()`
> - Decouples the REST API call from the page lifecycle

### XMLHttpRequest Pattern

```
1. Get form input value
2. Build request URL (append parameters)
3. Create XMLHttpRequest object
4. Set xhr.onreadystatechange = processResponse callback
5. xhr.open("GET", url, true)   // async = true
6. xhr.send()
```

```
processResponse(xhr):
  if xhr.readyState !== XMLHttpRequest.DONE → return
  get result div
  div.replaceChildren()          // clear previous results
  if xhr.status !== 200 → write error text, return
  const resourceList = JSON.parse(xhr.responseText)["resource-list"]
  for each item in resourceList:
      let employee = item.employee
      create <tr> with <td> for badge, surname, age, salary
      append to table → append to div
```

### AJAX Employee JS Code

![[rest-ajax-event-listener.jpg]]

*Figure: Event listener registration — `document.getElementById("ajaxButton").addEventListener("click", searchEmployeeBySalary)`.*

![[rest-ajax-xhr-request.jpg]]

*Figure: `searchEmployeeBySalary()` — reads salary field, builds URL, creates `XMLHttpRequest`, sets `onreadystatechange`, calls `xhr.open()` + `xhr.send()`.*

> [!Warning] Client-side Input Not Validated
> Slide 52 explicitly notes `[not safe enough, validation!]` — salary value read from form is appended directly to the URL without sanitisation. Always validate/encode user input before constructing request URLs.

![[rest-ajax-process-response.jpg]]

*Figure: `processResponse(xhr)` — checks `readyState === DONE`, handles non-200 status, builds HTML table node-by-node.*

![[rest-ajax-json-parse-dom.jpg]]

*Figure: JSON parsing — `JSON.parse(xhr.responseText)["resource-list"]`; iteration over array with `resourceList[i].employee`; `createElement("td")` + `createTextNode(employee["badge"])` for each field.*

> [!Example] Full AJAX JS skeleton
> ```javascript
> // setup
> document.getElementById("ajaxButton")
>         .addEventListener("click", searchEmployeeBySalary);
>
> function searchEmployeeBySalary() {
>     const salary = document.getElementById("salaryID").value;
>     const url    = "http://localhost:8080/employee-rest-ajax-1.00/rest/employee/salary/" + salary;
>
>     const xhr = new XMLHttpRequest();
>     if (!xhr) { alert("Cannot create XMLHttpRequest."); return false; }
>
>     xhr.onreadystatechange = function () { processResponse(this); };
>     xhr.open("GET", url, true);
>     xhr.send();
> }
>
> function processResponse(xhr) {
>     if (xhr.readyState !== XMLHttpRequest.DONE) return;
>
>     const div = document.getElementById("results");
>     div.replaceChildren();
>
>     if (xhr.status !== 200) {
>         div.appendChild(document.createTextNode("Unable to perform the AJAX request."));
>         return;
>     }
>
>     const table = document.createElement("table");
>     div.appendChild(table);
>
>     const e = document.createElement("tbody");
>     table.appendChild(e);
>
>     const resourceList = JSON.parse(xhr.responseText)["resource-list"];
>     for (let i = 0; i < resourceList.length; i++) {
>         let employee = resourceList[i].employee;
>         let ee = document.createElement("tr");
>         e.appendChild(ee);
>         // badge cell
>         let eee = document.createElement("td");
>         eee.appendChild(document.createTextNode(employee["badge"]));
>         ee.appendChild(eee);
>         // surname, age, salary — same pattern
>     }
> }
> ```

---

## Summary Table

| Component | Type | Role | Key Detail |
|-----------|------|------|------------|
| `Resource` | Interface | JSON-serialisable object | `toJSON(OutputStream)` |
| `AbstractResource` | Abstract class | Manages `JsonFactory`, delegates to `writeJSON()` | Disables auto-close on streams |
| `Employee` | Concrete resource | Domain object; JSON ↔ Java | `fromJSON()` static parser; `writeJSON()` serialiser |
| `Message` | Concrete resource | Error/info response | Fields: `message`, `error-code`, `error-details` |
| `ResourceList<T>` | Concrete resource | Collection wrapper | `writeRaw(',')` hack for array separators |
| `RestResource` | Interface | REST request handler | `void serve() throws IOException` |
| `AbstractRR` | Abstract class | Validates headers, wraps `doServe()`, catches `Throwable` | `checkMethodMediaType()` |
| `CreateEmployeeRR` | Concrete RR | POST /rest/employee | Parses JSON body → DAO → 201 or error |
| `RestDispatcherServlet` | Servlet | Front controller for REST | Overrides `service()`; routes to RR by URI+method |
| `AbstractDatabaseServlet` | Abstract servlet | JNDI connection pool | `init()` JNDI lookup; `getConnection()` |
| `CreateEmployeeDAO` | DAO | INSERT employee | `RETURNING *` → sets `outputParam` |
| `XMLHttpRequest` | Browser API | Async HTTP from client | `onreadystatechange`, `readyState === DONE` |
| WADL | XML format | REST API description | W3C submission 2009, not standardised |
| OpenAPI (OAI) | YAML format | REST API description | Linux Foundation standard, de-facto |
| `application/json` | MIME type | JSON media type | Required in `Accept` + `Content-Type` for POST/PUT |
