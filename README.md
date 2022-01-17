## Notes app APIs


## Setup

clone the repository:

```bash
$ git clone https://github.com/omer358/Notes-App.git
$ cd NotesApp
```

Create a virtual environment to install dependencies in and activate it:

```bash
$ virtualenv env
$ source env/bin/activate
```

Then install the dependencies:

```bash
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies:
```bash
(env)$ cd Notes
(env)$ python manage.py runserver
```
