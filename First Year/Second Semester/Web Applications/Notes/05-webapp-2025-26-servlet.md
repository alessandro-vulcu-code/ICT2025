# Java Servlet

## Table of Contents

- [[#Web Application Technologies|Web Application Technologies]]
  - [[#Browser and Server Architecture|Browser and Server Architecture]]
  - [[#Technologies Overview|Technologies Overview]]
- [[#Jakarta Enterprise Edition|Jakarta Enterprise Edition]]
  - [[#Package Naming|Package Naming]]
  - [[#Multi-tiered Architecture|Multi-tiered Architecture]]
- [[#Java Servlet|Java Servlet]]
  - [[#Definition and Properties|Definition and Properties]]
  - [[#jakarta.servlet Main Classes|jakarta.servlet Main Classes]]
  - [[#jakarta.servlet.http Main Classes|jakarta.servlet.http Main Classes]]
  - [[#UML Class Diagram|UML Class Diagram]]
  - [[#Servlet Lifecycle|Servlet Lifecycle]]
- [[#Apache Tomcat|Apache Tomcat]]
- [[#Project Setup|Project Setup]]
  - [[#Directory Structure|Directory Structure]]
  - [[#web.xml Configuration|web.xml Configuration]]
  - [[#Maven POM Configuration|Maven POM Configuration]]
- [[#Servlet Examples|Servlet Examples]]
  - [[#HelloWorld Servlet|HelloWorld Servlet]]
  - [[#Servlet Sequence Diagram|Servlet Sequence Diagram]]
  - [[#Servlet with Log4J|Servlet with Log4J]]
  - [[#GET and POST Forms|GET and POST Forms]]
- [[#Summary Table|Summary Table]]

---

## Web Application Technologies

### Browser and Server Architecture

![[servlet-browser-server-architecture.jpg]]

**Web Browser** components:
- **User Interface** — what user sees
- **Browser/Rendering Engine** — renders HTML/CSS
- **Document Object Model (DOM)** — in-memory tree of the page
- **Scripting Engine** — executes JavaScript
- **Parsing Engine** — parses HTML/CSS
- **Networking** — handles TCP/IP

**Web Server** components:
- **Request Analysis** — parses incoming HTTP request
- **Access Control** — authentication/authorization checks
- **Resource Handler** — dispatches to static or dynamic resource
- **Static Resources** — files served as-is (HTML, images, CSS)
- **Dynamic Resources** — servlets, scripts that generate content at runtime
- **Logging** — records activity
- **Networking** — handles TCP/IP

Communication uses **HTTP Request / HTTP Response** between browser and server.

### Technologies Overview
![[Pasted image 20260512114912.png]]

| Side | Programs | Scripts |
|------|----------|---------|
| **Server-side** | CGI, Java Servlet, JSP, PHP, ASP/ASP.NET, Django (Python via WSGI), Ruby on Rails | — |
| **Client-side** | Java Applet, ActiveX, Adobe Flash, Apache Flex | JavaScript, VBScript, AJAX (Web 2.0) |

---

## Jakarta Enterprise Edition

> [!Important] Jakarta EE
> **Jakarta Enterprise Edition (Jakarta EE)** is the standardized platform for developing multi-tiered enterprise applications. It defines APIs for Web development (servlets, REST, etc.) and is executed by a **Web container**.
>
> - **Web container**: implements the Jakarta EE API and executes web components
> - **Web component**: a part of a web app (servlet, JSP, …) hosted by the container
>
> **Intuition:** Jakarta EE is the spec; Tomcat is an implementation of the web container portion.

### Package Naming

| Phase | Organization | Package prefix |
|-------|-------------|----------------|
| J2EE / Java EE ≤ 8 | Sun Microsystems / Oracle | `javax.*` |
| Jakarta EE ≥ 9 | Eclipse Foundation | `jakarta.*` |

Key transition: **Tomcat 9** → `javax.*`; **Tomcat 10+** → `jakarta.*`. Course uses **Tomcat 11**.

Relevant version evolution (Servlet spec):

| Jakarta EE | Servlet | JSP | Java SE base |
|------------|---------|-----|--------------|
| Java EE 6 | 3.0 | 2.2 | SE 6 |
| Java EE 7 | 3.1 | 2.3 | SE 7 |
| Java EE 8 | 4.0 | 2.3 | SE 8 |
| Jakarta EE 9 | 5.0 | 3.0 | SE 8 |
| Jakarta EE 10 | 6.0 | 3.1 | SE 11 |
| Jakarta EE 11 | 6.1 | 4.0 | SE 21 |
| Jakarta EE 12 | 6.2 | 4.1 | SE 21 |

### Multi-tiered Architecture

![[servlet-javaee-multitier-architecture.jpg]]

Four tiers:
1. **Client Tier** — Web browser, applets, application clients
2. **Web Tier** — Servlets, JSP pages, JavaBeans (optional)
3. **Business Tier** — EJBs (Session Beans, Message-Driven Beans), JPA Entities
4. **EIS Tier** — Databases and legacy systems

---

## Java Servlet

### Definition and Properties

> [!Important] Java Servlet Definition
> A **servlet** is a ==Java-based Web component, managed by a container, that generates dynamic content==. Servlets are:
> - ==Platform-independent Java classes== compiled to bytecode
> - Loaded dynamically into and run by a Java-enabled web server
> - **Not thread-safe** — the container may send concurrent requests to a single servlet instance; developers must synchronize access to shared resources (files, network connections, instance variables)
>
> **Intuition:** a servlet is like a controller that receives an HTTP request and writes an HTTP response programmatically.

Packages: `jakarta.servlet` and `jakarta.servlet.http` (formerly `javax.*` up to Java EE 8).

### jakarta.servlet Main Classes

| Class/Interface | Role |
|----------------|------|
| `Servlet` | Interface — defines methods all servlets must implement |
| `ServletRequest` | Provides client request information to a servlet |
| `ServletResponse` | Assists a servlet in sending a response |
| `ServletConfig` | Passes container-to-servlet initialization info |
| `ServletContext` | Servlet's view of the web app; communication with container (MIME types, logging, dispatch) |
| `Filter` | Performs filtering on requests/responses (auth, logging, compression, image conversion) |

### jakarta.servlet.http Main Classes

| Class/Interface | Role |
|----------------|------|
| `HttpServlet` | Abstract class — subclass this to create HTTP servlets |
| `HttpServletRequest` | Extends `ServletRequest` with HTTP-specific request info |
| `HttpServletResponse` | Extends `ServletResponse` with HTTP-specific response functionality |
| `Cookie` | Small piece of info sent to browser, stored, sent back later |
| `HttpSession` | Identifies a user across multiple requests; stores per-user state |
| `Part` | Represents a part of a `multipart/form-data` upload (file or form field) |

### UML Class Diagram

![[servlet-uml-class-diagram.jpg]]

Key relationships:
- `HttpServlet` extends `GenericServlet` which implements `Servlet`
- `HttpServletRequest` and `HttpServletResponse` extend `ServletRequest`/`ServletResponse`
- `HttpSession`, `Cookie`, `Part`, and `Filter` are companions used by `HttpServletRequest`/`HttpServletResponse`
- `ServletContext` and `ServletConfig` are used by `Servlet` during init and runtime

### Servlet Lifecycle

> [!Important] Servlet Lifecycle — Three Methods
> The container calls these exactly once or per-request:
>
> 1. **`init(ServletConfig)`** — called **once** after instantiation, before any requests. Must complete successfully before `service()` is ever called. Gives access to `ServletContext` via `ServletConfig`.
>
> 2. **`service(ServletRequest, ServletResponse)`** — called **per request**. For `HttpServlet`, this is specialized into:
>    - `doGet(HttpServletRequest, HttpServletResponse)`
>    - `doPost(HttpServletRequest, HttpServletResponse)`
>    - `doPut(HttpServletRequest, HttpServletResponse)`
>    - `doDelete(HttpServletRequest, HttpServletResponse)`
>
> 3. **`destroy()`** — called **once** when the servlet is taken out of service. Only called after all active `service()` threads exit (or timeout). Used for cleanup: closing files, releasing connections, persisting state.
>
> **Intuition:** init → [service × N] → destroy.

> [!Warning] Thread Safety
> Containers run servlets in multithreaded environments. Concurrent requests hit the **same servlet instance**. Never store request-specific state in instance variables — use local variables or `ThreadLocal`.

---

## Apache Tomcat

- Reference: `http://tomcat.apache.org/`
- **Tomcat 9** → Java EE → `javax.*` packages
- **Tomcat 10+** → Jakarta EE → `jakarta.*` packages
- Course uses **Tomcat 11** (Jakarta EE, `jakarta.*`)
- Manager UI at `http://localhost:8080/manager/html/`
- Logs in `$CATALINA_BASE/logs/`

Deployment: upload `.war` file via Manager UI → Tomcat unpacks and starts the app.

---

## Project Setup

### Directory Structure

```
src/
  main/
    database/       SQL schema files
    java/           Java source (servlets, helpers)
    resources/      Property files, log4j2.xml
    webapp/
      css/
      html/
      js/
      jsp/
      media/
      WEB-INF/      web.xml (NOT publicly accessible)
  test/             JUnit tests
javadoc/            Generated documentation
target/             Compiled classes and WAR
```

> [!Important] WEB-INF
> `WEB-INF/` is **never served directly** by the container. It holds `web.xml` and private resources (compiled classes, jars). Browsers cannot access it directly.

### web.xml Configuration

> [!Example] Servlet Declaration and URL Mapping
> **Context:** `WEB-INF/web.xml` wires servlet classes to URL patterns. When the container receives a request matching a pattern, it instantiates the servlet and calls `service()`.
>
> ```xml
> <?xml version="1.0" encoding="UTF-8"?>
> <web-app id="hello-world-webapp" version="4.0"
>          xmlns="http://xmlns.jcp.org/xml/ns/javaee"
>          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
>          xsi:schemaLocation="http://java.sun.com/xml/ns/javaee
>                              http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd">
>
>   <display-name>Hello World Servlet</display-name>
>   <description>Example servlet answering "Hello, world!" to GET.</description>
>
>   <!-- Declare the servlet and its class -->
>   <servlet>
>     <servlet-name>HelloWorld</servlet-name>
>     <servlet-class>it.unipd.dei.webapp.HelloWorldServlet</servlet-class>
>   </servlet>
>
>   <!-- Map URL patterns to the servlet -->
>   <servlet-mapping>
>     <servlet-name>HelloWorld</servlet-name>
>     <url-pattern>/helloworld</url-pattern>
>   </servlet-mapping>
>   <servlet-mapping>
>     <servlet-name>HelloWorld</servlet-name>
>     <url-pattern>/hello</url-pattern>
>   </servlet-mapping>
>   <servlet-mapping>
>     <servlet-name>HelloWorld</servlet-name>
>     <url-pattern>/ciao</url-pattern>
>   </servlet-mapping>
>
> </web-app>
> ```
>
> **Explanation:** One servlet class can be bound to multiple URL patterns. The container matches the request URI against declared patterns.

For a static HTML-only app, use `<welcome-file-list>` instead of servlet mappings:

```xml
<welcome-file-list>
  <welcome-file>/html/hello.html</welcome-file>
</welcome-file-list>
```

### Maven POM Configuration

> [!Important] WAR Packaging
> Web apps must be packaged as a **WAR (Web ARchive)** file — a zip with a specific layout. Set `<packaging>war</packaging>` in `pom.xml`.

> [!Example] Essential POM for a Servlet Project
> ```xml
> <packaging>war</packaging>
>
> <properties>
>   <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
> </properties>
>
> <build>
>   <defaultGoal>compile</defaultGoal>
>   <sourceDirectory>${basedir}/src/main/java</sourceDirectory>
>   <directory>${basedir}/target</directory>
>   <finalName>${project.artifactId}-${project.version}</finalName>
>
>   <plugins>
>     <!-- Compiler -->
>     <plugin>
>       <groupId>org.apache.maven.plugins</groupId>
>       <artifactId>maven-compiler-plugin</artifactId>
>       <version>3.8.0</version>
>       <configuration><source>1.8</source><target>1.8</target></configuration>
>     </plugin>
>
>     <!-- WAR packager — must point to web.xml -->
>     <plugin>
>       <groupId>org.apache.maven.plugins</groupId>
>       <artifactId>maven-war-plugin</artifactId>
>       <version>3.2.2</version>
>       <configuration>
>         <webXml>${basedir}/src/main/webapp/WEB-INF/web.xml</webXml>
>       </configuration>
>     </plugin>
>
>     <!-- Javadoc -->
>     <plugin>
>       <groupId>org.apache.maven.plugins</groupId>
>       <artifactId>maven-javadoc-plugin</artifactId>
>       <version>3.1.0</version>
>       <configuration>
>         <reportOutputDirectory>${basedir}/javadoc</reportOutputDirectory>
>         <show>protected</show>
>       </configuration>
>     </plugin>
>   </plugins>
> </build>
>
> <!-- Servlet API: provided because Tomcat already has it -->
> <dependencies>
>   <dependency>
>     <groupId>javax.servlet</groupId>
>     <artifactId>javax.servlet-api</artifactId>
>     <version>4.0.0</version>
>     <scope>provided</scope>   <!-- NOT packaged in WAR -->
>   </dependency>
> </dependencies>
> ```
>
> **Key point:** `<scope>provided</scope>` means the servlet API is needed to compile locally but Tomcat already ships it — do not bundle it in the WAR.

Maven lifecycle phases used: `resources` → `compile` → `test` → `package` (produces `.war`) → `install` → `deploy`.

---

## Servlet Examples

### HelloWorld Servlet

> [!Example] Minimal GET Servlet
> **Context:** extend `HttpServlet`, override `doGet`, write HTML to the response.
>
> ```java
> public class HelloWorldServlet extends HttpServlet {
>
>     public void doGet(HttpServletRequest req, HttpServletResponse res)
>             throws ServletException, IOException {
>
>         // 1. Set MIME type of response
>         res.setContentType("text/html; charset=utf-8");
>
>         // 2. Get writer for response body
>         PrintWriter out = res.getWriter();
>
>         // 3. Write HTML
>         out.printf("<!DOCTYPE html>%n");
>         out.printf("<html lang=\"en\">%n");
>         out.printf("<head>%n");
>         out.printf("<meta charset=\"utf-8\">%n");
>         out.printf("<title>HelloWorld Servlet Response</title>%n");
>         out.printf("</head>%n");
>         out.printf("<body>%n");
>         out.printf("<h1>HelloWorld Servlet Response</h1>%n");
>         out.printf("<hr/>%n");
>         out.printf("<p>Hello, world!%n</p>%n");
>         out.printf("</body>%n");
>         out.printf("</html>%n");
>
>         // 4. Flush and close (don't forget)
>         out.flush();
>         out.close();
>
>         // 5. Log
>         System.out.printf("[INFO] HelloWorldServlet - %s - Request successfully served.%n",
>             new Timestamp(System.currentTimeMillis()).toString());
>     }
> }
> ```
>
> **Key steps:** set content type → get writer → write HTML → flush → close → log.

### Servlet Sequence Diagram

![[servlet-sequence-diagram.jpg]]

**First request flow:**
1. Browser sends `GET /hello-world-servlet/hello`
2. Container instantiates `HelloWorldServlet` (1.1)
3. Container calls `init(ServletConfig)` (1.2)
4. Container calls `service(HttpServletRequest, HttpServletResponse)` (1.4)
5. `service()` internally dispatches to `doGet()` (1.4.1)
6. `doGet()` writes the response, returns (1.4.2)
7. Browser receives HTML page (1.4.3)

**Subsequent requests:** servlet already instantiated and initialized — container calls `service()` directly (step 2).

### Servlet with Log4J

> [!Important] Log4J 2 Structure
> - **Logger** — named object that issues log messages; organized in a **hierarchy** (tree). Root is `Root`. Child loggers inherit appenders from parents.
> - **Appender** — destination for log messages (file, console, etc.)
> - **Level** (ascending): `TRACE < DEBUG < INFO < WARN < ERROR < FATAL`. Messages below the configured level are discarded.
> - **ThreadContext (MDC)** — per-thread key-value store for contextual info (user, IP, action, resource) automatically included in log output.

> [!Example] LogContext Helper Class
> **Context:** wrapper over `Log4J ThreadContext` to attach request-scoped metadata to log messages.
>
> ```java
> import org.apache.logging.log4j.ThreadContext;
>
> public final class LogContext {
>
>     private static final String USER     = "USER";
>     private static final String IP       = "IP";
>     private static final String ACTION   = "ACTION";
>     private static final String RESOURCE = "RESOURCE";
>
>     public static void setUser(final String user) {
>         if (user != null && !user.isEmpty()) ThreadContext.put(USER, user);
>     }
>     public static void removeUser() { ThreadContext.remove(USER); }
>
>     public static void setIPAddress(final String ip) {
>         if (ip != null && !ip.isEmpty()) ThreadContext.put(IP, ip);
>     }
>     public static void removeIPAddress() { ThreadContext.remove(IP); }
>
>     public static void setAction(final String action) {
>         if (action != null) ThreadContext.put(ACTION, action);
>     }
>     public static void removeAction() { ThreadContext.remove(ACTION); }
>
>     public static void setResource(final String resource) {
>         if (resource != null && !resource.isEmpty()) ThreadContext.put(RESOURCE, resource);
>     }
>     public static void removeResource() { ThreadContext.remove(RESOURCE); }
>
>     private LogContext() {
>         throw new AssertionError("No instances of " + LogContext.class.getName() + " allowed.");
>     }
> }
> ```

> [!Example] Servlet Using Log4J
> ```java
> public class HelloWorldServlet extends HttpServlet {
>
>     protected static final Logger LOGGER =
>         LogManager.getLogger(HelloWorldServlet.class, StringFormatterMessageFactory.INSTANCE);
>
>     public void doGet(HttpServletRequest req, HttpServletResponse res)
>             throws IOException {
>
>         // Set MDC context for this request
>         LogContext.setIPAddress(req.getRemoteAddr());
>         LogContext.setResource(req.getRequestURI());
>         LogContext.setAction("HELLO_WORLD");
>
>         try {
>             res.setContentType("text/html; charset=utf-8");
>             PrintWriter out = res.getWriter();
>             // ... write HTML ...
>             out.flush();
>             out.close();
>             LOGGER.info("Request successfully served.");
>         } catch (Exception e) {
>             LOGGER.error("Unable to serve request.", e);
>             throw e;
>         } finally {
>             // Always clear MDC to avoid leaking context across requests
>             LogContext.removeIPAddress();
>             LogContext.removeAction();
>             LogContext.removeResource();
>         }
>     }
> }
> ```
>
> **Pattern:** set MDC → try { process + LOGGER.info } catch { LOGGER.error + rethrow } finally { remove MDC }.

> [!Example] log4j2.xml Configuration
> ```xml
> <Configuration status="INFO" monitorInterval="0" name="hello-log4j">
>   <Appenders>
>     <!-- Rolling file: rotates daily and at 250 MB -->
>     <RollingRandomAccessFile name="RFILE"
>       fileName="${sys:catalina.base}/webapps/my-logs/hello-log4j.log"
>       filePattern="${sys:catalina.base}/webapps/my-logs/$${date:yyyy-MM}/hello-log4j-%d{yyyyMMdd}-%i.log.gz">
>       <PatternLayout>
>         <Pattern>%date{DEFAULT} %level [%thread] %class{1}.%method(%file:%line)%n
>           \tIP = %MDC{IP}; USER = %MDC{USER}; ACTION = %MDC{ACTION}; RESOURCE = %MDC{RESOURCE}%n
>           \t%message%n\t%throwable%n</Pattern>
>       </PatternLayout>
>       <Policies>
>         <TimeBasedTriggeringPolicy />
>         <SizeBasedTriggeringPolicy size="250 MB"/>
>       </Policies>
>     </RollingRandomAccessFile>
>
>     <!-- Console output -->
>     <Console name="STDOUT" target="SYSTEM_OUT">
>       <PatternLayout>
>         <Pattern>%date{DEFAULT} %level [%thread] %class{1}.%method(%file:%line)%n
>           \tIP = %MDC{IP}; USER = %MDC{USER}; ACTION = %MDC{ACTION}; RESOURCE = %MDC{RESOURCE}%n
>           \t%message%n\t%throwable%n</Pattern>
>       </PatternLayout>
>     </Console>
>   </Appenders>
>   <Loggers>
>     <Root level="TRACE">
>       <AppenderRef ref="RFILE"  level="INFO"/>
>       <AppenderRef ref="STDOUT" level="INFO"/>
>     </Root>
>   </Loggers>
> </Configuration>
> ```
>
> **Key:** `%MDC{KEY}` injects ThreadContext values into each log line.

Log4J Maven dependency (not `provided` — must be bundled in WAR):

```xml
<dependency>
  <groupId>org.apache.logging.log4j</groupId>
  <artifactId>log4j-api</artifactId>
  <version>2.x.x</version>
</dependency>
<dependency>
  <groupId>org.apache.logging.log4j</groupId>
  <artifactId>log4j-core</artifactId>
  <version>2.x.x</version>
</dependency>
```

### GET and POST Forms

> [!Example] HTML Forms — GET vs POST
> **Context:** HTML `<form>` sends parameters either as URL query string (GET) or request body (POST). The `action` path is relative to the current page location.
>
> ```html
> <!-- GET form: parameters appear in URL -->
> <form method="GET" action="../helloworld-get">
>   <label for="helloName">Enter your name:</label>
>   <input name="helloName" type="text"/>
>   <button type="submit">Submit</button>
>   <button type="reset">Reset the form</button>
> </form>
>
> <!-- POST form: parameters in request body, not visible in URL -->
> <form method="POST" action="../helloworld-post">
>   <label for="helloName">Enter your name:</label>
>   <input name="helloName" type="text"/>
>   <button type="submit">Submit</button>
>   <button type="reset">Reset the form</button>
> </form>
> ```
>
> **Note:** `../` is needed because servlets are at the webapp root `/` while HTML pages are under `/html/`.

> [!Example] Separate GET and POST Servlets
> ```java
> public class HelloWorldFormGetServlet extends HttpServlet {
>     public void doGet(HttpServletRequest req, HttpServletResponse res)
>             throws ServletException, IOException {
>         res.setContentType("text/html; charset=utf-8");
>         PrintWriter out = res.getWriter();
>         String name = req.getParameter("helloName");  // retrieve by input name attribute
>         out.printf("<!DOCTYPE html>%n<html lang=\"en\">...");
>         out.printf("Hello, %s!%n", name);
>         // ...
>         out.flush();
>         out.close();
>     }
> }
>
> public class HelloWorldFormPostServlet extends HttpServlet {
>     public void doPost(HttpServletRequest req, HttpServletResponse res)
>             throws ServletException, IOException {
>         res.setContentType("text/html; charset=utf-8");
>         PrintWriter out = res.getWriter();
>         String name = req.getParameter("helloName");  // same API, regardless of GET/POST
>         // ... same response writing ...
>         out.flush();
>         out.close();
>     }
> }
> ```
>
> **Key:** `req.getParameter("name")` retrieves form parameters identically for both GET and POST.

> [!Example] Unified GET+POST Servlet
> When parameter parsing is identical for both methods, delegate `doPost` to `doGet`:
>
> ```java
> public class HelloWorldFormServlet extends HttpServlet {
>
>     public void doGet(HttpServletRequest req, HttpServletResponse res)
>             throws ServletException, IOException {
>         String name = req.getParameter("helloName");
>         // ... generate response using name ...
>     }
>
>     public void doPost(HttpServletRequest req, HttpServletResponse res)
>             throws ServletException, IOException {
>         doGet(req, res);  // delegate entirely
>     }
> }
> ```

web.xml for multiple servlets with distinct URL patterns:

```xml
<servlet>
  <servlet-name>HelloWorldGet</servlet-name>
  <servlet-class>it.unipd.dei.webapp.HelloWorldFormGetServlet</servlet-class>
</servlet>
<servlet>
  <servlet-name>HelloWorldPost</servlet-name>
  <servlet-class>it.unipd.dei.webapp.HelloWorldFormPostServlet</servlet-class>
</servlet>

<servlet-mapping>
  <servlet-name>HelloWorldGet</servlet-name>
  <url-pattern>/helloworld-get</url-pattern>
</servlet-mapping>
<servlet-mapping>
  <servlet-name>HelloWorldPost</servlet-name>
  <url-pattern>/helloworld-post</url-pattern>
</servlet-mapping>
```

> [!Example] Using a Third-Party Library (Figlet)
> Add to `pom.xml` dependencies (no `provided` scope — must be in WAR):
>
> ```xml
> <dependency>
>   <groupId>com.github.dtmo.jfiglet</groupId>
>   <artifactId>jfiglet</artifactId>
>   <version>1.0.1</version>
> </dependency>
> ```
>
> Usage in servlet:
>
> ```java
> final FigletRenderer figletRenderer =
>     new FigletRenderer(FigFontResources.loadFigFontResource(FigFontResources.SLANT_FLF));
> final String output = figletRenderer.renderText("Hello, world!");
>
> out.printf("<p><pre>%n");
> out.printf("%s%n", output);   // use <pre> to preserve ASCII-art whitespace
> out.printf("</pre></p>%n");
> ```

---

## Summary Table

| Concept | Description | Notes |
|---------|-------------|-------|
| **Jakarta EE** | Standardized platform for multi-tiered enterprise apps | Formerly Java EE; moved to Eclipse Foundation in 2018 |
| **Web container** | Runtime that executes web components | Tomcat 11 implements Jakarta EE |
| **Servlet** | Java class generating dynamic HTTP responses | Extends `HttpServlet`; not thread-safe |
| **Servlet lifecycle** | `init()` → `service()` [×N] → `destroy()` | Container controls instantiation and destruction |
| **`doGet` / `doPost`** | HTTP-method-specific handlers called by `service()` | Override these, not `service()` directly |
| **`HttpServletRequest`** | Encapsulates the incoming HTTP request | `getParameter(name)` for form fields |
| **`HttpServletResponse`** | Encapsulates the outgoing HTTP response | `setContentType()` + `getWriter()` |
| **`web.xml`** | Deployment descriptor: declares servlets, URL mappings | Lives in `WEB-INF/`; not accessible to browsers |
| **WAR** | Web ARchive — deployable package for web apps | `<packaging>war</packaging>` in Maven |
| **`scope=provided`** | Servlet API dependency not bundled in WAR | Tomcat already provides it at runtime |
| **Log4J 2** | Logging framework: Loggers → Appenders → Layouts | `TRACE < DEBUG < INFO < WARN < ERROR < FATAL` |
| **ThreadContext (MDC)** | Per-thread key-value store for log context | Set before processing, remove in `finally` |
| **`Filter`** | Intercepts requests/responses before/after servlet | Used for auth, compression, logging |

## Questions

1. How do the browser and web server components cooperate to transform an HTTP request into a rendered response?
2. What distinguishes server-side web technologies such as servlets and JSP from client-side technologies such as JavaScript?
3. What is the role of Jakarta EE, and why is Tomcat considered an implementation of the web container part of that platform?
4. Why does the package transition from `javax.*` to `jakarta.*` matter when choosing a Tomcat version and servlet API dependency?
5. What makes a servlet a dynamic web component, and why is it not safe to store request-specific state in servlet instance variables?
6. How do `Servlet`, `GenericServlet`, `HttpServlet`, `HttpServletRequest`, and `HttpServletResponse` relate in the servlet class model?
7. What happens during the servlet lifecycle from first request through `init()`, repeated `service()` calls, and `destroy()`?
8. How does the first request sequence differ from subsequent requests in the servlet sequence diagram?
9. Why is `WEB-INF/` not directly accessible from the browser, and what kinds of files belong there?
10. How does `web.xml` connect servlet classes to URL patterns, and why can one servlet have multiple mappings?
11. Why must a servlet web application use WAR packaging, and how does Maven help produce the deployable archive?
12. Why is the servlet API dependency marked as `provided`, while libraries such as Log4J or Figlet must be bundled in the WAR?
13. What are the essential response-generation steps in the HelloWorld servlet, from setting the MIME type to closing the writer?
14. How does Log4J ThreadContext improve request logging, and why must the context be cleared in a `finally` block?
15. How do GET and POST forms differ in where parameters are sent, and why can `req.getParameter()` retrieve values for both?
