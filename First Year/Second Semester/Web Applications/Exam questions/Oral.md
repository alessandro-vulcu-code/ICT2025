# Login and Pool Management Speaker Notes

## Two-Minute Presentation Script
The Login Page solves the first access problem: every user enters from the same page, but the system must recognize who they are and protect what they can access.

On the frontend, the page has SPLASH branding, email and password fields, validation, and a Remember Me option.

After successful login, the user reaches the Dashboard; with wrong credentials, an error is shown directly on the page.

On the backend, authentication checks the email and hashed password in the database.

If login succeeds, the application creates a server session and returns JWT tokens for REST calls.

Then AuthenticationFilter and PageAccessPolicy protect private pages, including manager and admin sections.

The second page is Pool Management.

Here the problem is practical: managers need to maintain the pools of the park and specify how many lifeguards each one requires.

The frontend shows a table with pool ID, name, and required lifeguards.

Managers can create, edit, and delete pools from the interface.

Deletion has a confirmation step, because removing a pool is a sensitive action.

On the backend, the page uses REST endpoints for pool CRUD operations.

Those endpoints are role-protected, so only authorized users can modify pool data.

So my two pages cover two basic needs of SPLASH: secure entry into the system, and controlled management of pool information used later for planning shifts.

The full usage flow will be shown at the end in the live demo.



---

## If Asked: Login Page

### General Explanation



The Login Page is the entry point of the application.

On the frontend, it is a JSP page with a simple form: email, password, Remember Me, validation feedback, and an error message area.

When the user submits the form, login.js prevents the default form submission and sends an AJAX POST request to /users/authenticate with email, password, and rememberMe.

If authentication succeeds, the frontend stores the returned user data and tokens, then redirects the user to the Dashboard.

If authentication fails, the page shows an error message without reloading.
### Backend Flow
On the backend, /users/authenticate is handled by AuthenticateUserRR.

It parses the JSON request into an Auth object, checks that email and password are present, then calls AuthenticateUserDAO.

The DAO searches the user by email in the app_user table.

The password is not compared in plain text: the stored password is a BCrypt hash, and Utility.CheckHash verifies the submitted password against that hash.

If credentials are valid, the backend creates a server-side session, stores the authenticated User in the session, and returns JWT access and refresh tokens.

These tokens are then used by frontend REST calls.
### Remember Me
Remember Me works on both frontend and backend.

On the frontend, if Remember Me is checked, login.js stores tokens and user data in localStorage.

This means the data survives browser restart.

If it is not checked, the same data is stored in sessionStorage, so it lasts only for the browser session.

On the backend, the rememberMe value is also sent to AuthenticateUserRR.

If rememberMe is true, the session cookie lives longer.

If it is false, the session behaves like a normal browser session.
### Page Protection
After login, protected pages are controlled by AuthenticationFilter and PageAccessPolicy.

AuthenticationFilter checks whether the user has a valid session or JWT token.

PageAccessPolicy checks whether the user's role can access the requested page.

So even if someone manually types an admin or manager URL, unauthorized users are redirected away.
### Wrong Credentials

If credentials are wrong, AuthenticateUserDAO returns null.

AuthenticateUserRR then sends a 401 response with an error message.

The frontend reads that response and shows "Invalid email or password" on the login page.

---
## If Asked: Pool Management

### General Explanation
Pool Management is a manager-side page used to maintain pool information.

The goal is to centralize pool data: pool ID, pool name, and required number of lifeguards.

On the frontend, pools-management.jsp defines the page structure, table, create/edit modal, and delete confirmation modal.

pool-management.js loads the pool list from the backend, renders the rows dynamically, and handles create, update, and delete actions.
### Backend Flow

On the backend, pool actions are exposed through PoolServletRR.

It maps REST routes to specific resource classes:

GET /pools/all reads pools,

POST /pools/create creates a pool,

PUT /pools/update updates a pool,

DELETE /pools/delete/{id} deletes a pool.

Each resource class calls the related DAO, such as GetPoolsDAO, CreatePoolDAO, UpdatePoolDAO, or DeletePoolDAO.

The DAO layer executes SQL against the pool table in PostgreSQL.
### Create and Edit

For create and edit, the frontend uses a Bootstrap modal.

When creating a pool, the modal starts empty.

When editing, pool-management.js fills the modal with the selected pool's current name and required lifeguards.

When the user saves, JavaScript builds a JSON payload with id, name, and nrGuards.

If there is an id, it sends a PUT request to update the existing pool.

If there is no id, it sends a POST request to create a new pool.

After success, the table is re-rendered.
### Delete Confirmation
Delete is treated as a sensitive action.

When the user clicks Delete, pool-management.js opens a confirmation modal instead of deleting immediately.

The modal explains that deleting the pool can affect assigned shifts.

Only after confirmation does the frontend send DELETE /pools/delete/{id}.

If the backend succeeds, the pool is removed from the local table state and the table is updated.
### Role Protection
Pool modification is role-protected.

In PoolServletRR, create, update, and delete are allowed only for authorized roles such as Leader, Manager, and Admin.

Reading pools is available more broadly because shift and planning pages need pool information.
### Operational Value
The important point is that Pool Management is not only a CRUD page.

The required lifeguard count is operational data.

It helps managers understand how much coverage each pool needs before planning shifts.

---
## Useful Short Answers

### What happens after login?
After login, the backend creates a session and returns JWT tokens.

The frontend stores user data and redirects to the Dashboard.

Protected pages are checked by AuthenticationFilter and PageAccessPolicy.
### Why use Remember Me?
Remember Me decides where the frontend stores authentication data.

With Remember Me, data goes into localStorage and persists longer.

Without it, data goes into sessionStorage and ends with the browser session.
### Why delete confirmation for pools?
Pool deletion is sensitive because pools can be connected to operational planning.

The confirmation modal prevents accidental deletion before the REST delete call is sent.
### Why required lifeguards on pools?
Required lifeguards define the minimum coverage needed for each pool.

This makes pool data useful for shift planning, not only for display.
### Which files are involved?

Login frontend: login.jsp and login.js.

Login backend: AuthenticateUserRR, AuthenticateUserDAO, AuthenticationFilter, PageAccessPolicy.

Pool frontend: pools-management.jsp, pool-management.js, pool-management.css.

Pool backend: PoolServletRR, GetPoolsRR, CreatePoolRR, UpdatePoolRR, DeletePoolRR, and their DAO classes.