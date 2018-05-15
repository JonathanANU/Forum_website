# COMP1040 Group Project
Semester 2, 2016

This `README.md` document describes the project requirements and method of assessment.
Please read through the entire document carefully.

_The group project is worth **40%** of your course grade._

## Academic Honesty and Integrity

Honesty and integrity are of utmost importance. These goals are *not* at odds with
being resourceful and working collaboratively. You *should* be resourceful, you
should collaborate within your team, and you should discuss the assignment and
other aspects of the course with others taking the class. However, *you must never
misrepresent the work of others as your own*. If you have taken ideas from elsewhere
or used code sourced from elsewhere, you must say so with *utmost clarity*. At the
completion of your project you will be asked to submit a statement of originality.
This statement is the place for you to declare which ideas or code contained in
your submission were sourced from elsewhere.

Please read the ANU's [official position](http://academichonesty.anu.edu.au/) on
academic honesty. If you have any questions, please ask.

Carefully review the [statement of originality](ORIGINALITY.md) and [statement of
contributions](CONTRIBUTION.md) both of which you must edit as you complete your
project, ensuring that a truthful statement is committed and pushed to your repo.

## Overview

The group project is an opportunity for you to put your _craft of computing_
skills into practice on an interesting problem of your choosing. Projects
should be done in groups of 2-5 people. If you do not have a group by
the proposal deadline we will assign one to you. _You cannot work on the
group project alone._

Projects should have the flavour of what we have been doing in the course. That is,
they need to involve some sort of data processing and analysis or simulation, and
some form of visualisation. Apart from that, the projects can be very open ended
and you are free to propose anything that interests you. We will provide feedback
on projects that we think are either too ambitious, too simple, or otherwise
inappropriate. You can even choose to do your project in a different programming
language, but will need to provide a convincing argument as to why this is a good
idea.

As a guideline each group member should be spending 5-6 hours per week on the
project. Taking into account some project management overhead, we would expect
the scope of the project to be equivalent to approximately two assignments.

## Project Management

Your project should be managed using a GitLab repository. We will be
looking for activity from all group members in terms of code commits
and the use of the issue tracking system. You may also choose to
include a `MEETINGS.md` file to keep a record of meeting minutes or
make use of the GitLab wiki feature. You may also want to think about
the role of each group member and assign tasks accordingly.

## Project Repository Setup

At the start of the project, one group member must fork this
repository in GitLab and add the other group members as members of the
project with `Master` project access. You should also make sure that
the `comp1040-marker-2016` user is a member of the project with `Developer`
access. And finally, check that the project's visibility is set to
`Private`.  While one group member is the designated owner of the
repository, it is every group member's responsibility to contribute to
the project and make sure that the repo is setup correctly.

It is important that you do not change the project name. Our automatic
grading scripts rely on being able to find the project based on its
name and if you change it you will receive zero marks for the project.

Once the repo is setup each project member should be able to clone a local copy.
You must add a `PROPOSAL.md` file by the project proposal deadline (see below).
Don't forget to _commit_ and _push_ this file. The repository already has templates
for the statement of contributions and statement of originality that must be
completed for the milestone and final submission. These are `CONTRIBUTION.md`
and `ORIGINALITY.md`, respectively.

All code related to the project must be committed and pushed to the GitLab
repository on a regular basis.

**Do not** commit large datasets to your repository. This is not necessary if
the data is publicly available from another source. A better option is to
include a `NOTES.md` file with instructions on how to obtain the data or, even
better, a script for automatically downloading the data.

## Project Proposal

By **Friday, 23 September** you must have have setup your repository
and added a project proposal (`PROPOSAL.md`). The project proposal
must include (under the headings specified):

- Title
 - The title of the project
- Group Members
 - List of group members (names and university IDs)
- Overview
 - A 2-3 paragraph overview of what the project is about and
   what will be delivered at the end of the semester.
- Data
 - A description of where you will get your data.
- Milestones
 - A brief list of milestones (with dates) for tasks that you
   aim to achieve towards delivery of your project.
- Programming Language
 - The programming language that you will use for the project.
 - A strong justification must be given if the language is not Python.
- References
 - Any preliminary references that may be relevant for your project.

## Code and Final Report

Your project must be completed by **Friday, 28 October**. By this
date your repository should include:

- a working version of your code in the `master` branch
- an updated `NOTES.md` file explaining how to run your code
- completed `CONTRIBUTION.md` and `ORIGINALITY.md` files
- a report describing your project and results (as `REPORT.pdf` or `REPORT.md`)
  no more than four (printed) A4 pages

## Project Presentation

During the last week of semester we will schedule presentations of
your projects. These will take place in the normal lecture slots 
(and possibly lab slots depending on the number of groups).
At least one member of each group is expected to attend and
present. The presentations will be no longer than 5 minutes and should
include both an overview of the project and live demonstration.

A detailed schedule will be distributed by mid October.

## Assessment

Your project will be assessed based on three components:

- **Project code (40%):** includes
 - code quality, organisation and maintainability
 - regular GitLab commits by all group members
 - use of issue tracking and other project management tools
- **Project report (40%):** quality and clarity of the report.
- **Presentation (20%):** clarity of your in-class presentation and
  project demonstration.

## Important Dates

- **Friday, 23 September:** Project proposals due via GitLab
- **Monday, 24 October to Wednesday, 26 October:** In-class project presentations
- **Friday, 28 October:** Final project deliverable due via GitLab

## Data Sources

The following data sources may provide useful inspiration for your projects:

- http://data.gov.au/dataset
- https://github.com/caesar0301/awesome-public-datasets
- https://www.kaggle.com/competitions
- http://mldata.org
- http://labrosa.ee.columbia.edu/millionsong/
- http://www.abs.gov.au/ausstats/abs@.nsf/mf/1379.0.55.001/
- http://www.gutenberg.org/

Remember to cite the source of your data and **do not** commit large
datasets to your repo.