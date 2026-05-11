# 05-webapp-2025-26-servlet

_Source: `05-webapp-2025-26-servlet.pdf`_

## Slide 1 - Introduction to Java Servlet

Introduction to Java Servlet

Web Applications
Master Degree in Computer Engineering

Master Degree in Cybersecurity
Master Degree in ICT for Internet and Multimedia

Academic Year 2025/2026

Nicola Ferro

Intelligent Interactive Information Access (IIIA) Hub

## Slide 2 - Outline

Outline

Technologies for Web applications

Java Servlet

Apache Tomcat

Servlet Examples

![Figura 1 dalla slide 2](assets/slide-002-fig-01.jpg)

## Slide 3 - Web Application

Web Application

Technologies

![Figura 1 dalla slide 3](assets/slide-003-fig-01.jpg)

## Slide 4 - Browser and Server Architecture

Browser and Server Architecture

Web Browser
Web Server

HTTP Request

Browser/Rendering

Engine

Request
Analysis

Access
Control

Document Object Model

Resource Handler

(DOM)

Logging

Networking

Networking

User Interface

HTTP Response

Static
Resources

Dynamic
Resources

Parsing

Engine
Scripting

Engine

![Figura 1 dalla slide 4](assets/slide-004-fig-01.jpg)

## Slide 5 - Some Technologies for Web Applications

Some Technologies for Web Applications

Web Applications

Server-side Processing
Client-side Processing

Programs
Scripts
Programs
Scripts

CGI

ASP/ASP.NET (Core)

Java Applet

JavaScript

Java Servlet

JSP

ActiveX

VBScript

Adobe Flash

PHP

Apache Flex

Ruby on Rails

AJAX (Web 2.0)

Django (Python via WSGI)

![Figura 1 dalla slide 5](assets/slide-005-fig-01.jpg)

![Figura 2 dalla slide 5](assets/slide-005-fig-02.jpg)

![Figura 3 dalla slide 5](assets/slide-005-fig-03.jpg)

![Figura 4 dalla slide 5](assets/slide-005-fig-04.jpg)

## Slide 6 - Java Servlet

Java Servlet

![Figura 1 dalla slide 6](assets/slide-006-fig-01.jpg)

## Slide 7 - Jakarta Enterprise Edition

Jakarta Enterprise Edition

The Jakarta Enterprise Edition (Jakarta EE) platform aims at

standardise and reduce the complexity of developing multi-tiered enterprise applications

provide specific API for Web development, e.g. servlet, REST

formerly Java Enterprise Edition (Java EE), even formerly Java 2 Enterprise Edition (J2EE)

Web container: implements the API defined by Java EE and allows for executing applications

Web component: is a part of a Web application (servlet, JSP, …) hosted and executed by the Web container

Java EE 7

Java EE 8

Jakarta EE 9.1

Jakarta EE 10

Jakarta EE 11

Jakarta EE 12

Jakarta EE 9

Java EE 6

Jakarta EE 8

Servlet 3.1
JSP 2.3
JSTL 1.2
EL 3.0
JavaMail 1.5

Servlet 4.0
JSP 2.3
JSTL 1.2
EL 3.0
JavaMail 1.6

Servlet 5.0
JSP 3.0
JSTL 2.0
EL 4.0
Mail 2.0

Servlet 6.0
JSP 3.1
JSTL 3.0
EL 5.0
Mail 2.1

Servlet 6.1
JSP 4.0
JSTL 3.0.1
EL 6.0
Mail 2.1.2

Servlet 6.2
JSP 4.1
JSTL 3.1
EL 6.1
Mail 2.2

 Websocket

 HTTP/2

Java EE 5

Servlet 5.0
JSP 3.0
JSTL 2.0.0
EL 4.0.0
Mail 2.0.0

 JSON

Servlet 3.0
JSP 2.2
JSTL 1.2
EL 2.2
JavaMail 1.4

Java SE 8
[Java SE 11]

Java SE 11
[Java SE 17]

Java SE 8

 HTML5

Servlet 4.0.3
JSP 2.3.5
JSTL 1.2.4
EL 3.0
JavaMail 1.6.4

Java SE 17
[Java SE 21]

Java SE 21
[Java SE 25]

Java SE 8

 REST Web Services

Java SE 7

 Dependency Injection

Java SE 8

Servlet 2.5
JSP 2.1
JSTL 1.2
EL 2.1
JavaMail 1.4

J2EE 1.4

Java SE 6

 Annotations

Java SE 5

J2EE 1.3

Servlet 2.4
JSP 2.0
JSTL 1.0
EL 1.0
JavaMail 1.3

J2EE 1.2

 SOAP Web Services

JDBC 2.0 Extensions
Servlet 2.3
JSP 1.2
JavaMail 1.2

J2SE 1.4

JDBC 2.0 Extensions
Servlet 2.2
JSP 1.1
JNDI 1.2
JavaMail 1.1

 Connector Architect.

JPE Project

J2SE 1.2

J2SE 1.3

May 1998

Dec. 1999

Sept. 2001

Nov. 2003

May 2006

Dec. 2009

May 2013

Aug. 2017

Sept. 2019

Nov. 2020

May 2021

Sept. 2022

10 specs

11 specs

17 specs

24 specs

29 specs

33 specs

33 specs

28 specs

30 specs

33 specs

33 specs

Jul. 2024
32 specs

Jul. 2026
32 specs

Sun Microsystems
Oracle
Eclipse Foundation

Eclipse Foundation (2024). Jakarta EE Platform 11
https://jakarta.ee/specifications/platform/11/

![Figura 1 dalla slide 7](assets/slide-007-fig-01.jpg)

## Slide 8 - Jakarta EE

Jakarta EE

https://jakarta.ee/

Since 2018, Java EE has migrated
into the open source Jakarta EE
project under the Eclipse
Foundation

Jakarta EE 8 is the same as Java EE
8, just renaming Java into Jakarta

Jakarta EE 9 targeted package name
changes from javax.* into
jakarta.*

Jakarta@Eclipse has not to be
confounded with an Apache Software
Foundation sub-project, retired in
2011, aimed at developing open
source Java solutions, e.g. Maven,
Tomcat, Lucene, …

![Figura 1 dalla slide 8](assets/slide-008-fig-01.jpg)

## Slide 9 - Java EE: Multi-tiered Applications

Java EE: Multi-tiered Applications

![Figura 1 dalla slide 9](assets/slide-009-fig-01.jpg)

## Slide 10 - Java Servlet

Java Servlet

A servlet is a Java technology-based Web component, managed by a
container, that generates dynamic content

Servlets are platform-independent Java classes that are compiled to
platform-neutral byte code that can be loaded dynamically into and run by
a Java technology-enabled Web server

A servlet container may send concurrent requests to a servlet. To handle the
requests, the developer must make adequate provisions for concurrent
processing with multiple threads

servlets are not thread-safe

Servlets are part of JakartaEE platform and they are contained in the
jakarta.servlet and jakarta.servlet.http packages

Note that, up to JavaEE 8, the packages were named javax.servlet and

javax.servlet.http

Jakarta EE (2024). Jakarta Servlet Specification – Version 6.1
https://jakarta.ee/specifications/servlet/6.1/

![Figura 1 dalla slide 10](assets/slide-010-fig-01.jpg)

![Figura 2 dalla slide 10](assets/slide-010-fig-02.jpg)

## Slide 11 - Java Servlet UML Class Diagram

Java Servlet UML Class Diagram

![Figura 1 dalla slide 11](assets/slide-011-fig-01.jpg)

## Slide 12 - Java Servlet UML Class Diagram

Java Servlet UML Class Diagram

![Figura 1 dalla slide 12](assets/slide-012-fig-01.jpg)

## Slide 13 - Java Servlet UML Class Diagram

Java Servlet UML Class Diagram

## Slide 14 - Java Servlet UML Class Diagram

Java Servlet UML Class Diagram

## Slide 15 - Java Servlet UML Class Diagram

Java Servlet UML Class Diagram

## Slide 16 - Java Servlet UML Class Diagram

Java Servlet UML Class Diagram

![Figura 1 dalla slide 16](assets/slide-016-fig-01.jpg)

## Slide 17 - jakarta.servlet Main Classes

jakarta.servlet Main Classes

Servlet: defines methods that all servlets must implement

ServletRequest: defines an object to provide client request information to a

servlet

ServletResponse: Defines an object to assist a servlet in sending a response to the

client

ServletConfig: a servlet configuration object used by a servlet container to pass

information to a servlet during initialization

ServletContext: defines a set of methods that a servlet uses to communicate with

its servlet container, for example, to get the MIME type of a file, dispatch requests, or
write to a log file

Filter: performs filtering tasks on either the request to a resource (a servlet or static

content), or on the response from a resource, or both. Filters are used for:
authentication; logging and auditing; image conversion; data compression; and, more

## Slide 18 - jakarta.servlet.http Main Classes

jakarta.servlet.http Main Classes

HttpServlet: Provides an abstract class to be subclassed to create an HTTP

servlet suitable for a Web application

All your servlets will extend this calls

HttpServletRequest: extends the ServletRequest interface to provide

request information for HTTP servlets.

HttpServletResponse: extends the ServletResponse interface to provide

HTTP-specific functionality in sending a response

Cookie: creates a cookie, a small amount of information sent by a servlet to a Web

browser, saved by the browser, and later sent back to the server

HttpSession: provides a way to identify a user across more than one page

request or visit to a Web site and to store information about that user

Part: represents a part as uploaded to the server as part of a multipart/form-

data request body. The part may represent either an uploaded file or form data.

## Slide 19 - Servlet LifeCycle

Servlet LifeCycle

init(ServletConfig): called by the servlet container to indicate to a servlet that the servlet is being placed into

service. The servlet container calls the init method exactly once after instantiating the servlet. The init method

must complete successfully before the servlet can receive any requests

the ServletConfig object gives also access to a ServletContext object which defines a servlet’s view of the Web application within

which the servlet is running and allows for servlet-container communication

service(ServletRequest, ServletResponse): called by the servlet container to allow the servlet to

respond to a request

Servlets typically run inside multithreaded servlet containers that can handle multiple requests concurrently. Developers must be
aware to synchronize access to any shared resources such as files, network connections, and as well as the servlet's class and
instance variables

In the case of an HttpServlet this method is specialised by methods for each HTTP request

doGet(HttpServletRequest, HttpServletResponse): called by the server (via the service method) to allow a servlet to handle a GET request

doPost(HttpServletRequest, HttpServletResponse): called by the server (via the service method) to allow a servlet to handle a POST request

doPUT(HttpServletRequest, HttpServletResponse): called by the server (via the service method) to allow a servlet to handle a PUT request

doDelete(HttpServletRequest, HttpServletResponse): called by the server (via the service method) to allow a servlet to handle a DELETE

request

destroy(): called by the servlet container to indicate to a servlet that the servlet is being taken out of service. This

method is only called once all threads within the servlet’s service method have exited or after a timeout period has

passed. After the servlet container calls this method, it will not call the service method again on this servlet. This

method gives the servlet an opportunity to clean up any resources that are being held (for example, memory, file
handles, threads) and make sure that any persistent state is synchronized with the servlet's current state in memory.

## Slide 20 - Apache Tomcat

Apache Tomcat

![Figura 1 dalla slide 20](assets/slide-020-fig-01.jpg)

## Slide 21 - Apache Tomcat

Apache Tomcat

http://tomcat.apache.org/

Tomcat 10 (and onwards) implement
Jakarta EE, so everything is in the
jakarta.* package

Tomcat 9 implements Java EE, so
everything is in the javax.* package

We use Tomcat 11

![Figura 1 dalla slide 21](assets/slide-021-fig-01.jpg)

## Slide 22 - Apache Tomcat Documentation

Apache Tomcat Documentation

https://tomcat.apache.org/tomcat-11.0-doc/index.html

![Figura 1 dalla slide 22](assets/slide-022-fig-01.jpg)

## Slide 23 - Hello World HTML

Hello World HTML

![Figura 1 dalla slide 23](assets/slide-023-fig-01.jpg)

## Slide 24 - Hello World in HTML

Hello World in HTML

![Figura 1 dalla slide 24](assets/slide-024-fig-01.jpg)

## Slide 25 - Example of Hello World HTML Page

Example of Hello World HTML Page

<!DOCTYPE html>¬
<html lang="en">¬

<head>¬

<meta charset="utf-8">¬
¬

<meta name="description" content="Example of Hello World in HTML">¬
<meta name="author" content="Nicola Ferro">¬
¬

<title>¬

Hello World in HTML¬
</title>¬
</head>¬
<body>¬

<h1>¬

Example of use of the meta
element to provide metadata
about the page, often exploited

by search engines

Hello World in HTML¬
</h1>¬
<hr /> ¬
<p>¬

Hello, world! ¬
</p>¬
</body>¬
</html>¬

![Figura 1 dalla slide 25](assets/slide-025-fig-01.jpg)

## Slide 26 - Setup the Project Directory Structure

Setup the Project Directory Structure

src




development version

main



sources for the main application

database




sources for the database, e.g. schema creation SQL

java





sources for the Java application, also servlets

resources



any additional application resource, e.g. property files

webapp



sources for the Web application

css





CSS files

html




HTML files

js






JavaScript files

jsp





JSP pages

media





images and other media

WEB-INF




configuration for the web application, web.xml

test



sources for the test, e.g. JUnit

javadoc



documentation

target


folder for compiled code and packages

![Figura 1 dalla slide 26](assets/slide-026-fig-01.jpg)

## Slide 27 - The web.xml Configuration File

The web.xml Configuration File

Identifi

Information about the
webapp to be displayed
within Tomcat

<?xml version="1.0" encoding="UTF-8"?>¬
¬
<web-app id="hello-world-webapp" version="4.0" xmlns="http://xmlns.jcp.org/xml/ns/javaee"¬

xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"¬
xsi:schemaLocation="http://java.sun.com/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd">¬
    ¬

<display-name>Hello World HTML</display-name>¬
<description>Example of minimal HTML page writing "Hello, world!"</description>¬
¬

<welcome-file-list>¬

<welcome-file>/html/hello.html</welcome-file>¬
</welcome-file-list>¬
¬
</web-app>¬

List of fi

f
ifi

## Slide 28 - Configuration of the Maven Project

Configuration of the Maven Project

process-
resources

resources
resources

compile

compile
compiler

process-
test-resources

You need to create a WAR
(Web ARchive) fi

testResources
resources

test-compile

You use the war plugin.

testCompile
compile

test

test
surﬁre

package

war
war

install

install
install

deploy

deploy
deploy

POM

![Figura 1 dalla slide 28](assets/slide-028-fig-01.jpg)

## Slide 29 - Project Object Model (POM)

Project Object Model (POM)

<?xml version="1.0"?>¬
¬
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"¬

xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">¬
<modelVersion>4.0.0</modelVersion>¬
¬

<groupId>it.unipd.dei.webapp</groupId>¬
¬

<artifactId>hello-world-html</artifactId>¬
¬
<version>1.00</version>¬
¬

<packaging>war</packaging>¬
¬

Packaging is war to produce
a fi

<!-- Project description elements -->¬
<name>Hello World in HTML</name>¬
¬

<description>Basic HTML page saying "Hello, world!"</description>¬
¬

<url>https://bitbucket.org/frrncl/webapp-unipd</url>¬
¬

<inceptionYear>2019</inceptionYear>¬
¬

<developers>¬

<developer>¬

<id>nf</id>¬
<name>Nicola Ferro</name>¬
<email>ferro@dei.unipd.it</email>¬
<url>http://www.dei.unipd.it/~ferro/</url>¬
</developer>¬
</developers>¬
¬

<licenses>¬

<license>¬

<name>The Apache Software License, Version 2.0</name>¬
<url>http://www.apache.org/licenses/LICENSE-2.0.txt</url>¬
<distribution>repo</distribution>¬
</license>¬
</licenses>¬
¬

<organization>¬

<name>Department of Information Engineering (DEI), University of Padua, Italy</name>¬
<url>http://www.dei.unipd.it/en/</url>¬
</organization>¬
¬

<!-- Build settings -->¬
¬
<!-- Specifies the encoding to be used for project source files -->¬
<properties>¬

<project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>¬
</properties>¬
¬
<!-- Configuration of the default build lifecycle -->¬
<build>¬

<defaultGoal>compile</defaultGoal>¬
¬
<!-- source code folder -->¬
<sourceDirectory>${basedir}/src/main/java</sourceDirectory>¬
¬
<!-- compiled code folder -->¬
<directory>${basedir}/target</directory>¬
¬
<!-- name of the generated package -->¬
<finalName>${project.artifactId}-${project.version}</finalName>¬

![Figura 1 dalla slide 29](assets/slide-029-fig-01.jpg)

## Slide 30 - Project Object Model (POM)

Project Object Model (POM)

<!-- configuration of the plugins for the different goals -->¬
<plugins>¬
¬

<!-- compiler plugin: source and target code is for Java 1.8 -->¬
<plugin>¬

<groupId>org.apache.maven.plugins</groupId>¬
<artifactId>maven-compiler-plugin</artifactId>¬
<version>3.8.0</version>¬
<configuration>¬

<source>1.8</source>¬
<target>1.8</target>¬
</configuration>¬
</plugin>¬
¬
¬
<!-- javadoc plugin: output in the javadoc folder -->¬
<plugin>¬

You need to specify to the war plugin
where the web.xml fi

<groupId>org.apache.maven.plugins</groupId>¬
<artifactId>maven-javadoc-plugin</artifactId>¬
<version>3.1.0</version>¬
<configuration>¬

<reportOutputDirectory>${basedir}/javadoc</reportOutputDirectory>¬
<author>true</author>¬
<nosince>false</nosince>¬
<show>protected</show>¬
</configuration>¬
</plugin>¬

<!-- packager plugin: create a WAR file to be deployed -->¬
<plugin>¬

<groupId>org.apache.maven.plugins</groupId>¬
<artifactId>maven-war-plugin</artifactId>¬
<version>3.2.2</version>¬
<configuration>¬

<webXml>${basedir}/src/main/webapp/WEB-INF/web.xml</webXml>¬
</configuration>¬
</plugin>
¬
</plugins>¬
¬

![Figura 1 dalla slide 30](assets/slide-030-fig-01.jpg)

## Slide 31 - Cleaning, Compiling, Packaging

Cleaning, Compiling, Packaging

![Figura 1 dalla slide 31](assets/slide-031-fig-01.jpg)

## Slide 32 - Deploying and Run the Web Application

Deploying and Run the Web Application

http://localhost:8080/manager/html/

![Figura 1 dalla slide 32](assets/slide-032-fig-01.jpg)

## Slide 33 - Deploying and Run the Web Application

Deploying and Run the Web Application

Select the war fi

![Figura 1 dalla slide 33](assets/slide-033-fig-01.jpg)

## Slide 34 - Deploying and Run the Web Application

Deploying and Run the Web Application

If the Web application is correctly installed and running, the Start
button is not enable.

You can press the Stop button to stop the Web application from
running.

You can press the Undeploy  button to un-install the Web application.

![Figura 1 dalla slide 34](assets/slide-034-fig-01.jpg)

## Slide 35 - Deploying and Run the Web Application

Deploying and Run the Web Application

You see the HTML page from the webapp root because
you have specifi
fi

fi

![Figura 1 dalla slide 35](assets/slide-035-fig-01.jpg)

## Slide 36 - Where is my Webapp?

Where is my Webapp?

![Figura 1 dalla slide 36](assets/slide-036-fig-01.jpg)

## Slide 37 - Where is my Webapp?

Where is my Webapp?

![Figura 1 dalla slide 37](assets/slide-037-fig-01.jpg)

![Figura 2 dalla slide 37](assets/slide-037-fig-02.jpg)

## Slide 38 - HelloWorld Servlet

HelloWorld Servlet

![Figura 1 dalla slide 38](assets/slide-038-fig-01.jpg)

## Slide 39 - The HelloWorld Servlet

The HelloWorld Servlet

HelloWorldServlet extends HttpServlet {¬
¬

public void doGet(HttpServletRequest req, HttpServletResponse res)¬

Set the Content-Type HTTP response header

throws ServletException, IOException {¬
¬

// set the MIME media type of the response¬
res.setContentType("text/html; charset=utf-8");¬
¬

Obtain a Writer to send the response body

// get a stream to write the response¬
PrintWriter out = res.getWriter();¬
¬

Write the HTML page line-by-line

// write the HTML page¬
out.printf("<!DOCTYPE html>%n");¬
¬
out.printf("<html lang=\"en\">%n");¬
out.printf("<head>%n");¬
out.printf("<meta charset=\"utf-8\">%n");¬
out.printf("<title>HelloWorld Servlet Response</title>%n");¬
out.printf("</head>%n");¬
¬

Flush the buffer

(don’t forget)

out.printf("<body>%n");¬
out.printf("<h1>HelloWorld Servlet Response</h1>%n");¬
out.printf("<hr/>%n");¬
out.printf("<p>%n");¬
out.printf("Hello, world!%n");¬
out.printf("</p>%n");¬
out.printf("</body>%n");¬
¬
out.printf("</html>%n");¬
¬

Close the output stream

// flush the output stream buffer¬
out.flush();¬
¬

Write a “log” statment

// close the output stream¬
out.close();¬
¬

// write a "log" statement¬
System.out.printf("[INFO] HelloWorldServlet - %s - Request successfully served.%n",¬

  new Timestamp(System.currentTimeMillis()).toString());¬
¬

}¬
¬
}¬

## Slide 40 - Run the Web Application

Run the Web Application

![Figura 1 dalla slide 40](assets/slide-040-fig-01.jpg)

## Slide 41 - Calling the HelloWorld Servlet

Calling the HelloWorld Servlet

![Figura 1 dalla slide 41](assets/slide-041-fig-01.jpg)

## Slide 42 - Getting Out More from the Browser

Getting Out More from the Browser

![Figura 1 dalla slide 42](assets/slide-042-fig-01.jpg)

## Slide 43 - Getting Out More from the Browser

Getting Out More from the Browser

![Figura 1 dalla slide 43](assets/slide-043-fig-01.jpg)

## Slide 44 - Getting Out More from the Browser

Getting Out More from the Browser

![Figura 1 dalla slide 44](assets/slide-044-fig-01.jpg)

## Slide 45 - HelloWorld Servlet: What’s Going On? The Sequence Diagram

HelloWorld Servlet: What’s Going On? The Sequence Diagram

![Figura 1 dalla slide 45](assets/slide-045-fig-01.jpg)

## Slide 46 - Where are the logs?

Where are the logs?

![Figura 1 dalla slide 46](assets/slide-046-fig-01.jpg)

## Slide 47 - Where are the logs?

Where are the logs?

![Figura 1 dalla slide 47](assets/slide-047-fig-01.jpg)

## Slide 48 - Where are the logs?

Where are the logs?

![Figura 1 dalla slide 48](assets/slide-048-fig-01.jpg)

## Slide 49 - Setup the Project Directory Structure

Setup the Project Directory Structure

src




development version

main




sources for the main application

database



sources for the database, e.g. schema creation SQL

java




sources for the Java application, also servlets

resources



any additional application resource, e.g. property files

webapp




sources for the Web application

 css





CSS files

 html





HTML files

 js






JavaScript files

 jsp





JSP pages

 media





images and other media

 WEB-INF




configuration for the web application, web.xml

test




sources for the test, e.g. JUnit

javadoc


documentation

target



folder for compiled code and packages

![Figura 1 dalla slide 49](assets/slide-049-fig-01.jpg)

## Slide 50 - The web.xml Configuration File

The web.xml Configuration File

<?xml version="1.0" encoding="UTF-8"?>

Defi

fi

The HelloWorld servlet is associated with
three diff

When the Web container receives a GET
request for the /helloword (or /hello or /
ciao) URI, it understand it is a dynamic
resource, instantiates the HelloWorld servlet,
and calls its doGet methods to answer the

<web-app id="hello-world-webapp" version="4.0" xmlns="http://xmlns.jcp.org/xml/ns/javaee"
 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 xsi:schemaLocation="http://java.sun.com/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd">

 <display-name>Hello World Servlet</display-name>
 <description>Example of minimal servlet answering "Hello, world!" to a GET request.</description>
  <!-- HelloWorld Servlet -->
 <servlet>
  <servlet-name>HelloWorld</servlet-name>
  <servlet-class>it.unipd.dei.webapp.HelloWorldServlet</servlet-class>
 </servlet>

 <!-- Mapping between servlets and URIs -->
 <servlet-mapping>
  <servlet-name>HelloWorld</servlet-name>
  <url-pattern>/helloworld</url-pattern>
 </servlet-mapping>
 <servlet-mapping>
  <servlet-name>HelloWorld</servlet-name>
  <url-pattern>/hello</url-pattern>
 </servlet-mapping>
  <servlet-mapping>
  <servlet-name>HelloWorld</servlet-name>
  <url-pattern>/ciao</url-pattern>
 </servlet-mapping>

request

![Figura 1 dalla slide 50](assets/slide-050-fig-01.jpg)

## Slide 51 - Configuration of the Maven Project

Configuration of the Maven Project

process-
resources

resources
resources

compile

compile
compiler

process-
test-resources

You need to create a WAR
(Web ARchive) fi

testResources
resources

test-compile

You use the war plugin.

testCompile
compile

test

test
surﬁre

package

war
war

install

install
install

deploy

You need to add the

deploy
deploy

POM

dependency on
javaee.servlet

![Figura 1 dalla slide 51](assets/slide-051-fig-01.jpg)

## Slide 52 - Project Object Model (POM)

Project Object Model (POM)

<?xml version="1.0"?>

<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
 <modelVersion>4.0.0</modelVersion>

 <groupId>it.unipd.dei.webapp</groupId>

 <artifactId>hello-world-servlet</artifactId>
  <version>1.00</version>

 <packaging>war</packaging>

Packaging is war to produce
a fi

 <!-- Project description elements -->
 <name>Replies Hello World</name>

 <description>Basic servlet replying "Hello, world!" to a GET request.</description>

 <url>https://bitbucket.org/frrncl/webapp-unipd</url>

 <inceptionYear>2018</inceptionYear>

 <developers>
  <developer>
   <id>nf</id>
   <name>Nicola Ferro</name>
   <email>ferro@dei.unipd.it</email>
   <url>http://www.dei.unipd.it/~ferro/</url>
  </developer>
 </developers>

 <licenses>
  <license>
   <name>The Apache Software License, Version 2.0</name>
   <url>http://www.apache.org/licenses/LICENSE-2.0.txt</url>
   <distribution>repo</distribution>
  </license>
 </licenses>

 <organization>
  <name>Department of Information Engineering (DEI), University of Padua, Italy</name>
  <url>http://www.dei.unipd.it/en/</url>
 </organization>

 <!-- Build settings -->
  <!-- Specifies the encoding to be used for project source files -->
 <properties>
  <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
 </properties>

![Figura 1 dalla slide 52](assets/slide-052-fig-01.jpg)

## Slide 53 - Project Object Model (POM)

Project Object Model (POM)

  <!-- Configuration of the default build lifecycle -->
 <build>
  <defaultGoal>compile</defaultGoal>
    <!-- source code folder -->
  <sourceDirectory>${basedir}/src/main/java</sourceDirectory>
    <!-- compiled code folder -->
  <directory>${basedir}/target</directory>
    <!-- name of the generated package -->
  <finalName>${project.artifactId}-${project.version}</finalName>

You need to add the dependency on the servlet
API.

  <!-- configuration of the plugins for the different goals -->
  <plugins>
     <!-- compiler plugin: source and target code is for Java 1.8 -->
   <plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-compiler-plugin</artifactId>
    <version>3.7.0</version>
    <configuration>
     <source>1.8</source>
     <target>1.8</target>
    </configuration>
   </plugin>
         <!-- javadoc plugin: output in the javadoc folder -->
   <plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-javadoc-plugin</artifactId>
    <version>3.0.0</version>
    <configuration>
     <reportOutputDirectory>${basedir}/javadoc</reportOutputDirectory>
     <author>true</author>
     <nosince>false</nosince>
     <show>protected</show>
    </configuration>
   </plugin>

   <!-- packager plugin: create a WAR file to be deployed -->
   <plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-war-plugin</artifactId>
    <version>3.2.0</version>
    <configuration>
     <webXml>${basedir}/src/main/webapp/WEB-INF/web.xml</webXml>
    </configuration>
   </plugin>
   </plugins>
 </build>

However, the Web container (Tomcat) already has
this API installed. Therefore, you set scope to
provided to indicate that the libraries are
needed at compilation time on the local machine
but they will be available in the deployment
environment and so you do not need to package

them in the war fi

 <!-- Dependencies -->
 <dependencies>
  <dependency>
   <groupId>javax.servlet</groupId>
   <artifactId>javax.servlet-api</artifactId>
   <version>4.0.0</version>
   <scope>provided</scope>
  </dependency>
 </dependencies>

![Figura 1 dalla slide 53](assets/slide-053-fig-01.jpg)

## Slide 54 - HelloWorld Servlet with

HelloWorld Servlet with

Logging

![Figura 1 dalla slide 54](assets/slide-054-fig-01.jpg)

## Slide 55 - More Serious Logging?

More Serious Logging?

http://logging.apache.org/log4j/2.x/index.html

![Figura 1 dalla slide 55](assets/slide-055-fig-01.jpg)

## Slide 56 - The Project Structure

The Project Structure

Now it makes use of log
statements

Provides the log context for
the application

Confi

Add dependencies on Log4J

![Figura 1 dalla slide 56](assets/slide-056-fig-01.jpg)

## Slide 57 - The LogContext

The LogContext

Helper class to manage the
ThreadContext by Log4J in

a principled way

We defi

For each of those keys, we have a
couple of methods for setting/
removing a value for that key

import org.apache.logging.log4j.ThreadContext;¬
¬
¬
public final class LogContext {¬
¬
    private static final String USER = "USER";¬
¬
    private static final String IP = "IP";¬
¬
    private static final String ACTION = "ACTION";¬
¬
    private static final String RESOURCE = "RESOURCE";¬
¬
    public static void setUser(final String user) {¬
        if (user != null && !user.isEmpty()) {¬
            ThreadContext.put(USER, user);¬
        }¬
    }¬
¬
    public static void removeUser() {¬
        ThreadContext.remove(USER);¬
    }¬
¬
    public static void setIPAddress(final String ip) {¬
        if (ip != null && !ip.isEmpty()) {¬
            ThreadContext.put(IP, ip);¬
        }¬
    }¬
¬
    public static void removeIPAddress() {¬
        ThreadContext.remove(IP);¬
    }¬
¬
    public static void setAction(final String action) {¬
        if (action != null) {¬
            ThreadContext.put(ACTION, action);¬
        }¬
    }¬
¬
    public static void removeAction() {¬
        ThreadContext.remove(ACTION);¬
    }¬
¬
    public static void setResource(final String resource) {¬
        if (resource != null && !resource.isEmpty()) {¬
            ThreadContext.put(RESOURCE, resource);¬
        }¬
    }¬
¬
    public static void removeResource() {¬
        ThreadContext.remove(RESOURCE);¬
    }¬
¬
    private LogContext() {¬
        throw new AssertionError(String.format("No instances of %s allowed.", LogContext.class.getName()));¬
    }¬
}¬

## Slide 58 - The HelloWorld Servlet with Logging

The HelloWorld Servlet with Logging

Obtain a new Logger from Log4J

Set contextual log information (will
be part of the log messages)

Writes an INFO log message

Writes an ERROR log message, together
with the stack trace of the exception

Ensures that the log context is
cleared in any case

¬
public class HelloWorldServlet extends HttpServlet {¬
¬
    /**¬
     * A LOGGER available for all the subclasses.¬
     */¬
    protected static final Logger LOGGER = LogManager.getLogger(HelloWorldServlet.class,¬
            StringFormatterMessageFactory.INSTANCE);¬
¬
    public void doGet(HttpServletRequest req, HttpServletResponse res)¬
            throws IOException {¬
¬
        LogContext.setIPAddress(req.getRemoteAddr());¬
        LogContext.setResource(req.getRequestURI());¬
        LogContext.setAction("HELLO_WORLD");¬
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
            out.printf("<title>HelloWorld Servlet Response with Logging</title>%n");¬
            out.printf("</head>%n");¬
¬
            out.printf("<body>%n");¬
            out.printf("<h1>HelloWorld Servlet with Logging Response</h1>%n");¬
            out.printf("<hr/>%n");¬
            out.printf("<p>%n");¬
            out.printf("Hello, world!%n");¬
            out.printf("</p>%n");¬
            out.printf("</body>%n");¬
¬
            out.printf("</html>%n");¬
¬
            // flush the output stream buffer¬
            out.flush();¬
¬
            // close the output stream¬
            out.close();¬
¬
            // write a "log" statement¬
            LOGGER.info("Request successfully served.");¬
¬
        } catch(Exception e) {¬
            LOGGER.error("Unable to serve request.", e);¬
            throw e;¬
        } finally {¬
            LogContext.removeIPAddress();¬
            LogContext.removeAction();¬
            LogContext.removeResource();¬
        }¬
¬
    }¬
¬
}¬

## Slide 59 - The log4j2.xml Configuration File

The log4j2.xml Configuration File

https://logging.apache.org/log4j/2.x/manual/configuration.html

<Configuration status="INFO" monitorInterval="0" name="hello-lo4j">¬
    <Appenders>¬
        <RollingRandomAccessFile name="RFILE"
fileName="${sys:catalina.base}/webapps/my-logs/hello-log4j.log"
filePattern="${sys:catalina.base}/webapps/my-logs/$${date:yyyy-MM}/hello-log4j-%d{yyyyMMdd}-%i.log.gz">¬
            <PatternLayout>¬
                <Pattern>%date{DEFAULT} %level [%thread] %class{1}.%method(%file:%line)%n\tIP = %MDC{IP};
USER = %MDC{USER}; ACTION = %MDC{ACTION}; RESOURCE = %MDC{RESOURCE}%n\t%message%n\t%throwable%n</Pattern>¬
            </PatternLayout>¬
            <Policies>¬
                <TimeBasedTriggeringPolicy />¬
                <SizeBasedTriggeringPolicy size="250 MB"/>¬
            </Policies>¬
        </RollingRandomAccessFile>¬
        <Console name="STDOUT" target="SYSTEM_OUT">¬
            <PatternLayout>¬
                <Pattern>%date{DEFAULT} %level [%thread] %class{1}.%method(%file:%line)%n\tIP = %MDC{IP};
USER = %MDC{USER}; ACTION = %MDC{ACTION}; RESOURCE = %MDC{RESOURCE}%n\t%message%n\t%throwable%n</Pattern>¬
            </PatternLayout>¬
        </Console>¬
    </Appenders>¬
    <Loggers>¬
        <Root level="TRACE">¬
            <AppenderRef ref="RFILE" level="INFO"/>¬
           <AppenderRef ref="STDOUT" level="INFO"/>¬
        </Root>¬
    </Loggers>¬
</Configuration>

## Slide 60 - The log4j2.xml Configuration File

The log4j2.xml Configuration File

Appenders are destinations for log messages

The are many how them: https://logging.apache.org/log4j/2.x/manual/
appenders.html

In our case we configured a RollingRandomAccessFileAppender, which writes to a file and
rolls over to a new file when given conditions are met, and a ConsoleAppender

 For each appender you can define the Pattern for formatting the log messages: https://
logging.apache.org/log4j/2.x/manual/layouts.html#PatternLayout

Appenders are then attached to Loggers in order to write the messages issued by a given

Logger to the destination targeted by the Appender

Loggers are organized in a hierarchical (tree) fashion

Child Loggers inherit Appenders from their parents

The root of the hierarchy is a the Logger called Root

Log messages are associated with a Level: TRACE < DEBUG < INFO < WARN <

ERROR < FATAL

For each Logger you can configure its Level and all the messages below that Level are ignored

![Figura 1 dalla slide 60](assets/slide-060-fig-01.jpg)

## Slide 61 - Project Object Model (POM)

Project Object Model (POM)

Added dependency on Log4J. It
consist of an API and its default
implementation

![Figura 1 dalla slide 61](assets/slide-061-fig-01.jpg)

## Slide 62 - Example of Logs

Example of Logs

![Figura 1 dalla slide 62](assets/slide-062-fig-01.jpg)

## Slide 63 - Example of Logs

Example of Logs

![Figura 1 dalla slide 63](assets/slide-063-fig-01.jpg)

## Slide 64 - HelloWorld Servlet

HelloWorld Servlet

using Figlet

![Figura 1 dalla slide 64](assets/slide-064-fig-01.jpg)

## Slide 65 - First Attempt: What’s Wrong?

First Attempt: What’s Wrong?

![Figura 1 dalla slide 65](assets/slide-065-fig-01.jpg)

## Slide 66 - Second Attempt: What’s Wrong, again?

Second Attempt: What’s Wrong, again?

![Figura 1 dalla slide 66](assets/slide-066-fig-01.jpg)

## Slide 67 - Final Attempt: Eventually Right

Final Attempt: Eventually Right

![Figura 1 dalla slide 67](assets/slide-067-fig-01.jpg)

## Slide 68 - The HelloWorld Servlet Using Figlet

The HelloWorld Servlet Using Figlet

public class HelloWorldServletFiglet extends HttpServlet {¬
¬

public void doGet(HttpServletRequest req, HttpServletResponse res)¬

Generate the ASCII art

throws ServletException, IOException {¬
¬

// set the MIME media type of the response¬
res.setContentType("text/html; charset=utf-8");¬
¬

// render to write ASCII-art with the given font¬
final FigletRenderer figletRenderer = new FigletRenderer(FigFontResources.loadFigFontResource(FigFontResources.SLANT_FLF));¬
¬

// ASCII-art¬
final String output = figletRenderer.renderText("Hello, world!");¬
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
out.printf("<title>HelloWorld Servlet Response</title>%n");¬
out.printf("</head>%n");¬
¬

out.printf("<body>%n");¬
out.printf("<h1>HelloWorld Servlet Response</h1>%n");¬
out.printf("<hr/>%n");¬
out.printf("<p><pre>%n");¬
out.printf("%s%n", output);¬
out.printf("</pre></p>%n");¬
out.printf("</body>%n");¬
¬
out.printf("</html>%n");¬
¬

Use <pre> to keep the

formatting

// flush the output stream buffer¬
out.flush();¬
¬

// close the output stream¬
out.close();¬
¬

// write a "log" statement¬
System.out.printf("[INFO] HelloWorldServletFiglet - %s - Request successfully served.%n",¬

  new Timestamp(System.currentTimeMillis()).toString());¬
¬

}¬
¬
}¬

## Slide 69 - The web.xml Configuration File

The web.xml Configuration File

¬
<web-app id="hello-world-webapp" version="4.0" xmlns="http://xmlns.jcp.org/xml/ns/javaee"¬

xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"¬
xsi:schemaLocation="http://java.sun.com/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd">¬
    ¬

<display-name>Hello World Servlet</display-name>¬
<description>Example of minimal servlet answering "Hello, world!" to a GET request.</description>¬
¬
<!-- HelloWorld Servlet using Figlet -->  ¬
<servlet>¬

<servlet-name>HelloWorld</servlet-name>¬
<servlet-class>it.unipd.dei.webapp.HelloWorldServletFiglet</servlet-class>¬
</servlet>¬
    ¬

<!-- Mapping between servlets and URIs -->  ¬
<servlet-mapping>¬

The web.xml fi

<servlet-name>HelloWorld</servlet-name>¬
<url-pattern>/helloworld</url-pattern>¬
</servlet-mapping>¬
<servlet-mapping>¬

<servlet-name>HelloWorld</servlet-name>¬
<url-pattern>/hello</url-pattern>¬
</servlet-mapping>¬

<servlet-mapping>¬
<servlet-name>HelloWorld</servlet-name>¬
<url-pattern>/ciao</url-pattern>¬
</servlet-mapping>¬
¬
</web-app>¬

![Figura 1 dalla slide 69](assets/slide-069-fig-01.jpg)

## Slide 70 - Project Object Model (POM)

Project Object Model (POM)

<!-- Dependencies -->¬
<dependencies>¬

<dependency>¬

<groupId>javax.servlet</groupId>¬
<artifactId>javax.servlet-api</artifactId>¬
<version>4.0.0</version>¬
<scope>provided</scope>¬
</dependency>¬
¬

<dependency>¬

<groupId>com.github.dtmo.jfiglet</groupId>¬
<artifactId>jfiglet</artifactId>¬
<version>1.0.1</version>¬
</dependency>¬
</dependencies>¬
¬
</project>
The pom.xml fi

fi

![Figura 1 dalla slide 70](assets/slide-070-fig-01.jpg)

## Slide 71 - HelloWorld Servlet with

HelloWorld Servlet with

GET and POST

![Figura 1 dalla slide 71](assets/slide-071-fig-01.jpg)

## Slide 72 - The GET and POST Forms

The GET and POST Forms

<!DOCTYPE html>
<html lang="en">
 <head>
  <meta charset="utf-8">
  <title>GET Form Example</title>
 </head>

Servlet are under the root / of the Web application,
while HTML pages are in the /html folder. So, in
the action path, you have to go up one level.

<!DOCTYPE html>
<html lang="en">
 <head>
  <meta charset="utf-8">
  <title>POST Form Example</title>
 </head>

  <body>
 <h1>GET Form Example</h1>
  <form method="GET" action="../helloworld-get">
  <label for="helloName">Enter your name:</label>
  <input name="helloName" type="text"/><br/><br/>
  <button type="submit">Submit</button><br/>
  <button type="reset">Reset the form</button>
 </form>
 </body>
</html>

The value of the name attribute
(helloName) will be used by the
servlets to access the submitted

The value of the name attribute
(helloName) will be used by the
servlets to access the submitted

form parameter

form parameter

  <body>
 <h1>POST Form Example</h1>
  <form method="POST" action="../helloworld-post">
  <label for="helloName">Enter your name:</label>
  <input name="helloName" type="text"/><br/><br/>
  <button type="submit">Submit</button><br/>
  <button type="reset">Reset the form</button>
 </form>
 </body>
</html>

## Slide 73 - The GET and POST Servlets

The GET and POST Servlets

package it.unipd.dei.webapp;

package it.unipd.dei.webapp;

import java.io.IOException;
import java.io.PrintWriter;

import java.io.IOException;
import java.io.PrintWriter;

The HTTP method to serve
The HTTP method to serve

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class HelloWorldFormGetServlet extends HttpServlet {

public class HelloWorldFormPostServlet extends HttpServlet {

 public void doGet(HttpServletRequest req, HttpServletResponse res)
   throws ServletException, IOException {

 public void doPost(HttpServletRequest req, HttpServletResponse res)
   throws ServletException, IOException {

  // set the MIME media type of the response
  res.setContentType("text/html; charset=utf-8");

  // set the MIME media type of the response
  res.setContentType("text/html; charset=utf-8");

  // get a stream to write the response
  PrintWriter out = res.getWriter();

  // get a stream to write the response
  PrintWriter out = res.getWriter();

Retrieve the form
parameter via its name

Retrieve the form
parameter via its name

  // get the name to say hello
  String name = req.getParameter("helloName");

  // get the name to say hello
  String name = req.getParameter("helloName");

  // write the HTML page
  out.printf("<!DOCTYPE html>%n");
    out.printf("<html lang=\"en\">%n");
  out.printf("<head>%n");
  out.printf("<meta charset=\"utf-8\">%n");
  out.printf("<title>HelloWorld Form Post Servlet  Response</title>%n");
  out.printf("</head>%n");

  // write the HTML page
  out.printf("<!DOCTYPE html>%n");
    out.printf("<html lang=\"en\">%n");
  out.printf("<head>%n");
  out.printf("<meta charset=\"utf-8\">%n");
  out.printf("<title>HelloWorld Form Get Servlet Response</title>%n");
  out.printf("</head>%n");

  out.printf("<body>%n");
  out.printf("<h1>HelloWorld Form Get Servlet Response</h1>%n");
  out.printf("<hr/>%n");
  out.printf("<p>%n");
  out.printf("Hello, %s!%n", name);
  out.printf("</p>%n");
  out.printf("</body>%n");
    out.printf("</html>%n");

  out.printf("<body>%n");
  out.printf("<h1>HelloWorld Form Post Servlet Response</h1>%n");
  out.printf("<hr/>%n");
  out.printf("<p>%n");
  out.printf("Hello, %s!%n", name);
  out.printf("</p>%n");
  out.printf("</body>%n");
    out.printf("</html>%n");
    // flush the output stream buffer
  out.flush();

  // flush the output stream buffer
  out.flush();

Use to value of the
form parameter to

Use to value of the
form parameter to

generate dynamic HTML

generate dynamic HTML

  // close the output stream
  out.close();

  // close the output stream
  out.close();

## Slide 74 - The web.xml Configuration File

The web.xml Configuration File

<?xml version="1.0" encoding="UTF-8"?>

<web-app id="hello-world-webapp" version="4.0" xmlns="http://xmlns.jcp.org/xml/ns/javaee"
 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 xsi:schemaLocation="http://java.sun.com/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd">

 <display-name>Hello World Servlet Form</display-name>
 <description>Example of minimal servlet answering "Hello, [name]!" to a GET or POST form request.</description>
  <!-- HelloWorldGet Servlet -->
 <servlet>
  <servlet-name>HelloWorldGet</servlet-name>
  <servlet-class>it.unipd.dei.webapp.HelloWorldFormGetServlet</servlet-class>
 </servlet>
  <!-- HelloWorldPost Servlet -->
 <servlet>
  <servlet-name>HelloWorldPost</servlet-name>
  <servlet-class>it.unipd.dei.webapp.HelloWorldFormPostServlet</servlet-class>
 </servlet>

 <!-- Mapping between servlets and URIs -->
 <servlet-mapping>
  <servlet-name>HelloWorldGet</servlet-name>
  <url-pattern>/helloworld-get</url-pattern>
 </servlet-mapping>
  <servlet-mapping>
  <servlet-name>HelloWorldPost</servlet-name>
  <url-pattern>/helloworld-post</url-pattern>
 </servlet-mapping>
</web-app>

## Slide 75 - Running: The GET Form

Running: The GET Form

![Figura 1 dalla slide 75](assets/slide-075-fig-01.jpg)

## Slide 76 - Running: The GET Form

Running: The GET Form

![Figura 1 dalla slide 76](assets/slide-076-fig-01.jpg)

## Slide 77 - Running: The GET Form

Running: The GET Form

![Figura 1 dalla slide 77](assets/slide-077-fig-01.jpg)

## Slide 78 - Running: The POST Form

Running: The POST Form

![Figura 1 dalla slide 78](assets/slide-078-fig-01.jpg)

## Slide 79 - Running: The POST Form

Running: The POST Form

![Figura 1 dalla slide 79](assets/slide-079-fig-01.jpg)

## Slide 80 - Running: The POST Form

Running: The POST Form

![Figura 1 dalla slide 80](assets/slide-080-fig-01.jpg)

## Slide 81 - Can We Manage GET and POST Together?

Can We Manage GET and POST Together?

public class HelloWorldFormServlet extends HttpServlet {¬
¬

public void doGet(HttpServletRequest req, HttpServletResponse res)¬

throws ServletException, IOException {¬
¬

// set the MIME media type of the response¬
res.setContentType("text/html; charset=utf-8");¬
¬

// get a stream to write the response¬
PrintWriter out = res.getWriter();¬
¬

// get the name to say hello¬
String name = req.getParameter("helloName");¬
¬

// write the HTML page¬
out.printf("<!DOCTYPE html>%n");¬
¬
out.printf("<html lang=\"en\">%n");¬
out.printf("<head>%n");¬
out.printf("<meta charset=\"utf-8\">%n");¬
out.printf("<title>HelloWorld Form Get&Post Servlet Response</title>%n");¬
out.printf("</head>%n");¬
¬

Since, in this case, we parse form parameters in
exactly the same way, we can simply forward the

doPost method to to doGet one.

out.printf("<body>%n");¬
out.printf("<h1>HelloWorld Form Get&Post Servlet Response</h1>%n");¬
out.printf("<hr/>%n");¬
out.printf("<p>%n");¬
out.printf("Hello, %s!%n", name);¬
out.printf("</p>%n");¬
out.printf("</body>%n");¬
¬
out.printf("</html>%n");¬
¬

What if the way of parsing parameters is different

but the rest of the processing is still the same?

// flush the output stream buffer¬
out.flush();¬
¬

// close the output stream¬
out.close();¬
¬

}¬
¬

public void doPost(HttpServletRequest req, HttpServletResponse res)¬

throws ServletException, IOException {¬
doGet(req, res);¬
}¬
¬
}¬

![Figura 1 dalla slide 81](assets/slide-081-fig-01.jpg)

## Slide 82 - Exercise

Exercise
HelloWorld Servlet with

GET, POST, and Figlet

![Figura 1 dalla slide 82](assets/slide-082-fig-01.jpg)

## Slide 83 - The Application

The Application

![Figura 1 dalla slide 83](assets/slide-083-fig-01.jpg)

## Slide 84 - Slide 84
