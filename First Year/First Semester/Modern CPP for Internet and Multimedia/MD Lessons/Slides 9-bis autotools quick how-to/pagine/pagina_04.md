Top-level Makefile.am

AUTOMAKE_OPTIONS = foreign # it tells automake that the project will not follow GNU standards. Use it always, otherwise you need to deal with several txt files of the gnu standard, such as ChangeLog, README, NEWS, etc.

SUBDIRS = m4 \
basic_utilities \
example

it tells Automake which subdirectories are to be built, specifically: m4 and basic_utilities and example. “\” tells to escape the new line.

if WITH_TEST # if WITH_TEST is enabled,
SUBDIRS += \
test/bu_test # it adds test/bu_test folder to SUBDIR and
TESTS = \
test/bu_test/bu_test# it executes test/bu_test/bu_test when testing endif

ACLOCAL_AMFLAGS = -I m4 # it tells Autotools to store libtool configuration macros in the m4 folder

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p04_img01.jpg)
