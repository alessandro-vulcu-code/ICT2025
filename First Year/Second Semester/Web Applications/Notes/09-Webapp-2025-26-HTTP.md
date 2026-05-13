# 09 — HTTP (and Surroundings)

_Source: `09-Webapp-2025-26-HTTP.pdf` — Web Applications, Master Degree, A.Y. 2025/2026, Prof. Nicola Ferro_

---

## Table of Contents

- [[#Basic Web Technology|Basic Web Technology]]
- [[#URL and URI|URL and URI]]
  - [[#URI URL URN IRI|URI, URL, URN, IRI]]
  - [[#URI Syntax|URI Syntax]]
  - [[#URI Examples|URI Examples]]
  - [[#Percent-Encoding|Percent-Encoding]]
- [[#Character Encoding|Character Encoding]]
  - [[#ASCII|ASCII]]
  - [[#Extended ASCII|Extended ASCII]]
  - [[#Unicode and UTF-8|Unicode and UTF-8]]
- [[#MIME|MIME]]
  - [[#MIME Headers|MIME Headers]]
  - [[#Multipart Media Type|Multipart Media Type]]
  - [[#Form Encoding — multipart form-data vs x-www-form-urlencoded|Form Encoding]]
  - [[#File Upload — Jakarta Part API|File Upload — Jakarta Part API]]
  - [[#Sending Email — Jakarta Mail|Sending Email — Jakarta Mail]]
- [[#Employee Extended — Photo Upload and Email|Employee Extended — Photo Upload and Email]]
  - [[#Create Employee JSP Form|Create Employee JSP Form]]
  - [[#Employee Resource with Photo|Employee Resource with Photo]]
  - [[#parseRequest — multipart form processing|parseRequest — multipart form processing]]
  - [[#CreateEmployeeServlet — doPost|CreateEmployeeServlet — doPost]]
  - [[#sendCreationConfirmationEmail|sendCreationConfirmationEmail]]
  - [[#LoadEmployeePhotoDAO and LoadEmployeePhotoServlet|LoadEmployeePhotoDAO and LoadEmployeePhotoServlet]]
  - [[#web.xml Multipart Configuration|web.xml Multipart Configuration]]
  - [[#MailManager|MailManager]]
  - [[#Maven Dependencies — Jakarta Mail|Maven Dependencies — Jakarta Mail]]
- [[#HTTP 1.1|HTTP/1.1]]
  - [[#Overview of HTTP|Overview of HTTP]]
  - [[#HTTP Request Methods|HTTP Request Methods]]
  - [[#Properties of HTTP Methods|Properties of HTTP Methods]]
  - [[#HTTP Response Status Codes|HTTP Response Status Codes]]
  - [[#HTTP Request Headers|HTTP Request Headers]]
  - [[#HTTP Response Headers|HTTP Response Headers]]
- [[#Authentication|Authentication]]
  - [[#HTTP Basic Authentication|HTTP Basic Authentication]]
  - [[#Session-Based Authentication with ProtectedResourceFilter|Session-Based Authentication with ProtectedResourceFilter]]
- [[#Summary Table|Summary Table]]

---

## Basic Web Technology

> [!Important] Four Pillars of the Web
> | Standard | Full Name | Role |
> |----------|-----------|------|
> | **HTML** | HyperText Markup Language | Markup language to write Web pages |
> | **HTTP** | HyperText Transfer Protocol | Application-layer protocol for client-server communication |
> | **MIME** | Multipurpose Internet Mail Extensions | Media type and encoding of exchanged information |
> | **URL** | Uniform Resource Locator | Way to identify and locate resources on the Web |

---

## URL and URI

> [!Important] URI — Uniform Resource Identifier
> A **URI** is a compact sequence of characters that identifies an abstract or physical resource.
> - **Uniform**: allows different types of resource identifiers in the same context, even when access mechanisms differ
> - **Resource**: anything that can be identified — electronic document, image, concept, human being, book
> - **Identifier**: embodies the information required to distinguish what is being identified from all other things
>
> Reference: Berners-Lee, T., Fielding, R., and Masinter, L. (2005). *URI: Generic Syntax.* RFC 3986.

### URI, URL, URN, IRI

| Term | Full Name | Description | Example |
|------|-----------|-------------|---------|
| **URI** | Uniform Resource Identifier | Generic and abstract identification mechanism | — |
| **URL** | Uniform Resource Locator | URI that also provides a means to locate the resource (primary access mechanism) | `https://www.rfc-editor.org/rfc/rfc1738.txt` |
| **URN** | Uniform Resource Name | URI using the `urn:` scheme, with properties of a permanent name | `urn:isbn:978-951-0-18435-6` |
| **IRI** | Internationalized Resource Identifier | Extension of URI syntax to allow Unicode characters | `https://en.wiktionary.org/wiki/Ῥόδος` |

### URI Syntax

```
scheme:[//[user[:password]@]host[:port]][/path][?query][#fragment]
```

| Component | Description | Example |
|-----------|-------------|---------|
| `scheme` | Refers to a spec for assigning identifiers | `http`, `https`, `ftp`, `mailto`, `file` |
| `//` | Required by some schemes, not others | — |
| `user:password@` | Optional authentication section | `user:pass@` |
| `host` | Registered domain name or IP address | `www.dei.unipd.it` |
| `:port` | Optional port number | `:8080` |
| `/path` | Data in hierarchical form, segments separated by `/` | `/rest/employee/123` |
| `?query` | Optional, separated by `?`; `attribute=value` pairs separated by `&` | `?name=Rossi&age=34` |
| `#fragment` | Optional, separated by `#`; direction to a secondary resource | `#section-2` |

### URI Examples

Different schemes identify and locate resources in different ways:

| URI | Meaning |
|-----|---------|
| `ftp://ftp.is.co.za/rfc/rfc1808.txt` | File available through FTP |
| `http://www.ietf.org/rfc/rfc2396.txt` | HTTP resource |
| `mailto:John.Doe@example.com` | Email address |
| `news:comp.infosystems.www.servers.unix` | Usenet/news resource |
| `tel:+1-816-555-1212` | Telephone number |
| `telnet://192.0.2.16:80/` | Telnet access to host and port |
| `urn:oasis:names:specification:docbook:dtd:xml:4.1.2` | Persistent URN name |

### Percent-Encoding

**Percent-Encoding** encodes an octet as `%XX` where `XX` is the two-digit hex value. Used to escape:
- Reserved characters in URIs
- Non-ASCII characters

Common encodings:

| Character | Percent-Encoded |
|-----------|----------------|
| Space | `%20` |
| `?` | `%3F` |
| `&` | `%26` |
| `#` | `%23` |
| `/` | `%2F` |
| `à` | `%E0` |

> [!Example] Real-world URL with Percent-Encoding
> ```
> https://www.google.it/search?q=universit%C3%A0+di+padova&oq=universit%C3%A0+di+padova
> ```
> `%C3%A0` = UTF-8 encoding of `à` (two bytes: `0xC3 0xA0`)

---

## Character Encoding

### ASCII

> [!Important] ASCII — American Standard Code for Information Interchange
> - Introduced in 1963 by the American Standards Association (ASA)
> - Uses **7 bits** → represents **128 characters**
> - Covers: control characters, latin letters (lower/upper), digits, punctuation, symbols
> - Standardised by ISO in 1972
> - **Problem**: no coverage of non-English characters → led to national variants and incompatibilities

### Extended ASCII

- Uses **8 bits** → represents **256 characters**
- First 128 identical to 7-bit ASCII
- Upper 128 define alternative code tables for different languages → **compatibility issues**
- Standardised as **ISO 8859** sets of recommendations (since 1987)

### Unicode and UTF-8

> [!Important] Unicode
> - Developed in 1991 by the **Unicode Consortium**
> - Goal: single character set for all alphabets and symbols
> - First versions: **16 bits** → 65,536 characters
> - Modern versions: **32 bits** → up to 4,294,967,296 characters
> - First 256 characters in common with **ISO 8859-1**
> - Standardised by ISO in 1993 as **Universal Character Set (UCS)**
> - Unicode 18.0 (2026): 172,849 characters

> [!Important] UTF-8 — Unicode Transformation Format
> UTF-8 is the most adopted Unicode encoding. Memory-efficient variable-width encoding:
> - **8 bits** for characters in common with extended ASCII (ASCII range)
> - **16 bits** for characters added by first Unicode versions
> - **32 bits** for the newest characters
>
> **Intuition:** UTF-8 is backwards-compatible with ASCII for the first 128 characters — any ASCII file is a valid UTF-8 file.

The 16-bit limit (2¹⁶ = 65,536) was exceeded starting from Unicode 3.1 (2001, 94,205 chars).

---

## MIME

> [!Important] MIME — Multipurpose Internet Mail Extensions
> - Standard supporting the **encoding of information** for e-mail and the Web
> - Defines **media types** (e.g., `text`, `image`, `audio`, `application`) and **subtypes** (e.g., `plain`, `html`, `xml`)
> - Media types registered by **IANA** (Internet Assigned Numbers Authority)
> - Additional parameters possible, e.g. `charset` for text types
> - Defines headers used by SMTP (email) and HTTP (web)
>
> Reference: Freed, N. and Borenstein, N. (1996). *MIME Part One.* RFC 2045.

### MIME Headers

| Header | Purpose | Example |
|--------|---------|---------|
| `MIME-Version` | Version of MIME used | `MIME-Version: 1.0` |
| `Content-Type` | Media type + subtype + optional params | `Content-Type: text/plain; charset=ISO-8859-1` |
| `Content-Transfer-Encoding` | How binary data is encoded for transport | `Content-Transfer-Encoding: base64` |
| `Content-Disposition` | How to display/handle the content | `Content-Disposition: attachment; filename=genome.jpeg; size=9028` |

> [!Example] Binary file as base64
> ```
> Content-Type: application/octet-stream
> Content-Transfer-Encoding: base64
>
> PGh0bWw+CiAgPGhlYWQ+...
> ```

### Multipart Media Type

> [!Important] multipart — combining multiple body parts
> **`multipart`** media type: one or more body parts combined in a single body, each preceded by a **boundary delimiter line**.
>
> | Subtype | Semantics |
> |---------|-----------|
> | `multipart/mixed` | Parts are independent, bundled in order (e.g., email + attachments) |
> | `multipart/alternative` | Parts are alternative versions of the same content (e.g., plain text + HTML) |

> [!Example] multipart/mixed structure
> ```
> MIME-Version: 1.0
> Content-Type: multipart/mixed; boundary=frontier
>
> This is a message with multiple parts in MIME format.
> --frontier
> Content-Type: text/plain
>
> This is the body of the message.
> --frontier
> Content-Type: application/octet-stream
> Content-Transfer-Encoding: base64
>
> PGh0bWw+CiAgPGhlYWQ+...
> --frontier--
> ```
> Note: closing boundary has `--` suffix: `--frontier--`

### Form Encoding — multipart/form-data vs x-www-form-urlencoded

| Encoding | MIME Type | Use Case | Body Format |
|----------|-----------|----------|-------------|
| **multipart/form-data** | `multipart/form-data` | File upload + form fields | Each field/file is a separate MIME part |
| **URL-encoded** | `application/x-www-form-urlencoded` | Form fields only (no large binary) | `name=value&name2=value2` percent-encoded |

> [!Example] multipart/form-data — HTML form + HTTP body
> ```html
> <form action="http://www.xyz.com/" enctype="multipart/form-data" method="post">
>     What is your name? <input type="text" name="submit-name"/>
>     What file are you sending? <input type="file" name="files"/>
>     <input type="submit" value="Send"/>
>     <input type="reset" value="Clear"/>
> </form>
> ```
> Resulting HTTP body:
> ```
> Content-Type: multipart/form-data; boundary=AaB03x
>
> --AaB03x
> Content-Disposition: form-data; name="submit-name"
>
> Nicola
> --AaB03x
> Content-Disposition: form-data; name="files"; filename="06823700.pdf"
> Content-Type: application/pdf
>
>   ... contents of 06823700.pdf ...
> --AaB03x--
> ```

> [!Example] application/x-www-form-urlencoded
> ```html
> <form action="http://www.xyz.com/" enctype="application/x-www-form-urlencoded" method="post">
>     What is your name? <input type="text" name="submit-name"/>
>     What is your surname? <input type="text" name="submit-surname"/>
>     <input type="submit" value="Send"/>
>     <input type="reset" value="Clear"/>
> </form>
> ```
> Resulting HTTP body:
> ```
> Content-Type: application/x-www-form-urlencoded
>
> submit-name=Nicola&submit-surname=Ferro
> ```
> The same percent-encoded `name=value` string can also be appended as the query part of a URI.

### File Upload — Jakarta Part API

> [!Important] Since Servlet 5.0 — `Part` API
> `HttpServletRequest.getParts()` returns a collection of `Part` objects. Each `Part` represents either a form field or an uploaded file.
> - Max file/request size configured in `web.xml` (or via `@MultipartConfig` annotation)
> - `Part.getInputStream()` → raw bytes of the part
> - `Part.getContentType()` → MIME media type of uploaded file
> - `Part.getName()` → field name as in the HTML form
>
> Prior to Servlet 5.0: **Apache Commons FileUpload** library was used.

### Sending Email — Jakarta Mail

> [!Important] Jakarta Mail 2.1 (since Servlet 5.0)
> - Package: `jakarta.mail`
> - Replaces Apache Commons Email
> - Key classes: `Session`, `MimeMessage`, `Transport`, `MimeMultipart`, `MimeBodyPart`
> - SMTP configuration loaded from `mailManager.properties`
>
> Maven dependencies needed:
> ```xml
> <dependency>
>     <groupId>jakarta.mail</groupId>
>     <artifactId>jakarta.mail-api</artifactId>
>     <version>2.1.1</version>
> </dependency>
> <dependency>
>     <groupId>org.eclipse.angus</groupId>
>     <artifactId>angus-mail</artifactId>
>     <version>2.0.1</version>
> </dependency>
> ```

---

## Employee Extended — Photo Upload and Email

The Employee example is extended: database now stores `email`, `photo` (raw bytes), `photoMediaType`.

![[http-create-employee-form.jpg]]

*Figure: Create Employee Form — badge, surname, age, salary, email fields + file upload for photo.*

![[http-employee-mail-project-structure.jpg]]

*Figure: Project structure (`employee-multipart-mail-jdbc`) + Maven dependencies — `jakarta.mail-api`, `angus-mail`, PostgreSQL, Tomcat JDBC.*

### Create Employee JSP Form

> [!Important] Multipart Form Requirements
> The JSP form must use `method="POST"` and `enctype="multipart/form-data"`; otherwise uploaded file bytes are not sent as multipart parts.
>
> ```jsp
> <form method="POST" enctype="multipart/form-data" action="<c:url value="/create-employee"/>">
>   <input id="badgeID" name="badge" type="text"/>
>   <input id="surnameID" name="surname" type="text"/>
>   <input id="ageID" name="age" type="text"/>
>   <input id="salaryID" name="salary" type="text"/>
>   <input id="emailID" name="email" type="text"/>
>   <input id="photoID" name="photo" type="file"
>          accept="image/png, image/jpeg, .jpg, .jpeg, .png"/>
>   <button type="submit">Submit</button>
>   <button type="reset">Reset the form</button>
> </form>
> ```
>
> The `accept` attribute restricts selectable file types on the client side, but the servlet must still validate the uploaded MIME type.

### Employee Resource with Photo

> [!Example] Employee class — extended with email and photo
> ```java
> public class Employee {
>     private final int badge;
>     private final String surname;
>     private final int age;
>     private final int salary;
>     private final String email;
>     private final byte[] photo;          // raw bytes of uploaded image
>     private final String photoMediaType; // "image/png" or "image/jpeg"
>
>     public final boolean hasPhoto() {
>         return photo != null && photo.length > 0
>             && photoMediaType != null && !photoMediaType.isBlank();
>     }
>
>     public final int getPhotoSize() {
>         return photo != null ? photo.length : Integer.MIN_VALUE;
>     }
> }
> ```
> **Key:** `hasPhoto()` avoids NPEs and checks all conditions. EL in JSP can call `${employee.hasPhoto()}` because latest EL versions support non-JavaBeans method invocations too.

### parseRequest — multipart form processing

> [!Example] parseRequest() — iterate over Parts
> ```java
> private Employee parseRequest(HttpServletRequest req)
>         throws ServletException, IOException, MimeTypeParseException {
>
>     int badge = -1; String surname = null; int age = -1; int salary = -1;
>     String email = null; byte[] photo = null; String photoMediaType = null;
>
>     for (Part p : req.getParts()) {
>         switch (p.getName()) {
>             case "badge":
>                 try (InputStream is = p.getInputStream()) {
>                     badge = Integer.parseInt(new String(is.readAllBytes(), StandardCharsets.UTF_8).trim());
>                 }
>                 break;
>             case "surname":
>                 try (InputStream is = p.getInputStream()) {
>                     surname = new String(is.readAllBytes(), StandardCharsets.UTF_8).trim();
>                 }
>                 break;
>             // age, salary, email — same pattern
>             case "photo":
>                 photoMediaType = p.getContentType();
>                 switch (photoMediaType.toLowerCase().trim()) {
>                     case "image/png": case "image/jpeg": case "image/jpg":
>                         break; // accepted
>                     default:
>                         throw new MimeTypeParseException(
>                             String.format("Unsupported MIME media type %s.", photoMediaType));
>                 }
>                 try (InputStream is = p.getInputStream()) {
>                     photo = is.readAllBytes();
>                 }
>                 break;
>         }
>     }
>     return new Employee(badge, surname, age, salary, email, photo, photoMediaType);
> }
> ```
> **Key points:**
> - `try-with-resources` ensures `InputStream` is always closed
> - `p.getContentType()` gives the MIME type of the uploaded file part
> - **Always validate MIME type server-side**, even if the HTML form restricts `accept`
> - `is.readAllBytes()` loads entire file into memory as `byte[]`

> [!Warning] MIME Type Validation
> Never trust the `Content-Type` reported by the client for uploaded files — it can be spoofed. Always validate `p.getContentType()` server-side before storing or processing the file.

### CreateEmployeeServlet — doPost

> [!Example] CreateEmployeeServlet.doPost() flow
> ```java
> public void doPost(HttpServletRequest req, HttpServletResponse res)
>         throws ServletException, IOException {
>     Employee e = null; Message m = null;
>     try {
>         e = parseRequest(req);
>         new CreateEmployeeDAO(getConnection(), e).access();
>         sendCreationConfirmationEmail(e);
>         m = new Message(String.format("Employee %d successfully created and confirmation email sent.", e.getBadge()));
>
>     } catch (NumberFormatException ex) {
>         m = new Message("Cannot create the employee. Invalid input parameters.", "E100", ex.getMessage());
>     } catch (SQLException ex) {
>         if ("23505".equals(ex.getSQLState())) {
>             m = new Message(String.format("Employee %d already exists.", e.getBadge()), "E300", ex.getMessage());
>         } else {
>             m = new Message("Unexpected DB error.", "E200", ex.getMessage());
>         }
>     } catch (MimeTypeParseException ex) {
>         m = new Message("Unsupported MIME media type for photo. Expected: image/png or image/jpeg.", "E400", ex.getMessage());
>     } catch (MessagingException ex) {
>         // Employee created but email failed — not a fatal error
>         m = new Message(String.format("Employee %d created but unable to send confirmation email.", e.getBadge()));
>     }
>
>     req.setAttribute("employee", e);
>     req.setAttribute("message", m);
>     req.getRequestDispatcher("/jsp/create-employee-result.jsp").forward(req, res);
> }
> ```
> **Note:** `MessagingException` is caught separately — email failure is non-fatal (employee still created in DB). The user gets a warning message instead of an error.

### sendCreationConfirmationEmail

> [!Example] sendCreationConfirmationEmail()
> ```java
> private void sendCreationConfirmationEmail(Employee e) throws MessagingException {
>     final StringBuilder sb = new StringBuilder();
>     sb.append(String.format("<p>Dear %s,</p>%n", e.getSurname()));
>     sb.append(String.format("<p>Your account has been successfully created as follows:</p>%n"));
>     sb.append(String.format("<ul>%n"));
>     sb.append(String.format("<li><b>badge</b>: %d</li>%n", e.getBadge()));
>     sb.append(String.format("<li><b>surname</b>: %s</li>%n", e.getSurname()));
>     sb.append(String.format("<li><b>age</b>: %d</li>%n", e.getAge()));
>     sb.append(String.format("<li><b>salary</b>: %d</li>%n", e.getSalary()));
>     if (e.hasPhoto()) {
>         sb.append(String.format("<li><b>profile photo</b></li>%n"));
>         sb.append(String.format("<ul>%n"));
>         sb.append(String.format("<li><b>MIME media type</b>: %s</li>%n", e.getPhotoMediaType()));
>         sb.append(String.format("<li><b>size</b>: %d byte(s)</li>%n", e.getPhotoSize()));
>         sb.append(String.format("</ul>%n"));
>     }
>     sb.append(String.format("</ul>%n"));
>     sb.append(String.format("<p>Best regards,<br>The EMPLOYEE Team</p>%n"));
>
>     MailManager.sendMail(e.getEmail(),
>         String.format("Employee %s successfully created.", e.getBadge()),
>         sb.toString(), "text/html;charset=UTF-8");
> }
> ```
> Email body is HTML; MIME type of body passed as `"text/html;charset=UTF-8"`.

### LoadEmployeePhotoDAO and LoadEmployeePhotoServlet

> [!Example] LoadEmployeePhotoDAO — SELECT photo bytes from DB
> ```java
> private static final String STATEMENT =
>     "SELECT photo, photoMediaType FROM Ferro.Employee WHERE badge = ?";
>
> @Override
> public final void doAccess() throws SQLException {
>     // ...
>     if (rs.next()) {
>         e = new Employee(Integer.MIN_VALUE, null, Integer.MIN_VALUE, Integer.MIN_VALUE,
>                          null, rs.getBytes("photo"), rs.getString("photoMediaType"));
>     } else {
>         throw new SQLException(String.format("Employee %d not found.", badge), "NOT_FOUND");
>     }
>     this.outputParam = e;
> }
> ```
> **Note:** `Employee` used as a transport object — only `photo` and `photoMediaType` are meaningful; other fields set to sentinel values.

> [!Example] LoadEmployeePhotoServlet — stream raw bytes to browser
> ```java
> e = new LoadEmployeePhotoDAO(getConnection(), badge).access().getOutputParam();
>
> if (e.hasPhoto()) {
>     res.setContentType(e.getPhotoMediaType());      // set correct MIME type
>     res.getOutputStream().write(e.getPhoto());       // stream raw bytes
>     res.getOutputStream().flush();
> } else {
>     res.setStatus(HttpServletResponse.SC_NO_CONTENT); // 204
> }
> // On errors: res.setStatus(HttpServletResponse.SC_INTERNAL_SERVER_ERROR); // 500
> ```
> JSP `<img>` tag references this servlet:
> ```jsp
> <img src="<c:url value="/load-employee-photo">
>         <c:param name="badge" value="${employee.badge}"/>
>     </c:url>"/>
> ```

### web.xml Multipart Configuration

> [!Important] Multipart Upload Limits
> `web.xml` configures the multipart upload limits for `CreateEmployeeServlet`:
>
> ```xml
> <servlet>
>   <servlet-name>CreateEmployee</servlet-name>
>   <servlet-class>it.unipd.dei.webapp.servlet.CreateEmployeeServlet</servlet-class>
>   <multipart-config>
>     <max-file-size>1048576</max-file-size>        <!-- 1 Mbyte -->
>     <max-request-size>1049600</max-request-size>  <!-- 1 Mbyte + 1 Kbyte -->
>     <file-size-threshold>524288</file-size-threshold> <!-- 500 Kbyte -->
>   </multipart-config>
> </servlet>
> ```
>
> The same `web.xml` also declares `LoadEmployeePhotoServlet`, used by the JSP `<img>` URL to stream photo bytes back to the browser.

### MailManager

> [!Important] MailManager — static helper class for sending email
> `MailManager` uses a **static initialisation block** to load configuration once at class load time.
>
> Configuration file: `mailManager.properties` (on classpath in `resources/`).
> Properties read:
> - `MailManager.from` — sender address
> - `MailManager.smtp.host` — SMTP server hostname
> - `MailManager.smtp.port` — SMTP port (optional)
> - `MailManager.smtp.userName` — SMTP auth username
> - `MailManager.stmp.password` — SMTP auth password
>
> The static block sets `mail.transport.protocol = smtp`, enables `mail.smtp.starttls.enable = true`, disables mail debug, and creates an authenticated `Session` with `PasswordAuthentication` only when both username and password are configured.

> [!Example] MailManager.sendMail() — email without attachment
> ```java
> public static void sendMail(String to, String subject, String message, String messageMIME)
>         throws MessagingException {
>     final MimeMessage mm = new MimeMessage(session);
>     mm.setFrom();
>     mm.addRecipient(Message.RecipientType.TO, new InternetAddress(to));
>     mm.addRecipient(Message.RecipientType.BCC, new InternetAddress(from)); // sender in BCC
>     mm.setSubject(subject);
>     mm.setContent(message, messageMIME);
>     Transport.send(mm);
> }
> ```

> [!Example] MailManager.sendAttachmentMail() — email with attachment
> ```java
> public static void sendAttachmentMail(String to, String subject, String message, String messageMIME,
>         byte[] attachment, String attachmentMIME, String attachmentFileName)
>         throws MessagingException {
>
>     final MimeMessage mm = new MimeMessage(session);
>     final Multipart multipart = new MimeMultipart();
>
>     mm.setFrom();
>     mm.addRecipient(Message.RecipientType.TO, new InternetAddress(to));
>     mm.addRecipient(Message.RecipientType.BCC, new InternetAddress(from));
>     mm.setSubject(subject);
>
>     // body part
>     MimeBodyPart messageBodyPart = new MimeBodyPart();
>     messageBodyPart.setContent(message, messageMIME);
>     multipart.addBodyPart(messageBodyPart);
>
>     // attachment part
>     messageBodyPart = new MimeBodyPart();
>     messageBodyPart.setDataHandler(new DataHandler(new ByteArrayDataSource(attachment, attachmentMIME)));
>     messageBodyPart.setFileName(attachmentFileName);
>     multipart.addBodyPart(messageBodyPart);
>
>     mm.setContent(multipart); // multipart/mixed implicitly
>     Transport.send(mm);
> }
> ```
> The email structure is `multipart/mixed` — body text + binary attachment as separate MIME parts.

### Maven Dependencies — Jakarta Mail

![[http-employee-mail-project-structure.jpg]]

```xml
<dependency>
    <groupId>jakarta.mail</groupId>
    <artifactId>jakarta.mail-api</artifactId>
    <version>2.1.1</version>
</dependency>
<dependency>
    <groupId>org.eclipse.angus</groupId>
    <artifactId>angus-mail</artifactId>
    <version>2.0.1</version>
</dependency>
```
*(nota: `angus-mail` is the implementation; `jakarta.mail-api` is the API. Both required at runtime — no `provided` scope.)*

---

## HTTP/1.1

### Overview of HTTP

> [!Important] HTTP — HyperText Transfer Protocol
> - **Textual request-response protocol**: clients and servers exchange messages with a **header** and an optional **body**
> - **Stateless**: each request-response is independent; neither client nor server needs to track past messages
>   - Simplifies implementation; improves scalability
> - Supports **intermediaries / proxies**: typically for caching or security

![[Pasted image 20260512120450.png]]

*Figure: HTTP proxy chain — Browser → Proxy (gateway) → Proxy (firewall) → Web server. Each hop is an independent request-response.*

Reference: Fielding, R. et al. (1997). *HTTP/1.1.* RFC 2068.

### HTTP Request Methods

| Method | Semantics |
|--------|-----------|
| **GET** | Retrieve information identified by the request URI |
| **POST** | Submit data to create a new subordinate resource of the URI |
| **PUT** | Store the enclosed entity under the request URI (create or replace) |
| **DELETE** | Delete the resource identified by the request URI |
| **HEAD** | Identical to GET but server must not return body; headers only |
| **OPTIONS** | Request information about communication options for the URI |
### Properties of HTTP Methods

> [!Important] Safe, Idempotent, Cacheable
> - **Safe methods**: essentially read-only; no side effects on the server. Allows spiders and pre-fetching without harm.
>   - Safe: `GET`, `HEAD`, `OPTIONS`
> - **Idempotent methods**: multiple identical requests produce the same server-side effect as one. Allows automatic retry after connection failure.
>   - Idempotent: `GET`, `HEAD`, `OPTIONS`, `DELETE`, `PUT`; **NOT** idempotent: `POST`
> - **Cacheable methods**: responses may be stored for future reuse. Generally, safe methods are cacheable.

| HTTP Method | Request Has Body | Response Has Body | Safe | Idempotent | Cacheable |
|-------------|-----------------|-------------------|------|-----------|-----------|
| `GET` | Optional | Yes | Yes | Yes | Yes |
| `HEAD` | No | No | Yes | Yes | Yes |
| `POST` | Yes | Yes | No | No | Yes |
| `PUT` | Yes | Yes | No | Yes | No |
| `DELETE` | No | Yes | No | Yes | No |
| `OPTIONS` | Optional | Yes | Yes | Yes | No |

### HTTP Response Status Codes

> [!Important] Status Code Classes
> | Class | Meaning | Example |
> |-------|---------|---------|
> | **1xx** | Informational — request received, continuing | `101 Switching Protocols` |
> | **2xx** | Success — request successfully received, understood, accepted | `200 OK`, `201 Created`, `204 No Content` |
> | **3xx** | Redirection — further action needed to complete | `301 Moved Permanently` + `Location:` header |
> | **4xx** | Client Error — bad syntax or request cannot be fulfilled | `400 Bad Request`, `401 Unauthorized`, `404 Not Found`, `405 Method Not Allowed`, `409 Conflict`, `415 Unsupported Media Type` |
> | **5xx** | Server Error — server failed to fulfill a valid request | `500 Internal Server Error` |

### HTTP Request Headers

| Header | Purpose | Example |
|--------|---------|---------|
| `Accept` | Acceptable response media types | `Accept: text/plain, image/*` |
| `Accept-Charset` | Acceptable charsets | `Accept-Charset: iso-8859-5, UTF-8` |
| `Accept-Encoding` | Acceptable content encodings | `Accept-Encoding: compress, gzip` |
| `Accept-Language` | Preferred natural languages | `Accept-Language: it, da, en-gb` |
| `Authorization` | Authentication credentials | `Authorization: Basic bmljb2xhOmZlcnJv` |
| `Content-Type` | MIME type of request body (POST/PUT) | `Content-Type: application/json` |
| `Referer` | URI from which this request was obtained | `Referer: http://example.org/page.html` |
| `User-Agent` | Information about the client | `User-Agent: CERN-LineMode/2.15 libwww/2.17b3` |

### HTTP Response Headers

| Header | Purpose | Example |
|--------|---------|---------|
| `Content-Type` | MIME type of response body | `Content-Type: text/html; charset=ISO-8859-4` |
| `Content-Encoding` | Compression applied to body | `Content-Encoding: gzip` |
| `Content-Language` | Natural language of intended audience | `Content-Language: it, en` |
| `Content-Length` | Size in bytes of body | `Content-Length: 8092` |
| `Allow` | Supported HTTP methods for the resource | `Allow: GET, HEAD, PUT` |
| `WWW-Authenticate` | Authentication challenge mechanism | `WWW-Authenticate: Basic realm="Webapp"` |
| `Server` | Software info of origin server | `Server: CERN/3.0 libwww/2.17` |
| `Date` | Date/time message originated | `Date: Tue, 15 Nov 1994 08:12:31 GMT` |
| `Last-Modified` | Date/time resource was last modified | — |
| `Location` | URI for redirect (3xx) | `Location: http://www.dei.unipd.it/` |

---

## Authentication

### HTTP Basic Authentication

> [!Important] HTTP Basic Authentication
> - Client sends credentials via the `Authorization` header
> - Username and password concatenated with `:`, then **Base64 encoded**
> - Example: `nicola:ferro` → Base64 `bmljb2xhOmZlcnJv`
> ```
> GET /secured-resource/pippo.jpg HTTP/1.1
> Authorization: Basic bmljb2xhOmZlcnJv
> ```
> **Authentication challenge** — server returns `401 Unauthorized` + `WWW-Authenticate` header:
> ```
> HTTP/1.1 401 Unauthorized
> WWW-Authenticate: Basic realm="Webapp"
> ```
> - **realm**: partitions protected resources on a server; each realm has its own authentication scheme
> - After first successful auth, browser **automatically adds** `Authorization` header to all subsequent requests under the same realm

> [!Warning] Basic Auth is NOT Encrypted
> Credentials are only Base64-**encoded**, not encrypted. Anyone intercepting the HTTP traffic can decode them trivially. Must use together with **HTTPS** to ensure confidentiality.
> **Mitigation:** Always use Basic Auth over TLS/HTTPS only.

Reference: Fielding, R. and Reschke, J. (2014). *HTTP/1.1: Authentication.* RFC 7235.

### Session-Based Authentication with ProtectedResourceFilter

The `employee-session-jdbc` project adds a **Servlet Filter** to protect resources under `/protected/*`.

![[http-session-project-structure.jpg]]

*Figure: `employee-session-jdbc` project structure — new `filter/` package with `ProtectedResourceFilter`, `AuthenticateUserDAO`, and `/protected/` folder for protected JSPs.*

![[http-session-webxml.jpg]]

*Figure: `web.xml` — `ProtectedResourceFilter` mapped to `/protected/*`; `CreateEmployeeServlet` mapped to `/protected/create-employee`. All URLs under `/protected/` require authentication.*

The protected project keeps the database resource reference in `web.xml`:

```xml
<resource-ref>
  <description>Connection pool to the database</description>
  <res-ref-name>jdbc/employee-ferro</res-ref-name>
  <res-type>javax.sql.DataSource</res-type>
  <res-auth>Container</res-auth>
</resource-ref>
```

> [!Important] Jakarta Servlet Filter
> The `Filter` interface defines three lifecycle methods: `init()`, `doFilter()`, `destroy()`.
> - `doFilter(request, response, chain)` — process the request; call `chain.doFilter(req, res)` to pass to next element
> - Can intercept before AND after the servlet/JSP
> - Configured in `web.xml` with `<filter>` + `<filter-mapping>`

![[http-filter-class-fields.jpg]]

*Figure: `ProtectedResourceFilter` class fields — `Base64.Decoder DECODER`, `USER_ATTRIBUTE = "user"`, `FilterConfig config`, `DataSource ds`.*

> [!Example] ProtectedResourceFilter — field declarations
> ```java
> public class ProtectedResourceFilter implements Filter {
>     private static final Base64.Decoder DECODER = Base64.getDecoder();
>     public static final String USER_ATTRIBUTE = "user"; // key in HttpSession
>     private FilterConfig config = null;    // from web.xml
>     private DataSource ds;                 // JNDI connection pool
> }
> ```
> - `HttpSession` is basically a hash map; `USER_ATTRIBUTE` is the key used to store the authenticated username
> - In `init()`, the filter retrieves the connection pool with `new InitialContext().lookup("java:/comp/env/jdbc/employee-ferro")` and passes it to `AuthenticateUserDAO`

![[http-filter-dofilter-code.jpg]]

*Figure: `doFilter()` main logic — if no session → try authenticate; if session but no user → invalidate + try authenticate; if session with user → pass to next filter.*

> [!Example] doFilter() logic (text form)
> ```java
> final HttpSession session = req.getSession(false); // false = don't create if not exists
>
> if (session == null) {
>     // no session → try authentication
>     if (!authenticateUser(req, res)) return;
> } else {
>     final String user = (String) session.getAttribute(USER_ATTRIBUTE);
>     if (user == null || user.isBlank()) {
>         session.invalidate(); // stale session
>         if (!authenticateUser(req, res)) return;
>     }
>     // session + user valid → fall through to chain
> }
>
> chain.doFilter(req, res); // pass to next element
> ```

![[http-filter-authenticate-user.jpg]]

*Figure: `authenticateUser()` — reads `Authorization` header, checks `"BASIC "` prefix, Base64-decodes, splits on `:` to get username:password.*

> [!Example] authenticateUser() logic
> ```java
> private boolean authenticateUser(HttpServletRequest req, HttpServletResponse res) {
>     final String auth = req.getHeader("Authorization");
>
>     if (auth == null || auth.isBlank()) {
>         sendAuthenticationChallenge(res);
>         return false;
>     }
>
>     if (!auth.toUpperCase().startsWith("BASIC ")) {
>         sendAuthenticationChallenge(res);
>         return false;
>     }
>
>     // decode Base64, split at ':' (limit=2 to handle passwords containing ':')
>     final String pair = new String(DECODER.decode(auth.substring(6)));
>     final String[] userDetails = pair.split(":", 2);
>     // userDetails[0] = username, userDetails[1] = password
>
>     // authenticate against DB via AuthenticateUserDAO
>     boolean authenticated = new AuthenticateUserDAO(con, userDetails[0], userDetails[1]).access().getOutputParam();
>
>     if (authenticated) {
>         HttpSession session = req.getSession(true); // create new session
>         session.setAttribute(USER_ATTRIBUTE, userDetails[0]);
>         return true;
>     } else {
>         sendAuthenticationChallenge(res);
>         return false;
>     }
> }
> ```

![[http-filter-send-challenge.jpg]]

*Figure: `sendAuthenticationChallenge()` — sets `WWW-Authenticate: Basic realm=Employee` and sends `401 Unauthorized`.*

> [!Example] sendAuthenticationChallenge()
> ```java
> private void sendAuthenticationChallenge(HttpServletResponse res) throws IOException {
>     res.setHeader("WWW-Authenticate", "Basic realm=Employee");
>     res.sendError(HttpServletResponse.SC_UNAUTHORIZED); // 401
> }
> ```

> [!Important] AuthenticateUserDAO
> - Receives `username` and `password` in constructor
> - Queries DB to verify credentials
> - `outputParam` (boolean): `true` if authenticated, `false` otherwise
> - Separate DAO for authentication keeps concerns separated from employee DAOs

> [!Example] Using the Authenticated User
> Protected JSPs can check the session user and render different content:
>
> ```jsp
> <c:choose>
>   <c:when test="${empty sessionScope.user}">
>     <!-- unauthorized access page -->
>   </c:when>
>   <c:otherwise>
>     Welcome back, <c:out value="${sessionScope.user}"/>.
>   </c:otherwise>
> </c:choose>
> ```
>
> Protected servlets reuse the existing session with `req.getSession(false)`, read `ProtectedResourceFilter.USER_ATTRIBUTE`, and put the authenticated user into the logging context with `LogContext.setUser(user)`.

---

## Summary Table

| Topic | Standard/Technology | Key Detail |
|-------|---------------------|------------|
| URI | RFC 3986 | Generic identification; scheme + authority + path + query + fragment |
| URL | RFC 1738 | URI that also locates (network address) |
| URN | RFC 8141 | URI with `urn:` scheme; permanent name |
| IRI | RFC 3987 | URI extended with Unicode |
| Percent-Encoding | RFC 3986 | `%XX` hex encoding for reserved/non-ASCII chars |
| ASCII | ASA 1963 | 7 bits, 128 chars; English only |
| Extended ASCII | ISO 8859, 1987 | 8 bits, 256 chars; multiple incompatible variants |
| Unicode | Unicode Consortium, 1991 | Up to 32 bits; 172,849 chars (v18.0, 2026) |
| UTF-8 | ISO 1993 | Variable-width; backward-compat with ASCII |
| MIME | RFC 2045/2046 | Media type + encoding standard; `type/subtype` |
| `multipart/mixed` | RFC 2046 | Independent parts bundled (email + attachment) |
| `multipart/form-data` | RFC 7578 | File upload + form fields |
| `application/x-www-form-urlencoded` | HTML 4.01 | Form fields only; percent-encoded |
| Jakarta Part API | Servlet 5.0+ | `req.getParts()` → `Part.getInputStream()` |
| Multipart upload config | `web.xml` | `max-file-size`, `max-request-size`, `file-size-threshold` |
| Jakarta Mail 2.1 | EE 9+ | `MimeMessage`, `Transport.send()`, SMTP |
| `MailManager` SMTP setup | Jakarta Mail | `smtp`, STARTTLS, optional `PasswordAuthentication` |
| HTTP | RFC 2068 | Stateless, textual, request-response |
| Safe methods | HTTP/1.1 | GET, HEAD, OPTIONS — no side effects |
| Idempotent methods | HTTP/1.1 | GET, HEAD, OPTIONS, DELETE, PUT |
| HTTP Basic Auth | RFC 7235 | `user:pass` Base64-encoded; NOT encrypted |
| `ProtectedResourceFilter` | Jakarta Filter | `implements Filter`; `doFilter()` chain pattern |
| `HttpSession` | Jakarta Servlet | Key-value store per user session; `getSession(false)` |
| `sessionScope.user` | JSP EL | Read authenticated user in protected JSPs |
| `AuthenticateUserDAO` | DAO pattern | DB-backed credential check; `outputParam` boolean |

## Questions

1. How do HTML, HTTP, MIME, and URL work together as the four basic technologies of the Web?
2. How would you distinguish URI, URL, URN, and IRI using examples?
3. What information is encoded in the general URI syntax, and how do path, query, and fragment serve different purposes?
4. Why is percent-encoding necessary, and how does it relate to reserved characters and non-ASCII text?
5. How did the limitations of ASCII and Extended ASCII lead to Unicode and UTF-8?
6. Why is UTF-8 backward-compatible with ASCII, and why is that useful for the Web?
7. What does MIME add to HTTP and email communication, especially through `Content-Type`, `Content-Disposition`, and multipart bodies?
8. How does `multipart/form-data` represent form fields and uploaded files differently from `application/x-www-form-urlencoded`?
9. How does the Jakarta `Part` API expose uploaded files and form fields to a servlet?
10. Why must uploaded file MIME types be validated server-side, even when an HTML form restricts accepted file types?
11. How does the extended Employee example process a multipart request, store a photo, send a confirmation email, and later stream the photo back to the browser?
12. Why is an email with an attachment represented as `multipart/mixed`, and how do `MimeMultipart` and `MimeBodyPart` model that structure?
13. What does it mean for HTTP to be stateless, textual, and request-response based?
14. How do safe, idempotent, and cacheable properties differ across HTTP methods?
15. How should status code classes `2xx`, `3xx`, `4xx`, and `5xx` guide client and server behavior?
16. Why is HTTP Basic Authentication unsafe without HTTPS, despite using Base64 encoding?
17. How does `ProtectedResourceFilter` use `Authorization`, `WWW-Authenticate`, `HttpSession`, and `AuthenticateUserDAO` to protect `/protected/*` resources?
