# 1100 Group

## Table of Contents

### Project Deliverable 1
Located under `Deliverable_01/`
 - [Team Agreement](https://github.com/CSCC01/Team12/blob/master/Deliverable_01/C01_Team_Agreement.pdf)

### Project Deliverable 2
Located under `Deliverable_02/`
 - [Personas v0](https://github.com/CSCC01/Team12/blob/master/Deliverable_02/personas_v0.pdf)
 - [User Stories v0](https://github.com/CSCC01/Team12/blob/master/Deliverable_02/user_stories_v0.pdf)

### Project Deliverable 3
Located under `Deliverable_03/`
#### Sprint 1
 - [plan.csv](https://github.com/CSCC01/Team12/blob/master/Deliverable_03/backlog/sprint01/plan.csv)
 - [execution.csv](https://github.com/CSCC01/Team12/blob/master/Deliverable_03/backlog/sprint01/execution.csv)
 - [sprint report](https://github.com/CSCC01/Team12/blob/master/Deliverable_03/backlog/sprint01/sprint_report_01.pdf)

#### Sprint 2
 - [plan.csv](https://github.com/CSCC01/Team12/blob/master/Deliverable_03/backlog/sprint02/plan.csv)
 - [execution.csv](https://github.com/CSCC01/Team12/blob/master/Deliverable_03/backlog/sprint02/execution.csv)
 - [sprint report](https://github.com/CSCC01/Team12/blob/master/Deliverable_03/backlog/sprint02/sprint_report_02.pdf)

#### Instructions
 - source code located under `Deliverable_03/src/`
 - to run:
```
~ $ cd Deliverable_03/
~ $ make
```

### Project Deliverable 4
Located under `Deliverable_04/`
#### Sprint 3
 - [plan.csv](https://github.com/CSCC01/Team12/blob/master/Deliverable_04/backlog/sprint03/plan.csv)
 - [execution.csv](https://github.com/CSCC01/Team12/blob/master/Deliverable_04/backlog/sprint03/execution.csv)
 - [sprint report]()

#### Sprint 4
 - [plan.csv](https://github.com/CSCC01/Team12/blob/master/Deliverable_04/backlog/sprint04/plan.csv)
 - [execution.csv](https://github.com/CSCC01/Team12/blob/master/Deliverable_04/backlog/sprint04/execution.csv)
 - [sprint report]()

#### Instructions
 - source code located under `Deliverable_04/src/`
 - prerequisites
    - edit `src/config.py` to have the correct database configuration to connect to the database
    - Please make sure to run the following sqls on a database schema
```
CommunityConnection.sql
Employment.sql
InformationAndOrientation.sql
LanguageTrainingEnrolment.sql
LanguageTrainingExit.sql
LanguageTrainingSetup.sql
NeedAssessmentReferrals.sql

Template.sql
```

 - to run:
```
~ $ cd Deliverable_04/
~ $ make
```
 - Testing:
    - unittests are named with `_test`
    - acceptance tests are under `src/test`


### Dependencies
 - [python3](https://www.python.org/)
    - [pip](https://pypi.org/project/pip/)
 - [openpyxl](https://bitbucket.org/openpyxl/openpyxl)
 - [mysql-connector-python-rf](https://dev.mysql.com/doc/connector-python/en/connector-python-installation.html)
 - [PyQt5](https://www.riverbankcomputing.com/software/pyqt/download5)
 - [PyPika](https://pypika.readthedocs.io/en/latest/1_installation.html)
 - [pdfkit](https://github.com/JazzCore/python-pdfkit)
 - [wkhtmltopdf](https://github.com/JazzCore/python-pdfkit)
