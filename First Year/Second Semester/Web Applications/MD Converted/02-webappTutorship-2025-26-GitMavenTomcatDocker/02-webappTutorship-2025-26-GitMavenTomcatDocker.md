# 02-webappTutorship-2025-26-GitMavenTomcatDocker

_Source: `02-webappTutorship-2025-26-GitMavenTomcatDocker.pdf`_

## Slide 1 - Tutoring 02

Tutoring 02
Git, Maven, Tomcat & Docker

Francesco L. De Faveri

Web Applications Tutoring

Academic Year: 2025-2026

![Figura 1 dalla slide 1](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/13-webapp-2025-26-css/assets/slide-001-fig-01.jpg)

## Slide 2 - Outline

Outline

●
Git

●
Maven

●
Tomcat

●
Docker

![Figura 1 dalla slide 2](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-002-fig-01.jpg)

## Slide 3 - General Information for HW1

General Information for HW1

Tools for mockups:

Tools for ER schema, Logical
schema or diagrams:

●
https://draw.io/

●
https://balsamiq.cloud/
(30 days of free trial)

●
https://www.lucidchart.com/

●
https://draw.io/

![Figura 1 dalla slide 3](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/02-webappTutorship-2025-26-GitMavenTomcatDocker/assets/slide-003-fig-01.jpg)

![Figura 2 dalla slide 3](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/02-webappTutorship-2025-26-GitMavenTomcatDocker/assets/slide-003-fig-02.jpg)

![Figura 3 dalla slide 3](assets/slide-003-fig-03.jpg)

## Slide 4 - Git

Git

![Figura 1 dalla slide 4](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/13-webapp-2025-26-css/assets/slide-004-fig-01.jpg)

## Slide 5 - GIT

GIT

Git is a Distributed Version Control System (DVCS) used for tracking changes in source code during
software development.

Git allows:

●
collaboration
●
changes tracking
●
code sharing

Key features:

●
Version control
●
Distributed development
●
Branching
●
Merging

If you need to download git: https://git-scm.com/downloads

Linus Torvalds

![Figura 1 dalla slide 5](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/02-webappTutorship-2025-26-GitMavenTomcatDocker/assets/slide-005-fig-01.jpg)

## Slide 6 - Why GIT?

Why GIT?

Why using git instead of a shared “standard” repository (e.g. Google Drive)?

●
Deep integration with both IDEs and Shell → easy to use everywhere
(even on servers)

●
“Explicit” tracking of changes → easy to compare versions and revert
errors

Therefore, even if you work on a project on your own and you use
multiple PCs it can be useful to use git. (Learn it well for your future job!)

![Figura 1 dalla slide 6](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-006-fig-01.jpg)

## Slide 7 - GIT & Bitbucket Repositories

GIT & Bitbucket Repositories

Steps to clone a Bitbucket repository:

1.
Open the desired repository
(e.g., the one that the professor assigned to your group)

2.
Click on the clone button and copy the instruction

3.
Choose the local folder where you want to store the cloned repository.

4.
Open a new terminal in that folder and paste the copied instruction.

** Windows users: it is strongly suggested to execute git commands through GIT
BASH. GIT BASH is a shell that is installed automatically when you install git.

Otherwise, use it through the
integration via your favourite IDE

![Figura 1 dalla slide 7](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-007-fig-01.jpg)

## Slide 8 - Cloning the TA Web App Repository

Cloning the TA Web App Repository

![Figura 1 dalla slide 8](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/02-webappTutorship-2025-26-GitMavenTomcatDocker/assets/slide-008-fig-01.jpg)

## Slide 9 - GIT - commit

GIT - commit

Git comprises of 3 “components”:

Working Repository → The directory on your local computer where you are currently working with Git.
It is the directory that contains the ﬁles and directories of your project, and it represents the current
state of your project.

INDEX (Staging Area) → When you make changes to ﬁles in your working directory, those changes are
not immediately committed to the repository. They are ﬁrst added to the staging area where can be
reviewed and organized. The staging area allows you to selectively add changes to the snapshot, rather
than committing all changes at once. This is useful for when you want to commit only certain changes
that are related to a speciﬁc feature or bug ﬁx.

HEAD → A reference to the most recent commit in the current branch of the repository. It points to the
commit that represents the current state of the repository. HEAD is essentially a pointer to a speciﬁc
commit in the repository's commit history.

![Figura 1 dalla slide 9](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/13-webapp-2025-26-css/assets/slide-009-fig-01.jpg)

## Slide 10 - Git commit

Git commit

The overall workﬂow is the following:

1.
Up to the commit step, everything is local on your computer.
2.
However, the commit operation takes the ﬁles as they are in the staging area and
stores that snapshot permanently to your Git directory
3.
Push actually uploads the ﬁles to the remote repository.
4.
Pull synchronizes the content of your local repository with the remote repository

![Figura 1 dalla slide 10](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/02-webappTutorship-2025-26-GitMavenTomcatDocker/assets/slide-010-fig-01.jpg)

![Figura 2 dalla slide 10](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/05-webapp-2025-26-servlet/assets/slide-010-fig-02.jpg)

## Slide 11 - Branch

Branch

In your homework you will work in parallel with your colleagues, developing
different features.

Sometimes it is useful to create separate branches (one for each major
feature) to avoid interfering with your mate’s work.

To do this:

git checkout -b <branchname> #creates a branch

git checkout <branchname> #switches to the branch

Remember: at the end of your project all the branches must be merged to
the main branch.

![Figura 1 dalla slide 11](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-011-fig-01.jpg)

## Slide 12 - Branch

Branch

git merge <branchname> #merges the branch <branchname> with the
current one

git merge --abort  #aborts the merge

If different people updated the same ﬁles on different branches, when
you merge them conﬂicts arise. You will need to solve them

Branches can have a complex structure.

However there exist a single main branch. Pay attention when you create
and merge branches.

![Figura 1 dalla slide 12](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-012-fig-01.jpg)

## Slide 13 - Branch

Branch

Other commands:

git branch
 #lists all the branches

git branch <branchname> #creates a branch, same as “git checkout -b”

git branch -d <branchname> #deletes a branch LOCALLY

git push origin --delete <branchname> #deletes a branch REMOTELY

![Figura 1 dalla slide 13](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-013-fig-01.jpg)

## Slide 14 - Pull

Pull

To align the content of your local repository with the remote
repository (e.g., if others already did some work) you can use the
command:

git pull  #pulls every branch

If you work on separate branches (e.g., one for each group
component) you can also pull single branches:

git pull origin <branchname>  #pulls only the speciﬁed branch

![Figura 1 dalla slide 14](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/13-webapp-2025-26-css/assets/slide-014-fig-01.jpg)

## Slide 15 - Add

Add

Once you created/modiﬁed some ﬁles you need to commit them and
upload them.

1.
ADD

○
 Add single ﬁles, they must be separated by single spaces:
git add <ﬁle_1> <ﬁle_2> …. <ﬁle_n> #adds single ﬁles

○
Add ﬁles that are NOT at the same level of root:
git add /path/to/ﬁle/<ﬁlename> #add a single ﬁles in a folder

○
Add all the ﬁles
git add .  #adds all the changes

![Figura 1 dalla slide 15](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-015-fig-01.jpg)

## Slide 16 - Commit

Commit

Step 2.

git commit -m “message” #commits the changes to ALL the added
ﬁles (also before)

It is important to include a message on your commits. This allows to
properly keep track of the changes.

TIP: avoid non-explanatory commits like “update”, “new ﬁles”, etc. It is
better if the commits contains also infos about who performed it

NOTE: always pull before committing

![Figura 1 dalla slide 16](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-016-fig-01.jpg)

## Slide 17 - Push

Push

Step 3.

git push origin <branchname>  #uploads the modiﬁcations to the desired
branch

git push origin master  #uploads the modiﬁcations to the master branch

git push --all origin #uploads all the modiﬁcations

Git push actually uploads the local changes to the remote repository.

Until you do not push, your colleagues will not be able to see your changes.

![Figura 1 dalla slide 17](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-017-fig-01.jpg)

## Slide 18 - What you have to do for Web App Dev

What you have to do for Web App Dev

In general, the steps that you have to perform when developing
your web application are:

1.
clone
git clone
2.
pull (and solve conﬂicts, if present)
git pull
3.
add (if you created or modiﬁed ﬁles)
git add .
4.
commit (pull just before commit to avoid conﬂicts)
git commit -m “message”
5.
push
git push origin <branch>

![Figura 1 dalla slide 18](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-018-fig-01.jpg)

## Slide 19 - .gitignore

.gitignore

A gitignore ﬁle speciﬁes intentionally untracked ﬁles that Git
should ignore. Files already tracked by Git are not affected.

Each line in a gitignore ﬁle speciﬁes a pattern.
For example, you want to avoid tracking ﬁles in preliminary examples.

![Figura 1 dalla slide 19](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/02-webappTutorship-2025-26-GitMavenTomcatDocker/assets/slide-019-fig-01.jpg)

![Figura 2 dalla slide 19](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/04-webapp-2025-26-docker/assets/slide-019-fig-02.jpg)

## Slide 20 - Tips

Tips

If you use separate branches (e.g. one for each group member) do not
merge them only at the end, otherwise many conﬂicts may arise. Try to
merge them each time that you implement something signiﬁcant.

●
Pull each time when you start working AND before performing a
commit. This will reduce the number of conﬂicts and will make it easier
to solve them.
●
When you clone, if the repository is private you will be required to
provide your credentials. We suggest to use App Passwords:
https://support.atlassian.com/bitbucket-cloud/docs/app-passwords/

![Figura 1 dalla slide 20](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-020-fig-01.jpg)

## Slide 21 - Git on IDE (IntelliJ)

Git on IDE (IntelliJ)

![Figura 1 dalla slide 21](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/02-webappTutorship-2025-26-GitMavenTomcatDocker/assets/slide-021-fig-01.jpg)

![Figura 2 dalla slide 21](slide-021-fig-02.jpg)

## Slide 22 - Maven

Maven

![Figura 1 dalla slide 22](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-022-fig-01.jpg)

## Slide 23 - Maven

Maven

Apache Maven is a build automation and project management tool used primarily
for Java projects. It provides a standard way to build and manage Java-based
projects and their dependencies.

Maven uses a Project Object Model (POM) ﬁle to describe the project and its
dependencies, as well as the build process and any plugins that are needed. It
manages dependencies and builds the project, including compiling source code,
packaging artifacts, running tests, and generating documentation.

Maven also provides a set of standard lifecycle phases, such as compile, test,
package, and install, which deﬁne a common build process for all Maven-based
projects. This helps ensure consistency across projects and makes it easier for
developers to work with different ones.

![Figura 1 dalla slide 23](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-023-fig-01.jpg)

## Slide 24 - Lifecycle

Lifecycle

●
clean: Cleans the project by removing any previously
generated build artifacts, such as compiled classes and
packaged ﬁles.
●
validate: Validates the project conﬁguration, ensuring that it
is correct and all necessary information is available.
●
compile: Compiles the project's source code into bytecode,
typically stored in the target/classes directory.
●
test: Runs the project's tests using a suitable testing
framework.

![Figura 1 dalla slide 24](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-024-fig-01.jpg)

## Slide 25 - Lifecycle

Lifecycle

●
package: Packages the compiled code and resources into a
distributable format, such as a JAR, WAR, or ZIP ﬁle.
●
verify: Performs checks on the packaged artifact to ensure
its integrity and quality.
●
install: Installs the packaged artifact into the local Maven
repository, making it available for use by other projects on
the same machine.
●
deploy: Copies the packaged artifact to a remote repository.

![Figura 1 dalla slide 25](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-025-fig-01.jpg)

## Slide 26 - Dependencies

Dependencies

Where to ﬁnd the dependencies to add to your pom.xml?

Maven Repository: https://central.sonatype.com/

![Figura 1 dalla slide 26](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/02-webappTutorship-2025-26-GitMavenTomcatDocker/assets/slide-026-fig-01.jpg)

## Slide 27 - Before starting

Before starting

Remember that you can change the folder in which maven
stores the dependencies indicated in the pom.xml

To do so you just need to change the ﬁle settings.xml in the .m2
folder (in your home)

If you do not have the settings.xml ﬁle in your .m2 folder you
can copy, paste and modify the following:

https://bitbucket.org/frrncl/webapp-unipd/src/master/maven-setup/

![Figura 1 dalla slide 27](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-027-fig-01.jpg)

## Slide 28 - pom.xml

pom.xml

The pom ﬁle is an xml ﬁle that contains conﬁguration information about the project
and its dependencies.

●
Project information: such as groupid, artifactid, project and version.

●
Dependencies: external libraries or modules that the project relies on. Maven
uses this information to download the necessary libraries from remote
repositories and include them in the project's build process.

●
Build conﬁguration: how the project should be built. It includes settings for
compiling source code, running tests, packaging the project into distributable
formats.

●
Plugins: Maven plugins are extensions that provide additional functionality to the
build process.

![Figura 1 dalla slide 28](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-028-fig-01.jpg)

## Slide 29 - Example

Example

![Figura 1 dalla slide 29](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/02-webappTutorship-2025-26-GitMavenTomcatDocker/assets/slide-029-fig-01.jpg)

## Slide 30 - Setting Up Project in IntelliJ

Setting Up Project in IntelliJ

NOTE: if you start from an existing
project (e.g., professor’s examples)
when you open it the ﬁrst time a
message will appear asking you if
IntelliJ needs to open the project as
a maven project.

![Figura 1 dalla slide 30](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/02-webappTutorship-2025-26-GitMavenTomcatDocker/assets/slide-030-fig-01.jpg)

## Slide 31 - Usage

Usage

Once installed maven, you can use it:

●
From the command line: place yourself in the project folder
and run mvn clean package javadoc:javadoc
●
From IntelliJ, open the right Maven panel and select the
phase you want to run.

![Figura 1 dalla slide 31](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/02-webappTutorship-2025-26-GitMavenTomcatDocker/assets/slide-031-fig-01.jpg)

## Slide 32 - Tomcat

Tomcat

![Figura 1 dalla slide 32](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-032-fig-01.jpg)

## Slide 33 - Setup

Setup

Tomcat is a web server you use to deploy
the war ﬁle. Apache Tomcat is an
open-source web server and servlet
container for running Java applications.

Download:
https://tomcat.apache.org/download-11.cgi

Suggestion: Follow the procedure for
Linux/MacOS also for Windows

![Figura 1 dalla slide 33](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/02-webappTutorship-2025-26-GitMavenTomcatDocker/assets/slide-033-fig-01.jpg)

![Figura 2 dalla slide 33](slide-033-fig-02.jpg)

## Slide 34 - Setup

Setup

Once downloaded:

1.
Unzip the downloaded folder

2.
Go to %TOMCAT_HOME%/conf and open the
“tomcat-users.xml” ﬁle in my case
%TOMCAT_HOME% = kdf/Download/apache-tomcat-11.0.18

![Figura 1 dalla slide 34](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-034-fig-01.jpg)

## Slide 35 - Setup

Setup

3. “Create” your account.

Roles:

manager-gui: allows access to the HTML GUI and the status pages
manager-script: allows access to the text interface and the status
pages
manager-jmx: allows access to the JMX proxy and the status pages
manager-status: allows access to the status pages only

Suggestion: create your account with the role “manager-gui”

![Figura 1 dalla slide 35](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-035-fig-01.jpg)

## Slide 36 - Setup

Setup

4. Open a terminal in the folder %TOMCAT_HOME%/bin and run

chmod +x *.sh

5. To start the server: Open a terminal in the folder %TOMCAT_HOME%/bin and run

./startup.sh

6. To stop the server: Open a terminal in the folder %TOMCAT_HOME%/bin and run

./shutdown.sh

![Figura 1 dalla slide 36](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/13-webapp-2025-26-css/assets/slide-036-fig-01.jpg)

## Slide 37 - If everything went ok

If everything went ok

To start using tomcat:

●
Open your browser and go to http://localhost:8080/
●
Click on manager App
●
Login with the credentials you set in the tomcat-users.xml
ﬁle

![Figura 1 dalla slide 37](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/02-webappTutorship-2025-26-GitMavenTomcatDocker/assets/slide-037-fig-01.jpg)

## Slide 38 - After Logging…

After Logging…

![Figura 1 dalla slide 38](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/02-webappTutorship-2025-26-GitMavenTomcatDocker/assets/slide-038-fig-01.jpg)

## Slide 39 - Docker

Docker

![Figura 1 dalla slide 39](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-039-fig-01.jpg)

## Slide 40 - Containerization

Containerization

Containerizing means creating a software container, which is an
isolated and self-suﬃcient environment where an application
can run consistently, regardless of the operating system or
environment in which it is executed.

Advantages:

●
Portability
●
Eﬃciency
●
Scalability
●
Isolation

![Figura 1 dalla slide 40](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/02-webappTutorship-2025-26-GitMavenTomcatDocker/assets/slide-040-fig-01.jpg)

## Slide 41 - Dockerﬁles & Images

Dockerﬁles & Images

The dockerﬁles are the recipes to create the docker images.

Remember that docker images are immutable.

![Figura 1 dalla slide 41](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/02-webappTutorship-2025-26-GitMavenTomcatDocker/assets/slide-041-fig-01.jpg)

## Slide 42 - Docker Containers

Docker Containers

Docker containers can be seen as running instances of the
docker images.

A docker container may rely on multiple images.

The same image can be shared by multiple containers within
the same host.

![Figura 1 dalla slide 42](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/02-webappTutorship-2025-26-GitMavenTomcatDocker/assets/slide-042-fig-01.jpg)

## Slide 43 - Docker Volumes

Docker Volumes

A Docker volume is a mechanism for persistently storing data
generated by and accessed by the docker containers. A volume
provides a way to share and manage data between the host
machine and the containers.

Docker volumes are stored outside the container can be used to
store databases, conﬁguration ﬁles, logs, and any other data that
needs to persist beyond the lifecycle of a container.

![Figura 1 dalla slide 43](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-043-fig-01.jpg)

## Slide 44 - Download

Download

Download links & installation guidelines:

Docker: https://docs.docker.com/get-docker/

Docker compose: https://docs.docker.com/compose/

![Figura 1 dalla slide 44](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-044-fig-01.jpg)

## Slide 45 - Docker - In Our Case

Docker - In Our Case

Each service runs one
image

This is a
docker-compose.yml
ﬁle

![Figura 1 dalla slide 45](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/02-webappTutorship-2025-26-GitMavenTomcatDocker/assets/slide-045-fig-01.jpg)

## Slide 46 - Docker - In Our Case

Docker - In Our Case

Each service runs one
image

Two services
web & db

![Figura 1 dalla slide 46](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/02-webappTutorship-2025-26-GitMavenTomcatDocker/assets/slide-046-fig-01.jpg)

## Slide 47 - Docker - In Our Case

Docker - In Our Case

Tomcat will host our
web application

Postgres will hold the
data of our web
application

![Figura 1 dalla slide 47](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/02-webappTutorship-2025-26-GitMavenTomcatDocker/assets/slide-047-fig-01.jpg)

## Slide 48 - Docker - In Our Case

Docker - In Our Case

The image is tomcat:latest

●
Tomcat will host our web application
●
We map port 8080 within the container to
our 8081 local port

We set a volume, in this case, a ﬁle.
Pattern: local_path:container_path
The ﬁle will be copied from the local directory to
the container internal directory structure.

![Figura 1 dalla slide 48](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/02-webappTutorship-2025-26-GitMavenTomcatDocker/assets/slide-048-fig-01.jpg)

![Figura 2 dalla slide 48](slide-048-fig-02.jpg)

## Slide 49 - Docker - In Our Case

Docker - In Our Case

The image is postgres

We map the port 5432 within the container to
our 5433 local port

Setting environment variables. In this case,
for postgres authentication

We set a volume, in this case, a directory.
Files will be copied from the local directory to
the container directory and the other way
around.

![Figura 1 dalla slide 49](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/02-webappTutorship-2025-26-GitMavenTomcatDocker/assets/slide-049-fig-01.jpg)

## Slide 50 - Docker - In Our Case

Docker - In Our Case

Adding dependencies between
services

NOTE: the condition is needed
since normally the
dependencies are instantiated
as soon as the services are
running

In our case we want the
dependency to be instantiated
when the db is ready
(“healthy”)

Health check to

understand
when the db is up and

running

![Figura 1 dalla slide 50](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/02-webappTutorship-2025-26-GitMavenTomcatDocker/assets/slide-050-fig-01.jpg)

## Slide 51 - Docker - In Our Case

Docker - In Our Case

What if we also want to initialize our database starting from a “.sql” ﬁle that
contains our database schema?

We need to add a new volume to the db service:

●
 ./data/schema.sql:/docker-entrypoint-initdb.d/init.sql

Important notes:

●
Pay attention to the paths, they are relative to the folder which contain your
docker-compose.yml ﬁle
●
In the shown example the we mapped the container “standard” ports to
different local ports. This is needed because the “standard” ports might be
already used (e.g., if you already installed postgres locally).

![Figura 1 dalla slide 51](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-051-fig-01.jpg)

## Slide 52 - Docker Commands

Docker Commands

Execute these command in the same folder containing the yml ﬁle

●
creating and starting the container
docker compose up
●
stopping the container
docker compose down
●
list the containers
docker ps
●
Connect to DB in a container, if the container name is <my_container>
Docker exec -it my_container psql -U postgres

![Figura 1 dalla slide 52](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/07-Webapp-2025-26-jsp/assets/slide-052-fig-01.jpg)

## Slide 53 - Final Remark on HW1

Final Remark on HW1

![Figura 1 dalla slide 53](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/13-webapp-2025-26-css/assets/slide-053-fig-01.jpg)

## Slide 54 - README in the Group Repository

README in the Group Repository

Your bitbucket repository should contain a README.md ﬁle that describes the main
structure and contents.

These information include:

●
Installation and setup procedures, main features of the software, contributors
(I suggest you to also report here the contributions of the report, for the features of the
web app try to summarise in few lines, and be speciﬁc on the installation and setup)

To write the README you should use the markdown language which is quite simple and
intuitive.

You can ﬁnd the syntax here: https://www.markdownguide.org/basic-syntax/

![Figura 1 dalla slide 54](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/02-webappTutorship-2025-26-GitMavenTomcatDocker/assets/slide-054-fig-01.jpg)
