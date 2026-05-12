# 12-webapp-2025-26-WebSecurity

_Source: `12-webapp-2025-26-WebSecurity.pdf`_

## Slide 1 - Web Security

Web Security

Francesco L. De Faveri
Department of Information Engineering

Web App - A.Y. 2025/26

Padova -  April, 28th, 2026

![Figura 1 dalla slide 1](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/12-webapp-2025-26-WebSecurity/assets/slide-001-fig-01.jpg)

![Figura 2 dalla slide 1](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/12-webapp-2025-26-WebSecurity/assets/slide-001-fig-02.jpg)

![Figura 3 dalla slide 1](slide-001-fig-03.jpg)

## Slide 2 - ~$ whoami

~$ whoami

Contact:
     francescoluigi.defaveri@phd.unipd.it

2018 - 2021

2021 - 2023

2023 - 20…

Bachelor Degree in
Mathematics
@ University of Trieste

Master Degree in
Cybersecurity
@ University of Padova

PhD in Information Engineering
@ University of Padova
Visiting PhD
@ Max Planck Institute for Security and Privacy

Thesis:
“A possibilistic Approach to
Fuzzy Arithmetic.”

Thesis:
“A Feasibility Study and Privacy
Analysis of a Data Management
Infrastructure in the Oncology
Research Domain.”

Research Areas:
Privacy Preserving Information Retrieval
Anonymization & Differential Privacy for structured and unstructured
data in Oncological Domains
Evaluation in Information Retrieval, Large Language Models

![Figura 1 dalla slide 2](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/12-webapp-2025-26-WebSecurity/assets/slide-002-fig-01.jpg)

## Slide 3 - Privacy Preserving Information Access

Privacy Preserving Information Access

Privacy Preserving Information Access Course @ UniPD a.y. 2026/2027!

Anonymization
Differential

Privacy

Privacy in
Information Retrieval

Lecturer: Prof. Guglielmo Faggioli
    guglielmo.faggioli@unipd.it

![Figura 1 dalla slide 3](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/12-webapp-2025-26-WebSecurity/assets/slide-003-fig-01.jpg)

![Figura 2 dalla slide 3](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/12-webapp-2025-26-WebSecurity/assets/slide-003-fig-02.jpg)

## Slide 4 - Overview

Overview

●
Introduction to Cybersecurity
●
Web Security

Cybersecurity & Web
01

SQL Injection
02

●
What is SQL Injection?
●
Hands-On
●
How to protect from SQL Injection

Cross Site Scripting - XSS
03

●
What is XSS?
●
Hands-On
●
How to protect from XSS

Cross Site Request Forgery -
CSRF
04

●
What is CSRF?
●
Hands-On
●
How to protect from CSRF

![Figura 1 dalla slide 4](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/12-webapp-2025-26-WebSecurity/assets/slide-004-fig-01.jpg)

## Slide 5 - Material for the Hands-On labs

Material for the Hands-On labs

Git repository (docker containers + readme): WA-WebSecurity repo

VM used for the lab: VM Drive

![Figura 1 dalla slide 5](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/12-webapp-2025-26-WebSecurity/assets/slide-005-fig-01.jpg)

![Figura 2 dalla slide 5](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/12-webapp-2025-26-WebSecurity/assets/slide-005-fig-02.jpg)

![Figura 3 dalla slide 5](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/12-webapp-2025-26-WebSecurity/assets/slide-005-fig-03.jpg)

![Figura 4 dalla slide 5](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/12-webapp-2025-26-WebSecurity/assets/slide-005-fig-04.jpg)

## Slide 6 - Material for the Hands-On labs

Material for the Hands-On labs

~$ sudo nano /etc/hosts

Modify the hosts by following the instruction in Repo README.md

Exec NotePad as Administrator -> Open File -> Look at C:\Windows\System32\drivers\etc\hosts

Modify the hosts by following the instruction in Repo README.md

![Figura 1 dalla slide 6](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/12-webapp-2025-26-WebSecurity/assets/slide-006-fig-01.jpg)

## Slide 7 - Cybersecurity & Web

Cybersecurity & Web

## Slide 8 - Slide 8

![Figura 1 dalla slide 8](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/12-webapp-2025-26-WebSecurity/assets/slide-008-fig-01.jpg)

## Slide 9 - Slide 9

![Figura 1 dalla slide 9](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/12-webapp-2025-26-WebSecurity/assets/slide-009-fig-01.jpg)

![Figura 2 dalla slide 9](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/12-webapp-2025-26-WebSecurity/assets/slide-009-fig-02.jpg)

## Slide 10 - Slide 10

![Figura 1 dalla slide 10](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/12-webapp-2025-26-WebSecurity/assets/slide-010-fig-01.jpg)

![Figura 2 dalla slide 10](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/12-webapp-2025-26-WebSecurity/assets/slide-010-fig-02.jpg)

## Slide 11 - Cybersecurity objectives: CIA

Cybersecurity objectives: CIA

![Figura 1 dalla slide 11](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/12-webapp-2025-26-WebSecurity/assets/slide-011-fig-01.jpg)

## Slide 12 - Cybersecurity objectives: CIA

Cybersecurity objectives: CIA

Conﬁdentiality

“the information is available only
for the intended user”.

Cybersecurity

![Figura 1 dalla slide 12](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/12-webapp-2025-26-WebSecurity/assets/slide-012-fig-01.jpg)

## Slide 13 - Cybersecurity objectives: CIA

Cybersecurity objectives: CIA

Conﬁdentiality

“the information is available only
for the intended user”.

Cybersecurity

Integrity

“the information is not changed,
it is received exactly as sent”.

![Figura 1 dalla slide 13](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/12-webapp-2025-26-WebSecurity/assets/slide-013-fig-01.jpg)

## Slide 14 - Cybersecurity objectives: CIA

Cybersecurity objectives: CIA

Conﬁdentiality

“the information is available only
for the intended user”.

Availability

Cybersecurity

“the information is always
available any time the user

needs”.

Integrity

“the information is not changed,
it is received exactly as sent”.

![Figura 1 dalla slide 14](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/12-webapp-2025-26-WebSecurity/assets/slide-014-fig-01.jpg)

## Slide 15 - Web Security

Web Security

Web security refers to the exploitation and defense measures over websites and web
applications.

An attacker needs to ﬁrst understand which are the components of the application and how
it expects to interact with the user.

![Figura 1 dalla slide 15](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/12-webapp-2025-26-WebSecurity/assets/slide-015-fig-01.jpg)

![Figura 2 dalla slide 15](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/12-webapp-2025-26-WebSecurity/assets/slide-015-fig-02.jpg)

## Slide 16 - Motives behind cyber attacks

Motives behind cyber attacks

Espionage
Extortion
Theft
Fun

![Figura 1 dalla slide 16](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/12-webapp-2025-26-WebSecurity/assets/slide-016-fig-01.jpg)

![Figura 2 dalla slide 16](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/12-webapp-2025-26-WebSecurity/assets/slide-016-fig-02.jpg)

![Figura 3 dalla slide 16](slide-016-fig-03.jpg)

![Figura 4 dalla slide 16](slide-016-fig-04.jpg)

## Slide 17 - OWASP Top Ten

OWASP Top Ten

Open Worldwide Application Security Project

The OWASP Top 10 is a standard awareness
document for developers and web application
security.

●
ﬁrst step in changing the software
development towards a more secure
production.

![Figura 1 dalla slide 17](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/12-webapp-2025-26-WebSecurity/assets/slide-017-fig-01.jpg)

## Slide 18 - Possible attacks in Web Security

Possible attacks in Web Security

●SQL Injection

●Cross Site Scripting - XSS

●Cross Site Request Forgery - CSRF

●More @ OWASP TOP 10

![Figura 1 dalla slide 18](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/12-webapp-2025-26-WebSecurity/assets/slide-018-fig-01.jpg)

## Slide 19 - Scenario

Scenario

![Figura 1 dalla slide 19](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/12-webapp-2025-26-WebSecurity/assets/slide-019-fig-01.jpg)

## Slide 20 - SQL Injection

SQL Injection

## Slide 21 - What is SQL Injection?

What is SQL Injection?

https://xkcd.com/327/

SQL Injection is kind of Code Injection:

“It is an attack that exploits vulnerabilities in the interface of a Web Application.”

![Figura 1 dalla slide 21](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/12-webapp-2025-26-WebSecurity/assets/slide-021-fig-01.jpg)

## Slide 22 - SQL Injection

SQL Injection

![Figura 1 dalla slide 22](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/12-webapp-2025-26-WebSecurity/assets/slide-022-fig-01.jpg)

## Slide 23 - SQL Injection

SQL Injection

![Figura 1 dalla slide 23](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/12-webapp-2025-26-WebSecurity/assets/slide-023-fig-01.jpg)

## Slide 24 - SQL Basics for Injection

SQL Basics for Injection

Special Characters SQL:

SQL operation:

●
; Query terminator
●
-- and # Single line comment
●
/* */ Multi line comment
●
‘ Character string indicator
●
…

●
SELECT Record selection
●
DROP Delete (Table)
●
INSERT INTO Add record
●
UPDATE Updates record
●
…

![Figura 1 dalla slide 24](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/12-webapp-2025-26-WebSecurity/assets/slide-024-fig-01.jpg)

![Figura 2 dalla slide 24](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/12-webapp-2025-26-WebSecurity/assets/slide-024-fig-02.jpg)

## Slide 25 - A small example of SQL Injection

A small example of SQL Injection

New connection

![Figura 1 dalla slide 25](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/12-webapp-2025-26-WebSecurity/assets/slide-025-fig-01.jpg)

## Slide 26 - A small example of SQL Injection

A small example of SQL Injection

Mix user input & SQL Statement

![Figura 1 dalla slide 26](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/12-webapp-2025-26-WebSecurity/assets/slide-026-fig-01.jpg)

## Slide 27 - A small example of SQL Injection

A small example of SQL Injection

Query Execution

![Figura 1 dalla slide 27](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/12-webapp-2025-26-WebSecurity/assets/slide-027-fig-01.jpg)

## Slide 28 - A small example of SQL Injection

A small example of SQL Injection

![Figura 1 dalla slide 28](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/12-webapp-2025-26-WebSecurity/assets/slide-028-fig-01.jpg)

## Slide 29 - SQL - Injection

SQL - Injection

LAB

![Figura 1 dalla slide 29](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/12-webapp-2025-26-WebSecurity/assets/slide-029-fig-01.jpg)

## Slide 30 - How to protect?

How to protect?

●
Filter out - Encode any special characters that can be dangerous for SQL queries
●
Use prepared statement:

Code & data
separated

Binding code and input

![Figura 1 dalla slide 30](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/12-webapp-2025-26-WebSecurity/assets/slide-030-fig-01.jpg)

## Slide 31 - Cross Site Scripting - XSS

Cross Site Scripting - XSS

## Slide 32 - What is XSS?

What is XSS?

It is a type of vulnerability commonly found in web applications.
This vulnerability makes it possible for attackers to inject
malicious code (e.g. JavaScript programs) into victim’s web
browser.

●
Stored -> Script stored and executed when retrieved by the
user.
●
Reﬂected -> Malicious url written by the user, not stored in the
db but reﬂected by the server.
●
DOM Based -> Takes advantages on the DOM vulnerabilities.

## Slide 33 - Stored XSS - the html/js version of SQL Injection

Stored XSS - the html/js version of SQL Injection

![Figura 1 dalla slide 33](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/12-webapp-2025-26-WebSecurity/assets/slide-033-fig-01.jpg)

## Slide 34 - Stored XSS - the html/js version of SQL Injection

Stored XSS - the html/js version of SQL Injection

![Figura 1 dalla slide 34](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/12-webapp-2025-26-WebSecurity/assets/slide-034-fig-01.jpg)

## Slide 35 - Stored XSS - the html/js version of SQL Injection

Stored XSS - the html/js version of SQL Injection

The js code is executed when

encountered in the DOM

creation!

![Figura 1 dalla slide 35](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/12-webapp-2025-26-WebSecurity/assets/slide-035-fig-01.jpg)

## Slide 36 - A small example of XSS

A small example of XSS

![Figura 1 dalla slide 36](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/12-webapp-2025-26-WebSecurity/assets/slide-036-fig-01.jpg)

## Slide 37 - A small example of XSS

A small example of XSS

![Figura 1 dalla slide 37](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/12-webapp-2025-26-WebSecurity/assets/slide-037-fig-01.jpg)

## Slide 38 - XSS Attack

XSS Attack

LAB

![Figura 1 dalla slide 38](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/12-webapp-2025-26-WebSecurity/assets/slide-038-fig-01.jpg)

## Slide 39 - How to protect?

How to protect?

●
Modern Frameworks have less XSS vulnerabilities -> Build in Security Measures

●
Output encoding is recommended: Display as the user types

●
HTML Sanitization: OWASP suggests DOMPurify

However, these measures reduces the probability of a successful XSS, but no measure is 100% safe.

## Slide 40 - Cross Site Request Forgery - CSRF

Cross Site Request Forgery - CSRF

## Slide 41 - CSRF Schema 1

CSRF Schema 1

●
When a page from a website sends an
HTTP request back to the website, it is
called same-site request

●
If a request is sent to a different
website,it is called cross-site request
because where the page comes from and
where the request goes are different

Example:
A web page (not Facebook) can include a
Facebook link, so when users click on the link,
HTTP request is sent to Facebook.

![Figura 1 dalla slide 41](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/12-webapp-2025-26-WebSecurity/assets/slide-041-fig-01.jpg)

## Slide 42 - CSRF Schema 2

CSRF Schema 2

![Figura 1 dalla slide 42](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/12-webapp-2025-26-WebSecurity/assets/slide-042-fig-01.jpg)

## Slide 43 - A small example of CSRF

A small example of CSRF

Function
embedded in
the page that

foges a post

request

![Figura 1 dalla slide 43](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/12-webapp-2025-26-WebSecurity/assets/slide-043-fig-01.jpg)

## Slide 44 - A small example of CSRF

A small example of CSRF

Forge &
Submit when
page is loaded

![Figura 1 dalla slide 44](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/12-webapp-2025-26-WebSecurity/assets/slide-044-fig-01.jpg)

## Slide 45 - CSRF Attack

CSRF Attack

LAB

![Figura 1 dalla slide 45](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/12-webapp-2025-26-WebSecurity/assets/slide-045-fig-01.jpg)

## Slide 46 - How to protect?

How to protect?

●
A special type of cookie in browsers, like Chrome and Opera, provide a special attribute to
cookies called SameSite: This attribute is set by the servers and it tells the browsers whether
a cookie should be attached to a cross-site request or not!

●
Cookies with this attribute are always sent along with same-site requests, but whether they are
sent along with cross-site depends on the value of this attribute.

●
Values:

○
Strict (Not sent along with cross-site requests)
○
Lax (Sent along with cross-site requests)

## Slide 47 - Web Security

Web Security

Thanks for your attention!

Francesco L. De Faveri

Department of Information Engineering

Padova -  April, 28th, 2026

![Figura 1 dalla slide 47](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/12-webapp-2025-26-WebSecurity/assets/slide-047-fig-01.jpg)

![Figura 2 dalla slide 47](slide-047-fig-02.jpg)

![Figura 3 dalla slide 47](slide-047-fig-03.jpg)
