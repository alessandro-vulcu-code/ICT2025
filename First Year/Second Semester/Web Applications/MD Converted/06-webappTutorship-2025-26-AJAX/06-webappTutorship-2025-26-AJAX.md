# 06-webappTutorship-2025-26-AJAX

_Source: `06-webappTutorship-2025-26-AJAX.pdf`_

## Slide 1 - Tutoring 06

Tutoring 06
AJAX & Frontend Debugging

Francesco L. De Faveri

Web Applications Tutoring

Academic Year: 2025-2026

![Figura 1 dalla slide 1](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-webappTutorship-2025-26-AJAX/assets/slide-001-fig-01.jpg)

## Slide 2 - Outline

Outline

●
General Information

●
AJAX + Hands On

●
Debugging the Frontend: Live Console

![Figura 1 dalla slide 2](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-webappTutorship-2025-26-AJAX/assets/slide-002-fig-01.jpg)

## Slide 3 - General Information

General Information

![Figura 1 dalla slide 3](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-webappTutorship-2025-26-AJAX/assets/slide-003-fig-01.jpg)

## Slide 4 - General Information

General Information

Friday June 5th, 2026 → Homework 2 Deadline
For the June the 5th your project must be completed. Your
group must present code, oral presentation, and demo of the
web application - more info will be given.

Remember: you all need to equally contribute in all the parts of
the homework (code + presentation)

![Figura 1 dalla slide 4](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-webappTutorship-2025-26-AJAX/assets/slide-004-fig-01.jpg)

## Slide 5 - Tips for the second part

Tips for the second part

Final WebApp presentation (Slides + Demo) - June 2026
Be aware that your presentation as a ﬁxed time (10-15 minutes)

Tip #1

Try your presentation with all the members of your group: everyone is needed to
take part in the presentation. When the time is gone, your presentation is ﬁnished.

Tip #2

Consider the presentation to be organised presenting: Problem you are trying to
solve, Backend & Frontend implementation, and live demo on how to use your
web application.

(Expect some questions during and at the end of the live demo)

![Figura 1 dalla slide 5](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-webappTutorship-2025-26-AJAX/assets/slide-005-fig-01.jpg)

## Slide 6 - Useful resources

Useful resources

Useful resources for frontend development:

-
Codesandbox: https://codesandbox.io/ (Online)
-
VS Code Live Server: Live Server Extension (Local)
-
Built in tool of IntelliJ (Local)

-
Developer Mozilla: https://developer.mozilla.org/en-US/

-
Coolors: https://coolors.co/

-
Fontawesome: https://fontawesome.com/

![Figura 1 dalla slide 6](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-webappTutorship-2025-26-AJAX/assets/slide-006-fig-01.jpg)

## Slide 7 - AJAX

AJAX

![Figura 1 dalla slide 7](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-webappTutorship-2025-26-AJAX/assets/slide-007-fig-01.jpg)

## Slide 8 - Before AJAX

Before AJAX

At each user interaction:

➢
Call of a servlet that process and retrieve data from the DB
➢
Set the resource and call a jsp/Redirect the user to a new web page
➢
Browser renders the new resource

What is happening?

●
Reloading every time an entire Web Page

This means that the requests are performed at each reload and the
entire page is generated.

![Figura 1 dalla slide 8](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-webappTutorship-2025-26-AJAX/assets/slide-008-fig-01.jpg)

## Slide 9 - Before AJAX

Before AJAX

But:

●
If the state of the Web App does not change, perform the same
requests several times is not useful.

●
Some requests can be time and resource demanding, e.g., inner
joins in data layer or time demanding on js functions.

●
Unexpected behaviours can confuse the user.

![Figura 1 dalla slide 9](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-webappTutorship-2025-26-AJAX/assets/slide-009-fig-01.jpg)

## Slide 10 - AJAX

AJAX

●
AJAX stands for Asynchronous JavaScript And XML

●
AJAX is not a programming language

●
AJAX is a technique for accessing web servers from a web page (HTTP
requests between client and server)

Asynchronous:

Client and server communicate behind the scenes and the user has not to
wait the entire page to be reloaded and keep interact.

![Figura 1 dalla slide 10](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-webappTutorship-2025-26-AJAX/assets/slide-010-fig-01.jpg)

## Slide 11 - AJAX - Developer’s dream

AJAX - Developer’s dream

●
Update a web page w/o reloading the page

●
Request/Receive data from a server - after the page has loaded

●
Send data to a server - in the background

●
Fast and efﬁcient user interaction

●
Backend agnostic

![Figura 1 dalla slide 11](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-webappTutorship-2025-26-AJAX/assets/slide-011-fig-01.jpg)

## Slide 12 - Keep this concepts in mind (but separated)…

Keep this concepts in mind (but separated)…

Architectural

Application Layer

Way of managing

Paradigm

Protocol

HTTP calls

(GET, POST, PUT,

(Stateless protocol)

(Asynchronous calls)

DELETE…)

![Figura 1 dalla slide 12](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-webappTutorship-2025-26-AJAX/assets/slide-012-fig-01.jpg)

![Figura 2 dalla slide 12](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-webappTutorship-2025-26-AJAX/assets/slide-012-fig-02.jpg)

![Figura 3 dalla slide 12](slide-012-fig-03.jpg)

![Figura 4 dalla slide 12](slide-012-fig-04.jpg)

## Slide 13 - What you will need for AJAX

What you will need for AJAX

When you implement AJAX in your projects, you have to
exchange json (or xml or html) representations of your
resources which are used to update speciﬁc part of the web
page (instead of the entire web page).

![Figura 1 dalla slide 13](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-webappTutorship-2025-26-AJAX/assets/slide-013-fig-01.jpg)

## Slide 14 - Technically AJAX works like this

Technically AJAX works like this

1. Event

Browser
Server
XMLHttpRequest

![Figura 1 dalla slide 14](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-webappTutorship-2025-26-AJAX/assets/slide-014-fig-01.jpg)

![Figura 2 dalla slide 14](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-webappTutorship-2025-26-AJAX/assets/slide-014-fig-02.jpg)

![Figura 3 dalla slide 14](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-webappTutorship-2025-26-AJAX/assets/slide-014-fig-03.jpg)

## Slide 15 - Technically AJAX works like this

Technically AJAX works like this

1. Event

Browser
Server
XMLHttpRequest

2. Update

JavaScript - DOM

![Figura 1 dalla slide 15](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-webappTutorship-2025-26-AJAX/assets/slide-015-fig-01.jpg)

## Slide 16 - Some methods

Some methods

![Figura 1 dalla slide 16](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-webappTutorship-2025-26-AJAX/assets/slide-016-fig-01.jpg)

## Slide 17 - More on XHR

More on XHR

Value
State
Description

0
Unsent
Client has been created

1
Opened
open() is called

send() is called - .status and .headers available

2
Headers
Received

3
Loading
Downloading; responseText holds partial data

4
Done
Operation complete

## Slide 18 - More on XHR

More on XHR

![Figura 1 dalla slide 18](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-webappTutorship-2025-26-AJAX/assets/slide-018-fig-01.jpg)

![Figura 2 dalla slide 18](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-webappTutorship-2025-26-AJAX/assets/slide-018-fig-02.jpg)

## Slide 19 - SIGIR25 WebApp (ajax-demo.html)

SIGIR25 WebApp (ajax-demo.html)

Container with
buttons to load a

prediﬁned paper

## Slide 20 - SIGIR25 WebApp (ajax-demo.html)

SIGIR25 WebApp (ajax-demo.html)

Input box to get
the name of the

ﬁle .json

## Slide 21 - SIGIR25 WebApp (ajax-demo.html)

SIGIR25 WebApp (ajax-demo.html)

Input box to get
the name of the

ﬁle .json

When the
button is clicked,

a js function is

called.

## Slide 22 - SIGIR25 WebApp (ajax-demo.html)

SIGIR25 WebApp (ajax-demo.html)

The function
showPaper() is

in script.js
The function
showPaperJSON()

is in script2.js

![Figura 1 dalla slide 22](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-webappTutorship-2025-26-AJAX/assets/slide-022-fig-01.jpg)

## Slide 23 - SIGIR25 WebApp (script.js)

SIGIR25 WebApp (script.js)

Logging some

information

Instantiating

variables
(Note that
paper.html is

ﬁxed in this

demo)

![Figura 1 dalla slide 23](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-webappTutorship-2025-26-AJAX/assets/slide-023-fig-01.jpg)

## Slide 24 - SIGIR25 WebApp (script.js)

SIGIR25 WebApp (script.js)

If everything is
ok, than get the

text

Else raise an
alert and log the

problem of not

ﬁnd

![Figura 1 dalla slide 24](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-webappTutorship-2025-26-AJAX/assets/slide-024-fig-01.jpg)

## Slide 25 - SIGIR25 WebApp (script.js)

SIGIR25 WebApp (script.js)

GET the ﬁle
.html and send

the data
(eventually)

collected

![Figura 1 dalla slide 25](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-webappTutorship-2025-26-AJAX/assets/slide-025-fig-01.jpg)

## Slide 26 - Results

Results

ajax-demo.html

Rendered
paper.html

![Figura 1 dalla slide 26](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-webappTutorship-2025-26-AJAX/assets/slide-026-fig-01.jpg)

## Slide 27 - Loading a JSON ﬁle (script2.js)

Loading a JSON ﬁle (script2.js)

Get input title

name

![Figura 1 dalla slide 27](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-webappTutorship-2025-26-AJAX/assets/slide-027-fig-01.jpg)

## Slide 28 - Loading a JSON ﬁle (script2.js)

Loading a JSON ﬁle (script2.js)

Sanity checks

![Figura 1 dalla slide 28](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-webappTutorship-2025-26-AJAX/assets/slide-028-fig-01.jpg)

## Slide 29 - Loading a JSON ﬁle (script2.js)

Loading a JSON ﬁle (script2.js)

Parse data and

render
everything

AJAX XHR

methods

![Figura 1 dalla slide 29](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-webappTutorship-2025-26-AJAX/assets/slide-029-fig-01.jpg)

## Slide 30 - Loading a JSON ﬁle (script2.js)

Loading a JSON ﬁle (script2.js)

Helper function

to render
everything

correctly

![Figura 1 dalla slide 30](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-webappTutorship-2025-26-AJAX/assets/slide-030-fig-01.jpg)

![Figura 2 dalla slide 30](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-webappTutorship-2025-26-AJAX/assets/slide-030-fig-02.jpg)

## Slide 31 - Results

Results

ajax-demo.html

Rendered data

from
paper-2.json

![Figura 1 dalla slide 31](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-webappTutorship-2025-26-AJAX/assets/slide-031-fig-01.jpg)

## Slide 32 - Debugging Console

Debugging Console

![Figura 1 dalla slide 32](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-webappTutorship-2025-26-AJAX/assets/slide-032-fig-01.jpg)

## Slide 33 - How can I debug a Web Application?

How can I debug a Web Application?

Frontend development:

●
When you modify a small part of a web app – i.e., html or css – building the
war ﬁle and entire lifecycle of the webapp can be a waste of time;

●
To develop a speciﬁc frontend component and check the correctness, try to
use codesandbox or live server or the default version of your IDE to build
prototypes before add them to production.

●
Developer tools: change colors and add elements (html+css) & test js code

![Figura 1 dalla slide 33](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-webappTutorship-2025-26-AJAX/assets/slide-033-fig-01.jpg)

## Slide 34 - General Tools

General Tools

●
Elements

●
Console

●
Sources

●
Network

●
Security and Privacy
●
…

![Figura 1 dalla slide 34](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-webappTutorship-2025-26-AJAX/assets/slide-034-fig-01.jpg)

## Slide 35 - Elements

Elements

The Elements tool is used for:

●
Access the html and css code
of the Web Page.

●
Verify how the Web Page is
rendered.

●
Inspect how your code
behaves LIVE!

![Figura 1 dalla slide 35](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-webappTutorship-2025-26-AJAX/assets/slide-035-fig-01.jpg)

## Slide 36 - Switch between device views

Switch between device views

## Slide 37 - More on Elements

More on Elements

●
See Responsive Rendering.

●
CSS fast prototyping.

●
Manipulate the DOM.

Remark:
If you modify something,
remember to save!

![Figura 1 dalla slide 37](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-webappTutorship-2025-26-AJAX/assets/slide-037-fig-01.jpg)

## Slide 38 - Console

Console

The Console is used log information
used in the Web Page.

●
Log information about the
behaviour of the Web Page.

●
Prevent unwanted behaviours by
inspecting how the js functions
works.

![Figura 1 dalla slide 38](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-webappTutorship-2025-26-AJAX/assets/slide-038-fig-01.jpg)

## Slide 39 - Sources

Sources

The sources can help you to:

●
Step in your code.
●
Used for debugging of your js code.
●
Deﬁne speciﬁc breakpoints.

![Figura 1 dalla slide 39](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-webappTutorship-2025-26-AJAX/assets/slide-039-fig-01.jpg)

## Slide 40 - Network

Network

The Network tool is used for:

●
Verify the efﬁciency of loading
the resources of the Web Page.

●
You can ﬁlter by the kind of
resource and found loading
time values and size.

●
Find size of loaded resources.

![Figura 1 dalla slide 40](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-webappTutorship-2025-26-AJAX/assets/slide-040-fig-01.jpg)

![Figura 2 dalla slide 40](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-webappTutorship-2025-26-AJAX/assets/slide-040-fig-02.jpg)

## Slide 41 - Security & Privacy

Security & Privacy

Finally, the Security & Privacy Tool
serves as:

●
Analyse security Certiﬁcates.

●
See how resources are loaded.

●
Verify connection protocols.

![Figura 1 dalla slide 41](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-webappTutorship-2025-26-AJAX/assets/slide-041-fig-01.jpg)

## Slide 42 - Wrap up

Wrap up

![Figura 1 dalla slide 42](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-webappTutorship-2025-26-AJAX/assets/slide-042-fig-01.jpg)

## Slide 43 - Wrap Up

Wrap Up

●
AJAX: How to improve the efﬁciency of your Web App and perform
Asynchronous calls.

●
Live example on the Web App for SIGIR 25 (call and display single
pages html and json ﬁles).

●
What is Live Console and how to use it.

●
Live examples of using Live Console.

![Figura 1 dalla slide 43](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-webappTutorship-2025-26-AJAX/assets/slide-043-fig-01.jpg)

## Slide 44 - Acknowledgments

Acknowledgments

-
Template for Live Console Hands On from:
https://www.free-css.com/free-css-templates

-
Doc:
https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest_API

-
Slides Main Course (Prof. Nicola Ferro)

-
Slides Web Security (Francesco L. De Faveri)

-
Online Open Source Resources!

![Figura 1 dalla slide 44](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/06-webappTutorship-2025-26-AJAX/assets/slide-044-fig-01.jpg)
