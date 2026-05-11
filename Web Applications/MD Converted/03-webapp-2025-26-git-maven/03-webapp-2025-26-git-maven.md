# 03-webapp-2025-26-git-maven

_Source: `03-webapp-2025-26-git-maven.pdf`_

## Slide 1 - Git and Maven

Git and Maven

Web Applications
Master Degree in Computer Engineering

Master Degree in Cybersecurity
Master Degree in ICT for Internet and Multimedia

Academic Year 2025/2026

Nicola Ferro

Intelligent Interactive Information Access (IIIA) Hub

## Slide 2 - Outline

Outline

Introduction to Git

Introduction to Maven

Use of Maven to compile, package, and document
applications

![Figura 1 dalla slide 2](assets/slide-002-fig-01.jpg)

## Slide 3 - Git

Git

![Figura 1 dalla slide 3](assets/slide-003-fig-01.jpg)

## Slide 4 - Git

Git

https://git-scm.com/

![Figura 1 dalla slide 4](assets/slide-004-fig-01.jpg)

## Slide 5 - Source Code Management

Source Code Management

A version control system manages the versions, called
revisions, of files and directories

it also manages conflicts, e.g. when the same file is edited concurrently,
and their resolution (merge)

Centralized approach (cvs, svn)

a single central repository manages all the versions of files and
directories, allowing us to keep track of all the changes over time

the client uses a local copy of the files and keeps the synchronisation
with the central repository

Distributed approach (git)

the local copy of every client is a complete repository

the synchronisation happens exchanging patches among peers

Code development is modelled ad a directed graph where, from
the main development line (master), alternative development
lines (branch) and/or stable versions (tag) can depart and join

![Figura 1 dalla slide 5](assets/slide-005-fig-01.jpg)

## Slide 6 - Git: Creation of a New Repository

Git: Creation of a New Repository

To create a new repository, create a new folder on your
disk and, within that folder, run

git init

To create a local copy of an existing repository (checkout)

git clone username@host:/path/to/repos

![Figura 1 dalla slide 6](assets/slide-006-fig-01.jpg)

## Slide 7 - Cloning an Empty Bitbucket Repository

Cloning an Empty Bitbucket Repository

![Figura 1 dalla slide 7](assets/slide-007-fig-01.jpg)

## Slide 8 - Cloning an Empty Bitbucket Repository

Cloning an Empty Bitbucket Repository

![Figura 1 dalla slide 8](assets/slide-008-fig-01.jpg)

## Slide 9 - Cloning an Empty Bitbucket Repository

Cloning an Empty Bitbucket Repository

![Figura 1 dalla slide 9](assets/slide-009-fig-01.jpg)

## Slide 10 - Workflow

Workflow

The local copy of a repository consists of three trees

Working directory: keeps the actual files and directories, which may or may
not be unversioned

Index: is a staging area

HEAD: represents the last commit made

![Figura 1 dalla slide 10](assets/slide-010-fig-01.jpg)

![Figura 2 dalla slide 10](assets/slide-010-fig-02.jpg)

## Slide 11 - Add and Commit

Add and Commit

You can add files/directories to the Index by

git add <filename>

You can confirm updates and add the to the HEAD by

git commit -m “Description”

You can send committed updates to a remote server by

git push origin master

master (or any other name) is the repository branch to send to the

remote server

origin indicates the default remote repository, e.g. the one from

which we cloned the repository

![Figura 1 dalla slide 11](assets/slide-011-fig-01.jpg)

## Slide 12 - Branch

Branch

Branches are used to develop independent features, e.g. new versions of
a software

The master branch is the default one when you create a new repository

The other branches may be merged into the master one when

appropriate

![Figura 1 dalla slide 12](assets/slide-012-fig-01.jpg)

![Figura 2 dalla slide 12](assets/slide-012-fig-02.jpg)

## Slide 13 - Branch Management

Branch Management

To create a new branch

git checkout -b <branch-name>

To get back to the master branch (or any other branch

name)

git checkout master

To send a branch to the remote repository

git push origin <branch-name>

![Figura 1 dalla slide 13](assets/slide-013-fig-01.jpg)

## Slide 14 - Update and Merge

Update and Merge

To update a local repository from a remote one

git pull origin <branch-name>

To merge a branch into the currently selected one

git merge <branch-name>

![Figura 1 dalla slide 14](assets/slide-014-fig-01.jpg)

## Slide 15 - Pull Requests

Pull Requests

Development platforms, such as GitHub and Bitbucket, provide pull
requests as a mechanism to foster collaboration among developers

Pull requests are a mechanism for a developer to notify team
members that they have completed a feature.

Once their feature branch is ready, the developer files a pull request.
This lets everybody involved know that they need to review and
discuss the code and, eventually, merge it into the master branch

![Figura 1 dalla slide 15](assets/slide-015-fig-01.jpg)

## Slide 16 - The .gitignore File

The .gitignore File

The .gitignore file has to be put in the root folder of

your development tree

It specifies intentionally untracked files that Git should
ignore

Each line in a .gitignore file specifies a pattern to be

matched to decide whether to exclude files and/or
directories

https://git-scm.com/docs/gitignore

![Figura 1 dalla slide 16](assets/slide-016-fig-01.jpg)

## Slide 17 - Example of .gitignore File

Example of .gitignore File

# IntelliJ Idea

# Package Files

*.iml

*.jar

.idea/

*.war

*.ear

*.zip

# Java

*.tar.gz

*.class

*.rar

target/

javadoc/

### OSX ###

log/

.DS_Store

![Figura 1 dalla slide 17](assets/slide-017-fig-01.jpg)

## Slide 18 - The README File

The README File

The README file has to be put in the root folder of your development tree

It provides overall information about your project which are displayed on its
Web page

you can use the Markdown syntax (https://bitbucket.org/tutorials/

markdowndemo) to format it

Example of README.md file

# Web Applications (webapp)

This directory contains the source code distribution complementing the lectures.

Web Applications lectures are held at:

* Master Degree in Computer Engineering
* Master Degree in ICT for Internet and Multimedia
* Master Degree in Cybersecurity

of the Department of Information Engineering, University of Padua, Italy

Copyright and license information can be found in the file LICENSE.
Additional information can be found in the file NOTICE.

![Figura 1 dalla slide 18](assets/slide-018-fig-01.jpg)

## Slide 19 - Examples of Code

Examples of Code

All the code examples are available in the following
Bitbucket repository

https://bitbucket.org/frrncl/webapp-unipd

You can clone it and pull from it as it gets updated

![Figura 1 dalla slide 19](assets/slide-019-fig-01.jpg)

## Slide 20 - Maven

Maven

![Figura 1 dalla slide 20](assets/slide-020-fig-01.jpg)

## Slide 21 - Maven

Maven

Maven, a Yiddish word meaning accumulator of knowledge, was originally started as an
attempt to simplify the build processes in the Jakarta Turbine project,  a servlet based
framework to build secure web applications.

Maven is a tool for managing Java software projects and supporting developers in keeping
track of the status of a project

build

dependency management

deployment and packaging

collaboration and documentation

Advantages

coherence: standardisation of the management of Java project, increased transparency and reduced
time to get an understanding of the different projects of an organisation;

reuse: similar projects can reuse and extend the setup of previous projects;

simplicity: simplification of the creation and integration of new components as well as of the sharing of
packages and executables. Moreover, the learning curve for each project is reduced;

maintenance: reduced effort and resources to keep building scripts as well as development and
deployment environments

## Slide 22 - Maven Homepage

Maven Homepage

http://maven.apache.org/

![Figura 1 dalla slide 22](assets/slide-022-fig-01.jpg)

## Slide 23 - Maven: Main Concepts

Maven: Main Concepts

Software development happens according to a life cycle made up

of  phases

Zero or more goals are associated to each phase and they are the

operations actually carried out in that phase

Goals are implemented by means of plugins and each plugin may

implement one or more goals

Phase 1

The Project Object Model (POM) is a single XML file which puts

Plugin 1

together, in a declarative way, phases, goals and plugins for a project

Plugin 1

Plugin 1

Goal A
Goal B
Goal C
Goal B

Phase 2

Goal D

Plugin 2

Plugin 1

Plugin 1

Goal B
Goal A

Phase 3

Plugin 3

Plugin 4

Goal E
Goal F

POM

Phase N

![Figura 1 dalla slide 23](assets/slide-023-fig-01.jpg)

## Slide 24 - Build Lifecycle

Build Lifecycle

A build lifecycle is needed to create, compile, integrate, test, and
distribute a software project

The phases of a lifecycle are executed in sequence to complete that
lifecycle

if you invoke an intermediate phase of a lifecycles, all the phases up to that
phase will be execute

if you invoke the last phase, all the phases will be executed

There are three predefined build lifecycles

clean: manages the cleaning of the project, i.e. it deletes all the files generated
by a build

default: manages the whole development of the project

site: manages the creation of a project site and of the documentation

## Slide 25 - The Default Build LifeCycle

The Default Build LifeCycle

Setup of the project

process-test-classes: post-processes the generated files from test
compilation, for example to do bytecode enhancement on Java classes

validate: validates the project is correct and all necessary information
is available.

test: runs tests using a suitable unit testing framework. These tests
should not require the code be packaged or deployed

initialize: initialize build state, e.g. set properties or create directories.

Packaging

Source processing

prepare-package: performs any operations necessary to prepare a
package before the actual packaging.

generate-sources: generates any source code for inclusion in
compilation

package: takes the compiled code and package it in its distributable
format, such as a JAR

process-sources: processes the source code, for example to filter any
values

Integration

generate-resources: generates resources for inclusion in the package

process-resources: copies and processes the resources into the
destination directory, ready for packaging

pre-integration-test: performs actions required before integration tests
are executed. This may involve things such as setting up the required
environment.

compile: compiles the source code of the project

integration-test: process and deploy the package if necessary into an
environment where integration tests can be run

process-classes: post-processes the generated files from
compilation, for example to do bytecode enhancement on Java classes

Testing

post-integration-test: performs actions required after integration tests
have been executed. This may including cleaning up the environment

Deployment

generate-test-sources: generates any test source code for inclusion
in compilation

verify: runs any checks to verify the package is valid and meets quality
criteria

process-test-sources: processes the test source code, for example
to filter any values

generate-test-resources: creates resources for testing

install: installs the package into the local repository, for use as a
dependency in other projects locally

process-test-resources: copies and processes the resources into the
test destination directory

deploy: done in an integration or release environment, copies the final
package to the remote repository for sharing with other developers and
projects

test-compile: compiles the test source code into the test destination
directory

![Figura 1 dalla slide 25](assets/slide-025-fig-01.jpg)

## Slide 26 - Default Build Lifecycle for JAR Packages

Default Build Lifecycle for JAR Packages

process-
resources

resources
resources

compile

compile
compiler

process-
test-resources

testResources
resources

test-compile

testCompile
compile

test

test
surﬁre

package

jar
jar

install

install
install

deploy

deploy
deploy

POM

![Figura 1 dalla slide 26](assets/slide-026-fig-01.jpg)

## Slide 27 - Project Object Model (POM)

Project Object Model (POM)

Project Object Model (POM)

Relationships
Build Settings

Build

Directories

Relationships: defines the structure of
the project (coordinates and modules), its
relationships with other projects
(inheritance), dependencies on other
projects and libraries

Coordinates
groupId
artifactId
version

Extensions

Multi-Module

Resources

Plugins

Inheritance

Dependencies

Reporting

General project information: maintains
general information about the project,
such as, project name, project Web site,
organization developing the project,
developers, licences

General Project Information
Build Environment

General

Environment Information

Contributors

Maven Environment

Build settings: customises the default
build lifecycle by adding goals and plugins
to the different phases as well as
information about source, test, and
resources

Proﬁles

Licenses

Build environment: defines profiles
corresponding to different environments
and/or operating systems

![Figura 1 dalla slide 27](assets/slide-027-fig-01.jpg)

## Slide 28 - Maven Repositories

Maven Repositories

Maven Central

Repository

Local
cache

Sonatype
Repository

Local
cache

…
Repository

Local
cache

![Figura 1 dalla slide 28](assets/slide-028-fig-01.jpg)

![Figura 2 dalla slide 28](assets/slide-028-fig-02.jpg)

![Figura 3 dalla slide 28](assets/slide-028-fig-03.jpg)

![Figura 4 dalla slide 28](assets/slide-028-fig-04.jpg)

## Slide 29 - Setting up Maven: the settings.xml file

Setting up Maven: the settings.xml file

The settings.xml file contains the overall configuration for
Maven

where to store the local cache for libraries and plugins

the configuration about a local repository, if any, and credentials to
access it

The settings.xml has to be saved in the .m2 folder in

each own home. If it does not already exist, you need to
create it

![Figura 1 dalla slide 29](assets/slide-029-fig-01.jpg)

## Slide 30 - Example of settings.xml

Example of settings.xml

<settings xmlns="http://maven.apache.org/SETTINGS/1.0.0"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://maven.apache.org/SETTINGS/1.0.0
http://maven.apache.org/xsd/settings-1.0.0.xsd">¬

<localRepository>/Users/ferro/.m2/repository</localRepository>
¬
</settings>¬

![Figura 1 dalla slide 30](assets/slide-030-fig-01.jpg)

## Slide 31 - Running Maven

Running Maven

mvn [options] [<goal(s)>] [<phase(s)>]

phase: one or more phase names according to the available build
lifecycles

remember that all the phases up to the selected one(s) will be executed

goal: one or more goal names to be executed

goal names have the following formata:
<plugin-name>:<goal-name>

For example, the following command

mvn clean deploy checkstyle:check

invokes the clean phase of the clean build lifecycle

invokes the deploy phase (and all the phases before it) of the default build lifecycle

invokes the check goal of the checkstyle plugin

![Figura 1 dalla slide 31](assets/slide-031-fig-01.jpg)

## Slide 32 - First Application without

First Application without

dependencies using

Maven

![Figura 1 dalla slide 32](assets/slide-032-fig-01.jpg)

## Slide 33 - Main Steps

Main Steps

Only once: configure the settings.xml file in the .m2

folder

Create a repository in Bitbucket for your application

Clone that repository on your local machine

add appropriate .gitignore and README/README.md files

Create the directory structure and POM file, add source
files, etc.

Build and package with Maven

generate Javadoc

Push to the repository

![Figura 1 dalla slide 33](assets/slide-033-fig-01.jpg)

## Slide 34 - Setup the Project Directory Structure

Setup the Project Directory Structure

src



development version

main



sources for the main application

database


sources for the database, e.g. schema creation SQL

java



sources for the Java application

resources

any additional application resource, e.g. property files

webapp


sources for the Web application, e.g. HTML, CSS, JS

test



sources for the test, e.g. JUnit

javadoc

documentation

target


folder for compiled code and packages

![Figura 1 dalla slide 34](assets/slide-034-fig-01.jpg)

## Slide 35 - Project Object Model (POM)

Project Object Model (POM)

<?xml version="1.0"?>

<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
 <modelVersion>4.0.0</modelVersion>

 <groupId>it.unipd.dei.webapp</groupId>

 <artifactId>hello-world</artifactId>

 <version>1.00</version>

 <packaging>jar</packaging>

 <!-- Project description elements -->
 <name>Hello World</name>

 <description>Writes "Hello, world!" on the console</description>

Coordinates of the project
• groupId: a unique id of the “producer” of the
project, e.g. the domain name of the company
• artifactId: the name of the project
• version: the version of the project
• packaging: how to package the project; jar for
desktop applications; war for web

 <url>http://www.dei.unipd.it/en/</url>

 <inceptionYear>2018</inceptionYear>

 <developers>
  <developer>
   <id>nf</id>
   <name>Nicola Ferro</name>
   <email>ferro@dei.unipd.it</email>
   <url>http://www.dei.unipd.it/~ferro/</url>
  </developer>
 </developers>

Various (optional) description elements about the
project, e.g. the year the project started, the
developers involved, the type of license, the

organization running the project

 <licenses>
  <license>
   <name>The Apache Software License, Version 2.0</name>
   <url>http://www.apache.org/licenses/LICENSE-2.0.txt</url>
   <distribution>repo</distribution>
  </license>
 </licenses>

 <organization>
  <name>Department of Information Engineering (DEI), University of Padua, Italy</name>
  <url>http://www.dei.unipd.it/en/</url>
 </organization>

![Figura 1 dalla slide 35](assets/slide-035-fig-01.jpg)

## Slide 36 - Project Object Model (POM)

Project Object Model (POM)

Project fi
<!-- Specifies the encoding to be used for project source files -->
<properties>
 <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
</properties>

Source input and compiled output
folders. You can omit these if you use the
default directory structure: convention

over confi

<!-- Configuration of the default build lifecycle -->
<build>
 <defaultGoal>compile</defaultGoal>
  <!-- source code folder -->
 <sourceDirectory>${basedir}/src/main/java</sourceDirectory>
  <!-- compiled code folder -->
 <directory>${basedir}/target</directory>
  <!-- name of the generated package -->
 <finalName>${project.artifactId}-${project.version}</finalName>

Name of the generated

jar/war package fi

Source code and generated
class fi

Confi
• reportOutputDirectory: where to write the
generated Javadoc
• author: whether to print the @author tag
• nosince: whether to print the @since tag
• show: the scope of methods/variables which has to
be reported

 <!-- configuration of the plugins for the different goals -->
 <plugins>
   <!-- compiler plugin: source and target code is for Java 1.8 -->
  <plugin>
   <groupId>org.apache.maven.plugins</groupId>
   <artifactId>maven-compiler-plugin</artifactId>
   <version>3.7.0</version>
   <configuration>
    <source>1.8</source>
    <target>1.8</target>
   </configuration>
  </plugin>
      <!-- javadoc plugin: output in the javadoc folder -->
  <plugin>
   <groupId>org.apache.maven.plugins</groupId>
   <artifactId>maven-javadoc-plugin</artifactId>
   <version>3.0.0</version>
   <configuration>
    <reportOutputDirectory>${basedir}/javadoc</reportOutputDirectory>
    <author>true</author>
    <nosince>false</nosince>
    <show>protected</show>
   </configuration>
  </plugin>
   </plugins>
</build>
project>

## Slide 37 - The HelloWorld Class

The HelloWorld Class

package it.unipd.dei.webapp;

/**
 * Sample class to say "Hello, world".
 *
 * @author Nicola Ferro  (ferro@dei.unipd.it)
 * @version 1.0
 * @since 1.0
 */
public class HelloWorld {

 /**
  * Main method of the class.
  *
  * Just prints "Hello, world!".
  *
  * @param args input arguments from the command line, if any.
  */
 public static void main(String[] args) {
    System.out.printf("Hello, world!%n");

 }

}

![Figura 1 dalla slide 37](assets/slide-037-fig-01.jpg)

## Slide 38 - Cleaning, Compiling, Packaging, Documenting, and Running

Cleaning, Compiling, Packaging, Documenting, and Running

![Figura 1 dalla slide 38](assets/slide-038-fig-01.jpg)

## Slide 39 - Cleaning, Compiling, Packaging, Documenting, and Running

Cleaning, Compiling, Packaging, Documenting, and Running

![Figura 1 dalla slide 39](assets/slide-039-fig-01.jpg)

## Slide 40 - Cleaning, Compiling, Packaging, Documenting, and Running

Cleaning, Compiling, Packaging, Documenting, and Running

![Figura 1 dalla slide 40](assets/slide-040-fig-01.jpg)

## Slide 41 - Cleaning, Compiling, Packaging, Documenting, and Running

Cleaning, Compiling, Packaging, Documenting, and Running

![Figura 1 dalla slide 41](assets/slide-041-fig-01.jpg)

## Slide 42 - First Application with

First Application with

dependencies using

Maven

![Figura 1 dalla slide 42](assets/slide-042-fig-01.jpg)

## Slide 43 - JFigLet

JFigLet

https://github.com/dtmo/jfiglet

![Figura 1 dalla slide 43](assets/slide-043-fig-01.jpg)

## Slide 44 - The HelloWorldFigLet Class

The HelloWorldFigLet Class

// name of the font to be used¬
final String font;¬
¬

Print help and exit, if
the are no arguments

// "parse" the command line and set the proper Figlet font name or throw an error¬
switch (args[0].trim().toLowerCase()) {¬

case "banner":¬

font = FigFontResources.BANNER_FLF;¬
break;¬
case "big":¬

¬
package it.unipd.dei.webapp;¬
¬
import com.github.dtmo.jfiglet.FigFontResources;¬
import com.github.dtmo.jfiglet.FigletRenderer;¬
¬
import java.io.IOException;¬
¬
public class HelloWorldFiglet {¬
¬

public static void main(String[] args) throws IOException {¬
¬

font = FigFontResources.BIG_FLF;¬
break;¬
case "block":¬

if (args.length == 0) {¬

Name of the Figlet
font to be used and
“parsing” of the

font = FigFontResources.BLOCK_FLF;¬
break;¬
case "bubble":¬

command line

font = FigFontResources.BUBBLE_FLF;¬
break;¬
case "digital":¬

font = FigFontResources.DIGITAL_FLF;¬
break;¬
case "ivrit":¬

font = FigFontResources.IVRIT_FLF;¬
break;¬
case "lean":¬

font = FigFontResources.LEAN_FLF;¬
break;¬
case "mini":¬

font = FigFontResources.MINI_FLF;¬
break;¬
case "mnemonic":¬

System.out.printf("Please, pick on of the following Figlet fonts:%n");¬
System.out.printf("- Banner%n");¬
System.out.printf("- Big%n");¬
System.out.printf("- Block%n");¬
System.out.printf("- Bubble%n");¬
System.out.printf("- Digital%n");¬
System.out.printf("- Ivrit%n");¬
System.out.printf("- Lean%n");¬
System.out.printf("- Mini%n");¬
System.out.printf("- Mnemonic%n");¬
System.out.printf("- Script%n");¬
System.out.printf("- Shadow%n");¬
System.out.printf("- Slant%n");¬
System.out.printf("- Small%n");¬
System.out.printf("- SmScript%n");¬
System.out.printf("- SmShadow%n");¬
System.out.printf("- SmSlant%n");¬
System.out.printf("- Standard%n");¬
System.out.printf("- Terminal%n");¬
¬

font = FigFontResources.MNEMONIC_FLF;¬
break;¬
case "script":¬

System.exit(0);¬
}¬
¬

font = FigFontResources.SCRIPT_FLF;¬
break;¬
case "shadow":¬

font = FigFontResources.SHADOW_FLF;¬
break;¬
case "slant":¬

font = FigFontResources.SLANT_FLF;¬
break;¬
case "small":¬

font = FigFontResources.SMALL_FLF;¬
break;¬
case "smscript":¬

font = FigFontResources.SMSCRIPT_FLF;¬
break;¬
case "smshadow":¬

font = FigFontResources.SMSHADOW_FLF;¬
break;¬
case "smslant":¬

Create a new Figlet renderer,
render the “Hello, world!” string,

font = FigFontResources.SMSLANT_FLF;¬
break;¬
case "standard":¬

and print it to the terminal

font = FigFontResources.STANDARD_FLF;¬
break;¬
case "terminal":¬

font = FigFontResources.TERM_FLF;¬
break;¬
default:¬

throw new IllegalArgumentException("Invalid Figfont: " + args[0]);¬
}¬
¬

// render to write ASCII-art with the given font¬
final FigletRenderer figletRenderer = new FigletRenderer(FigFontResources.loadFigFontResource(font));¬
¬

// ASCII-art¬
final String output = figletRenderer.renderText("Hello, world!");¬
¬

// write to the console¬
System.out.printf("%s%n", output);¬
¬

## Slide 45 - Looking for the JFiglet Library Dependency

Looking for the JFiglet Library Dependency

http://search.maven.org/

![Figura 1 dalla slide 45](assets/slide-045-fig-01.jpg)

## Slide 46 - Looking for the JFiglet Library Dependency

Looking for the JFiglet Library Dependency

http://search.maven.org/

![Figura 1 dalla slide 46](assets/slide-046-fig-01.jpg)

## Slide 47 - Looking for the JFiglet Library Dependency

Looking for the JFiglet Library Dependency

http://search.maven.org/

![Figura 1 dalla slide 47](assets/slide-047-fig-01.jpg)

## Slide 48 - The Updated POM File

The Updated POM File

¬

The name of the jar fi

<!-- generates jar files including any dependencies -->¬
<plugin>¬

<artifactId>maven-assembly-plugin</artifactId>¬
<version>3.3.0</version>¬
<configuration>¬

<descriptorRefs>¬

<descriptorRef>jar-with-dependencies</descriptorRef>¬
</descriptorRefs>¬
</configuration>¬
<executions>¬

<execution>¬

<id>make-assembly</id> <!-- this is used for inheritance merges -->¬
<phase>package</phase> <!-- bind to the packaging phase -->¬
<goals>¬

Binds the single goal of the maven-
assembly-plugin to the package phase

of the default build lifecycle

<goal>single</goal> <!-- the only goal of the assembly plugin -->¬
</goals>¬
</execution>¬
</executions>¬
</plugin>¬
¬
</plugins>¬
</build>¬
¬

<!-- Dependencies -->¬
<dependencies>¬

<dependency>¬

Adds the dependency on
the JFiglet library

<groupId>com.github.dtmo.jfiglet</groupId>¬
<artifactId>jfiglet</artifactId>¬
<version>1.0.1</version>¬
</dependency>¬
</dependencies>¬
</project>

## Slide 49 - Cleaning, Compiling, Packaging, Documenting, and Running

Cleaning, Compiling, Packaging, Documenting, and Running

![Figura 1 dalla slide 49](assets/slide-049-fig-01.jpg)

## Slide 50 - Cleaning, Compiling, Packaging, Documenting, and Running

Cleaning, Compiling, Packaging, Documenting, and Running

![Figura 1 dalla slide 50](assets/slide-050-fig-01.jpg)

## Slide 51 - Cleaning, Compiling, Packaging, Documenting, and Running

Cleaning, Compiling, Packaging, Documenting, and Running

![Figura 1 dalla slide 51](assets/slide-051-fig-01.jpg)

## Slide 52 - Cleaning, Compiling, Packaging, Documenting, and Running

Cleaning, Compiling, Packaging, Documenting, and Running

![Figura 1 dalla slide 52](assets/slide-052-fig-01.jpg)

![Figura 2 dalla slide 52](assets/slide-052-fig-02.jpg)

![Figura 3 dalla slide 52](assets/slide-052-fig-03.jpg)
