# 08-Webapp-2025-26-REST

_Source: `08-Webapp-2025-26-REST.pdf`_

## Slide 1 - REST Web Services

REST Web Services

Web Applications
Master Degree in Computer Engineering

Master Degree in Cybersecurity
Master Degree in ICT for Internet and Multimedia

Academic Year 2025/2026

Nicola Ferro

Intelligent Interactive Information Access (IIIA) Hub

## Slide 2 - Outline

Outline

The REST architectural paradigm

Development of a REST Web service

AJAX

Use of a REST Web service with AJAX

![Figura 1 dalla slide 2](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/08-Webapp-2025-26-REST/assets/slide-002-fig-01.jpg)

## Slide 3 - REST Web Services

REST Web Services

![Figura 1 dalla slide 3](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/08-Webapp-2025-26-REST/assets/slide-003-fig-01.jpg)

## Slide 4 - REST: REpresentational State Transfer

REST: REpresentational State Transfer

REST is an architectural paradigm which applies the
architectural principles of the Web to Web services

REST relies on a network of Web resources where users
proceed in the application by following links (state
transitions) which provide the representation of the next
resource (new state) to them

Features

simplicity

state-less

scalability

![Figura 1 dalla slide 4](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/08-Webapp-2025-26-REST/assets/slide-004-fig-01.jpg)

## Slide 5 - Resource

Resource

A resource is whatever has identity

Resources have a state which can change over time

Resources have an identifier (URI) which is unique and
global

Resources can transfer a representation of their state

![Figura 1 dalla slide 5](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/08-Webapp-2025-26-REST/assets/slide-005-fig-01.jpg)

## Slide 6 - REST: Overview

REST: Overview

Representation:  upon request, a resource may transfer a representation of its
state to a client

resources expose a uniform interface for their management

Stateless: each request between client and server must contain all the
information needed to understand the request

messages must be self-explaining

![Figura 1 dalla slide 6](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/08-Webapp-2025-26-REST/assets/slide-006-fig-01.jpg)

## Slide 7 - HTTP and REST

HTTP and REST

HTTP is a stateless protocol

HTTP provides an uniform interface to access
resources, i.e. the HTTP methods which have a well-
defined semantics

GET, POST, PUT, DELETE

HTTP requests/response rely on headers/bodies which
are self-explaining

![Figura 1 dalla slide 7](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/08-Webapp-2025-26-REST/assets/slide-007-fig-01.jpg)

## Slide 8 - REST: Example of Resources and URIs

REST: Example of Resources and URIs

Resource
URI

List of the students
/student

Data about the student with badge
number 123456
/student/123456

/student/123456/exam/webapp

Data of the exam “Web
Applications” for the student with
badge number 123456

Each resource has a unique identifier, i.e. an URI, which has to be descriptive
enough

REST relies on URI templates to specify how resources are identified

/student/{badge}/exam/{id}

![Figura 1 dalla slide 8](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/08-Webapp-2025-26-REST/assets/slide-008-fig-01.jpg)

![Figura 2 dalla slide 8](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/08-Webapp-2025-26-REST/assets/slide-008-fig-02.jpg)

## Slide 9 - REST and HTTP Request Methods

REST and HTTP Request Methods

HTTP Method
Operation

POST
Create a resource

GET
Read a resource

PUT
Update a resource

DELETE
Delete a resource

GET /student/123456: reads the data about the student with badge number

123456 and returns them in the media type specified by the Accept request header

POST /student: creates a new student according to the sent data

PUT /student/123456: updates an existing student with badge number 123456

according to the sent data

DELETE /student/123456: deletes the student with badge number 123456

![Figura 1 dalla slide 9](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/08-Webapp-2025-26-REST/assets/slide-009-fig-01.jpg)

![Figura 2 dalla slide 9](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/08-Webapp-2025-26-REST/assets/slide-009-fig-02.jpg)

## Slide 10 - Example of XML Representation

Example of XML Representation

GET /student HTTP/1.1
Accept = application/xml	 	 	 [or text/xml]

<?xml version="1.0"?>
<students xmlns:xlink="http://www.w3.org/1999/xlink">
 <student badge="123456" xlink:href="http://www.dei.unipd.it/my-rest-app/student/123456" />
 <student badge="123457" xlink:href="http://www.dei.unipd.it/my-rest-app/student/123457" />
 <student badge="123458" xlink:href="http://www.dei.unipd.it/my-rest-app/student/123458" />
</students>

GET /student/123456 HTTP/1.1
Accept = application/xml	 	 	 [or text/xml]

<?xml version="1.0"?>
<student xmlns:xlink="http://www.w3.org/1999/xlink" badge="123456" name="Mario" surname="Rossi" >
 <exams>
  <exam id="webapp" xlink:href="http://www.dei.unipd.it/my-rest-app/student/123456/exam/webapp" />
  <exam id="dbms" xlink:href="http://www.dei.unipd.it/my-rest-app/student/123456/exam/dbms" />
  <exam id="iot" xlink:href="http://www.dei.unipd.it/my-rest-app/student/123456/exam/iot" />
 </exams>
</student>

## Slide 11 - Example of JSON Representation

Example of JSON Representation

GET /student HTTP/1.1
Accept = application/json

{
   "students":[
      {
         "student":{
            "badge":123456,
            "link":"http://www.dei.unipd.it/my-rest-app/student/123456"
         }
      },
      {
         "student":{
            "badge":123457,
            "link":"http://www.dei.unipd.it/my-rest-app/student/123457"
         }
      },
      {
         "student":{
            "badge":123458,
            "link":"http://www.dei.unipd.it/my-rest-app/student/123458"
         }
      }
   ]
}

## Slide 12 - Example of JSON Representation

Example of JSON Representation

GET /student/123456 HTTP/1.1
Accept = application/json

{
   "student":{
      "badge":123456,
      "name":"Mario",
      "surname":"Rossi",
      "exams":[
         {
            "exam":{
               "id":"webapp",
               "link":"http://www.dei.unipd.it/my-rest-app/student/123456/exam/webapp"
            }
         },
         {
            "exam":{
               "id":"dbms",
               "link":"http://www.dei.unipd.it/my-rest-app/student/123457/exam/dbms"
            }
         },
         {
            "student":{
               "id":"iot",
               "link":"http://www.dei.unipd.it/my-rest-app/student/123458/iot"
            }
         }
      ]
   }
}

## Slide 13 - Example of HTML Representation

Example of HTML Representation

GET /student HTTP/1.1
Accept = text/html

Students: <br/>
<table>
 <thead>
  <tr>
   <th>Badge</th><th>Link</th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>123456</td>
   <td>
    <a href="http://www.dei.unipd.it/my-rest-app/student/123456" target="_blank">
     http://www.dei.unipd.it/my-rest-app/student/123456
    </a>
   </td>
  </tr>
  <tr>
   <td>123457</td>
   <td>
    <a href="http://www.dei.unipd.it/my-rest-app/student/123457" target="_blank">
     http://www.dei.unipd.it/my-rest-app/student/123457
    </a>
   </td>
  </tr>
  <tr>
   <td>123458</td>
   <td>
    <a href="http://www.dei.unipd.it/my-rest-app/student/123458" target="_blank">
     http://www.dei.unipd.it/my-rest-app/student/123458
    </a>
   </td>
  </tr>
 </tbody>
</table>

![Figura 1 dalla slide 13](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/08-Webapp-2025-26-REST/assets/slide-013-fig-01.jpg)

## Slide 14 - Example of HTML Representation

Example of HTML Representation

GET /student/123456 HTTP/1.1
Accept = text/html

Student:
<ul>
 <li>Mario Rossi, badge number 123456 </li>
</ul>

Exams:
<ul>
 <li><a href="http://www.dei.unipd.it/my-rest-app/student/123456/exam/webapp" target="_blank">webapp</a></li>
 <li><a href="http://www.dei.unipd.it/my-rest-app/student/123456/exam/dbms" target="_blank">dbms</a></li>
 <li><a href="http://www.dei.unipd.it/my-rest-app/student/123456/exam/iot" target="_blank">iot</a></li>
</ul>

![Figura 1 dalla slide 14](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/08-Webapp-2025-26-REST/assets/slide-014-fig-01.jpg)

## Slide 15 - REST: Design Principles

REST: Design Principles

Identify all the resources which have to be exposed

Create a URI for each resource, preferably using nouns
and verbs

Determine which HTTP request methods are needed for
each resource

Link resource and “unveil” information by following links

Specify the format of representation of a resource,
possibly using a schema

Accurately document all the services

![Figura 1 dalla slide 15](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/08-Webapp-2025-26-REST/assets/slide-015-fig-01.jpg)

## Slide 16 - Documenting a REST API

Documenting a REST API

/{ }

*(7
3267
'(/(7(
387

GET

LG >LQWHJHU@

id=[integer]

SKRWRBLG >DOSKDQXPHULF@

{ id : 12, name : "Michael Bloom" }

^ LG
  `

{ error : "User doesn't exist" }

^ HUURU
 /RJ LQ `

{ error : "You are unauthorized to make this request." }

^ HUURU
 (PDLO ,QYDOLG `

 $.ajax({

 url: "/users/1",
 dataType: "json",
 type : "GET",
 success : function(r) {

 console.log(r);
 }
 });

## Slide 17 - WADL: Web Application Description Language

WADL: Web Application Description Language

WADL is a machine-
readable XML description
of HTTP-based web services,
in particular REST services

WADL was submitted to
the W3C by Sun
Microsystems on 31 August
2009, but W3C has no
current plans to standardise it

<?xml version="1.0"?>
<application xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 xsi:schemalocation="http://wadl.dev.java.net/2009/02 wadl.xsd"
 xmlns:tns="urn:yahoo:yn" xmlns:xsd="http://www.w3.org/2001/XMLSchema"
 xmlns:yn="urn:yahoo:yn" xmlns:ya="urn:yahoo:api"
 xmlns="http://wadl.dev.java.net/2009/02">
 <grammars>
  <include href="NewsSearchResponse.xsd" /> <include href="Error.xsd" />
 </grammars>
 <resources base="http://api.search.yahoo.com/NewsSearchService/V1/">
  <resource path="newsSearch">
   <method name="GET" id="search">
    <request>
     <param name="appid" type="xsd:string" style="query" required="true" />
     <param name="query" type="xsd:string" style="query" required="true" />
     <param name="type" style="query" default="all">
      <option value="all" /> <option value="any" />
      <option value="phrase" />
     </param>
     <param name="results" style="query" type="xsd:int" default="10" />
     <param name="start" style="query" type="xsd:int" default="1" />
     <param name="sort" style="query" default="rank">
      <option value="rank" /> <option value="date" />
     </param>
     <param name="language" style="query" type="xsd:string" />
    </request>
    <response status="200">
     <representation mediatype="application/xml" element="yn:ResultSet" />
    </response>
    <response status="400">
     <representation mediatype="application/xml" element="ya:Error" />
    </response>
   </method>
  </resource>
 </resources>
</application>
Hadley, M. (2009). Web Application Description Language – W3C Member Submission 31 August 2009
https://www.w3.org/Submission/wadl/

## Slide 18 - OAI: OpenAPI Initiative

OAI: OpenAPI Initiative

openapi: "3.0.0"
info:
  version: 1.0.0
  title: Swagger Petstore
  license:
    name: MIT
servers:
  - url: http://petstore.swagger.io/v1
paths:
  /pets:
    get:
      summary: List all pets
      operationId: listPets
      tags:
        - pets
      parameters:
        - name: limit
          in: query
          description: How many items to return at one time (max 100)
          required: false
          schema:
            type: integer
            format: int32
      responses:
        '200':
          description: An paged array of pets
          headers:
            x-next:
              description: A link to the next page of responses
              schema:
                type: string
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Pets"
        default:
          description: unexpected error
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Error"
    post:
      summary: Create a pet
      operationId: createPets
      tags:
        - pets
      responses:
        '201':
          description: Null response
        default:
          description: unexpected error
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Error"

p
  /pets/{petId}:
    get:
      summary: Info for a specific pet
      operationId: showPetById
      tags:
        - pets
      parameters:
        - name: petId
          in: path
          required: true
          description: The id of the pet to retrieve
          schema:
            type: string
      responses:
        '200':
          description: Expected response to a valid request
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Pets"
        default:
          description: unexpected error
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Error"
components:
  schemas:
    Pet:
      required:
        - id
        - name
      properties:
        id:
          type: integer
          format: int64
        name:
          type: string
        tag:
          type: string
    Pets:
      type: array
      items:
        $ref: "#/components/schemas/Pet"
    Error:
      required:
        - code
        - message
      properties:
        code:
          type: integer
          format: int32
        message:
          type: string

 OpenAPI Initiative (OAI) was created by a consortium of industries to standardise how REST APIs are described

It is one of the Linux Foundation’s Collaborative Projects

![Figura 1 dalla slide 18](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/08-Webapp-2025-26-REST/assets/slide-018-fig-01.jpg)

## Slide 19 - Accessing a database via

Accessing a database via

REST and JDBC

![Figura 1 dalla slide 19](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/08-Webapp-2025-26-REST/assets/slide-019-fig-01.jpg)

## Slide 20 - REST API

REST API

URI
Method
Description

/rest/employee
GET
lists all the employees

/rest/employee
POST
creates a new employee

/rest/employee/{badge}
GET
reads the data about the employee with
the given badge

/rest/employee/{badge}
PUT
updates the data about the employee
with the given badge

/rest/employee/{badge}
DELETE
deletes the data about the employee
with the given badge

/rest/employee/salary/{salary}
GET
searches for all the employees with
salary above salary

## Slide 21 - JSON Resources

JSON Resources

{
   "employee":{
      "badge":7309,
      "surname":"Rossi",
      "age":34,
      "salary":45
   }
}

{
   "message":{
      "message":"Unsupported operation.",
      "error-code":"E500",
      "error-details":"OPTIONS"
   }
}

{
   "resource-list":[
      {
         "employee":{
            "badge":7309,
            "surname":"Rossi",
            "age":34,
            "salary":45
         }
      },
      {
         "employee":{
            "badge":4076,
            "surname":"Mori",
            "age":45,
            "salary":50
         }
      }
   ]
}

![Figura 1 dalla slide 21](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/08-Webapp-2025-26-REST/assets/slide-021-fig-01.jpg)

## Slide 22 - Error Codes

Error Codes

Error Code
HTTP Status Code
Cause

E4A1
400
Bad Request
Output media type not specified

E4A2
406
Not Acceptable
Unsupported output media type

E4A3
400
Bad Request
Input media type not specified

E4A4
415
Unsupported Media Type
Unsupported input media type

E4A5
405
Method Not Allowed
Unsupported operation

E4A6
 404
Not Found
Unknown resource requested

E4A7
400
Bad Request
Wrong URI format

E4A8
400
Bad Request
Wrong resource provided

## Slide 23 - Error Codes

Error Codes

Error Code
HTTP Status Code
Cause

E5A1
500
500 Internal Server Error

Unexpected error while processing a
resource

E5A2
 409
Conflict
Resource already exists

E5A3
 404
Not Found
Resource not found

E5A4
 409
Conflict

Cannot modify a resource because
other resources depend on it

## Slide 24 - Employee REST Web Service Class Diagram

Employee REST Web Service Class Diagram

![Figura 1 dalla slide 24](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/08-Webapp-2025-26-REST/assets/slide-024-fig-01.jpg)

## Slide 25 - Employee REST Web Service: CREATE Sequence Diagram

Employee REST Web Service: CREATE Sequence Diagram

![Figura 1 dalla slide 25](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/08-Webapp-2025-26-REST/assets/slide-025-fig-01.jpg)

## Slide 26 - The Resource Interface

The Resource Interface

![Figura 1 dalla slide 26](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/08-Webapp-2025-26-REST/assets/slide-026-fig-01.jpg)

## Slide 27 - The AbstractResource Class

The AbstractResource Class

Sets up the JsonFactory to create
JsonParser and JsonGenerator objects

Delegate the actual writing of
JSON to subclasses and

manage exceptions

public abstract class AbstractResource implements Resource {¬
¬
    protected static final Logger LOGGER = LogManager.getLogger(AbstractResource.class, ¬
        StringFormatterMessageFactory.INSTANCE);¬
¬
    protected static final JsonFactory JSON_FACTORY;¬
¬
    static {¬
        // set up the JSON factory¬
        JSON_FACTORY = new JsonFactory();¬
        JSON_FACTORY.disable(JsonGenerator.Feature.AUTO_CLOSE_TARGET);¬
        JSON_FACTORY.disable(JsonParser.Feature.AUTO_CLOSE_SOURCE);¬
¬
        LOGGER.debug("JSON factory successfully setup.");¬
    }¬
¬
    @Override¬
    public void toJSON(final OutputStream out) throws IOException {¬
¬
        if(out == null) {¬
            LOGGER.error("The output stream cannot be null.");¬
            throw new IOException("The output stream cannot be null.");¬
        }¬
¬
        try {¬
            writeJSON(out);¬
        } catch(Exception e) {¬
            LOGGER.error("Unable to serialize the resource to JSON.", e);¬
            throw new IOException("Unable to serialize the resource to JSON.", e);¬
        }¬
¬
    }¬
¬
    protected abstract void writeJSON(OutputStream out) throws Exception;¬
}¬

![Figura 1 dalla slide 27](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/08-Webapp-2025-26-REST/assets/slide-027-fig-01.jpg)

## Slide 28 - The Message Class

The Message Class

Obtain a new JsonGenerator to
represent the resource to JSON

Write the actual content of the
representation, step-by-step

Always ensure to fl
ff

![Figura 1 dalla slide 28](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/08-Webapp-2025-26-REST/assets/slide-028-fig-01.jpg)

## Slide 29 - The Employee Class

The Employee Class

Obtain a new JsonGenerator to
represent the resource to JSON

Write the actual content of the
representation, step-by-step

Always ensure to fl
ff

![Figura 1 dalla slide 29](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/08-Webapp-2025-26-REST/assets/slide-029-fig-01.jpg)

## Slide 30 - The Employee Class

The Employee Class

Obtain a new JsonParser to
parse Employee from JSON

Looks for a fi

Iterate through the fi

Create and return a new Employee from the
parsed information

public static Employee fromJSON(final InputStream in) throws IOException  {¬
¬
        // the fields read from JSON¬
        int jBadge = -1;¬
        String jSurname = null;¬
        int jAge = -1;¬
        int jSalary = -1;¬
¬
        try {¬
            final JsonParser jp = JSON_FACTORY.createParser(in);¬
¬
            // while we are not on the start of an element or the element is not¬
            // a token element, advance to the next element (if any)¬
            while (jp.getCurrentToken() != JsonToken.FIELD_NAME || !"employee".equals(jp.getCurrentName())) {¬
¬
                // there are no more events¬
                if (jp.nextToken() == null) {¬
                    LOGGER.error("No Employee object found in the stream.");¬
                    throw new EOFException("Unable to parse JSON: no Employee object found.");¬
                }¬
            }¬
¬
            while (jp.nextToken() != JsonToken.END_OBJECT) {¬
¬
                if (jp.getCurrentToken() == JsonToken.FIELD_NAME) {¬
¬
                    switch (jp.getCurrentName()) {¬
                        case "badge":¬
                            jp.nextToken();¬
                            jBadge = jp.getIntValue();¬
                            break;¬
                        case "surname":¬
                            jp.nextToken();¬
                            jSurname = jp.getText();¬
                            break;¬
                        case "age":¬
                            jp.nextToken();¬
                            jAge = jp.getIntValue();¬
                            break;¬
                        case "salary":¬
                            jp.nextToken();¬
                            jSalary = jp.getIntValue();¬
                            break;¬
                    }¬
                }¬
            }¬
        } catch(IOException e) {¬
            LOGGER.error("Unable to parse an Employee object from JSON.", e);¬
            throw e;¬
        }¬
¬
        return new Employee(jBadge, jSurname, jAge, jSalary);¬
}

## Slide 31 - The ResourceList Class

The ResourceList Class

Hold a generic list of Resource
objects (subclasses of)

Begin a new resource-list
JSON object (an array)

Iterate through the list and ask each
resource to represent itself to JSON

Need to add , between elements of
an array in JSON

public final class ResourceList<T extends Resource> extends AbstractResource {¬
¬
    private final Iterable<T> list;¬
¬
    public ResourceList(final Iterable<T> list) {¬
¬
        if(list == null) {¬
            LOGGER.error("Resource list cannot be null.");¬
            throw new NullPointerException("Resource list cannot be null.");¬
        }¬
¬
        this.list = list;¬
    }¬
¬
    @Override¬
    protected void writeJSON(final OutputStream out) throws IOException {¬
¬
        final JsonGenerator jg = JSON_FACTORY.createGenerator(out);¬
¬
        jg.writeStartObject();¬
¬
        jg.writeFieldName("resource-list");¬
¬
        jg.writeStartArray();¬
¬
        jg.flush();¬
¬
        boolean firstElement = true;¬
¬
        for (final Resource r : list) {¬
¬
            // very bad work-around to add commas between resources¬
            if (firstElement) {¬
                r.toJSON(out);¬
                jg.flush();¬
¬
                firstElement = false;¬
            } else {¬
                jg.writeRaw(',');¬
                jg.flush();¬
¬
                r.toJSON(out);¬
                jg.flush();¬
            }¬
        }¬
¬
        jg.writeEndArray();¬
¬
        jg.writeEndObject();¬
¬
        jg.flush();¬
    }¬
¬
}

## Slide 32 - The AbstractDatabaseServlet Class

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

![Figura 1 dalla slide 32](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/08-Webapp-2025-26-REST/assets/slide-032-fig-01.jpg)

## Slide 33 - The RestDispatcherServlet Class

The RestDispatcherServlet Class

We override the service method
to personalize the way in which we
analyze the request and decide which

REST resource should handle it

Check whether the request is for an Employee
resource and, in case, delegate its processing.

You can have as many of these checks as many

diff

If no check succeeded, it
means that an unknown

resource has been requested.

Always ensure to fl

![Figura 1 dalla slide 33](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/08-Webapp-2025-26-REST/assets/slide-033-fig-01.jpg)

## Slide 34 - The RestDispatcherServlet Class

The RestDispatcherServlet Class

Layman analysis the request and, if it is
actually about one of the Employee API,
delegate its actual processing to the REST

resource

If it is not one of the Employee API, return.

E.g., if it matches GET /employee delegate
to the ListEmployeeRR REST resource the

handling of the request

![Figura 1 dalla slide 34](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/08-Webapp-2025-26-REST/assets/slide-034-fig-01.jpg)

## Slide 35 - The RestResource Interface

The RestResource Interface

![Figura 1 dalla slide 35](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/08-Webapp-2025-26-REST/assets/slide-035-fig-01.jpg)

## Slide 36 - The AbstractRR Class

The AbstractRR Class

Convenience list of
MIME media types

The request, response, and
connection to the database

The action performed by the REST
resource, for logging purposes

public abstract class AbstractRR implements RestResource {¬
¬
    protected static final Logger LOGGER = LogManager.getLogger(AbstractRR.class,¬
            StringFormatterMessageFactory.INSTANCE);¬
¬
    protected static final String JSON_MEDIA_TYPE = "application/json";¬
¬
    protected static final String JSON_UTF_8_MEDIA_TYPE = "application/json; charset=utf-8";¬
¬
    protected static final String ALL_MEDIA_TYPE = "*/*";¬
¬
    protected final HttpServletRequest req;¬
¬
    protected final HttpServletResponse res;¬
¬
    protected final Connection con;¬
¬
    private final String action;¬
¬
    protected AbstractRR(final String action, final HttpServletRequest req, final HttpServletResponse res, final Connection con) {¬
¬
        if (action == null || action.isBlank()) {¬
            LOGGER.warn("Action is null or empty.");¬
        }¬
        this.action = action;¬
        LogContext.setAction(action);¬
¬
        if (req == null) {¬
            LOGGER.error("The HTTP request cannot be null.");¬
            throw new NullPointerException("The HTTP request cannot be null.");¬
        }¬
        this.req = req;¬
¬
        if (res == null) {¬
            LOGGER.error("The HTTP response cannot be null.");¬
            throw new NullPointerException("The HTTP response cannot be null.");¬
        }¬
        this.res = res;¬
¬
        if (con == null) {¬
            LOGGER.error("The connection cannot be null.");¬
            throw new NullPointerException("The connection cannot be null.");¬
        }¬
        this.con = con;¬
    }¬
¬

## Slide 37 - The AbstractRR Class

The AbstractRR Class

 @Override¬
 public void serve() throws IOException {¬

Check that the input/output MIME
media types are what expected for

     try {¬
         // if the request method and/or the MIME media type are not allowed, return.¬
         // Appropriate error message sent by {@code checkMethodMediaType}¬
         if (!checkMethodMediaType(req, res)) {¬
             return;¬
         }¬

the request HTTP method

         doServe();¬
     } catch (Throwable t) {¬
         LOGGER.error("Unable to serve the REST request.", t);¬

Delegate to subclasses the
handling of the REST request

and manage error conditions

         final Message m = new Message(String.format("Unable to serve the REST request: %s.", action), "E5A1",¬
                 t.getMessage());¬
         res.setStatus(HttpServletResponse.SC_INTERNAL_SERVER_ERROR);¬
         m.toJSON(res.getOutputStream());¬
     } finally {¬
         LogContext.removeAction();¬
         LogContext.removeResource();¬
     }¬
 }¬

 protected abstract void doServe() throws IOException;¬

Subclasses have to implement
the actual logic for serving the

REST request

![Figura 1 dalla slide 37](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/08-Webapp-2025-26-REST/assets/slide-037-fig-01.jpg)

## Slide 38 - The AbstractRR Class

The AbstractRR Class

 protected boolean checkMethodMediaType(final HttpServletRequest req, final HttpServletResponse res) throws¬
         IOException {¬

Subclasses may override
checkMethodMediaType to

implement their own behavior

     final String method = req.getMethod();¬
     final String contentType = req.getHeader("Content-Type");¬
     final String accept = req.getHeader("Accept");¬
     final OutputStream out = res.getOutputStream();¬

     Message m = null;¬

An output media type
needs to be specifi

     if (accept == null) {¬
         LOGGER.error("Output media type not specified. Accept request header missing.");¬
         m = new Message("Output media type not specified.", "E4A1", "Accept request header missing.");¬
         res.setStatus(HttpServletResponse.SC_BAD_REQUEST);¬
         m.toJSON(out);¬
         return false;¬
     }¬

The output media type must
be either any or JSON

     if (!accept.contains(JSON_MEDIA_TYPE) && !accept.equals(ALL_MEDIA_TYPE)) {¬
         LOGGER.error(¬
                 "Unsupported output media type. Resources are represented only in application/json. Requested representation is %s.",¬
                 accept);¬
         m = new Message("Unsupported output media type. Resources are represented only in application/json.",¬
                 "E4A2", String.format("Requested representation is %s.", accept));¬
         res.setStatus(HttpServletResponse.SC_NOT_ACCEPTABLE);¬
         m.toJSON(out);¬
         return false;¬
     }¬

For GET and DELETE methods the above
checks on the output media type are enough

     // if the method is supposed to send a body, check its MIME media type¬
     switch (method) {¬
         case "GET":¬
         case "DELETE":¬
             // nothing to do¬
             break;¬

For PUT and POST we need to
check that an input media type is

         case "POST":¬
         case "PUT":¬
             if (contentType == null) {¬
                 LOGGER.error("Input media type not specified. Content-Type request header missing.");¬
                 m = new Message("Input media type not specified.", "E4A3", "Content-Type request header missing.");¬
                 res.setStatus(HttpServletResponse.SC_BAD_REQUEST);¬
                 m.toJSON(out);¬
                 return false;¬
             }¬

specifi

             if (!contentType.contains(JSON_MEDIA_TYPE)) {¬
                 LOGGER.error(¬
                         "Unsupported input media type. Resources are represented only in application/json. Submitted representation is %s.",¬
                         contentType);¬
                 m = new Message("Unsupported input media type. Resources are represented only in application/json.",¬
                         "E4A4", String.format("Submitted representation is %s.", contentType));¬
                 res.setStatus(HttpServletResponse.SC_UNSUPPORTED_MEDIA_TYPE);¬
                 m.toJSON(out);¬
                 return false;¬
             }¬

No other HTTP methods
are allowed

             break;¬
         default:¬
             LOGGER.error("Unsupported operation. Requested operation %s.", method);¬
             m = new Message("Unsupported operation.", "E4A5", String.format("Requested operation %s.", method));¬
             res.setStatus(HttpServletResponse.SC_METHOD_NOT_ALLOWED);¬
             m.toJSON(out);¬
             return false;¬
     }¬

## Slide 39 - The CreateEmployeeRR Class

The CreateEmployeeRR Class

Calls the superclass constructor
specifying the action performed by

this REST resource

Reads the employee JSON
object from the request and

creates an Employee object

Delegates to the DAO the
access to the database

Asks the Employee to write
itself to the response

Manages error conditions and
writes appropriate message to

the response

public final class CreateEmployeeRR extends AbstractRR {¬
¬
    public CreateEmployeeRR(final HttpServletRequest req, final HttpServletResponse res, Connection con) {¬
        super(Actions.CREATE_EMPLOYEE, req, res, con);¬
    }¬
¬
¬
    @Override¬
    protected void doServe() throws IOException {¬
¬
        Employee e = null;¬
        Message m = null;¬
¬
        try {¬
            final Employee employee = Employee.fromJSON(req.getInputStream());¬
¬
            LogContext.setResource(Integer.toString(employee.getBadge()));¬
¬
            // creates a new DAO for accessing the database and stores the employee¬
            e = new CreateEmployeeDAO(con, employee).access().getOutputParam();¬
¬
            if (e != null) {¬
                LOGGER.info("Employee successfully created.");¬
¬
                res.setStatus(HttpServletResponse.SC_CREATED);¬
                e.toJSON(res.getOutputStream());¬
            } else { // it should not happen¬
                LOGGER.error("Fatal error while creating employee.");¬
¬
                m = new Message("Cannot create the employee: unexpected error.", "E5A1", null);¬
                res.setStatus(HttpServletResponse.SC_INTERNAL_SERVER_ERROR);¬
                m.toJSON(res.getOutputStream());¬
            }¬
        } catch (EOFException ex) {¬
            LOGGER.warn("Cannot create the employee: no Employee JSON object found in the request.", ex);¬
¬
            m = new Message("Cannot create the employee: no Employee JSON object found in the request.", "E4A8",¬
                    ex.getMessage());¬
            res.setStatus(HttpServletResponse.SC_BAD_REQUEST);¬
            m.toJSON(res.getOutputStream());¬
        } catch (SQLException ex) {¬
            if ("23505".equals(ex.getSQLState())) {¬
                LOGGER.warn("Cannot create the employee: it already exists.");¬
¬
                m = new Message("Cannot create the employee: it already exists.", "E5A2", ex.getMessage());¬
                res.setStatus(HttpServletResponse.SC_CONFLICT);¬
                m.toJSON(res.getOutputStream());¬
            } else {¬
                LOGGER.error("Cannot create the employee: unexpected database error.", ex);¬
¬
                m = new Message("Cannot create the employee: unexpected database error.", "E5A1", ex.getMessage());¬
                res.setStatus(HttpServletResponse.SC_INTERNAL_SERVER_ERROR);¬
                m.toJSON(res.getOutputStream());¬
            }¬
        }¬
    }¬
¬
¬
}¬

## Slide 40 - The CreateEmployeeDAO Class

The CreateEmployeeDAO Class

public final class CreateEmployeeDAO extends AbstractDAO<Employee> {¬
¬

   private static final String STATEMENT = "INSERT INTO Ferro.Employee (badge, surname, age, salary) VALUES (?, ?, ?, ?) RETURNING *";¬
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

RETURNING is a PostgreSQL
extension to standard SQL to read the
row as it is in the database just after

executing the requested statement

   @Override¬
   protected final void doAccess() throws SQLException {¬
¬

       PreparedStatement pstmt = null;¬
       ResultSet rs = null;¬
¬

       // the created employee¬
       Employee e = null;¬
¬

       try {¬
           pstmt = con.prepareStatement(STATEMENT);¬
           pstmt.setInt(1, employee.getBadge());¬
           pstmt.setString(2, employee.getSurname());¬
           pstmt.setInt(3, employee.getAge());¬
           pstmt.setInt(4, employee.getSalary());¬
¬

Create a new Employee as it is
returned from the just executed
database statement

           rs = pstmt.executeQuery();¬
¬

           if (rs.next()) {¬
               e = new Employee(rs.getInt("badge"), rs¬
                       .getString("surname"), rs.getInt("age"),¬
                       rs.getInt("salary"));¬
¬

               LOGGER.info("Employee %d successfully stored in the database.", e.getBadge());¬
           }¬
       } finally {¬
           if (pstmt != null) {¬
               pstmt.close();¬
           }¬
       }¬
¬

       outputParam = e;¬
¬

Set the output parameter for the DAO
with the employee just created from
the database

![Figura 1 dalla slide 40](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/08-Webapp-2025-26-REST/assets/slide-040-fig-01.jpg)

## Slide 41 - The web.xml Configuration File

The web.xml Configuration File

Every request under the /rest URL
is sent to the

RestDispactherServlet class

![Figura 1 dalla slide 41](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/08-Webapp-2025-26-REST/assets/slide-041-fig-01.jpg)

## Slide 42 - Project Object Model (POM)

Project Object Model (POM)

Adds the dependency on
the Jackson JSON parser.

![Figura 1 dalla slide 42](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/08-Webapp-2025-26-REST/assets/slide-042-fig-01.jpg)

## Slide 43 - Example of execution

Example of execution

![Figura 1 dalla slide 43](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/08-Webapp-2025-26-REST/assets/slide-043-fig-01.jpg)

## Slide 44 - Example of execution

Example of execution

![Figura 1 dalla slide 44](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/08-Webapp-2025-26-REST/assets/slide-044-fig-01.jpg)

## Slide 45 - Example of execution

Example of execution

![Figura 1 dalla slide 45](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/08-Webapp-2025-26-REST/assets/slide-045-fig-01.jpg)

## Slide 46 - Example of execution

Example of execution

![Figura 1 dalla slide 46](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/08-Webapp-2025-26-REST/assets/slide-046-fig-01.jpg)

## Slide 47 - Example of execution

Example of execution

![Figura 1 dalla slide 47](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/08-Webapp-2025-26-REST/assets/slide-047-fig-01.jpg)

## Slide 48 - Example of execution

Example of execution

![Figura 1 dalla slide 48](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/08-Webapp-2025-26-REST/assets/slide-048-fig-01.jpg)

## Slide 49 - Accessing a database via

Accessing a database via

REST, JDBC and AJAX

![Figura 1 dalla slide 49](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/08-Webapp-2025-26-REST/assets/slide-049-fig-01.jpg)

## Slide 50 - The Search-Employee-Form JSP Page

The Search-Employee-Form JSP Page

The JS code reads the value in this
text fi

An EventListener is added to the
button to issue an AJAX call when it is

pressed

The JS code writes the results of the
AJAX call in this div.

Bad practice to use the style attribute!

The JS code performing all
the needed operations

![Figura 1 dalla slide 50](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/08-Webapp-2025-26-REST/assets/slide-050-fig-01.jpg)

## Slide 51 - The AJAX Employee JS Code

The AJAX Employee JS Code

Adds the
searchEmployeeBySalary() event

listener call back to the button

Logs to the (browser) console.

![Figura 1 dalla slide 51](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/08-Webapp-2025-26-REST/assets/slide-051-fig-01.jpg)

## Slide 52 - The AJAX Employee JS Code

The AJAX Employee JS Code

Retrieves the value of
salary from the form

Prepares the URL of the
request, appending the salary

[not safe enough, validation!]

Defi

Performs the actual HTTP request

![Figura 1 dalla slide 52](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/08-Webapp-2025-26-REST/assets/slide-052-fig-01.jpg)

## Slide 53 - The AJAX Employee JS Code

The AJAX Employee JS Code

Checks whether the
response is ready to be

processed

Obtains the div where to write
the outcomes of the response

If the request was not successful,
writes an error message in the div

At this point the request was
successful and it writes the result

table step by step

![Figura 1 dalla slide 53](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/08-Webapp-2025-26-REST/assets/slide-053-fig-01.jpg)

## Slide 54 - The AJAX Employee JS Code

The AJAX Employee JS Code

Parses the body of the response
into a JSON object and obtains the

array of employees

Iterates over each employee in
the array and writes and HTML

table row for it

![Figura 1 dalla slide 54](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/08-Webapp-2025-26-REST/assets/slide-054-fig-01.jpg)

## Slide 55 - Slide 55
