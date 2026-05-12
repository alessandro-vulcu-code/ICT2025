# 07-Webapp-2025-26-jsp

_Source: `07-Webapp-2025-26-jsp.pdf`_

## Slide 1 - Introduction to

Introduction to
Java Server Pages (JSP)

Web Applications
Master Degree in Computer Engineering

Master Degree in Cybersecurity
Master Degree in ICT for Internet and Multimedia

Academic Year 2025/2026

Nicola Ferro

Intelligent Interactive Information Access (IIIA) Hub

## Slide 2 - Outline

Outline

JavaServer Pages (JSP)

Model-View-Controller (MVC) paradigm

![Figura 1 dalla slide 2](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-002-fig-01.jpg)

## Slide 3 - JavaServer Pages

JavaServer Pages

![Figura 1 dalla slide 3](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-003-fig-01.jpg)

## Slide 4 - JavaServer Pages (JSP)

JavaServer Pages (JSP)

Creating HTML (CSS, JS) directly from servlets is a cumbersome process

no support to code in HTML (CSS, JS) since they are just Java strings

ease of errors

difficult maintenance and upgrade of the code

JavaServer Pages (JSP) technology provides the means for textual specification of
the creation of a dynamic response to a request

The technology builds on the following concepts:

Template Data: a substantial portion of most dynamic content is fixed or template content. Text
or XML fragments are typical template data. JSP technology supports natural manipulation of
template data

Addition of Dynamic Data: JSP technology provides a simple, yet powerful, way to add
dynamic data to template data

Encapsulation of Functionality: JSP technology provides two related mechanisms for the
encapsulation of functionality: JavaBeans component architecture, and tag libraries delivering
custom actions, functions, listener classes, and validation

Eclipse Foundation (2020). JavaServer Page Specification – Version 3.0.
https://jakarta.ee/specifications/pages/3.0/jakarta-server-pages-spec-3.0.html

## Slide 5 - Execution of a JSP Page

Execution of a JSP Page

hello.jsp

JSP

 Browser
Web server
GET /hello-world-

jsp/hello.jsp

hello_jsp.java

Java

hello.html

hello_jsp.class

Class

On first invocation, JSP pages are turned into the “corresponding servlet” and compiled to a
Java class

subsequent invocation will directly refer to the compiled class

You can ask the Web container to pre-compile JSP pages before use

## Slide 6 - Example of HelloWorld JSP Page

Example of HelloWorld JSP Page

 <!--
 Copyright 2018 University of Padua, Italy

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.

 Author: Nicola Ferro (ferro@dei.unipd.it)
 Version: 1.0
 Since: 1.0
-->
<%@ page contentType="text/html;charset=UTF-8" %>

Set the Content-Type HTTP response header

<!DOCTYPE html>
<html lang="en">
 <head>
  <meta charset="utf-8">
  <title>
   HelloWorld JSP Response
  </title>
 </head>
 <body>
  <h1>
   HelloWorld JSP Response
  </h1>
  <hr />
  <p>
   Hello, world!
  </p>
 </body>
</html>

![Figura 1 dalla slide 6](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-006-fig-01.jpg)

## Slide 7 - Calling the HelloWorld JSP Page

Calling the HelloWorld JSP Page

Whatever is not JSP
“instructions” is sent

back to the client

![Figura 1 dalla slide 7](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-007-fig-01.jpg)

## Slide 8 - Components of a JSP page

Components of a JSP page

template text: it is the static HTML (CSS, …) text

directives: provide global information that is conceptually valid independent of any specific request received by the

JSP page

<%@ page … %>: defines pages dependent attributes

<%@ include … %>: includes a file (static)

<%@ taglib … %>: declares a tag library

actions: perform a given operation. The use standard XML syntax <prefix:action>, e.g <jsp:param>

standard action: a set of base action defined in the JSP specification

custom action: personalised actions to support specific task and collected into tag libraries.
The JSTL (JSP Standard Tag Library) is one of such extensions, it is standardised and supports all the typical needs of an
applications (conditional instructions, formatting, internationalisation, …)

scripting: it is raw Java code to add further flexibility (to be avoided as much as possible)

<% … %> scriptlet: a fragment of Java code

<%= … %> expression: embeds the results of a Java expression

<%! … %> declaration: allows for declaring variables and methods which will be used in the JSP page

expression language (EL): is it a simple language to access data and variable made available from the application

${…}: it contains the expression to be evaluated and executed

Eclipse Foundation (2021). Jakarta Standard Tag Library 3.0.0
https://projects.eclipse.org/projects/ee4j.jstl/releases/3.0.0
https://github.com/eclipse-ee4j/jstl-api

Eclipse Foundation (2020). Jakarta Expression Language - Version 4.0
https://jakarta.ee/specifications/expression-language/4.0/jakarta-expression-language-spec-4.0.html
https://github.com/jakartaee/expression-language

![Figura 1 dalla slide 8](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-008-fig-01.jpg)

## Slide 9 - JavaBeans

JavaBeans

A JavaBean is a Java class, providing a reusable software
component which follows a specific naming conventions
and can thus be manipulated in an applicative framework

for example, component of a GUI framework

JavaBean conventions

it must have a no-argument constructor, to facilitate its instantiation

its fields must be exposed through accessor methods which are
called: getXXX and setXXX for a generic field name XXX, and isXXX
for a boolean field XXX

JSP relies on JavaBeans to exchange information among the
different components of the application

Hamilton, G. (1997). JavaBeans – Version 1.01-A.
http://www.oracle.com/technetwork/java/javase/documentation/spec-136004.html

## Slide 10 - (Some) Standard Actions

(Some) Standard Actions

Action
Description

<jsp:useBean>
makes a JavaBean available to a page

<jsp:getProperty> gets the values of a JavaBean property and adds it to the

response

<jsp:setProperty> sets the value of a JavaBean property

<jsp:include>
includes the response of a JSP or servlet. Only inside the
Web container

<jsp:forward>
forwards the processing to another JSP or servlet. Only inside
the Web container.

<jsp:param>
adds parameters to the request by <jsp:include> or
<jsp:forward>

![Figura 1 dalla slide 10](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-010-fig-01.jpg)

## Slide 11 - JSP Standard Tag Library (JSTL)

JSP Standard Tag Library (JSTL)

Area
Prefix
URI
Description

Core
c
http://java.sun.com/jsp/jstl/core

conditional instructions,
iteration, import of external
resources, ….

XML
Processing
x
http://java.sun.com/jsp/jstl/xml
XML processing

fmt
http://java.sun.com/jsp/jstl/fmt

I18N
Capable
Formatting

formatting,
internationalisation and
localisation

Relational
DB Access
sql
http://java.sun.com/jsp/jstl/sql
access to relational
databases

Functions
fn
http://java.sun.com/jsp/jstl/functions generic functions, e.g. to

manipulate strings

![Figura 1 dalla slide 11](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-011-fig-01.jpg)

## Slide 12 - (Some) JSTL Core Actions

(Some) JSTL Core Actions

Action
Description

<c:out>
evaluates an expression and writes the result in the response,
escaping XML

<c:if>
evaluates the body if the condition is true

<c:choose>
evaluates only the first branch for which the condition is true

<c:forEach>
iterates of a set of object

<c:url>
creates an URL applying the appropriate rewrite rules

<c:import>
imports the content of a resource and writes it into the
response or a variable. Also outside the container

<c:redirect>
send an HTTP redirect response to a client

<c:param>
adds a parameter to a request made by <c:url>,
<c:import> or <c:redirect>

![Figura 1 dalla slide 12](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-012-fig-01.jpg)

## Slide 13 - (Some) JSTL Formatting Actions

(Some) JSTL Formatting Actions

Action
Descriptions

<fmt:setLocale>
sets the locale (en_UK, it_IT, …)

<fmt:setBundle>
sets the resource bundle to localise messages

<fmt:message>
writes a localised message

<fmt:param>
provides a parameter for writing a localised message

<fmt:formatNumber> formats a number according to the format and locale

<fmt:formatDate>
formats a date/time according to the format and locale

![Figura 1 dalla slide 13](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-013-fig-01.jpg)

## Slide 14 - (Some) JSTL Functions Actions

(Some) JSTL Functions Actions

Action
Description

<fn:contains>
checks whether a string contains the given sub-string

<fn:endsWith>
checks whether a string ends with the given sub-string

<fn:escapeXml>
escapes XML markup characters

<fn:length>
returns the length of a string or the number of elements in a
collection

<fn:replace>
replaces a sub-string in a string

<fn:split>
splits a string into an array of sub-strings

<fn:substring>
extracts a sub-string from a string

## Slide 15 - Expression Language (EL): Operators

Expression Language (EL): Operators

Operator
Description

.
accesses a property of a JavaBean or an element of a Map

[]
access to an element of an array or a List

()
grouping among expression

? :
conditional instruction

+ - * / %
basic math operations

< > <= >= == !=
basic relational operators

&& || !
basic boolean operators

empty
checks whether a variable is empty (null or empty for strings,
array and collections)

func(arg)
invokes a JSTL function

![Figura 1 dalla slide 15](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-015-fig-01.jpg)

![Figura 2 dalla slide 15](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-015-fig-02.jpg)

## Slide 16 - (Some) Expression Language (EL) Implicit Variables

(Some) Expression Language (EL) Implicit Variables

Variable
Description

pageScope
Map of all the variables within the page scope

requestScope
Map of all the variables within the request scope

sessionScope
Map of all the variables within the session scope

applicationScope
Map of all the variables within the application scope

param
Map of all the request parameters whose values are single
strings

paramValues
Map of all the request parameters whose values are arrays of
strings

header
Map of all the HTTP headers whose values are single strings

headerValues
Map of all the HTTP headers whose values are arrays of
strings

cookie
Map of all the cookies represented as
javax.servlet.http.Cookie objects

![Figura 1 dalla slide 16](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-016-fig-01.jpg)

## Slide 17 - HelloWorld JSP

HelloWorld JSP
Web Application

![Figura 1 dalla slide 17](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-017-fig-01.jpg)

## Slide 18 - Welcome Page: index.jsp

Welcome Page: index.jsp

![Figura 1 dalla slide 18](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-018-fig-01.jpg)

## Slide 19 - Simple Hello World: hello-world.jsp

Simple Hello World: hello-world.jsp

![Figura 1 dalla slide 19](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-019-fig-01.jpg)

## Slide 20 - GET Form Hello World: get-form.jsp and

GET Form Hello World: get-form.jsp and

hello-world-param.jsp

![Figura 1 dalla slide 20](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-020-fig-01.jpg)

## Slide 21 - GET Form Hello World: get-form.jsp and

GET Form Hello World: get-form.jsp and

hello-world-param.jsp

![Figura 1 dalla slide 21](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-021-fig-01.jpg)

## Slide 22 - GET Form Hello World: get-form.jsp and

GET Form Hello World: get-form.jsp and

hello-world-param.jsp

![Figura 1 dalla slide 22](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-022-fig-01.jpg)

## Slide 23 - POST Form Hello World: post-form.jsp and

POST Form Hello World: post-form.jsp and

hello-world-param.jsp

![Figura 1 dalla slide 23](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-023-fig-01.jpg)

## Slide 24 - POST Form Hello World: post-form.jsp and

POST Form Hello World: post-form.jsp and

hello-world-param.jsp

![Figura 1 dalla slide 24](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-024-fig-01.jpg)

## Slide 25 - POST Form Hello World: post-form.jsp and

POST Form Hello World: post-form.jsp and

hello-world-param.jsp

![Figura 1 dalla slide 25](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-025-fig-01.jpg)

## Slide 26 - index.jsp

index.jsp

Declares the use of the core JSTL

Imports another JSP

Resolves URLs
Resolves URLs

Resolves URLs

¬
            <!-- Start Post form card-->¬
            <div class="card">¬
                <img src="<c:url value="/media/post.png"/>" class="card-img-top" alt="Post form card image">¬
                <div class="card-body">¬
                    <h5 class="card-title">Minimal POST form JSP page</h5>¬
                    <p class="card-text text-center">¬
                        <code class="badge-pill badge-primary p-2">post-form.jsp</code>¬
                        <a href="<c:url value="/jsp/post-form.jsp"/>" target="_blank"¬
                           title="Click to run the example"><i class="fas fa-cogs fa-3x align-middle ml-3"></i></a
                    </p>¬
                    <p class="card-text">¬
                        <small class="text-muted">It asks for your name using a POST form and replies "Hello, &lt;
                            with the current time and date.¬
                        </small>¬
                    </p>¬
                </div>¬
            </div>¬
            <!-- End POST form card-->¬
¬
        </div> <!-- End Card Deck-->¬
¬
    </div> <!-- End of Content-->¬
¬
    <!-- footer -->¬
    <c:import url="/jsp/include/footer.jsp"/>¬
¬
</div> <!-- /.container -->¬
¬
<c:import url="/jsp/include/foot.jsp"/>¬
</body>¬
</html>¬

Imports another JSP

Imports another JSP

<%@ page contentType="text/html;charset=UTF-8" %>¬
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>¬
¬
<!DOCTYPE html>¬
<html lang="en">¬
<head>¬
¬
    <c:import url="/jsp/include/head.jsp"/>¬
¬
    <title>Basic Web Application with JavaServer Pages</title>¬
¬
</head>¬
¬
<body>¬
¬
<div class="container">¬
¬
    <!-- header -->¬
    <header class="mt-5 mb-5">¬
        <div class="jumbotron jumbotron-fluid">¬
            <div class="container">¬
                <h1 class="display-4">Basic Web Application with JavaServer Pages</h1>¬
            </div>¬
        </div>¬
    </header>¬
¬
    <!-- body -->¬
    <div class="content mt-5 mb-5">¬
¬
        <div class="card-deck">¬
¬
            <!-- Start Hello World card-->¬
            <div class="card">¬
                <img src="<c:url value="/media/hello.png"/>" class="card-img-top" alt="Hello World card image">¬
                <div class="card-body">¬
                    <h5 class="card-title">Minimal JSP page</h5>¬
                    <p class="card-text text-center">¬
                        <code class="badge-pill badge-primary p-2">hello-world.jsp</code>¬
                        <a href="<c:url value="/jsp/hello-world.jsp"/>" target="_blank"¬
                           title="Click to run the example"><i class="fas fa-cogs fa-3x align-middle ml-3"></i></a>¬
                    </p>¬
                    <p class="card-text">¬
                        <small class="text-muted">It just says "Hello, world!"</small>¬
                    </p>¬
                </div>¬
            </div>¬
            <!-- End Hello World card-->¬
¬
            <!-- Start GET form card-->¬
            <div class="card">¬
                <img src="<c:url value="/media/get.png"/>" class="card-img-top" alt="Get form card image">¬
                <div class="card-body">¬
                    <h5 class="card-title">Minimal GET form JSP page</h5>¬
                    <p class="card-text text-center">¬
                        <code class="badge-pill badge-primary p-2">get-form.jsp</code>¬
                        <a href="<c:url value="/jsp/get-form.jsp"/>" target="_blank"¬
                           title="Click to run the example"><i class="fas fa-cogs fa-3x align-middle ml-3"></i></a>¬
                    </p>¬
                    <p class="card-text">¬
                        <small class="text-muted">It asks for your name using a GET form and replies "Hello, &lt;your-name&gt;!"¬
                            with the current time and date.¬
                        </small>¬
                    </p>¬
                </div>¬
            </div>¬
            <!-- End GET form card-->¬
¬

## Slide 27 - head.jsp and foot.jsp

head.jsp and foot.jsp

<%@ page contentType="text/html;charset=UTF-8" %>¬
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>¬
¬
¬
<meta charset="utf-8">¬
<meta http-equiv="X-UA-Compatible" content="IE=edge">¬
<meta name="viewport" content="width=device-width, initial-scale=1">¬
<meta name="description" content="Basic Web Application with JavaServer
Pages">¬
<meta name="author" content="Nicola Ferro">¬
¬
<!-- Bootstrap core CSS -->¬
<link rel="stylesheet"
href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.
css"
integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/
iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">¬
¬
<!-- Font Awesome CSS-->¬
<link rel="stylesheet"
href="https://use.fontawesome.com/releases/v5.8.1/css/all.css"
integrity="sha384-50oBUHEmvpQ+1lW4y57PTFmhCaXp0ML5d60M1M7uH2+
nqUivzIebhndOJK28anvf" crossorigin="anonymous">¬

<%@ page contentType="text/html;charset=UTF-8" %>¬
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>¬
¬
<!-- Bootstrap, Popper, and JQuery JS -->¬
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+
8abtTE1Pi6jizo" crossorigin="anonymous"></script>¬
<script
src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.
js"
integrity="sha384-
UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1"
crossorigin="anonymous"></script>¬
<script
src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+
B07jRM" crossorigin="anonymous"></script>¬

![Figura 1 dalla slide 27](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-027-fig-01.jpg)

## Slide 28 - footer.jsp

footer.jsp

Resolves URLs

Resolves URLs

<%@ page contentType="text/html;charset=UTF-8" %>¬
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>¬
¬
<footer class="mt-5 mb-5">¬
¬
    <div class="row justify-content-center">¬
        <div class="col-md-8 text-center">¬
            <hr/>¬
        </div>¬
    </div>¬
¬
    <div class="row justify-content-center align-items-center">¬
        <div class="col-md-1 text-center">¬
            <a href="http://www.unipd.it/" target="_blank">¬
                <img class="img-fluid" src="<c:url value="/media/logo-UNIPD.png"/>"¬
                     alt="logo University of Padua">¬
            </a>¬
        </div>¬
        <div class="col-md-4 text-center text-muted small">¬
            Copyright &copy; 2019, University of Padua, Italy¬
        </div>¬
        <div class="col-md-1 text-center">¬
            <a href="http://www.dei.unipd.it/" target="_blank">¬
                <img class="img-fluid" src="<c:url value="/media/logo-DEI.png"/>"¬
                     alt="logo Department of Information Engineering">¬
            </a>¬
        </div>¬
    </div>¬
¬
</footer>

![Figura 1 dalla slide 28](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-028-fig-01.jpg)

## Slide 29 - get-form.jsp (post-form.jsp)

get-form.jsp (post-form.jsp)

Imports another JSP
Imports another JSP
Imports another JSP

¬
                <div class="form-group row mt-4">¬
                    <div class="col-md-12 text-center">¬
                        <button class="btn btn-outline-dark btn-lg" type="submit">¬
                            Submit <i class="fas fa-signature fa-2x align-middle ml-3"></i>¬
                        </button>¬
                    </div>¬
                </div>¬
            </form>¬
¬
        </div>¬
    </div> <!-- End of Content-->¬
¬
    <!-- footer -->¬
    <c:import url="/jsp/include/footer.jsp"/>¬
¬
</div> <!-- /.container -->¬
¬
<c:import url="/jsp/include/foot.jsp"/>¬
</body>¬
</html>¬

Resolves URLs

method  is  post in the case of

post-form.jsp

<%@ page contentType="text/html;charset=UTF-8" %>¬
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>¬
¬
¬
<!DOCTYPE html>¬
<html lang="en">¬
<head>¬
¬
    <c:import url="/jsp/include/head.jsp"/>¬
¬
    <title>Basic Web Application with JavaServer Pages - GET Form Example</title>¬
¬
</head>¬
¬
<body>¬
¬
<div class="container">¬
¬
    <!-- header -->¬
    <header class="mt-5 mb-5">¬
        <div class="jumbotron jumbotron-fluid">¬
            <div class="container">¬
                <h1 class="display-4">Basic Web Application with JavaServer Pages</h1>¬
                <p class="lead">GET Form Example</p>¬
            </div>¬
        </div>¬
    </header>¬
¬
    <!-- body -->¬
    <div class="content mt-5 mb-5">¬
¬
        <div class="row justify-content-center">¬
¬
            <form method="get" action="<c:url value="/jsp/hello-world-param.jsp"/>"¬
                  class="shadow-sm p-3 bg-light rounded">¬
¬
                <div class="form-group row align-items-center mt-5">¬
                    <div class="col-md-2 text-right">¬
                        <label class="col-form-label" for="helloName">Name</label>¬
                    </div>¬
                    <div class="col-md-10 text-center">¬
                        <div class="input-group mb3">¬
                            <input class="form-control form-control-lg" type="text" id="helloName" name="helloName"¬
                                   size="45" required placeholder="Please enter your name">¬
                            <div class="input-group-append">¬
                                <span class="input-group-text"><i class="fas fa-id-badge fa-2x"></i></span>¬
                            </div>¬
                        </div>¬
                    </div>¬
                </div>¬
¬

## Slide 30 - hello-world-param.jsp

hello-world-param.jsp

Declares the use of the core  and

internationalisation JSTL

Tests for alternative conditions

empty is an EL operator and param is

the EL  map of request parameters

c:out prints the output value of the

provided expression

<%@ page contentType="text/html;charset=UTF-8" %>¬
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>¬
<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt" %>¬
¬
<!DOCTYPE html>¬
<html lang="en">¬
<head>¬
¬
    <c:import url="/jsp/include/head.jsp"/>¬
¬
    <title>Basic Web Application with JavaServer Pages - JSP using request parameter</title>¬
¬
</head>¬
¬
<div class="container">¬
¬
    <!-- header -->¬
    <header class="mt-5 mb-5">¬
        <div class="jumbotron jumbotron-fluid">¬
            <div class="container">¬
                <h1 class="display-4">Basic Web Application with JavaServer Pages</h1>¬
                <p class="lead"><code class="text-secondary">hello-world-param.jsp</code> Response</p>¬
            </div>¬
        </div>¬
    </header>¬
¬
    <!-- body -->¬
    <div class="content mt-5 mb-5">¬
        <div class="row justify-content-center">¬
¬
            <!-- even if the field is required in the form, this page may be called directly.¬
              Therefore, you need to  validate form fields again -->¬
            <c:choose>¬
                <c:when test="${empty param.helloName}">¬
                    <div class="col-md-6 h2 text-left alert alert-danger" role="alert">¬
                        Please, enter your name!¬
                    </div>¬
                </c:when>¬
                <c:otherwise>¬
                    <div class="col-md-6 h2 text-left text-light bg-dark">¬
                        Hello, <c:out value="${param.helloName}"/>!¬
                    </div>¬
                </c:otherwise>¬
            </c:choose>¬
¬
        </div>¬
¬

## Slide 31 - hello-world-param.jsp

hello-world-param.jsp

Standard action to (instantiate) and make

available a Java object

Use the internationalisation tags to set the

locale and format the current date
Use the internationalisation tags to set the

locale and format the current date

¬
        <div class="row justify-content-center">¬
            <div class="col-md-6 h5 text-left text-muted">¬
¬
                <!-- use a java.util.Date object to hold the current date -->¬
                <jsp:useBean id="now" class="java.util.Date"/>¬
¬
                <!-- set the locale to British English -->¬
                <fmt:setLocale value="en_UK"/>¬
¬
                <!-- format the date and time according to that locale -->¬
                on <fmt:formatDate value="${now}" type="date" dateStyle="long"/>¬
                at <fmt:formatDate value="${now}" type="time" timeStyle="long"/>¬
            </div>¬
        </div>¬
    </div><!-- End of Content-->¬
¬
    <!-- footer -->¬
    <c:import url="/jsp/include/footer.jsp"/>¬
¬
</div> <!-- /.container -->¬
¬
<c:import url="/jsp/include/foot.jsp"/>¬
</body>¬
</html>¬

![Figura 1 dalla slide 31](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-031-fig-01.jpg)

## Slide 32 - The web.xml Configuration File

The web.xml Configuration File

<web-app id="hello-world-jsp-form" version="2.5"
xmlns="http://java.sun.com/xml/ns/javaee"¬

xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"¬
xsi:schemaLocation="http://java.sun.com/xml/ns/javaee
http://java.sun.com/xml/ns/javaee/web-app_2_5.xsd">¬
    ¬

<display-name>Basic Web Application with JavaServer Pages</display-name>¬
<description>Example of use of minimal JSP to create a Web
application.</description>¬

¬
<welcome-file-list>¬

<welcome-file>jsp/index.jsp</welcome-file>¬
</welcome-file-list>¬
¬
</web-app>¬

![Figura 1 dalla slide 32](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-032-fig-01.jpg)

## Slide 33 - Configuration of the Maven Project

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

You need to add the
dependency on JSTL

![Figura 1 dalla slide 33](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-033-fig-01.jpg)

## Slide 34 - Project Object Model (POM)

Project Object Model (POM)

Adds the dependencies on
the JSTL taglibs.

Note that taglibs are not already
available in the deployment
environment on Tomcat, so the

scope cannot be  provided.

![Figura 1 dalla slide 34](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-034-fig-01.jpg)

## Slide 35 - Model-View-Controller

Model-View-Controller

![Figura 1 dalla slide 35](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-035-fig-01.jpg)

## Slide 36 - Model-View-Controller (MVC) Paradigm

Model-View-Controller (MVC) Paradigm

Queries to the

Updates to the

state

state

Model

Notiﬁcations of

state updates

View
Controller

Actions

Selection and
messages to the

View

Input from

Users
Output to

Users

Krasner, G. E. and Pope, S. T. (1988). A Cookbook for Using the Model-View-Controller User
Interface Paradigm in Smalltalk-80. Journal of Object-Oriented Programming, 1(3):26–49.

## Slide 37 - MVC and Java/Web Technologies

MVC and Java/Web Technologies

Java
[JavaBeans]

Queries to the

Updates to the

state

state

Model

Notiﬁcations of

state updates

View
Controller

Servlet
JSP
[HTML, CSS, JS]

Actions

Selection and
messages to the

View

Input from

Users
Output to

Users

## Slide 38 - MVC and Distributed Application Layers

MVC and Distributed Application Layers

View

Presentation Logic

Controller

          Model

Application Logic

Data Logic

![Figura 1 dalla slide 38](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-038-fig-01.jpg)

## Slide 39 - Accessing a database via

Accessing a database via

JSP, servlets and JDBC

![Figura 1 dalla slide 39](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-039-fig-01.jpg)

## Slide 40 - Application Functionalities: Create Employee

Application Functionalities: Create Employee

![Figura 1 dalla slide 40](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-040-fig-01.jpg)

## Slide 41 - Application Functionalities: Create Employee

Application Functionalities: Create Employee

![Figura 1 dalla slide 41](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-041-fig-01.jpg)

## Slide 42 - Application Functionalities: Search Employee

Application Functionalities: Search Employee

![Figura 1 dalla slide 42](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-042-fig-01.jpg)

## Slide 43 - MVC in the Employee Application

MVC in the Employee Application

Output to

Input from

Users

Users

View

View

create-employee-form.jsp
search-employee-form.jsp

create-employee-result.jsp
search-employee-result.jsp

POST /create-employee
POST /search-employee-by-salary

FORWARD create-employee-result.jsp
FORWARD search-employee-result.jsp

Controller

CreateEmployeeServlet
SearchEmployeeBySalaryServlet

INVOKE CreateEmployeeDAO
INVOKE SearchEmployeeBySalaryDAO

Model

Employee

Message

Data Logic

CreateEmployeeDAO
SearchEmployeeBySalaryDAO

![Figura 1 dalla slide 43](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-043-fig-01.jpg)

![Figura 2 dalla slide 43](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-043-fig-02.jpg)

![Figura 3 dalla slide 43](slide-043-fig-03.jpg)

![Figura 4 dalla slide 43](slide-043-fig-04.jpg)

![Figura 5 dalla slide 43](slide-043-fig-05.jpg)

## Slide 44 - MVC and Layers in the Employee Application

MVC and Layers in the Employee Application

create-employee-form.jsp
create-employee-result.jsp

search-employee-form.jsp
search-employee-result.jsp

View

Presentation Logic

Controller

          Model

Application Logic

Employee

Message

CreateEmployeeDAO
SearchEmployeeBySalaryDAO

CreateEmployeeServlet

Data Logic

SearchEmployeeBySalaryServlet

![Figura 1 dalla slide 44](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-044-fig-01.jpg)

## Slide 45 - Employee Web Application Class Diagram

Employee Web Application Class Diagram

![Figura 1 dalla slide 45](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-045-fig-01.jpg)

## Slide 46 - Create Employee: Sequence Diagram

Create Employee: Sequence Diagram

![Figura 1 dalla slide 46](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-046-fig-01.jpg)

## Slide 47 - Search Employee: Sequence Diagram

Search Employee: Sequence Diagram

![Figura 1 dalla slide 47](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-047-fig-01.jpg)

## Slide 48 - The Create and Search Employee Forms in JSP

The Create and Search Employee Forms in JSP

Set the Content-Type
response header and use

Set the Content-Type
response header and use

the Core taglib

the Core taglib

<%@ page contentType="text/html;charset=utf-8" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>

<%@ page contentType="text/html;charset=utf-8" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>

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
 <h1>Create Employee Form</h1>
  <form method="POST" action="<c:url value="/create-employee"/>">
  <label for="badge">Badge:</label>
  <input name="badge" type="text"/><br/>
    <label for="surname">Surname:</label>
  <input name="surname" type="text"/><br/>
    <label for="age">Age:</label>
  <input name="age" type="text"/><br/>
    <label for="salary">Salary:</label>
  <input name="salary" type="text"/><br/><br/>

  <body>
 <h1>Search Employee Form</h1>
  <form method="POST" action="<c:url value="/search-employee-by-salary"/>">
  <label for="salary">Salary:</label>
  <input name="salary" type="text"/><br/><br/>
    <button type="submit">Submit</button><br/>
  <button type="reset">Reset the form</button>
 </form>
 </body>
</html>

  <button type="submit">Submit</button><br/>
  <button type="reset">Reset the form</button>
 </form>
 </body>
</html>

Use the c:url tag to specify
the path relative to the web

Use the c:url tag to specify
the path relative to the web

application root path

application root path

## Slide 49 - The Employee Class: Almost JavaBeans

The Employee Class: Almost JavaBeans

package it.unipd.dei.webapp.resource;

public class Employee {

 private final int badge;

There are not setXXX methods to set the
properties which are final instead

 private final String surname;

 private final int age;

 private final int salary;

 public Employee(final int badge, final String surname, final int age, final int salary) {
  this.badge = badge;
  this.surname = surname;
  this.age = age;
  this.salary = salary;
 }

Lack of no-argument constructor

 public final int getBadge() {
  return badge;
 }

 public final String getSurname() {
  return surname;
 }

Comply with the JavaBeans convention
on getXXX method names
Comply with the JavaBeans convention
on getXXX method names
Comply with the JavaBeans convention
on getXXX method names
Comply with the JavaBeans convention
on getXXX method names

 public final int getAge() {
  return age;
 }

 public final int getSalary() {
  return salary;
 }

## Slide 50 - The Message Class: Almost JavaBeans

The Message Class: Almost JavaBeans

package it.unipd.dei.webapp.resource;

public class Message {

There are not setXXX methods to set the
properties which are final instead

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

Lack of no-argument constructor
Lack of no-argument constructor

 public Message(final String message) {
  this.message = message;
  this.errorCode = null;
  this.errorDetails = null;
  this.isError = false;
 }

 public final String getMessage() {
  return message;
 }

Comply with the JavaBeans convention
on getXXX method names and isXXX

Comply with the JavaBeans convention
on getXXX method names and isXXX

Comply with the JavaBeans convention
on getXXX method names and isXXX

Comply with the JavaBeans convention
on getXXX method names and isXXX

for booleans

for booleans

for booleans

for booleans

 public final String getErrorCode() {
  return errorCode;
 }
  public final String getErrorDetails() {
  return errorDetails;
 }

 public final boolean isError() {
  return isError;
 }

## Slide 51 - The Data Access Object (DAO) Interface

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

![Figura 1 dalla slide 51](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-051-fig-01.jpg)

## Slide 52 - The AbstractDAO class

The AbstractDAO class

The AbstractDAO class provides a base

implementation of the DataAccessObject interface

so that all the subclasses have a uniform behavior
and focus just on implementing the specific logic for
performing the requested data access operation

The implementation of the access() method takes
care of always closing the connection to the database
and of rolling-back the transaction, if needed

The  access() method delegates the actual logic to
perform the access to the datasource to its sub-
classes, via the abstract doAccess() method which
has to be implemented by them

DAO objects are one-shot and they are not expected
to be re-used; in this respect, they would not need to
be concerned with thread-safety.

However, the AbstractDAO class assumes the possibility

of a mis-use of a DAO (or leakage) and manages, to a

certain extent, concurrency issues via lock object and the

accessed flag

![Figura 1 dalla slide 52](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-052-fig-01.jpg)

## Slide 53 - The CreateEmployeeDatabase Class

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

## Slide 54 - The SearchEmployeeBySalaryDAO Class

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

## Slide 55 - Pool of Database Connections via Tomcat: context.xml

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

## Slide 56 - The web.xml Configuration File

The web.xml Configuration File

<?xml version="1.0" encoding="UTF-8"?>

No confi

<web-app id="hello-world-webapp" version="4.0" xmlns="http://xmlns.jcp.org/xml/ns/javaee"
 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 xsi:schemaLocation="http://java.sun.com/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd">

 <display-name>Employee JSP/Servlet JDBC</display-name>
 <description>Example JSP/servlet-based application accessing a DBMS via JDBC.</description>
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

![Figura 1 dalla slide 56](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-056-fig-01.jpg)

![Figura 2 dalla slide 56](slide-056-fig-02.jpg)

## Slide 57 - The AbstractDatabaseServlet Class

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

![Figura 1 dalla slide 57](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-057-fig-01.jpg)

## Slide 58 - The CreateEmployeeServlet Class

The CreateEmployeeServlet Class

Retrieves request parameters and creates
the corresponding Employee object

Retrieves the connection from the
superclass and uses the helper DAO to

access the database

Manages error/success conditions and
creates the corresponding Message

Adds the Employee and the Message
as requests attributes and forwards control

to the JSP view

public final class CreateEmployeeServlet extends AbstractDatabaseServlet {¬
¬
    public void doPost(HttpServletRequest req, HttpServletResponse res)¬
            throws ServletException, IOException {¬
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
            // set the badge of the employee as the resource in the log context¬
            // at this point we know it is a valid integer¬
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
            m = new Message("Cannot create the employee. Invalid input parameters: badge, age, and salary must be integer.", "E100", ex.getMessage());¬
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
        try {¬
            // stores the employee and the message as a request attribute¬
            req.setAttribute("employee", e);¬
            req.setAttribute("message", m);¬
¬
            // forwards the control to the create-employee-result JSP¬
            req.getRequestDispatcher("/jsp/create-employee-result.jsp").forward(req, res);¬
        } catch(Exception ex) {¬
            LOGGER.error(new StringFormattedMessage("Unable to send response when creating employee %d.", badge), ex);¬
            throw ex;¬
        } finally {¬
            LogContext.removeIPAddress();¬
            LogContext.removeAction();¬
            LogContext.removeResource();¬
        }¬
¬
    }¬
¬
}¬

![Figura 1 dalla slide 58](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-058-fig-01.jpg)

## Slide 59 - The SearchEmployeeBySalaryServlet Class

The SearchEmployeeBySalaryServlet Class

Retrieves the connection to the database,
uses the helper DAO to access the database,
and getOutputParam() to retrieve the list

of Employee objects

Manages error/success conditions and
creates the corresponding Message

Adds the Employee list and the
Message as requests attributes and

forwards control to the JSP view

public final class SearchEmployeeBySalaryServlet extends AbstractDatabaseServlet {¬
¬
    public void doPost(HttpServletRequest req, HttpServletResponse res)¬
            throws ServletException, IOException {¬
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
¬
        try {¬
            // stores the employee list and the message as a request attribute¬
            req.setAttribute("employeeList", el);¬
            req.setAttribute("message", m);¬
¬
            // forwards the control to the search-employee-result JSP¬
            req.getRequestDispatcher("/jsp/search-employee-result.jsp").forward(req, res);¬
        } catch(Exception ex) {¬
            LOGGER.error(new StringFormattedMessage("Unable to send response when creating employee %d.", salary), ex);¬
            throw ex;¬
        } finally {¬
            LogContext.removeIPAddress();¬
            LogContext.removeAction();¬
            LogContext.removeUser();¬
        }¬
    }¬
¬
}¬

![Figura 1 dalla slide 59](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-059-fig-01.jpg)

## Slide 60 - The create-employee-result JSP

The create-employee-result JSP

<%@ page contentType="text/html;charset=utf-8" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>

Set the Content-Type
response header and use

the Core taglib

<!DOCTYPE html>
<html lang="en">
 <head>
  <title>Create Employee</title>
 </head>

Import the output of the
show-message.jsp to print

any message

 <body>
  <h1>Create Employee</h1>
  <hr/>
    <!-- display the message -->
  <c:import url="/jsp/include/show-message.jsp"/>

Check whether there is any
employee attribute and whether

there is no error

Write the contents of the
Employee object using the

JavaBeans conventions

  <!-- display the just created employee, if any and no errors -->
  <c:if test='${not empty employee && !message.error}'>
   <ul>
    <li>badge: <c:out value="${employee.badge}"/></li>
    <li>surname: <c:out value="${employee.surname}"/></li>
    <li>age: <c:out value="${employee.age}"/></li>
    <li>salary: <c:out value="${employee.salary}"/></li>
   </ul>
  </c:if>
 </body>
</html>

![Figura 1 dalla slide 60](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-060-fig-01.jpg)

## Slide 61 - The show-message JSP

The show-message JSP

Set the Content-Type
response header and use

the Core taglib

<%@ page contentType="text/html;charset=utf-8" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>

If it is an error message

<c:choose>
 <c:when test="${message.error}">
  <ul>
   <li>error code: <c:out value="${message.errorCode}"/></li>
   <li>message: <c:out value="${message.message}"/></li>
   <li>details: <c:out value="${message.errorDetails}"/></li>
  </ul>
 </c:when>

else

Write the message and
additional error information

 <c:otherwise>
  <p><c:out value="${message.message}"/></p>
 </c:otherwise>
</c:choose>

Write only the message

## Slide 62 - The search-employee-result JSP

The search-employee-result JSP

<%@ page contentType="text/html;charset=utf-8" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>

Set the Content-Type response
header and use the Core taglib

<!DOCTYPE html>
<html lang="en">
 <head>
  <title>Search Employee</title>
 </head>

Import the output of the
show-message.jsp to print

any message

 <body>
  <h1>Search Employee</h1>
  <hr/>
    <!-- display the message -->
  <c:import url="/jsp/include/show-message.jsp"/>

If there is a not empty list

  <!-- display the list of found employees, if any -->
  <c:if test='${not empty employeeList}'>
   <table>
    <thead>
     <tr>
      <th>Badge</th><th>Surname</th><th>Age</th><th>Salary</th>
     </tr>
    </thead>

Iterate over each
element of the list

Write the contents of the
Employee object using the

JavaBeans conventions

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
 </body>
</html>

## Slide 63 - Project Object Model (POM)

Project Object Model (POM)

Adds the dependencies on the JSTL taglibs.

Note that taglibs are not already available in
the deployment environment on Tomcat, so

the scope cannot be  provided.

![Figura 1 dalla slide 63](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-063-fig-01.jpg)

## Slide 64 - Slide 64
