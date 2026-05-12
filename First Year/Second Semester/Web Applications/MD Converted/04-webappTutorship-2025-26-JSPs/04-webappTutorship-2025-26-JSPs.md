# 04-webappTutorship-2025-26-JSPs

_Source: `04-webappTutorship-2025-26-JSPs.pdf`_

## Slide 1 - Tutoring 04

Tutoring 04

JSPs

Francesco L. De Faveri

Web Applications Tutoring

Academic Year: 2025-2026

![Figura 1 dalla slide 1](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webappTutorship-2025-26-JSPs/assets/slide-001-fig-01.jpg)

## Slide 2 - Outline

Outline

●
General Information

●
DAOs

●
JavaBeans & JSP

●
Example from SIGIR25 WebApp

![Figura 1 dalla slide 2](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webappTutorship-2025-26-JSPs/assets/slide-002-fig-01.jpg)

## Slide 3 - General Information

General Information

![Figura 1 dalla slide 3](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webappTutorship-2025-26-JSPs/assets/slide-003-fig-01.jpg)

## Slide 4 - Reminders: Tutoring Lectures

Reminders: Tutoring Lectures

●
No Tutoring lecture on April 6th 2026 - Easter Monday

●
No Tutoring lecture on April 13th 2026

●
Next Tutoring lecture (number 5) on April 20th 2026

●
HW 1 Code + Project Deadline on April 24th 2026

![Figura 1 dalla slide 4](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webappTutorship-2025-26-JSPs/assets/slide-004-fig-01.jpg)

## Slide 5 - General Information

General Information

If you have issues with your local PC conﬁguration try to solve
them as soon as

possible (we can discuss about conﬁguration problems after the
tutorships).

Remember: you all need to equally contribute in all the parts of
the homework!

![Figura 1 dalla slide 5](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webappTutorship-2025-26-JSPs/assets/slide-005-fig-01.jpg)

## Slide 6 - DAOs

DAOs

![Figura 1 dalla slide 6](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webappTutorship-2025-26-JSPs/assets/slide-006-fig-01.jpg)

## Slide 7 - DAOs

DAOs

The Data Access Object (DAO) pattern abstracts and
encapsulates all the logic need to access a data source,
typically a relational database.

DAO objects are one-shot and they are not expected to be
re-used.

![Figura 1 dalla slide 7](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webappTutorship-2025-26-JSPs/assets/slide-007-fig-01.jpg)

## Slide 8 - Connect to the DB

Connect to the DB

1.
Write the context.xml ﬁle
The context.xml is a conﬁguration ﬁle deﬁnes a connection pool that
your application can use to connect to the database. Basing on the
professor’s examples change the following elements: Name, url,
username, password according to your postgres conﬁguration
Remember that if you run a docker container the URL must not contain
localhost!! It must contain the docker service name instead (i.e., db)
followed by the port you are mapping to.

2.
In the web.xml add the <resource-ref> where you report the resource
name declared in the context.xml

![Figura 1 dalla slide 8](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webappTutorship-2025-26-JSPs/assets/slide-008-fig-01.jpg)

## Slide 9 - DAOs

DAOs

1.
In the dao folder, put the AbstractDAO and the DataAccessObject interface.
They should not be modiﬁed. Put these class and interface in your project and
extend/implement them (DO NOT LEAVE THEM AS THEY ARE).

2.
The AbstractDAO implements the DataAccessObject interface. In this way, all
the subclasses have a uniform behaviour.

3.
The DataAccessObject interface encapsulates all the logic to access the
database.

4.
Deﬁne a DAO for each access operation
→ If we have to search some users, insert new users, modify users’ data, delete
an user, we will have 4 DAOs.

![Figura 1 dalla slide 9](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webappTutorship-2025-26-JSPs/assets/slide-009-fig-01.jpg)

## Slide 10 - SIGIR WebApp - DAOs

SIGIR WebApp - DAOs

1.
SearchUserDAO → allows to search for a user given an
attribute

2.
SearchTrackDAO → allows to search for a track given an
attribute

3.
InsertUserDAO → allows to insert a new user.

![Figura 1 dalla slide 10](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webappTutorship-2025-26-JSPs/assets/slide-010-fig-01.jpg)

## Slide 11 - DAO - Transactions

DAO - Transactions

A DAO might contain multiple statements which can involve different tables.

Ex. I want to create a new user together with a new track → I have to add the track
in the track table, the users in the users table and “link them”.
But, if something strange happens – i.e., connection goes down – I don’t want that
the track is added but its user(s) are not.

I want to execute these two operations in a single transaction (multiple operations
executed as a single unit) which rolls back if needed.

Here you can ﬁnd an example:

https://bitbucket.org/frrncl/tutor-2023/src/master/group_creation_rest_17042023/sr
c/main/java/GroupCreation/dao/CreateGroupDAO.java

![Figura 1 dalla slide 11](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webappTutorship-2025-26-JSPs/assets/slide-011-fig-01.jpg)

## Slide 12 - Example: Adding a new user

Example: Adding a new user

## Slide 13 - JavaBeans & JSP

JavaBeans & JSP

![Figura 1 dalla slide 13](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webappTutorship-2025-26-JSPs/assets/slide-013-fig-01.jpg)

## Slide 14 - JavaBeans

JavaBeans

How do JSPs communicate with the application? → JavaBeans

JavaBeans:
Java classes providing reusable software component which
follows a speciﬁc naming conventions and that are manipulated
in an application framework.

They have some accessor methods: “get” and “set” depending
on the ﬁeld, and “is” for boolean.

![Figura 1 dalla slide 14](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webappTutorship-2025-26-JSPs/assets/slide-014-fig-01.jpg)

## Slide 15 - Java Server Pages (JSP)

Java Server Pages (JSP)

Writing HTML pages directly from the server is not the best
practice especially if you need to add styles to the page (i.e.,
css) or dynamic content (i.e., javascript).

●
JSPs are dynamic pages that can generate HTML (or other
types of documents) in response to a user request.

●
JSPs are server-side technologies, hence they are executed
on the server before rendering a page to a browser.

![Figura 1 dalla slide 15](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webappTutorship-2025-26-JSPs/assets/slide-015-fig-01.jpg)

## Slide 16 - Java Server Pages (JSP)

Java Server Pages (JSP)

Writing HTML pages directly from the server is not the best practice
especially if you need to add styles to the page (i.e., css) or dynamic
content (i.e., javascript)

●
JSPs are dynamic pages that can generate HTML (or other types
of documents) in response to a user request.

●
JSPs are server-side technologies, hence they are executed on
the server before rendering a page to a browser.

In the Developer tools (F12, more to see in Tutoring Lecture 6) there is
only the HTML code, there are no JSP tags!

![Figura 1 dalla slide 16](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webappTutorship-2025-26-JSPs/assets/slide-016-fig-01.jpg)

## Slide 17 - JSP Components

JSP Components

Template → Static HTML

Directives → global information, independent of the requests received by the JSP pages

<@ page .. @>

<@ include .. @>

<@ taglib .. @>

Actions → Perform an operation (standard/custom)

Scripting → TO BE AVOIDED IF IT IS POSSIBLE!

Expression Language → used to access data and variables made available from the
application ${...} - You will use it a lot!!!!

![Figura 1 dalla slide 17](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webappTutorship-2025-26-JSPs/assets/slide-017-fig-01.jpg)

## Slide 18 - <@ include … @> VS <jsp:include>

<@ include … @> VS <jsp:include>

<@ include ... @> is static → the inclusion occurs at translation time. This means
that the contents of the included ﬁle are merged with the JSP page before it is
compiled into a servlet. This can be useful for reusing code across multiple pages
and ensuring consistency across them.

Examples: header and footer of the web app

<jsp:include> is dynamic → Standard action in JSP that allows you to include the
contents of another ﬁle in the current page at the time of request processing. This
means that the contents of the included ﬁle are merged with the JSP page at
runtime, when the page is requested by the client. This can be useful for including
dynamic content or content that may change frequently.

Examples: the list of products related to a product the user checked

![Figura 1 dalla slide 18](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webappTutorship-2025-26-JSPs/assets/slide-018-fig-01.jpg)

## Slide 19 - <c:import>

<c:import>

<c:import url= ...> allows you to import AT REQUEST TIME the
value of the URL attribute.

→ The url can also correspond to a remote resource! ←

<jsp:include> works only with local resources.

![Figura 1 dalla slide 19](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webappTutorship-2025-26-JSPs/assets/slide-019-fig-01.jpg)

## Slide 20 - Redirection

Redirection

In order to redirect the client to a different URL we need to call the sendRedirect method in
our servlets, which is provided by the HttpServletResponse interface.

The unique argument of this method is the new URL to be redirected to. In this case the
client creates a new request to the new URL, the original request and response are lost
(together with the associated parameters)!

Example: after login redirect to userpage

If we call a sendRedirect directly from the doPost or the doGet servlet, the client will always
issue a get request to the desired URL!

If in the argument of the sendRedirect we put a jsp page, the browser will retrieve the
resource using a GET request.

→ THE URL YOU SEE IN THE URL BAR WILL CHANGE AFTER THE REDIRECTION

![Figura 1 dalla slide 20](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webappTutorship-2025-26-JSPs/assets/slide-020-fig-01.jpg)

## Slide 21 - Redirection

Redirection

In order to redirect the client to a different URL we need to call the sendRedirect method in
our servlets, which is provided by the HttpServletResponse interface.

The unique argument of this method is the new URL to be redirected to. In this case the
client creates a new request to the new URL, the original request and response are lost
(together with the associated parameters)!

Example: after login redirect to userpage

If we call a sendRedirect directly from the doPost or the doGet servlet, the client will always
issue a get request to the desired URL!

If in the argument of the sendRedirect we put a jsp page, the browser will retrieve the
resource using a GET request.

→ THE URL YOU SEE IN THE URL BAR WILL CHANGE AFTER THE REDIRECTION

![Figura 1 dalla slide 21](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webappTutorship-2025-26-JSPs/assets/slide-021-fig-01.jpg)

## Slide 22 - RequestDispatcher - Forward

RequestDispatcher - Forward

To pass the control from Servlets to other Servlets/JSPs we use the method forward of the
RequestDispatcher.
The unique argument of this method is the new URL to be redirected to.

In this case, the response of the other resource is sent back to the client (NOT THE ONE OF THE
SERVLET WHICH CALLED THE FORWARD).

If you execute the forward from a doPost, the doPost of the required servlet will be called:

doPost → forward → doPost

doGet → forward → doGet

The URL does not change → the client never knows about how many jsp pages or servlets were
involved in the response generation.

Example: request.getRequestDispatcher(“forwardServlet").forward()

![Figura 1 dalla slide 22](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webappTutorship-2025-26-JSPs/assets/slide-022-fig-01.jpg)

## Slide 23 - RequestDispatcher - Include

RequestDispatcher - Include

To to include in a servlet the output of another servlet, we call the include
method of the RequestDispatcher.

Things to pay attention to when you use include:

●
The «included» servlet must not return anything to the client while it is
handled.

●
The path of the included resource is relative to the current servlet: if you
want to include a resource located in a different directory make sure
you speciﬁed the full path.

Example: request.getRequestDispatcher(“includeServlet").include()

![Figura 1 dalla slide 23](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webappTutorship-2025-26-JSPs/assets/slide-023-fig-01.jpg)

## Slide 24 - Forward, include or redirect?

Forward, include or redirect?

Use forward if you want to:

●
 Delegate the processing of a request to another resource and the client should not
know it.
●
 Transfer request attributes and parameters to another resource which is able to
manage them.

Use include if you want to:

●
Include in a response of a servlet, the output generated by another.
●
Modify the response generated by another servlet.

Use redirect if you want to:

●
Redirect the client to another URL.
●
NOT transfer any request attribute to the new resource.

![Figura 1 dalla slide 24](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webappTutorship-2025-26-JSPs/assets/slide-024-fig-01.jpg)

## Slide 25 - Example from SIGIR25 WebApp

Example from SIGIR25 WebApp

![Figura 1 dalla slide 25](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webappTutorship-2025-26-JSPs/assets/slide-025-fig-01.jpg)

## Slide 26 - Idea of a Conference Program

Idea of a Conference Program

The Paper of the

Author(s)

Happens

Slot

![Figura 1 dalla slide 26](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webappTutorship-2025-26-JSPs/assets/slide-026-fig-01.jpg)

![Figura 2 dalla slide 26](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webappTutorship-2025-26-JSPs/assets/slide-026-fig-02.jpg)

## Slide 27 - Idea of a Conference Program

Idea of a Conference Program

The Paper of the

Author(s)

Happens

Slot

Belongs
Situated

Location (e.g., Room)
Track (e.g., full)

![Figura 1 dalla slide 27](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webappTutorship-2025-26-JSPs/assets/slide-027-fig-01.jpg)

## Slide 28 - ER Schema

ER Schema

![Figura 1 dalla slide 28](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webappTutorship-2025-26-JSPs/assets/slide-028-fig-01.jpg)

## Slide 29 - ER Schema

ER Schema

![Figura 1 dalla slide 29](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webappTutorship-2025-26-JSPs/assets/slide-029-fig-01.jpg)

## Slide 30 - What Do We Need to do?

What Do We Need to do?

●
List all the Slots

●
List all the Locations

●
List all the Tracks

●
Allow the user to select Slot, Track and Location to link and
set the “restricted” ﬂag

●
Insert the provided data in the DB

![Figura 1 dalla slide 30](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webappTutorship-2025-26-JSPs/assets/slide-030-fig-01.jpg)

## Slide 31 - Expected Outcome

Expected Outcome

![Figura 1 dalla slide 31](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webappTutorship-2025-26-JSPs/assets/slide-031-fig-01.jpg)

![Figura 2 dalla slide 31](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webappTutorship-2025-26-JSPs/assets/slide-031-fig-02.jpg)

## Slide 32 - Resources

Resources

We will need 3 resources

●
Track
●
Slot
●
Location
●
Occurrence → class that keeps track of the link between
Track, Slot and Location

![Figura 1 dalla slide 32](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webappTutorship-2025-26-JSPs/assets/slide-032-fig-01.jpg)

## Slide 33 - Which DAOs?

Which DAOs?

●
List all the Slots

●
List all the Locations

●
List all the Tracks

●
Allow the user to select Slot, Track and Location to link and
set the “restricted” ﬂag

●
Insert the provided data in the DB

![Figura 1 dalla slide 33](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webappTutorship-2025-26-JSPs/assets/slide-033-fig-01.jpg)

## Slide 34 - List all the Slots

List all the Slots

![Figura 1 dalla slide 34](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webappTutorship-2025-26-JSPs/assets/slide-034-fig-01.jpg)

## Slide 35 - List all the Locations

List all the Locations

![Figura 1 dalla slide 35](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webappTutorship-2025-26-JSPs/assets/slide-035-fig-01.jpg)

## Slide 36 - List all the Tracks

List all the Tracks

![Figura 1 dalla slide 36](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webappTutorship-2025-26-JSPs/assets/slide-036-fig-01.jpg)

## Slide 37 - Insert data into DB

Insert data into DB

![Figura 1 dalla slide 37](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webappTutorship-2025-26-JSPs/assets/slide-037-fig-01.jpg)

![Figura 2 dalla slide 37](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webappTutorship-2025-26-JSPs/assets/slide-037-fig-02.jpg)

## Slide 38 - Showing Slots, Location, Tracks (

Showing Slots, Location, Tracks (

1.
We retrieve all the data
from the DB

## Slide 39 - Showing Slots, Location, Tracks (

Showing Slots, Location, Tracks (

1.
We retrieve all the data
from the DB

## Slide 40 - Showing Slots, Location, Tracks (Servlet & JSP)

Showing Slots, Location, Tracks (Servlet & JSP)

2.
Forward to jsp

## Slide 41 - redirect function

redirect function

Note that in the
forwarding request
we pass:
List of slots, locations
and tracks, and the
message.

![Figura 1 dalla slide 41](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webappTutorship-2025-26-JSPs/assets/slide-041-fig-01.jpg)

## Slide 42 - show-mesage.jsp

show-mesage.jsp

Two messages
means two styles

![Figura 1 dalla slide 42](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webappTutorship-2025-26-JSPs/assets/slide-042-fig-01.jpg)

## Slide 43 - slot-for-location.jsp

slot-for-location.jsp

Some imports that might be
useful

![Figura 1 dalla slide 43](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webappTutorship-2025-26-JSPs/assets/slide-043-fig-01.jpg)

## Slide 44 - slot-for-location.jsp: Listing Slots

slot-for-location.jsp: Listing Slots

Check if the lists
are available
Iterate through
Slots

“show” the slot
data

![Figura 1 dalla slide 44](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webappTutorship-2025-26-JSPs/assets/slide-044-fig-01.jpg)

## Slide 45 - slot-for-location.jsp: Adding Slots

slot-for-location.jsp: Adding Slots

We create the
form

Hint: Using c:url
“automatically”
resolves
the paths
(webapp name
is omitted)

![Figura 1 dalla slide 45](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webappTutorship-2025-26-JSPs/assets/slide-045-fig-01.jpg)

## Slide 46 - slot-for-location.jsp: Adding Slots

slot-for-location.jsp: Adding Slots

Drop-down
menu for Slots,
Track &
Locations

![Figura 1 dalla slide 46](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webappTutorship-2025-26-JSPs/assets/slide-046-fig-01.jpg)

## Slide 47 - slot-for-location.jsp: Adding Slots

slot-for-location.jsp: Adding Slots

Drop-down
menu for Slots,
Track &
Locations

Radio button for
selecting the
kind of access

![Figura 1 dalla slide 47](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webappTutorship-2025-26-JSPs/assets/slide-047-fig-01.jpg)

## Slide 48 - Adding a new occurrence (LocationforSlotServlet.java)

Adding a new occurrence (LocationforSlotServlet.java)

We need to add a new
“link” between the
selected Slot, Location
and Track → Add data in
the “Occurence” table

We get the parameters
from the request and we
check them

![Figura 1 dalla slide 48](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webappTutorship-2025-26-JSPs/assets/slide-048-fig-01.jpg)

![Figura 2 dalla slide 48](slide-048-fig-02.jpg)

## Slide 49 - Adding a new occurrence (LocationforSlotServlet.java)

Adding a new occurrence (LocationforSlotServlet.java)

2. Add the Occurrence
1.
Check if already
present

![Figura 1 dalla slide 49](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webappTutorship-2025-26-JSPs/assets/slide-049-fig-01.jpg)

![Figura 2 dalla slide 49](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webappTutorship-2025-26-JSPs/assets/slide-049-fig-02.jpg)
