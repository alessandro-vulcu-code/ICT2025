# 06-Webapp-2025-26-servlet-database

_Source: `06-Webapp-2025-26-servlet-database.pdf`_

## Slide 1 - Java Servlets and

Java Servlets and
Access to the Database

Web Applications
Master Degree in Computer Engineering

Master Degree in Cybersecurity
Master Degree in ICT for Internet and Multimedia

Academic Year 2025/2026

Nicola Ferro

Intelligent Interactive Information Access (IIIA) Hub

![Figura 1 dalla slide 1](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-Webapp-2025-26-servlet-database/assets/slide-001-fig-01.jpg)

## Slide 2 - Outline

Outline

Overall architecture of a full-stack application

The resource (Java Beans) classes

The Data Access Object (DAO) pattern

Pool of connections

SQL Injection

![Figura 1 dalla slide 2](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-Webapp-2025-26-servlet-database/assets/slide-002-fig-01.jpg)

## Slide 3 - Overall Architecture

Overall Architecture

![Figura 1 dalla slide 3](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-Webapp-2025-26-servlet-database/assets/slide-003-fig-01.jpg)

## Slide 4 - Application Functionalities: Create Employee

Application Functionalities: Create Employee

![Figura 1 dalla slide 4](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-Webapp-2025-26-servlet-database/assets/slide-004-fig-01.jpg)

## Slide 5 - Application Functionalities: Create Employee

Application Functionalities: Create Employee

![Figura 1 dalla slide 5](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-Webapp-2025-26-servlet-database/assets/slide-005-fig-01.jpg)

## Slide 6 - Application Functionalities: Create Employee

Application Functionalities: Create Employee

![Figura 1 dalla slide 6](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-Webapp-2025-26-servlet-database/assets/slide-006-fig-01.jpg)

## Slide 7 - Application Functionalities: Search Employee

Application Functionalities: Search Employee

![Figura 1 dalla slide 7](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-Webapp-2025-26-servlet-database/assets/slide-007-fig-01.jpg)

## Slide 8 - Application Functionalities: Search Employee

Application Functionalities: Search Employee

![Figura 1 dalla slide 8](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-Webapp-2025-26-servlet-database/assets/slide-008-fig-01.jpg)

## Slide 9 - The Full-Stack

The Full-Stack

![Figura 1 dalla slide 9](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-Webapp-2025-26-servlet-database/assets/slide-009-fig-01.jpg)

## Slide 10 - Employee Web Application Class Diagram

Employee Web Application Class Diagram

![Figura 1 dalla slide 10](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-Webapp-2025-26-servlet-database/assets/slide-010-fig-01.jpg)

## Slide 11 - Create Employee: Sequence Diagram

Create Employee: Sequence Diagram

![Figura 1 dalla slide 11](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-Webapp-2025-26-servlet-database/assets/slide-011-fig-01.jpg)

## Slide 12 - Search Employee: Sequence Diagram

Search Employee: Sequence Diagram

![Figura 1 dalla slide 12](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-Webapp-2025-26-servlet-database/assets/slide-012-fig-01.jpg)

## Slide 13 - The Data Logic Layer

The Data Logic Layer

![Figura 1 dalla slide 13](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-Webapp-2025-26-servlet-database/assets/slide-013-fig-01.jpg)

## Slide 14 - The Employee Database

The Employee Database

Employee
Manager
7309
5698

5998
5698

9553
4076

5698
4076

4076
8123
Manage

Employee

Badge
Surname
Age
Salary
7309
Rossi
34
45

5998
Bianchi
37
38

9553
Neri
42
35

5698
Bruni
43
42

4076
Mori
45
50

8123
Lupi
46
60

## Slide 15 - The Employee Class

The Employee Class

package it.unipd.dei.webapp.resource;

public class Employee {

Fields for describing an Employee.

 private final int badge;

Using final fi

 private final String surname;

 private final int age;

 private final int salary;

 public Employee(final int badge, final String surname, final int age, final int salary) {
  this.badge = badge;
  this.surname = surname;
  this.age = age;
  this.salary = salary;
 }

The Employee class can be subclassed but
the accessor methods to the private fi

The Employee class can be subclassed but
the accessor methods to the private fi

 public final int getBadge() {
  return badge;
 }

 public final String getSurname() {
  return surname;
 }

 public final int getAge() {
  return age;
 }

 public final int getSalary() {
  return salary;
 }

## Slide 16 - The Message Class

The Message Class

package it.unipd.dei.webapp.resource;

public class Message {

The Message class represents both
informative and error messages

 private final String message;
   private final String errorCode;

 private final String errorDetails;
  private final boolean isError;

 public Message(final String message, final String errorCode, final String errorDetails) {
  this.message = message;
  this.errorCode = errorCode;
  this.errorDetails = errorDetails;
  this.isError = true;
 }

This constructor is used
for error messages

This constructor is used
for informative messages

 public Message(final String message) {
  this.message = message;
  this.errorCode = null;
  this.errorDetails = null;
  this.isError = false;
 }

 public final String getMessage() {
  return message;
 }

 public final String getErrorCode() {
  return errorCode;
 }
  public final String getErrorDetails() {
  return errorDetails;
 }

 public final boolean isError() {
  return isError;
 }

## Slide 17 - The Data Access Object (DAO) Interface

The Data Access Object (DAO) Interface

The Data Access Object (DAO) pattern
abstracts and encapsulates all the logic
need to access a data source, typically a
relational database

https://www.oracle.com/java/
technologies/
dataaccessobject.html

Each DAO is responsible for the persistence
of a given resource, e.g. Employee in our

case

All the DAO implement a common interface
and each of them provides an access
operation, e.g. create Employee, read

Employee, …

the generic type T is the class of the resource
the DAO is about, e.g. Employee

the access method performs the actual
access to the datasource

the getOutputParam method is used to
retrieve any output parameter resulting from
the access to the datasource, if any

The use of a common interface potentially
allows for automating the DAO creation and
use via reflection

![Figura 1 dalla slide 17](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-Webapp-2025-26-servlet-database/assets/slide-017-fig-01.jpg)

## Slide 18 - The AbstractDAO class

The AbstractDAO class

The AbstractDAO class provides a base

implementation of the DataAccessObject interface

so that all the subclasses have a uniform behavior and
focus just on implementing the specific logic for
performing the requested data access operation

The implementation of the access() method takes
care of always closing the connection to the database
and of rolling-back the transaction, if needed

The  access() method delegates the actual logic to
perform the access to the datasource to its sub-
classes, via the abstract doAccess() method which
has to be implemented by them

DAO objects are one-shot and they are not expected to
be re-used; in this respect, they would not need to be
concerned with thread-safety.

However, the AbstractDAO class assumes the possibility of

a mis-use of a DAO (or leakage) and manages, to a certain

extent, concurrency issues via lock object and the

![Figura 1 dalla slide 18](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-Webapp-2025-26-servlet-database/assets/slide-018-fig-01.jpg)

## Slide 19 - The CreateEmployeeDatabase Class

The CreateEmployeeDatabase Class

There is no output parameter,
so no need of a generic

The SQL statement
to be executed

The class is not concerned with
obtaining the connection to the database or
the data about the employee, which are just

passed from the classes calling it

The class just focuses on accessing the database,
copies to/from application data structures, ensures to release
the connection, and delegates the management of any

exception to the super class (AbstractDAO)

public final class CreateEmployeeDAO extends AbstractDAO {¬
¬
    private static final String STATEMENT = "INSERT INTO Ferro.Employee (badge, surname, age, salary) VALUES (?, ?, ?, ?)";¬
¬
    private final Employee employee;¬
¬
    public CreateEmployeeDAO(final Connection con, final Employee employee) {¬
        super(con);¬
¬
        if (employee == null) {¬
            LOGGER.error("The employee cannot be null.");¬
            throw new NullPointerException("The employee cannot be null.");¬
        }¬
¬
        this.employee = employee;¬
    }¬
¬
    @Override¬
    protected final void doAccess() throws SQLException {¬
¬
        PreparedStatement pstmt = null;¬
¬
        try {¬
            pstmt = con.prepareStatement(STATEMENT);¬
            pstmt.setInt(1, employee.getBadge());¬
            pstmt.setString(2, employee.getSurname());¬
            pstmt.setInt(3, employee.getAge());¬
            pstmt.setInt(4, employee.getSalary());¬
¬
            pstmt.execute();¬
¬
            LOGGER.info("Employee %d successfully stored in the database.", employee.getBadge());¬
        } finally {¬
            if (pstmt != null) {¬
                pstmt.close();¬
            }¬
        }¬
¬
    }¬
}¬

## Slide 20 - The SearchEmployeeBySalaryDAO Class

The SearchEmployeeBySalaryDAO Class

The type of the output
parameter as a generic

The SQL statement
to be executed

Processes the ResultSet,
for each row, creates an new
Employee object
corresponding to that row,
and appends it to the List of

employees to be returned

Sets the output parameter that can be
retrieved by calling getOutputParameter()

public final class SearchEmployeeBySalaryDAO extends AbstractDAO<List<Employee>> {¬
¬
    private static final String STATEMENT = "SELECT badge, surname, age, salary FROM Ferro.Employee WHERE salary > ?";¬
¬
    private final int salary;¬
¬
    public SearchEmployeeBySalaryDAO(final Connection con, final int salary) {¬
        super(con);¬
        this.salary = salary;¬
    }¬
¬
    @Override¬
    public final void doAccess() throws SQLException {¬
¬
        PreparedStatement pstmt = null;¬
        ResultSet rs = null;¬
¬
        // the results of the search¬
        final List<Employee> employees = new ArrayList<Employee>();¬
¬
        try {¬
            pstmt = con.prepareStatement(STATEMENT);¬
            pstmt.setInt(1, salary);¬
¬
            rs = pstmt.executeQuery();¬
¬
            while (rs.next()) {¬
                employees.add(new Employee(rs.getInt("badge"), rs.getString("surname"), rs.getInt("age"),¬
                        rs.getInt("salary")));¬
            }¬
¬
            LOGGER.info("Employee(s) with salary above %d successfully listed.", salary);¬
        } finally {¬
            if (rs != null) {¬
                rs.close();¬
            }¬
¬
            if (pstmt != null) {¬
                pstmt.close();¬
            }¬
¬
        }¬
¬
        this.outputParam = employees;¬
    }¬
}¬

## Slide 21 - Pool of Database Connections via Tomcat: context.xml

Pool of Database Connections via Tomcat: context.xml

<Context>¬
¬
   <Resource name="jdbc/employee-ferro"¬
          auth="Container"¬
          type="javax.sql.DataSource"¬
          factory="org.apache.tomcat.jdbc.pool.DataSourceFactory"¬
          driverClassName="org.postgresql.Driver"¬
          url="jdbc:postgresql://localhost:5432/esami"¬
          username="ferro"¬
          password="ferro"¬
          testOnBorrow="true"¬
          validationQuery="SELECT 1"¬
          timeBetweenEvictionRunsMillis="30000"¬
          maxActive="10"¬
          minIdle="5"¬
          maxWait="10000"¬
          initialSize="2"¬
          removeAbandonedTimeout="60"¬
          removeAbandoned="true"¬
          closeMethod="close"¬

/>¬
¬
</Context>

https://tomcat.apache.org/tomcat-10.1-doc/jdbc-pool.html
https://tomcat.apache.org/tomcat-10.1-doc/jndi-resources-howto.html

![Figura 1 dalla slide 21](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-Webapp-2025-26-servlet-database/assets/slide-021-fig-01.jpg)

## Slide 22 - Pool of Database Connections via Tomcat: context.xml

Pool of Database Connections via Tomcat: context.xml

Java

fi
fi

fi

fi

<Context>¬
¬
   <Resource name="jdbc/employee-ferro"¬
          auth="Container"¬
          type="javax.sql.DataSource"¬
          factory="org.apache.tomcat.jdbc.pool.DataSourceFactory"¬
          driverClassName="org.postgresql.Driver"¬
          url="jdbc:postgresql://localhost:5432/esami"¬
          username="ferro"¬
          password="ferro"¬
          testOnBorrow="true"¬
          validationQuery="SELECT 1"¬
          timeBetweenEvictionRunsMillis="30000"¬
          maxActive="10"¬
          minIdle="5"¬
          maxWait="10000"¬
          initialSize="2"¬
          removeAbandonedTimeout="60"¬
          removeAbandoned="true"¬
          closeMethod="close"¬

/>¬
¬
</Context>

https://tomcat.apache.org/tomcat-10.1-doc/jdbc-pool.html
https://tomcat.apache.org/tomcat-10.1-doc/jndi-resources-howto.html

![Figura 1 dalla slide 22](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-Webapp-2025-26-servlet-database/assets/slide-022-fig-01.jpg)

## Slide 23 - Pool of Database Connections via Tomcat: context.xml

Pool of Database Connections via Tomcat: context.xml

Overall confi
•auth=“Container” means that Tomcat will perform the authentication via the
provided parameters
• type specifi
• factory specifi

<Context>¬
¬
   <Resource name="jdbc/employee-ferro"¬
          auth="Container"¬
          type="javax.sql.DataSource"¬
          factory="org.apache.tomcat.jdbc.pool.DataSourceFactory"¬
          driverClassName="org.postgresql.Driver"¬
          url="jdbc:postgresql://localhost:5432/esami"¬
          username="ferro"¬
          password="ferro"¬
          testOnBorrow="true"¬
          validationQuery="SELECT 1"¬
          timeBetweenEvictionRunsMillis="30000"¬
          maxActive="10"¬
          minIdle="5"¬
          maxWait="10000"¬
          initialSize="2"¬
          removeAbandonedTimeout="60"¬
          removeAbandoned="true"¬
          closeMethod="close"¬

• driverClassName the JDBC driver to be user
•url, username, password are the connection parameters

/>¬
¬
</Context>

https://tomcat.apache.org/tomcat-10.1-doc/jdbc-pool.html
https://tomcat.apache.org/tomcat-10.1-doc/jndi-resources-howto.html

![Figura 1 dalla slide 23](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-Webapp-2025-26-servlet-database/assets/slide-023-fig-01.jpg)

## Slide 24 - Pool of Database Connections via Tomcat: context.xml

Pool of Database Connections via Tomcat: context.xml

Advanced confi

<Context>¬
¬
   <Resource name="jdbc/employee-ferro"¬
          auth="Container"¬
          type="javax.sql.DataSource"¬
          factory="org.apache.tomcat.jdbc.pool.DataSourceFactory"¬
          driverClassName="org.postgresql.Driver"¬
          url="jdbc:postgresql://localhost:5432/esami"¬
          username="ferro"¬
          password="ferro"¬
          testOnBorrow="true"¬
          validationQuery="SELECT 1"¬
          timeBetweenEvictionRunsMillis="30000"¬
          maxActive="10"¬
          minIdle="5"¬
          maxWait="10000"¬
          initialSize="2"¬
          removeAbandonedTimeout="60"¬
          removeAbandoned="true"¬
          closeMethod="close"¬

/>¬
¬
</Context>

https://tomcat.apache.org/tomcat-10.1-doc/jdbc-pool.html
https://tomcat.apache.org/tomcat-10.1-doc/jndi-resources-howto.html

![Figura 1 dalla slide 24](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-Webapp-2025-26-servlet-database/assets/slide-024-fig-01.jpg)

## Slide 25 - Pool of Database Connections via Tomcat: context.xml

Pool of Database Connections via Tomcat: context.xml

The method to call on a singleton resource
when it is no longer required. This is intended
to speed up clean-up of resources that would
otherwise happen as part of garbage

collection.

Avoid

<Context>¬
¬
   <Resource name="jdbc/employee-ferro"¬
          auth="Container"¬
          type="javax.sql.DataSource"¬
          factory="org.apache.tomcat.jdbc.pool.DataSourceFactory"¬
          driverClassName="org.postgresql.Driver"¬
          url="jdbc:postgresql://localhost:5432/esami"¬
          username="ferro"¬
          password="ferro"¬
          testOnBorrow="true"¬
          validationQuery="SELECT 1"¬
          timeBetweenEvictionRunsMillis="30000"¬
          maxActive="10"¬
          minIdle="5"¬
          maxWait="10000"¬
          initialSize="2"¬
          removeAbandonedTimeout="60"¬
          removeAbandoned="true"¬
          closeMethod="close"¬

/>¬
¬
</Context>

https://tomcat.apache.org/tomcat-10.1-doc/jdbc-pool.html
https://tomcat.apache.org/tomcat-10.1-doc/jndi-resources-howto.html

![Figura 1 dalla slide 25](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-Webapp-2025-26-servlet-database/assets/slide-025-fig-01.jpg)

## Slide 26 - The web.xml Configuration File

The web.xml Configuration File

<?xml version="1.0" encoding="UTF-8"?>

<web-app id="hello-world-webapp" version="4.0" xmlns="http://xmlns.jcp.org/xml/ns/javaee"
 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 xsi:schemaLocation="http://java.sun.com/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd">

 <display-name>Employee Servlet JDBC</display-name>
 <description>Example servlet-based application accessing a DBMS via JDBC.</description>
  <servlet>
  <servlet-name>SearchEmployeeBySalary</servlet-name>
  <servlet-class>it.unipd.dei.webapp.servlet.SearchEmployeeBySalaryServlet</servlet-class>
 </servlet>
  <servlet>
  <servlet-name>CreateEmployee</servlet-name>
  <servlet-class>it.unipd.dei.webapp.servlet.CreateEmployeeServlet</servlet-class>
 </servlet>

Reference to the JDBC pool to
make it available to the Web

Application

 <servlet-mapping>
  <servlet-name>SearchEmployeeBySalary</servlet-name>
  <url-pattern>/search-employee-by-salary</url-pattern>
 </servlet-mapping>
  <servlet-mapping>
  <servlet-name>CreateEmployee</servlet-name>
  <url-pattern>/create-employee</url-pattern>
 </servlet-mapping>

 <resource-ref>
      <description>Connection pool to the database</description>
      <res-ref-name>jdbc/employee-ferro</res-ref-name>
      <res-type>javax.sql.DataSource</res-type>
      <res-auth>Container</res-auth>

</resource-ref>
</web-app>

![Figura 1 dalla slide 26](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-Webapp-2025-26-servlet-database/assets/slide-026-fig-01.jpg)

## Slide 27 - Project Object Model (POM)

Project Object Model (POM)

Copies the context.xml
confi
fi

    <!--  process resources before compilation and packaging -->
  <resources>
      <!--  copy HTML files to the target directory -->
   <resource>
    <targetPath>${basedir}/target/${project.artifactId}-${project.version}/html</targetPath>
    <directory>${basedir}/src/main/webapp/html</directory>
    <includes>
     <include>**/*.*</include>
    </includes>
   </resource>
      <!--  copy configuration files to the target directory -->
   <resource>
    <targetPath>${basedir}/target/${project.artifactId}-${project.version}/META-INF</targetPath>
    <directory>${basedir}/src/main/webapp/META-INF</directory>
    <includes>
     <include>**/*.*</include>
    </includes>
   </resource>
     </resources>
 </build>

Adds the dependencies on the Postgresql
JDBC driver and the Tomcat connection
pool.

Note that the scope of the Tomcat
connection pool is provided since it is
already available in the deployment

environment on Tomcat.

 <!-- Dependencies -->
 <dependencies>
  <dependency>
   <groupId>javax.servlet</groupId>
   <artifactId>javax.servlet-api</artifactId>
   <version>4.0.0</version>
   <scope>provided</scope>
  </dependency>
    <dependency>
   <groupId>org.postgresql</groupId>
   <artifactId>postgresql</artifactId>
   <version>42.2.2</version>
  </dependency>
    <dependency>
   <groupId>org.apache.tomcat</groupId>
   <artifactId>tomcat-jdbc</artifactId>
   <version>9.0.7</version>
   <scope>provided</scope>
  </dependency>
 </dependencies>

## Slide 28 - The Business&Interface

The Business&Interface

Logic Layers

![Figura 1 dalla slide 28](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-Webapp-2025-26-servlet-database/assets/slide-028-fig-01.jpg)

## Slide 29 - The Create and Search Employee Forms

The Create and Search Employee Forms

<!DOCTYPE html>
<html lang="en">
 <head>
  <meta charset="utf-8">
  <title>Create Employee Form</title>
 </head>

<!DOCTYPE html>
<html lang="en">
 <head>
  <meta charset="utf-8">
  <title>Search Employee Form</title>
 </head>

  <body>
 <h1>Search Employee Form</h1>
  <form method="POST" action="../search-employee-by-salary">
  <label for="salary">Salary:</label>
  <input name="salary" type="text"/><br/><br/>
    <button type="submit">Submit</button><br/>
  <button type="reset">Reset the form</button>
 </form>
 </body>
</html>

  <body>
 <h1>Create Employee Form</h1>
  <form method="POST" action="../create-employee">
  <label for="badge">Badge:</label>
  <input name="badge" type="text"/><br/>
    <label for="surname">Surname:</label>
  <input name="surname" type="text"/><br/>
    <label for="age">Age:</label>
  <input name="age" type="text"/><br/>
    <label for="salary">Salary:</label>
  <input name="salary" type="text"/><br/><br/>

  <button type="submit">Submit</button><br/>
  <button type="reset">Reset the form</button>
 </form>
 </body>
</html>

![Figura 1 dalla slide 29](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-Webapp-2025-26-servlet-database/assets/slide-029-fig-01.jpg)

## Slide 30 - The AbstractDatabaseServlet Class

The AbstractDatabaseServlet Class

Use the init servlet
lifecycle method to lookup the

connection pool from JNDI

The InitialContext is
the JNDI directory to look up
(not to be confused with
ServletContext) by using the
name assigned to the JDBC
pool in the context.xml fi

The DataSource fi

Use the DataSource to return a

connection to the database for a

public abstract class AbstractDatabaseServlet extends HttpServlet {¬
¬
    protected static final Logger LOGGER = LogManager.getLogger(AbstractDatabaseServlet.class,¬
            StringFormatterMessageFactory.INSTANCE);¬
¬
    private DataSource ds;¬
¬
    public void init(ServletConfig config) throws ServletException {¬
¬
        // the JNDI lookup context¬
        InitialContext cxt;¬
¬
        try {¬
            cxt = new InitialContext();¬
            ds = (DataSource) cxt.lookup("java:/comp/env/jdbc/employee-ferro");¬
¬
            LOGGER.info("Connection pool to the database pool successfully acquired.");¬
        } catch (NamingException e) {¬
            ds = null;¬
¬
            LOGGER.error("Unable to acquire the connection pool to the database.", e);¬
¬
            throw new ServletException("Unable to acquire the connection pool to the database", e);¬
        }¬
    }¬
¬
    public void destroy() {¬
        ds = null;¬
        LOGGER.info("Connection pool to the database pool successfully released.");¬
    }¬
¬
    protected final Connection getConnection() throws SQLException {¬
        try {¬
            return ds.getConnection();¬
        } catch (final SQLException e) {¬
            LOGGER.error("Unable to acquire the connection from the pool.", e);¬
            throw e;¬
        }¬
    }¬
¬
}¬

![Figura 1 dalla slide 30](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-Webapp-2025-26-servlet-database/assets/slide-030-fig-01.jpg)

## Slide 31 - The CreateEmployeeServlet Class

The CreateEmployeeServlet Class

Retrieves the connection
from the superclass and uses
the helper DAO to access the

database

Retrieves request
parameters and creates
the corresponding

Employee object

public final class CreateEmployeeServlet extends AbstractDatabaseServlet {¬
¬
    public void doPost(HttpServletRequest req, HttpServletResponse res) throws IOException {¬
¬
        LogContext.setIPAddress(req.getRemoteAddr());¬
        LogContext.setAction(Actions.CREATE_EMPLOYEE);¬
¬
        // request parameters¬
        int badge = -1;¬
        String surname = null;¬
        int age = -1;¬
        int salary = -1;¬
¬
        // model¬
        Employee e = null;¬
        Message m = null;¬
¬
        try {¬
            // retrieves the request parameters¬
            badge = Integer.parseInt(req.getParameter("badge"));¬
            surname = req.getParameter("surname");¬
            age = Integer.parseInt(req.getParameter("age"));¬
            salary = Integer.parseInt(req.getParameter("salary"));¬
¬
            // set the badge of the employee as the resource in the log context at this point we know it is a valid integer¬
            LogContext.setResource(req.getParameter("badge"));¬
¬
            // creates a new employee from the request parameters¬
            e = new Employee(badge, surname, age, salary);¬
¬
            // creates a new object for accessing the database and stores the employee¬
            new CreateEmployeeDAO(getConnection(), e).access();¬
¬
            m = new Message(String.format("Employee %d successfully created.", badge));¬
¬
            LOGGER.info("Employee %d successfully created in the database.", badge);¬
¬
        } catch (NumberFormatException ex) {¬
            m = new Message(¬
                    "Cannot create the employee. Invalid input parameters: badge, age, and salary must be integer.", "E100", ex.getMessage());¬
¬
            LOGGER.error("Cannot create the employee. Invalid input parameters: badge, age, and salary must be integer.", ex);¬
        } catch (SQLException ex) {¬
            if (ex.getSQLState().equals("23505")) {¬
                m = new Message(String.format("Cannot create the employee: employee %d already exists.", badge), "E300", ex.getMessage());¬
¬
                LOGGER.error(new StringFormattedMessage("Cannot create the employee: employee %d already exists.", badge), ex);¬
            } else {¬
                m = new Message("Cannot create the employee: unexpected error while accessing the database.", "E200", ex.getMessage());¬
¬
                LOGGER.error("Cannot create the employee: unexpected error while accessing the database.", ex);¬
            }¬
        }¬
¬

Writes out the

HTML page

Manages error/success conditions and
creates the corresponding Message

¬
        try {¬
            // set the MIME media type of the response¬
            res.setContentType("text/html; charset=utf-8");¬
¬
            // get a stream to write the response¬
            PrintWriter out = res.getWriter();¬
¬
            // write the HTML page¬
            out.printf("<!DOCTYPE html>%n");¬
¬
            out.printf("<html lang=\"en\">%n");¬
            out.printf("<head>%n");¬
            out.printf("<meta charset=\"utf-8\">%n");¬
            out.printf("<title>Create Employee</title>%n");¬
            out.printf("</head>%n");¬
¬
            out.printf("<body>%n");¬
            out.printf("<h1>Create Employee</h1>%n");¬
            out.printf("<hr/>%n");¬
¬
            if (m.isError()) {¬
                out.printf("<ul>%n");¬
                out.printf("<li>error code: %s</li>%n", m.getErrorCode());¬
                out.printf("<li>message: %s</li>%n", m.getMessage());¬
                out.printf("<li>details: %s</li>%n", m.getErrorDetails());¬
                out.printf("</ul>%n");¬
            } else {¬
                out.printf("<p>%s</p>%n", m.getMessage());¬
                out.printf("<ul>%n");¬
                out.printf("<li>badge: %s</li>%n", e.getBadge());¬
                out.printf("<li>surname: %s</li>%n", e.getSurname());¬
                out.printf("<li>age: %s</li>%n", e.getAge());¬
                out.printf("<li>salary: %s</li>%n", e.getSalary());¬
                out.printf("</ul>%n");¬
            }¬
¬
            out.printf("</body>%n");¬
¬
            out.printf("</html>%n");¬
¬
            // flush the output stream buffer¬
            out.flush();¬
¬
            // close the output stream¬
            out.close();¬
        } catch (IOException ex) {¬
            LOGGER.error(new StringFormattedMessage("Unable to send response when creating employee %d.", badge), ex);¬
            throw ex;¬
        } finally {¬
            LogContext.removeIPAddress();¬
            LogContext.removeAction();¬
            LogContext.removeResource();¬
        }¬
¬
    }¬
}¬

## Slide 32 - The SearchEmployeeBySalaryServlet Class

The SearchEmployeeBySalaryServlet Class

Writes out the

HTML page

public final class SearchEmployeeBySalaryServlet extends AbstractDatabaseServlet {¬
¬
    public void doPost(HttpServletRequest req, HttpServletResponse res) throws IOException {¬
¬
        LogContext.setIPAddress(req.getRemoteAddr());¬
        LogContext.setAction(Actions.SEARCH_EMPLOYEE_BY_SALARY);¬
¬
        // request parameter¬
        int salary = -1;¬
¬
        // model¬
        List<Employee> el = null;¬
        Message m = null;¬
¬
        try {¬
¬
            // retrieves the request parameter¬
            salary = Integer.parseInt(req.getParameter("salary"));¬
¬
            // creates a new object for accessing the database and searching the employees¬
            el = new SearchEmployeeBySalaryDAO(getConnection(), salary).access().getOutputParam();¬
¬
            m = new Message("Employees successfully searched.");¬
¬
            LOGGER.info("Employees successfully searched by salary %d.", salary);¬
¬
        } catch (NumberFormatException ex) {¬
            m = new Message("Cannot search for employees. Invalid input parameters: salary must be integer.", "E100", ex.getMessage());¬
¬
            LOGGER.error("Cannot search for employees. Invalid input parameters: salary must be integer.", ex);¬
        } catch (SQLException ex) {¬
            m = new Message("Cannot search for employees: unexpected error while accessing the database.", "E200", ex.getMessage());¬
¬
            LOGGER.error("Cannot search for employees: unexpected error while accessing the database.", ex);¬
        }¬
¬

Retrieves the connection to the database,
uses the helper DAO to access the
database, and getOutputParam() to

retrieve the list of Employee objects

¬
        try {¬
            // set the MIME media type of the response¬
            res.setContentType("text/html; charset=utf-8");¬
¬
            // get a stream to write the response¬
            PrintWriter out = res.getWriter();¬
¬
            // write the HTML page¬
            out.printf("<!DOCTYPE html>%n");¬
¬
            out.printf("<html lang=\"en\">%n");¬
            out.printf("<head>%n");¬
            out.printf("<meta charset=\"utf-8\">%n");¬
            out.printf("<title>Search Employee</title>%n");¬
            out.printf("</head>%n");¬
¬
            out.printf("<body>%n");¬
            out.printf("<h1>Search Employee</h1>%n");¬
            out.printf("<hr/>%n");¬
¬
            if (m.isError()) {¬
                out.printf("<ul>%n");¬
                out.printf("<li>error code: %s</li>%n", m.getErrorCode());¬
                out.printf("<li>message: %s</li>%n", m.getMessage());¬
                out.printf("<li>details: %s</li>%n", m.getErrorDetails());¬
                out.printf("</ul>%n");¬
            } else {¬
                out.printf("<p>%s</p>%n", m.getMessage());¬
¬
                out.printf("<table>%n");¬
                out.printf("<tr>%n");¬
                out.printf("<td>Badge</td><td>Surname</td><td>Age</td><td>Salary</td>%n");¬
                out.printf("</tr>%n");¬
¬
                for (Employee e : el) {¬
                    out.printf("<tr>%n");¬
                    out.printf("<td>%s</td><td>%s</td><td>%s</td><td>%s</td>%n", e.getBadge(), e.getSurname(),¬
                            e.getAge(), e.getSalary());¬
                    out.printf("</tr>%n");¬
                }¬
                out.printf("</table>%n");¬
            }¬
¬
            out.printf("</body>%n");¬
¬
            out.printf("</html>%n");¬
¬
            // flush the output stream buffer¬
            out.flush();¬
¬
            // close the output stream¬
            out.close();¬
        } catch (IOException ex) {¬
            LOGGER.error(new StringFormattedMessage("Unable to send response when creating employee %d.", salary), ex)
            throw ex;¬
        } finally {¬
            LogContext.removeIPAddress();¬
            LogContext.removeAction();¬
            LogContext.removeUser();¬
        }¬
    }¬
¬
}¬

![Figura 1 dalla slide 32](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-Webapp-2025-26-servlet-database/assets/slide-032-fig-01.jpg)

## Slide 33 - Slide 33
