# Introduction to Java Server Pages (JSP)

## Table of Contents

- [[#JavaServer Pages (JSP)|JavaServer Pages (JSP)]]
  - [[#Why JSP|Why JSP]]
  - [[#JSP Execution Model|JSP Execution Model]]
  - [[#Components of a JSP Page|Components of a JSP Page]]
- [[#JavaBeans|JavaBeans]]
- [[#Standard Actions|Standard Actions]]
- [[#JSP Standard Tag Library (JSTL)|JSP Standard Tag Library (JSTL)]]
  - [[#JSTL Core Actions|JSTL Core Actions]]
  - [[#JSTL Formatting Actions|JSTL Formatting Actions]]
  - [[#JSTL Functions|JSTL Functions]]
- [[#Expression Language (EL)|Expression Language (EL)]]
  - [[#EL Operators|EL Operators]]
  - [[#EL Implicit Variables|EL Implicit Variables]]
- [[#JSP Examples|JSP Examples]]
  - [[#Minimal JSP Page|Minimal JSP Page]]
  - [[#JSP with JSTL and Parameters|JSP with JSTL and Parameters]]
  - [[#Shared JSP Includes|Shared JSP Includes]]
- [[#Model-View-Controller (MVC) Paradigm|Model-View-Controller (MVC) Paradigm]]
  - [[#MVC Definition|MVC Definition]]
  - [[#MVC and Java Web Technologies|MVC and Java Web Technologies]]
  - [[#MVC and Application Layers|MVC and Application Layers]]
- [[#MVC Employee Application with JSP|MVC Employee Application with JSP]]
  - [[#MVC Mapping in the Employee App|MVC Mapping in the Employee App]]
  - [[#Key Difference: Forward vs Direct Response|Key Difference: Forward vs Direct Response]]
  - [[#Resource Classes as Almost JavaBeans|Resource Classes as Almost JavaBeans]]
  - [[#Servlet Controllers with JSP Forward|Servlet Controllers with JSP Forward]]
  - [[#JSP View Pages|JSP View Pages]]
  - [[#Sequence Diagrams|Sequence Diagrams]]
  - [[#Maven POM for JSTL|Maven POM for JSTL]]
- [[#Summary Table|Summary Table]]

---

## JavaServer Pages (JSP)

### Why JSP

Creating HTML (CSS, JS) directly from servlets is **cumbersome**:
- No IDE support for writing HTML — it's just Java strings
- Prone to errors (unclosed tags, escaping issues)
- Hard to maintain and upgrade

**JavaServer Pages (JSP)** provides textual (HTML-like) specification of dynamic responses. Three core concepts:

1. **Template Data**: most of a page is static HTML — JSP handles this naturally
2. **Addition of Dynamic Data**: simple mechanisms to embed runtime values
3. **Encapsulation of Functionality**: via *JavaBeans* and *tag libraries* (JSTL)

### JSP Execution Model

> [!Important] JSP Compilation and Execution
> On the **first invocation**, the container:
> 1. Translates `hello.jsp` → `hello_jsp.java` (a servlet class)
> 2. Compiles `hello_jsp.java` → `hello_jsp.class`
> 3. Executes the class to serve the request
>
> **Subsequent invocations** reuse the compiled `.class` directly. The container can also **pre-compile** JSP pages before deployment.
>
> **Intuition:** JSP is syntactic sugar. Under the hood it's a servlet — it just lets you write HTML and embed Java/EL snippets instead of writing `out.printf("<html>...")`.

Flow: `hello.jsp` → (translation) → `hello_jsp.java` → (compilation) → `hello_jsp.class` → (execution) → `hello.html` sent to browser.
![[Pasted image 20260512115326.png]]
### Components of a JSP Page

| Component | Syntax | Purpose |
|-----------|--------|---------|
| **Template text** | plain HTML | Static content sent as-is |
| **Directive** `page` | `<%@ page … %>` | Page-level attributes (content type, imports, …) |
| **Directive** `include` | `<%@ include … %>` | Static file inclusion at translation time |
| **Directive** `taglib` | `<%@ taglib … %>` | Declare a tag library |
| **Standard action** | `<jsp:useBean>`, `<jsp:forward>`, … | Standard JSP operations (XML syntax) |
| **Custom action** | `<c:if>`, `<fmt:formatDate>`, … | JSTL or other tag library actions |
| **Scriptlet** | `<% … %>` | Raw Java code fragment (avoid!) |
| **Expression** | `<%= … %>` | Evaluates a Java expression and writes result |
| **Declaration** | `<%! … %>` | Declares variables/methods for the JSP class |
| **Expression Language** | `${…}` | Concise access to beans, scopes, parameters |

> [!Warning] Avoid Scriptlets
> Scriptlets (`<% %>`) embed raw Java in HTML — this defeats the purpose of JSP and makes code hard to maintain. Prefer EL (`${…}`) and JSTL tags (`<c:if>`, `<c:forEach>`, etc.) for all logic in JSP pages.

---

## JavaBeans

> [!Important] JavaBeans Convention
> A **JavaBean** is a Java class following specific naming conventions so that frameworks can manipulate it generically:
> - Must have a **no-argument constructor**
> - Fields exposed via **`getXXX()`** / **`setXXX()`** for a field named `XXX`
> - Boolean fields use **`isXXX()`** instead of `getXXX()`
>
> JSP and EL use these conventions to read/write bean properties without reflection boilerplate.
>
> **Intuition:** `${employee.badge}` in EL calls `employee.getBadge()` — EL knows this from the `get` + capitalization convention.

---

## Standard Actions

| Action              | Description                                                              |
| ------------------- | ------------------------------------------------------------------------ |
| `<jsp:useBean>`     | Instantiates (or locates) a JavaBean and makes it available to the page  |
| `<jsp:getProperty>` | Gets a bean property value and writes it to the response                 |
| `<jsp:setProperty>` | Sets a bean property value                                               |
| `<jsp:include>`     | Includes the response of another JSP/servlet (inside web container only) |
| `<jsp:forward>`     | Forwards processing to another JSP/servlet (inside web container only)   |
| `<jsp:param>`       | Adds parameters to a request made by `<jsp:include>` or `<jsp:forward>`  |
![[Pasted image 20260512115436.png]]
![[Pasted image 20260512115449.png]]

---

## JSP Standard Tag Library (JSTL)

**JSTL** is a standardized collection of custom tag libraries covering common needs.

| Area | Prefix | URI | Purpose |
|------|--------|-----|---------|
| Core | `c` | `http://java.sun.com/jsp/jstl/core` | Conditionals, iteration, URL rewriting, import, redirect |
| XML Processing | `x` | `http://java.sun.com/jsp/jstl/xml` | XPath, XSLT processing |
| I18N Formatting | `fmt` | `http://java.sun.com/jsp/jstl/fmt` | Locale, date/number formatting, resource bundles |
| Relational DB | `sql` | `http://java.sun.com/jsp/jstl/sql` | Direct SQL from JSP (avoid in production) |
| Functions | `fn` | `http://java.sun.com/jsp/jstl/functions` | String utilities |

### JSTL Core Actions

| Action | Description |
|--------|-------------|
| `<c:out>` | Evaluates expression, writes to response — **escapes XML/HTML by default** |
| `<c:if>` | Conditional rendering — evaluates body only if condition true |
| `<c:choose>` | Switch-like: evaluates first matching `<c:when>`, or `<c:otherwise>` |
| `<c:forEach>` | Iterates over a collection or a numeric range |
| `<c:url>` | Constructs a URL applying session/rewrite rules; handles context path |
| `<c:import>` | Imports content of a resource (local or external URL) into response or variable |
| `<c:redirect>` | Sends HTTP redirect to client |
| `<c:param>` | Adds a parameter to `<c:url>`, `<c:import>`, or `<c:redirect>` |

> [!Important] Use `<c:out>` Not `${…}` for Output
> `<c:out value="${...}"/>` escapes XML characters (`<`, `>`, `&`, `"`, `'`) → prevents **XSS**. Bare `${...}` in template text does **not** escape. Always use `<c:out>` when outputting user-controlled data.

### JSTL Formatting Actions

| Action | Description |
|--------|-------------|
| `<fmt:setLocale>` | Sets locale (e.g., `en_UK`, `it_IT`) |
| `<fmt:setBundle>` | Sets the resource bundle for message localization |
| `<fmt:message>` | Outputs a localized message from the bundle |
| `<fmt:param>` | Provides a parameter for a localized message |
| `<fmt:formatNumber>` | Formats a number according to locale and format |
| `<fmt:formatDate>` | Formats a date/time according to locale and style |

### JSTL Functions

| Function | Description |
|----------|-------------|
| `fn:contains` | Checks if string contains a sub-string |
| `fn:endsWith` | Checks if string ends with a sub-string |
| `fn:escapeXml` | Escapes XML markup characters |
| `fn:length` | Returns string length or collection size |
| `fn:replace` | Replaces a sub-string |
| `fn:split` | Splits string into array |
| `fn:substring` | Extracts sub-string |

---

## Expression Language (EL)

### EL Operators

| Operator | Description |
|----------|-------------|
| `.` | Access JavaBean property or Map entry (`${employee.badge}` → `getBadge()`) |
| `[]` | Access array/List element (`${list[0]}`) |
| `()` | Grouping |
| `? :` | Conditional (ternary) |
| `+ - * / %` | Arithmetic |
| `< > <= >= == !=` | Relational |
| `&& \|\| !` | Boolean |
| `empty` | True if variable is null, empty string, empty array/collection |
| `func(arg)` | Invoke a JSTL function |

### EL Implicit Variables

| Variable | Description |
|----------|-------------|
| `pageScope` | Map of variables in **page** scope |
| `requestScope` | Map of variables in **request** scope |
| `sessionScope` | Map of variables in **session** scope |
| `applicationScope` | Map of variables in **application** (servlet context) scope |
| `param` | Map of request parameters (single-value strings) |
| `paramValues` | Map of request parameters (arrays of strings) |
| `header` | Map of HTTP headers (single-value strings) |
| `headerValues` | Map of HTTP headers (arrays of strings) |
| `cookie` | Map of cookies as `javax.servlet.http.Cookie` objects |

*(nota: scopes resolve in order page → request → session → application if no explicit prefix used)*

---

## JSP Examples

### Minimal JSP Page

> [!Example] hello-world.jsp — Minimal JSP
> ```jsp
> <%@ page contentType="text/html;charset=UTF-8" %>
> <!DOCTYPE html>
> <html lang="en">
>  <head>
>   <meta charset="utf-8">
>   <title>HelloWorld JSP Response</title>
>  </head>
>  <body>
>   <h1>HelloWorld JSP Response</h1>
>   <hr />
>   <p>Hello, world!</p>
>  </body>
> </html>
> ```
>
> **Explanation:** `<%@ page contentType="text/html;charset=UTF-8" %>` sets the `Content-Type` response header. Everything else is template text sent as-is.

### JSP with JSTL and Parameters

> [!Example] hello-world-param.jsp — JSTL conditionals and EL
> ```jsp
> <%@ page contentType="text/html;charset=UTF-8" %>
> <%@ taglib prefix="c"   uri="http://java.sun.com/jsp/jstl/core" %>
> <%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt" %>
>
> <!-- ... head and header ... -->
>
> <c:choose>
>     <c:when test="${empty param.helloName}">
>         <div class="alert alert-danger">Please, enter your name!</div>
>     </c:when>
>     <c:otherwise>
>         <div>Hello, <c:out value="${param.helloName}"/>!</div>
>     </c:otherwise>
> </c:choose>
>
> <!-- Display current date using a JavaBean and fmt tags -->
> <jsp:useBean id="now" class="java.util.Date"/>
> <fmt:setLocale value="en_UK"/>
> on <fmt:formatDate value="${now}" type="date" dateStyle="long"/>
> at <fmt:formatDate value="${now}" type="time" timeStyle="long"/>
> ```
>
> **Key points:**
> - `${empty param.helloName}` — EL `empty` operator checks for null/empty; `param` is the EL implicit Map of request parameters
> - `<c:out value="${param.helloName}"/>` — safe output with XML escaping
> - `<jsp:useBean id="now" class="java.util.Date"/>` — instantiates a `java.util.Date` and binds it to the name `now` in page scope
> - `<fmt:formatDate>` formats `${now}` per `en_UK` locale

> [!Warning] Always validate in the JSP even if form has `required`
> A JSP like `hello-world-param.jsp` can be called **directly** by URL without going through the form — bypassing the `required` attribute. Always validate parameters in the JSP (or servlet) regardless of HTML-side validation.

### Shared JSP Includes

**Pattern**: common fragments (header, footer, scripts) are factored into include files under `/jsp/include/`:

```
/jsp/include/head.jsp    — <meta>, CSS links (Bootstrap, FontAwesome)
/jsp/include/foot.jsp    — Bootstrap/jQuery JS scripts
/jsp/include/footer.jsp  — copyright footer markup
```

Referenced with `<c:import url="/jsp/include/head.jsp"/>` — this includes the *response* of the target JSP (dynamic include, evaluated at request time).

> [!Example] index.jsp — Composing the page from includes
> ```jsp
> <%@ page contentType="text/html;charset=UTF-8" %>
> <%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
>
> <!DOCTYPE html>
> <html lang="en">
> <head>
>     <c:import url="/jsp/include/head.jsp"/>
>     <title>Basic Web Application with JavaServer Pages</title>
> </head>
> <body>
> <div class="container">
>     <!-- ... header ... -->
>
>     <!-- URL resolved relative to webapp root using c:url -->
>     <img src="<c:url value="/media/hello.png"/>" alt="...">
>     <a href="<c:url value="/jsp/hello-world.jsp"/>">...</a>
>
>     <!-- footer -->
>     <c:import url="/jsp/include/footer.jsp"/>
> </div>
> <c:import url="/jsp/include/foot.jsp"/>
> </body>
> </html>
> ```
>
> **`<c:url>`**: always use this tag for URL resolution — it handles the webapp context path prefix and session URL rewriting automatically.

---

## Model-View-Controller (MVC) Paradigm

### MVC Definition

> [!Important] MVC Pattern
> **Model-View-Controller (MVC)** (Krasner & Pope, 1988) is an architectural pattern that separates an application into three roles:
>
> | Role | Responsibility | Interactions |
> |------|---------------|--------------|
> | **Model** | Holds application state and business logic | Queried/updated by Controller; notifies View of state changes |
> | **View** | Renders output to users | Reads from Model; receives selection from Controller |
> | **Controller** | Handles user input | Queries/updates Model; selects which View to display |
>
> **Intuition:** User clicks button → Controller handles event → updates Model → tells View to render → user sees result.

### MVC and Java Web Technologies

| MVC Role | Java Web Technology |
|----------|-------------------|
| **Model** | Java classes / *JavaBeans* (e.g., `Employee`, `Message`) |
| **View** | JSP pages (HTML, CSS, JS) |
| **Controller** | *Servlet* |

Flow: Browser → (HTTP request) → Servlet (Controller) → (invokes) → DAO (Model layer) → Servlet sets request attributes → (forwards) → JSP (View) → (HTML) → Browser.

### MVC and Application Layers
![[Pasted image 20260512115525.png]]
![[jsp-mvc-layers-employee.jpg]]

MVC roles map to application layers:

| MVC Role | Application Layer | In Employee App |
|----------|------------------|-----------------|
| **View** | Presentation Logic | `create-employee-form.jsp`, `create-employee-result.jsp`, `search-employee-form.jsp`, `search-employee-result.jsp` |
| **Controller** | Application Logic | `CreateEmployeeServlet`, `SearchEmployeeBySalaryServlet` |
| **Model** | Data Logic + Domain | `Employee`, `Message`, `CreateEmployeeDAO`, `SearchEmployeeBySalaryDAO` |

---

## MVC Employee Application with JSP

### MVC Mapping in the Employee App

```
Input from Users
    ↓
View (form JSPs)                   create-employee-form.jsp
                                   search-employee-form.jsp
    ↓ POST /create-employee
    ↓ POST /search-employee-by-salary

Controller (Servlets)              CreateEmployeeServlet
                                   SearchEmployeeBySalaryServlet
    ↓ INVOKE DAO
    ↓ FORWARD to result JSP

Model (resources + DAOs)           Employee, Message
                                   CreateEmployeeDAO, SearchEmployeeBySalaryDAO

View (result JSPs)                 create-employee-result.jsp
                                   search-employee-result.jsp
    ↓
Output to Users
```

### Key Difference: Forward vs Direct Response

> [!Important] Servlet → JSP via `RequestDispatcher.forward()`
> In the previous (servlet-only) approach, the servlet wrote HTML directly with `PrintWriter`.
>
> In the MVC approach:
> 1. Servlet sets **request attributes** with the model objects
> 2. Servlet calls `req.getRequestDispatcher("/jsp/view.jsp").forward(req, res)` — transfers control to the JSP
> 3. JSP reads the attributes via EL and renders HTML
>
> ```java
> // Servlet (Controller)
> req.setAttribute("employee", e);
> req.setAttribute("message", m);
> req.getRequestDispatcher("/jsp/create-employee-result.jsp").forward(req, res);
> ```
>
> ```jsp
> <%-- JSP (View) — reads request attributes via EL --%>
> <c:out value="${employee.badge}"/>
> <c:out value="${message.message}"/>
> ```
>
> **Intuition:** forward stays inside the server — the browser sees one HTTP response but two components collaborate to generate it.

### Resource Classes as Almost JavaBeans

The `Employee` and `Message` classes **partially** follow JavaBeans conventions:

| Convention | Employee/Message | Status |
|------------|-----------------|--------|
| No-arg constructor | ❌ Missing | Not full JavaBeans |
| `getXXX()` accessors | ✅ Present | Compliant |
| `isXXX()` for booleans | ✅ `isError()` | Compliant |
| `setXXX()` mutators | ❌ Missing (fields are `final`) | Not full JavaBeans |

They are **"almost JavaBeans"** — EL can call `getXXX()` methods via `${employee.badge}` syntax even without full compliance, as long as the getter naming convention is followed.

### Servlet Controllers with JSP Forward

> [!Example] CreateEmployeeServlet with JSP Forward
> ```java
> public final class CreateEmployeeServlet extends AbstractDatabaseServlet {
>
>     public void doPost(HttpServletRequest req, HttpServletResponse res)
>             throws ServletException, IOException {
>
>         LogContext.setIPAddress(req.getRemoteAddr());
>         LogContext.setAction(Actions.CREATE_EMPLOYEE);
>
>         int badge = -1; String surname = null; int age = -1; int salary = -1;
>         Employee e = null; Message m = null;
>
>         try {
>             badge   = Integer.parseInt(req.getParameter("badge"));
>             surname = req.getParameter("surname");
>             age     = Integer.parseInt(req.getParameter("age"));
>             salary  = Integer.parseInt(req.getParameter("salary"));
>             LogContext.setResource(req.getParameter("badge"));
>
>             e = new Employee(badge, surname, age, salary);
>             new CreateEmployeeDAO(getConnection(), e).access();
>             m = new Message(String.format("Employee %d successfully created.", badge));
>
>         } catch (NumberFormatException ex) {
>             m = new Message("Invalid parameters: badge, age, salary must be integer.", "E100", ex.getMessage());
>         } catch (SQLException ex) {
>             if (ex.getSQLState().equals("23505"))
>                 m = new Message(String.format("Employee %d already exists.", badge), "E300", ex.getMessage());
>             else
>                 m = new Message("Unexpected DB error.", "E200", ex.getMessage());
>         }
>
>         try {
>             // Set model objects as request attributes for the JSP
>             req.setAttribute("employee", e);
>             req.setAttribute("message", m);
>
>             // Forward to JSP view — JSP generates the HTML response
>             req.getRequestDispatcher("/jsp/create-employee-result.jsp").forward(req, res);
>
>         } catch (Exception ex) {
>             LOGGER.error("Unable to forward to JSP.", ex);
>             throw ex;
>         } finally {
>             LogContext.removeIPAddress();
>             LogContext.removeAction();
>             LogContext.removeResource();
>         }
>     }
> }
> ```

> [!Example] SearchEmployeeBySalaryServlet with JSP Forward
> ```java
> public final class SearchEmployeeBySalaryServlet extends AbstractDatabaseServlet {
>
>     public void doPost(HttpServletRequest req, HttpServletResponse res)
>             throws ServletException, IOException {
>
>         int salary = -1;
>         List<Employee> el = null; Message m = null;
>
>         try {
>             salary = Integer.parseInt(req.getParameter("salary"));
>             el = new SearchEmployeeBySalaryDAO(getConnection(), salary).access().getOutputParam();
>             m = new Message("Employees successfully searched.");
>         } catch (NumberFormatException ex) {
>             m = new Message("Salary must be integer.", "E100", ex.getMessage());
>         } catch (SQLException ex) {
>             m = new Message("Unexpected DB error.", "E200", ex.getMessage());
>         }
>
>         try {
>             // Set list and message as request attributes
>             req.setAttribute("employeeList", el);
>             req.setAttribute("message", m);
>
>             // Forward to JSP view
>             req.getRequestDispatcher("/jsp/search-employee-result.jsp").forward(req, res);
>         } catch (Exception ex) {
>             LOGGER.error("Unable to forward.", ex);
>             throw ex;
>         } finally {
>             LogContext.removeIPAddress();
>             LogContext.removeAction();
>             LogContext.removeUser();
>         }
>     }
> }
> ```

### JSP View Pages

> [!Example] JSP Form Pages — using `<c:url>` for action
> ```jsp
> <%@ page contentType="text/html;charset=utf-8" %>
> <%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
>
> <!-- Create Employee Form -->
> <form method="POST" action="<c:url value="/create-employee"/>">
>   <input name="badge"   type="text"/>
>   <input name="surname" type="text"/>
>   <input name="age"     type="text"/>
>   <input name="salary"  type="text"/>
>   <button type="submit">Submit</button>
> </form>
>
> <!-- Search Employee Form -->
> <form method="POST" action="<c:url value="/search-employee-by-salary"/>">
>   <input name="salary" type="text"/>
>   <button type="submit">Submit</button>
> </form>
> ```
>
> **Key**: `<c:url value="/create-employee"/>` prepends the webapp context path — required because the JSP is in `/jsp/` but the servlet is at the webapp root `/`.

> [!Example] create-employee-result.jsp — Render model via EL
> ```jsp
> <%@ page contentType="text/html;charset=utf-8" %>
> <%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
>
> <!DOCTYPE html>
> <html lang="en">
>  <head><title>Create Employee</title></head>
>  <body>
>   <h1>Create Employee</h1>
>   <hr/>
>
>   <!-- Delegate message rendering to reusable include -->
>   <c:import url="/jsp/include/show-message.jsp"/>
>
>   <!-- Show employee only if present and no error -->
>   <c:if test="${not empty employee && !message.error}">
>    <ul>
>     <li>badge:   <c:out value="${employee.badge}"/></li>
>     <li>surname: <c:out value="${employee.surname}"/></li>
>     <li>age:     <c:out value="${employee.age}"/></li>
>     <li>salary:  <c:out value="${employee.salary}"/></li>
>    </ul>
>   </c:if>
>  </body>
> </html>
> ```

> [!Example] show-message.jsp — Reusable error/success fragment
> ```jsp
> <%@ page contentType="text/html;charset=utf-8" %>
> <%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
>
> <c:choose>
>  <c:when test="${message.error}">
>   <ul>
>    <li>error code: <c:out value="${message.errorCode}"/></li>
>    <li>message:    <c:out value="${message.message}"/></li>
>    <li>details:    <c:out value="${message.errorDetails}"/></li>
>   </ul>
>  </c:when>
>  <c:otherwise>
>   <p><c:out value="${message.message}"/></p>
>  </c:otherwise>
> </c:choose>
> ```

> [!Example] search-employee-result.jsp — Iterate list with `<c:forEach>`
> ```jsp
> <%@ page contentType="text/html;charset=utf-8" %>
> <%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
>
> <body>
>  <h1>Search Employee</h1>
>  <hr/>
>  <c:import url="/jsp/include/show-message.jsp"/>
>
>  <c:if test="${not empty employeeList}">
>   <table>
>    <thead>
>     <tr><th>Badge</th><th>Surname</th><th>Age</th><th>Salary</th></tr>
>    </thead>
>    <tbody>
>     <c:forEach var="employee" items="${employeeList}">
>      <tr>
>       <td><c:out value="${employee.badge}"/></td>
>       <td><c:out value="${employee.surname}"/></td>
>       <td><c:out value="${employee.age}"/></td>
>       <td><c:out value="${employee.salary}"/></td>
>      </tr>
>     </c:forEach>
>    </tbody>
>   </table>
>  </c:if>
> </body>
> ```
>
> **`<c:forEach var="employee" items="${employeeList}">`** — `items` = EL expression for the `employeeList` request attribute (a `List<Employee>`); `var` = loop variable name accessible via EL within the body.

### Sequence Diagrams

![[jsp-create-employee-sequence.jpg]]

**Create Employee (MVC) steps:**
1. Browser: `POST /create-employee`
2. Container instantiates `CreateEmployeeServlet`, calls `init()` → JNDI lookup
3. `service()` → `doPost()` → parse params → create `Employee` → `CreateEmployeeDAO.access()` → INSERT
4. Create `Message`
5. `req.setAttribute("employee", e)` + `req.setAttribute("message", m)` (1.4.8)
6. `getRequestDispatcher("/jsp/create-employee-result.jsp").forward(req, res)` (1.4.9)
7. JSP generates HTML (step 2)
8. Browser receives HTML (3.1)

![[jsp-search-employee-sequence.jpg]]

**Search Employee (MVC) steps:**
1. Browser: `POST /search-employee`
2. `doPost()` → parse salary → `SearchEmployeeBySalaryDAO.access().getOutputParam()` → SELECT → `List<Employee>`
3. Create `Message`
4. `req.setAttribute("employeeList", el)` + `req.setAttribute("message", m)` (1.4.9)
5. Forward to `search-employee-result.jsp` (1.4.10)
6. JSP renders table (step 2) → HTML → Browser (3.1)

### Class Diagram

![[jsp-employee-class-diagram.jpg]]

Same class structure as the servlet-only version (slide 06) — the key addition is that servlets now **forward to JSP views** instead of writing HTML directly.

### Maven POM for JSTL

> [!Important] JSTL Scope Must NOT Be `provided`
> Unlike the servlet API and Tomcat JDBC pool, **JSTL taglibs are not bundled with Tomcat**. They must be packaged into the WAR:
>
> ```xml
> <dependencies>
>   <dependency>
>     <groupId>javax.servlet</groupId>
>     <artifactId>javax.servlet-api</artifactId>
>     <version>4.0.0</version>
>     <scope>provided</scope>   <!-- Tomcat provides this -->
>   </dependency>
>
>   <!-- JSTL API + implementation — must be IN the WAR -->
>   <dependency>
>     <groupId>javax.servlet</groupId>
>     <artifactId>jstl</artifactId>
>     <version>1.2</version>
>     <!-- No scope = compile scope = bundled in WAR -->
>   </dependency>
> </dependencies>
> ```

---

## Summary Table

| Concept | Technology | Notes |
|---------|------------|-------|
| **JSP** | Template text + directives + tags + EL | Compiled to servlet on first access |
| **Directive `page`** | `<%@ page contentType="..." %>` | Sets response Content-Type |
| **Directive `taglib`** | `<%@ taglib prefix="c" uri="..." %>` | Declares JSTL or custom tags |
| **EL** | `${expression}` | Accesses beans, scopes, params — no Java code needed |
| **JavaBeans** | `getXXX()` / `isXXX()` convention | EL resolves `${obj.field}` to `obj.getField()` |
| **`<c:out>`** | JSTL Core | Escaped output — prevents XSS |
| **`<c:if>`** | JSTL Core | Conditional rendering |
| **`<c:choose>`** / `<c:when>` / `<c:otherwise>` | JSTL Core | Multi-branch conditional |
| **`<c:forEach>`** | JSTL Core | Iterate collections |
| **`<c:url>`** | JSTL Core | Context-aware URL resolution |
| **`<c:import>`** | JSTL Core | Dynamic include of another JSP/resource |
| **`<fmt:formatDate>`** | JSTL Fmt | Locale-aware date formatting |
| **`<jsp:useBean>`** | Standard action | Instantiate/find a JavaBean in a scope |
| **`RequestDispatcher.forward()`** | Servlet API | Transfers control server-side to a JSP |
| **`req.setAttribute()`** | Servlet API | Passes model objects to the JSP via request scope |
| **MVC — Model** | JavaBeans (`Employee`, `Message`) | Domain objects; DAOs for persistence |
| **MVC — View** | JSP pages | Presentation only; no business logic |
| **MVC — Controller** | Servlets | Parse request, call model, forward to view |
| **JSTL scope** | Maven: no `provided` | Must be bundled in WAR; Tomcat does not include it |

## Questions

1. Why does writing HTML directly with `PrintWriter` inside servlets become difficult to maintain as pages grow?
2. How does the JSP execution model translate a `.jsp` file into a servlet class, and why is the first invocation different from later ones?
3. What roles do template text, directives, standard actions, JSTL tags, scriptlets, expressions, declarations, and EL play inside a JSP page?
4. Why are scriptlets discouraged, and how do EL and JSTL provide a cleaner alternative?
5. How does the JavaBeans naming convention allow EL expressions such as `${employee.badge}` to access Java object properties?
6. Why is `<c:out>` safer than writing a bare `${...}` expression when displaying user-controlled data?
7. How do JSTL core tags such as `<c:if>`, `<c:choose>`, `<c:forEach>`, `<c:url>`, and `<c:import>` support view logic without raw Java code?
8. How do EL implicit variables such as `param`, `requestScope`, `sessionScope`, and `cookie` help JSP pages access web application data?
9. Why should a JSP validate parameters even when the corresponding HTML form uses `required` attributes?
10. How does `<c:url>` solve context-path and URL-rewriting problems in JSP links, images, and form actions?
11. How does MVC separate responsibilities among servlets, JSP pages, resource classes, and DAOs in the employee application?
12. What changes when a servlet forwards to a JSP with `RequestDispatcher.forward()` instead of writing the whole HTML response itself?
13. How do request attributes carry `Employee`, `Message`, or `employeeList` objects from the controller to the JSP view?
14. In the MVC sequence diagrams, where are database access, request attribute setup, forwarding, and HTML rendering performed?
15. Why must JSTL dependencies be bundled in the WAR instead of marked as `provided`?
