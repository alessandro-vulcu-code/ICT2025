# Java Servlets and Access to the Database

## Table of Contents

- [[#Overall Architecture|Overall Architecture]]
  - [[#Full-Stack Technology Stack|Full-Stack Technology Stack]]
  - [[#Application Layers|Application Layers]]
- [[#Resource Classes (Java Beans)|Resource Classes (Java Beans)]]
  - [[#The Employee Class|The Employee Class]]
  - [[#The Message Class|The Message Class]]
  - [[#The Employee Database Schema|The Employee Database Schema]]
- [[#The Data Access Object (DAO) Pattern|The Data Access Object (DAO) Pattern]]
  - [[#DataAccessObject Interface|DataAccessObject Interface]]
  - [[#AbstractDAO Class|AbstractDAO Class]]
  - [[#CreateEmployeeDAO|CreateEmployeeDAO]]
  - [[#SearchEmployeeBySalaryDAO|SearchEmployeeBySalaryDAO]]
- [[#Connection Pool via Tomcat|Connection Pool via Tomcat]]
  - [[#context.xml Configuration|context.xml Configuration]]
  - [[#web.xml Resource Reference|web.xml Resource Reference]]
  - [[#Maven POM Dependencies|Maven POM Dependencies]]
- [[#Servlet Layer|Servlet Layer]]
  - [[#AbstractDatabaseServlet|AbstractDatabaseServlet]]
  - [[#CreateEmployeeServlet|CreateEmployeeServlet]]
  - [[#SearchEmployeeBySalaryServlet|SearchEmployeeBySalaryServlet]]
- [[#Sequence Diagrams|Sequence Diagrams]]
- [[#SQL Injection|SQL Injection]]
- [[#Summary Table|Summary Table]]

---

## Overall Architecture

### Full-Stack Technology Stack

Full-stack web applications combine multiple layers. The course uses:

- **Client tier**: HTML5, CSS3, JavaScript (jQuery, AJAX)
- **Web tier**: Java Servlets, JSP
- **API layer**: REST (JSON), SOAP
- **Database tier**: *PostgreSQL*
- **Infrastructure**: Docker, Maven, Tomcat

### Application Layers

The architecture is split into three logical layers:

1. **Interface/Business Logic Layer** — Servlets handle HTTP, parse parameters, call DAOs, write HTML responses
2. **Data Logic Layer** — DAO classes encapsulate all SQL; no SQL outside DAO classes
3. **Data Layer** — PostgreSQL DBMS

![[PLACEHOLDER_Fig_1 — overall architecture layer diagram]]

The application demonstrates two features:
- **Create Employee**: POST form → servlet → DAO → INSERT into DB
- **Search Employee by Salary**: POST form → servlet → DAO → SELECT → return list

---

## Resource Classes (Java Beans)

Resource classes (**Java Beans**) represent domain objects. They live in `it.unipd.dei.webapp.resource`. They are **immutable** — all fields are `final`, only getters, no setters.

### The Employee Class

```java
package it.unipd.dei.webapp.resource;

public class Employee {

    private final int badge;
    private final String surname;
    private final int age;
    private final int salary;

    public Employee(final int badge, final String surname, final int age, final int salary) {
        this.badge = badge;
        this.surname = surname;
        this.age = age;
        this.salary = salary;
    }

    public final int getBadge()      { return badge; }
    public final String getSurname() { return surname; }
    public final int getAge()        { return age; }
    public final int getSalary()     { return salary; }
}
```

**Key design**: fields are `final` → immutable after construction. Accessor methods are also `final` → subclasses cannot override them.

### The Message Class

```java
package it.unipd.dei.webapp.resource;

public class Message {

    private final String message;
    private final String errorCode;
    private final String errorDetails;
    private final boolean isError;

    // Constructor for error messages
    public Message(final String message, final String errorCode, final String errorDetails) {
        this.message = message;
        this.errorCode = errorCode;
        this.errorDetails = errorDetails;
        this.isError = true;
    }

    // Constructor for informative (non-error) messages
    public Message(final String message) {
        this.message = message;
        this.errorCode = null;
        this.errorDetails = null;
        this.isError = false;
    }

    public final String getMessage()      { return message; }
    public final String getErrorCode()    { return errorCode; }
    public final String getErrorDetails() { return errorDetails; }
    public final boolean isError()        { return isError; }
}
```

`Message` is used by servlets to carry either success info or structured error info (code + details) to the view.

### The Employee Database Schema

```
Employee(Badge PK, Surname, Age, Salary)
Manage(Manager FK→Employee.Badge, Employee FK→Employee.Badge)
```

Sample data:

| Badge | Surname | Age | Salary |
|-------|---------|-----|--------|
| 7309  | Rossi   | 34  | 45     |
| 5998  | Bianchi | 37  | 38     |
| 9553  | Neri    | 42  | 35     |
| 5698  | Bruni   | 43  | 42     |
| 4076  | Mori    | 45  | 50     |
| 8123  | Lupi    | 46  | 60     |

---

## The Data Access Object (DAO) Pattern

> [!Important] DAO Pattern
> The **Data Access Object (DAO)** pattern abstracts and encapsulates all logic needed to access a data source (typically a relational DB). Benefits:
> - Decouples business logic from persistence logic
> - Each DAO is responsible for the persistence of **one resource** (e.g., `Employee`)
> - All DAOs implement a **common interface** → uniform usage; enables automation via reflection
>
> **Intuition:** Servlets never write SQL. They instantiate a DAO, call `access()`, and get results via `getOutputParam()`.

### DataAccessObject Interface

![[db-dao-interface.jpg]]

```java
public interface DataAccessObject<T> {

    /**
     * Accesses the database.
     * @return reference to this DataAccessObject (for chaining)
     * @throws SQLException if something goes wrong
     */
    DataAccessObject<T> access() throws SQLException;

    /**
     * Retrieves any output parameters after the database access.
     * @return output parameter, or null if none
     */
    T getOutputParam();
}
```

- `T` = type of the output parameter (e.g., `List<Employee>`, or `Void`)
- `access()` performs the operation and returns `this` (enabling chaining: `.access().getOutputParam()`)
- `getOutputParam()` retrieves the result after `access()` completes

### AbstractDAO Class

![[db-abstract-dao.jpg]]

`AbstractDAO<T>` provides the base implementation:

| Member | Role |
|--------|------|
| `LOGGER` | Log4J logger |
| `con` | JDBC `Connection` (injected via constructor) |
| `outputParam : T` | Stores the result of `doAccess()` |
| `accessed : boolean` | Guards against double-execution |
| `lock : Object` | Synchronization object |
| `access()` | Calls `doAccess()`, always closes the connection, rolls back on error |
| `doAccess()` | **Abstract** — subclasses implement the actual SQL logic |
| `getOutputParam()` | Returns `outputParam` after `access()` |

Key design decisions:
- **One-shot**: DAO objects are not meant to be reused; `accessed` flag prevents re-use
- **Connection lifetime**: `access()` always closes the connection in `finally`, even on error
- **Rollback**: `access()` rolls back the transaction if `doAccess()` throws
- **Thread safety**: `lock` and `accessed` guard against misuse (e.g., shared DAO reference)

### CreateEmployeeDAO

```java
public final class CreateEmployeeDAO extends AbstractDAO {

    private static final String STATEMENT =
        "INSERT INTO Ferro.Employee (badge, surname, age, salary) VALUES (?, ?, ?, ?)";

    private final Employee employee;

    public CreateEmployeeDAO(final Connection con, final Employee employee) {
        super(con);
        if (employee == null) {
            LOGGER.error("The employee cannot be null.");
            throw new NullPointerException("The employee cannot be null.");
        }
        this.employee = employee;
    }

    @Override
    protected final void doAccess() throws SQLException {
        PreparedStatement pstmt = null;
        try {
            pstmt = con.prepareStatement(STATEMENT);
            pstmt.setInt(1, employee.getBadge());
            pstmt.setString(2, employee.getSurname());
            pstmt.setInt(3, employee.getAge());
            pstmt.setInt(4, employee.getSalary());
            pstmt.execute();
            LOGGER.info("Employee %d successfully stored in the database.", employee.getBadge());
        } finally {
            if (pstmt != null) pstmt.close();
        }
    }
}
```

- No generic type parameter (no output) — extends `AbstractDAO` without `<T>`
- Uses `PreparedStatement` with `?` placeholders — **prevents SQL injection**
- Closes `PreparedStatement` in `finally`; connection closed by `AbstractDAO.access()`

### SearchEmployeeBySalaryDAO

```java
public final class SearchEmployeeBySalaryDAO extends AbstractDAO<List<Employee>> {

    private static final String STATEMENT =
        "SELECT badge, surname, age, salary FROM Ferro.Employee WHERE salary > ?";

    private final int salary;

    public SearchEmployeeBySalaryDAO(final Connection con, final int salary) {
        super(con);
        this.salary = salary;
    }

    @Override
    public final void doAccess() throws SQLException {
        PreparedStatement pstmt = null;
        ResultSet rs = null;
        final List<Employee> employees = new ArrayList<Employee>();

        try {
            pstmt = con.prepareStatement(STATEMENT);
            pstmt.setInt(1, salary);
            rs = pstmt.executeQuery();

            while (rs.next()) {
                employees.add(new Employee(
                    rs.getInt("badge"),
                    rs.getString("surname"),
                    rs.getInt("age"),
                    rs.getInt("salary")
                ));
            }
            LOGGER.info("Employee(s) with salary above %d successfully listed.", salary);
        } finally {
            if (rs != null)    rs.close();
            if (pstmt != null) pstmt.close();
        }

        this.outputParam = employees;  // set AFTER finally block
    }
}
```

- Generic parameter `<List<Employee>>` — `getOutputParam()` returns the list
- Iterates `ResultSet`, maps each row to an `Employee` object
- `outputParam` set **after** `finally` — closed resources are not accessed again

---

## Connection Pool via Tomcat

> [!Important] Connection Pool
> Opening a new JDBC connection per request is expensive (TCP handshake, authentication, protocol negotiation). A **connection pool** maintains a set of pre-opened connections that are lent to requests and returned after use.
>
> Tomcat manages the pool; servlets obtain connections via **JNDI** (*Java Naming and Directory Interface*) lookup.
>
> **Intuition:** Pool = shared parking lot of DB connections. Servlet borrows one, uses it, returns it.

### context.xml Configuration

`context.xml` is placed in `src/main/webapp/META-INF/` and is copied to the WAR's `META-INF/` folder by Maven.

```xml
<Context>
  <Resource name="jdbc/employee-ferro"
            auth="Container"
            type="javax.sql.DataSource"
            factory="org.apache.tomcat.jdbc.pool.DataSourceFactory"
            driverClassName="org.postgresql.Driver"
            url="jdbc:postgresql://localhost:5432/esami"
            username="ferro"
            password="ferro"
            testOnBorrow="true"
            validationQuery="SELECT 1"
            timeBetweenEvictionRunsMillis="30000"
            maxActive="10"
            minIdle="5"
            maxWait="10000"
            initialSize="2"
            removeAbandonedTimeout="60"
            removeAbandoned="true"
            closeMethod="close"
  />
</Context>
```

| Parameter | Meaning |
|-----------|---------|
| `name` | JNDI name used to look up the pool (`java:/comp/env/jdbc/employee-ferro`) |
| `auth="Container"` | Tomcat authenticates using the provided credentials |
| `type` | Java type returned by lookup — `javax.sql.DataSource` |
| `factory` | Tomcat JDBC pool factory class |
| `driverClassName` | PostgreSQL JDBC driver |
| `url` | JDBC URL: `jdbc:postgresql://host:port/db` |
| `username` / `password` | DB credentials |
| `testOnBorrow` | Validate connection before lending it out |
| `validationQuery` | Query used to validate (`SELECT 1`) |
| `timeBetweenEvictionRunsMillis` | How often idle connections are checked (ms) |
| `maxActive` | Max connections in the pool |
| `minIdle` | Minimum idle connections kept alive |
| `maxWait` | Max ms to wait for a connection before throwing exception |
| `initialSize` | Connections created at pool startup |
| `removeAbandoned` | Reclaim connections not returned within timeout |
| `removeAbandonedTimeout` | Seconds before an un-returned connection is reclaimed |
| `closeMethod` | Method called on the pool when Tomcat no longer needs it (`close`) |

### web.xml Resource Reference

The `web.xml` must declare a `<resource-ref>` to expose the JNDI resource to the web application:

```xml
<resource-ref>
  <description>Connection pool to the database</description>
  <res-ref-name>jdbc/employee-ferro</res-ref-name>
  <res-type>javax.sql.DataSource</res-type>
  <res-auth>Container</res-auth>
</resource-ref>
```

Full `web.xml` also declares servlets and URL mappings:

```xml
<servlet>
  <servlet-name>SearchEmployeeBySalary</servlet-name>
  <servlet-class>it.unipd.dei.webapp.servlet.SearchEmployeeBySalaryServlet</servlet-class>
</servlet>
<servlet>
  <servlet-name>CreateEmployee</servlet-name>
  <servlet-class>it.unipd.dei.webapp.servlet.CreateEmployeeServlet</servlet-class>
</servlet>

<servlet-mapping>
  <servlet-name>SearchEmployeeBySalary</servlet-name>
  <url-pattern>/search-employee-by-salary</url-pattern>
</servlet-mapping>
<servlet-mapping>
  <servlet-name>CreateEmployee</servlet-name>
  <url-pattern>/create-employee</url-pattern>
</servlet-mapping>
```

### Maven POM Dependencies

```xml
<dependencies>
  <!-- Servlet API — provided by Tomcat -->
  <dependency>
    <groupId>javax.servlet</groupId>
    <artifactId>javax.servlet-api</artifactId>
    <version>4.0.0</version>
    <scope>provided</scope>
  </dependency>

  <!-- PostgreSQL JDBC driver — must be bundled in WAR -->
  <dependency>
    <groupId>org.postgresql</groupId>
    <artifactId>postgresql</artifactId>
    <version>42.2.2</version>
  </dependency>

  <!-- Tomcat JDBC pool — provided by Tomcat, do NOT bundle -->
  <dependency>
    <groupId>org.apache.tomcat</groupId>
    <artifactId>tomcat-jdbc</artifactId>
    <version>9.0.7</version>
    <scope>provided</scope>
  </dependency>
</dependencies>
```

Maven also copies `context.xml` to the WAR's `META-INF/`:

```xml
<resource>
  <targetPath>${basedir}/target/${project.artifactId}-${project.version}/META-INF</targetPath>
  <directory>${basedir}/src/main/webapp/META-INF</directory>
  <includes><include>**/*.*</include></includes>
</resource>
```

---

## Servlet Layer

### AbstractDatabaseServlet

`AbstractDatabaseServlet` extends `HttpServlet` and provides DB connection management to all concrete servlets via inheritance.

```java
public abstract class AbstractDatabaseServlet extends HttpServlet {

    protected static final Logger LOGGER = LogManager.getLogger(
        AbstractDatabaseServlet.class, StringFormatterMessageFactory.INSTANCE);

    private DataSource ds;

    @Override
    public void init(ServletConfig config) throws ServletException {
        InitialContext cxt;
        try {
            cxt = new InitialContext();
            // JNDI lookup: "java:/comp/env/" prefix is mandatory
            ds = (DataSource) cxt.lookup("java:/comp/env/jdbc/employee-ferro");
            LOGGER.info("Connection pool to the database pool successfully acquired.");
        } catch (NamingException e) {
            ds = null;
            LOGGER.error("Unable to acquire the connection pool to the database.", e);
            throw new ServletException("Unable to acquire the connection pool to the database", e);
        }
    }

    @Override
    public void destroy() {
        ds = null;
        LOGGER.info("Connection pool to the database pool successfully released.");
    }

    protected final Connection getConnection() throws SQLException {
        try {
            return ds.getConnection();
        } catch (final SQLException e) {
            LOGGER.error("Unable to acquire the connection from the pool.", e);
            throw e;
        }
    }
}
```

**Key points:**
- `init()` runs **once** at servlet startup — looks up the `DataSource` from JNDI
- `destroy()` runs **once** at shutdown — releases the `DataSource` reference
- `getConnection()` called per-request — returns a pooled connection
- The JNDI name prefix `java:/comp/env/` is **mandatory** at lookup time; it matches `jdbc/employee-ferro` declared in `web.xml`

### CreateEmployeeServlet

```java
public final class CreateEmployeeServlet extends AbstractDatabaseServlet {

    public void doPost(HttpServletRequest req, HttpServletResponse res) throws IOException {

        LogContext.setIPAddress(req.getRemoteAddr());
        LogContext.setAction(Actions.CREATE_EMPLOYEE);

        int badge = -1;
        String surname = null;
        int age = -1;
        int salary = -1;
        Employee e = null;
        Message m = null;

        try {
            badge   = Integer.parseInt(req.getParameter("badge"));
            surname = req.getParameter("surname");
            age     = Integer.parseInt(req.getParameter("age"));
            salary  = Integer.parseInt(req.getParameter("salary"));

            LogContext.setResource(req.getParameter("badge"));

            e = new Employee(badge, surname, age, salary);
            new CreateEmployeeDAO(getConnection(), e).access();
            m = new Message(String.format("Employee %d successfully created.", badge));
            LOGGER.info("Employee %d successfully created in the database.", badge);

        } catch (NumberFormatException ex) {
            m = new Message(
                "Cannot create the employee. Invalid input parameters: badge, age, and salary must be integer.",
                "E100", ex.getMessage());
            LOGGER.error("...", ex);

        } catch (SQLException ex) {
            if (ex.getSQLState().equals("23505")) {
                // 23505 = unique_violation in PostgreSQL
                m = new Message(
                    String.format("Cannot create the employee: employee %d already exists.", badge),
                    "E300", ex.getMessage());
            } else {
                m = new Message(
                    "Cannot create the employee: unexpected error while accessing the database.",
                    "E200", ex.getMessage());
            }
            LOGGER.error("...", ex);
        }

        try {
            res.setContentType("text/html; charset=utf-8");
            PrintWriter out = res.getWriter();
            out.printf("<!DOCTYPE html>%n<html lang=\"en\">...");

            if (m.isError()) {
                out.printf("<ul>%n");
                out.printf("<li>error code: %s</li>%n", m.getErrorCode());
                out.printf("<li>message: %s</li>%n", m.getMessage());
                out.printf("<li>details: %s</li>%n", m.getErrorDetails());
                out.printf("</ul>%n");
            } else {
                out.printf("<p>%s</p>%n", m.getMessage());
                out.printf("<li>badge: %s</li>%n", e.getBadge());
                // ... other fields ...
            }

            out.flush();
            out.close();
        } catch (IOException ex) {
            LOGGER.error("Unable to send response when creating employee %d.", badge, ex);
            throw ex;
        } finally {
            LogContext.removeIPAddress();
            LogContext.removeAction();
            LogContext.removeResource();
        }
    }
}
```

**Error codes used:**

| Code | Condition |
|------|-----------|
| E100 | Invalid input — badge/age/salary not integers (`NumberFormatException`) |
| E200 | Unexpected SQL error |
| E300 | Duplicate badge (PostgreSQL SQL state `23505` = unique_violation) |

### SearchEmployeeBySalaryServlet

```java
public final class SearchEmployeeBySalaryServlet extends AbstractDatabaseServlet {

    public void doPost(HttpServletRequest req, HttpServletResponse res) throws IOException {

        LogContext.setIPAddress(req.getRemoteAddr());
        LogContext.setAction(Actions.SEARCH_EMPLOYEE_BY_SALARY);

        int salary = -1;
        List<Employee> el = null;
        Message m = null;

        try {
            salary = Integer.parseInt(req.getParameter("salary"));

            // chain: access() returns this, then getOutputParam() returns the list
            el = new SearchEmployeeBySalaryDAO(getConnection(), salary).access().getOutputParam();

            m = new Message("Employees successfully searched.");
            LOGGER.info("Employees successfully searched by salary %d.", salary);

        } catch (NumberFormatException ex) {
            m = new Message(
                "Cannot search for employees. Invalid input parameters: salary must be integer.",
                "E100", ex.getMessage());
        } catch (SQLException ex) {
            m = new Message(
                "Cannot search for employees: unexpected error while accessing the database.",
                "E200", ex.getMessage());
        }

        try {
            res.setContentType("text/html; charset=utf-8");
            PrintWriter out = res.getWriter();
            // ...
            if (m.isError()) {
                // print error details
            } else {
                out.printf("<table>%n");
                out.printf("<tr><td>Badge</td><td>Surname</td><td>Age</td><td>Salary</td></tr>%n");
                for (Employee e : el) {
                    out.printf("<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>%n",
                        e.getBadge(), e.getSurname(), e.getAge(), e.getSalary());
                }
                out.printf("</table>%n");
            }
            out.flush();
            out.close();
        } catch (IOException ex) {
            LOGGER.error("Unable to send response.", ex);
            throw ex;
        } finally {
            LogContext.removeIPAddress();
            LogContext.removeAction();
            LogContext.removeUser();
        }
    }
}
```

**HTML Forms** (from `src/main/webapp/html/`):

```html
<!-- Create Employee -->
<form method="POST" action="../create-employee">
  <input name="badge"   type="text"/>
  <input name="surname" type="text"/>
  <input name="age"     type="text"/>
  <input name="salary"  type="text"/>
  <button type="submit">Submit</button>
</form>

<!-- Search Employee by Salary -->
<form method="POST" action="../search-employee-by-salary">
  <input name="salary" type="text"/>
  <button type="submit">Submit</button>
</form>
```

---

## Sequence Diagrams

### Create Employee

![[db-create-employee-sequence.jpg]]

1. Browser: `POST /create-employee`
2. Container instantiates `CreateEmployeeServlet` (1.1)
3. `init(ServletConfig)` → JNDI lookup → obtains `DataSource` (1.2–1.3)
4. `service()` → `doPost()` (1.4–1.4.1)
5. Parse POST params → create `Employee` object (1.4.2)
6. `getConnection()` from pool (1.4.3)
7. Instantiate `CreateEmployeeDAO(connection, employee)` (1.4.4)
8. `access()` → `doAccess()` → execute `INSERT INTO` on DB (1.4.5–1.4.5.1)
9. Create `Message` (success or error) (1.4.7)
10. Generate HTML response from `Employee` + `Message` (1.4.8–1.4.10)

### Search Employee

![[db-search-employee-sequence.jpg]]

1. Browser: `POST /search-employee`
2. Container instantiates `SearchEmployeeBySalaryServlet` (1.1–1.3)
3. `doPost()` → parse salary param (1.4.1–1.4.2)
4. `getConnection()` (1.4.2)
5. Instantiate `SearchEmployeeBySalaryDAO(connection, salary)` (1.4.3)
6. `access()` → `doAccess()` → execute `SELECT` → process `ResultSet` → build `Employee` list (1.4.4–1.4.4.1.4)
7. `getOutputParam()` → retrieve list (1.4.6–1.4.7)
8. Create `Message`, generate HTML table (1.4.8–1.4.11)

---

## SQL Injection

> [!Warning] SQL Injection
> SQL injection occurs when user-supplied input is concatenated directly into a SQL string, allowing attackers to alter the query structure.
>
> **Vulnerable example:**
> ```java
> // NEVER DO THIS
> String query = "SELECT * FROM Employee WHERE salary > " + req.getParameter("salary");
> Statement stmt = con.createStatement();
> ResultSet rs = stmt.executeQuery(query);
> ```
> An attacker can submit `salary = 0 OR 1=1` to return all rows, or `0; DROP TABLE Employee; --` to destroy data.
>
> **Mitigation:** Always use `PreparedStatement` with `?` placeholders:
> ```java
> String query = "SELECT * FROM Employee WHERE salary > ?";
> PreparedStatement pstmt = con.prepareStatement(query);
> pstmt.setInt(1, salary);   // value is escaped/typed — cannot alter query structure
> ResultSet rs = pstmt.executeQuery();
> ```
> `PreparedStatement` sends the query structure and parameters separately to the DB. The DB treats parameters as **data**, never as SQL syntax.

> [!Important] Why PreparedStatement is Safe
> - The SQL template is compiled by the DB engine **before** the parameter values are bound
> - Parameters are transmitted as typed values (int, String, …), not as raw SQL text
> - No user input can escape the parameter context and become SQL syntax
> - **Additional benefit**: for repeated queries with different values, the DB can reuse the compiled query plan (performance gain)

The DAO pattern enforces `PreparedStatement` usage by centralizing all SQL in DAO classes — no SQL ever appears in servlet code.

---

## Class Diagram

![[db-employee-class-diagram.jpg]]

Key relationships:
- `CreateEmployeeServlet` and `SearchEmployeeBySalaryServlet` both extend `AbstractDatabaseServlet`
- Both servlets use `Message` (resource class)
- Both servlets use their respective DAO (`CreateEmployeeDAO`, `SearchEmployeeBySalaryDAO`)
- Both DAOs extend `AbstractDAO` which implements `DataAccessObject<T>`
- Both DAOs use `Employee` (resource class)

---

## Summary Table

| Component | Package | Role |
|-----------|---------|------|
| `Employee` | `resource` | Immutable bean: badge, surname, age, salary |
| `Message` | `resource` | Carries success or structured error info |
| `DataAccessObject<T>` | `database` | Interface: `access()` + `getOutputParam()` |
| `AbstractDAO<T>` | `database` | Base: manages connection lifecycle, rollback, one-shot guard |
| `CreateEmployeeDAO` | `database` | INSERT employee; no output param |
| `SearchEmployeeBySalaryDAO` | `database` | SELECT employees by salary; returns `List<Employee>` |
| `AbstractDatabaseServlet` | `servlet` | Base servlet: JNDI lookup in `init()`, `getConnection()` helper |
| `CreateEmployeeServlet` | `servlet` | POST handler: parse → DAO → respond |
| `SearchEmployeeBySalaryServlet` | `servlet` | POST handler: parse → DAO → respond with table |
| `context.xml` | `META-INF` | Defines Tomcat JDBC connection pool (JNDI resource) |
| `web.xml` | `WEB-INF` | Declares servlets, URL mappings, JNDI resource-ref |
| `PreparedStatement` | JDBC | Parameterized SQL — prevents SQL injection |
| JNDI | Tomcat | Directory service for looking up the connection pool |
| Connection Pool | Tomcat | Reuses DB connections; avoids per-request connection overhead |

## Questions

1. How do the client tier, web tier, API layer, database tier, and infrastructure components combine in the full-stack web application architecture?
2. Why should SQL logic be isolated inside DAO classes instead of being written directly inside servlets?
3. What makes the `Employee` and `Message` resource classes useful for passing domain data and structured outcomes through the application?
4. Why are immutable resource classes with `final` fields and getters often safer than mutable objects in request processing?
5. How does the generic `DataAccessObject<T>` interface support both commands with no output and queries returning values such as `List<Employee>`?
6. What responsibilities does `AbstractDAO` centralize, and why are connection closing, rollback, and one-shot execution handled there?
7. How does `CreateEmployeeDAO` use `PreparedStatement` placeholders to insert an employee safely?
8. How does `SearchEmployeeBySalaryDAO` transform a `ResultSet` into a list of `Employee` objects?
9. Why is opening a new database connection for every request expensive, and how does a Tomcat connection pool reduce that cost?
10. How do `context.xml`, `web.xml`, JNDI, and `AbstractDatabaseServlet` work together to provide database connections to servlets?
11. What is the purpose of pool parameters such as `testOnBorrow`, `validationQuery`, `maxActive`, `maxWait`, and `removeAbandoned`?
12. How does the create-employee sequence move from an HTTP POST request to an inserted database row and an HTML response?
13. How does the search-by-salary sequence use `access().getOutputParam()` to retrieve data for the response?
14. How do the error codes `E100`, `E200`, and `E300` distinguish validation, unexpected SQL errors, and duplicate keys?
15. Why does the DAO pattern make SQL injection protection easier to enforce across the application?
