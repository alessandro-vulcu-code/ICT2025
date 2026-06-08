
-- Slide 1 --
Good morning. I'm Alessandro Vulcu and today we are presenting our project SPLASH, which stays for Staff Planning & Lifeguard Activity Scheduling Hub.

-- Slide 2 --
Our project was born from a real problem that still exists in the water park where I work during the summer.
Currently, our manager creates the monthly shift schedule in an Excel file, prints it, and hangs it in the lifeguard station. If someone needs to swap a shift or request vacation days, the printed sheet has to be changed manually with a pen, which means the person usually needs to be physically present at the park.
Pool assignments (above) are also managed on paper and then shared in the lifeguards' WhatsApp group.

-- Slide 3 --
SPLASH aims to digitalize these practices, making the process easier for managers, but especially for lifeguards, who can access their shifts, requests, and communications directly through the web application.
Each team member developed 2 pages end-to-end: from UI to REST API integration.

-- Slide 4 --
We start obviously with the Login. Every user enters from the same page, then the system recognizes who they are and protect what they can access.

On the frontend, the page has SPLASH branding with minimal background, email and password fields, validation, and a Remember Me option.

After successful login, the user reaches the Dashboard; with wrong credentials, an error is shown directly on the page.

On the backend, authentication checks the email and hashed password in the database.

If login succeeds, the application creates a server session and returns JWT tokens for REST calls.
(JWT tokens are used to authenticate REST API requests after login.
Instead of sending the password again, the frontend sends a token, and the backend verifies it to know who is making the request and what role they have.)

Remember Me is connected to token persistence. The backend always returns JWT tokens, but when Remember Me is enabled the frontend stores them in localStorage, so the user remains authenticated for longer.

-- Slide 5 --
The I present Pool Management. 

Here the problem is practical: managers need to maintain the pools of the park and specify how many lifeguards each one requires.

The frontend shows a table with pool ID, name, and required lifeguards.

Managers can create, edit, and delete pools from the interface.

Deletion has a confirmation step, because removing a pool is a sensitive action.

On the backend, the page uses REST endpoints for pool CRUD operations.
(REST Endpoints = URL backend che frontend chiama per fare operazioni sui dati.)
CRUD = quattro operazioni base:

```text
Create -> creare
Read -> leggere
Update -> modificare
Delete -> eliminare
```

Nel Pool Management:

```text
GET /pools/all
```

legge tutte le piscine.

```text
POST /pools/create
```

crea nuova piscina.

```text
PUT /pools/update
```

modifica piscina esistente.

```text
DELETE /pools/delete/{id}
```

Those endpoints are role-protected, so only authorized users can modify pool data.