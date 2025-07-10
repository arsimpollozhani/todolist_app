## Todo Web App

Technologies:
- Frontend: HTML, CSS, Bootstrap
- Backend: Django (Python)

## Description

This repository contains the source code of a Todo Web Application.
The source code may have bugs.
The application is not user friendly, even though contains bootstrap elements,
the user may be lost at first glance.

## Core functionalities:

- User registration
- User login/logout
- Create a ToDo List
- Insert items to a List
- View Lists
- View items of a list


## Test in your PC

Clone the repo

> I reccomend to create a virtual environment. Search on the internet how to do it.


In your Command Line Interface execute the commands:

### Install the requirements

```
pip install -r requirements.txt
```
> Execute the command where requirements.txt is placed.
Explaination: To download the needed applications for app functionality.

## Run the server

```
python manage.py runserver
``` 

> Execute in the directory where manage.py is placed.
Explanation: This command will create a local web server in your PC. Copy the URL generated and paste in your web browser.

## Database information

By registering you will be recorded in the database file in the project `db.sqlite3`

By accessing this information you can use Django Admin Dashboard or install third party apps to see database files.

For more info...do research...