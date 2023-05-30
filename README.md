# c214-design-patterns
C214 - Design Patterns

## Summary :clipboard:

* [Requirements](#requirements)
* [Setup and Installation](#setup-installation)
* [How to Test](#how-to-test)
* [Documentation](#documentation)

*********************
##  Requirements :pencil: <a name="requirements"></a>

* [Python 3.10+](https://www.python.org/)
* Pip 23.1+ (comes with Python 3)

*********************
##  Setup and Installation :white_check_mark: <a name="setup-installation"></a>

### Cloning the repo :file_folder:
First off, in order to get a copy of the project in order to run/test it, clone the repository into a folder on your machine:

```
git clone git@github.com:MaycolTeles/c214-design-patterns.git
```

### Creating and Activating the Virtual Environment :open_file_folder:
It is recommended to install the dependencies inside a [virtualenv](https://docs.python.org/3/tutorial/venv.html). So, inside the folder where you cloned the repository, create a new virtualenv:

```
python3 -m virtualenv venv
```

If you don't have the virtualenv package installed, you can install it with pip:

```
pip install virtualenv
```
    
Now, activate the virtualenv (for Linux/MacOS):

```
source venv/bin/activate
```

or (for Windows):

```
.\venv\Scripts\activate
```

### Installing Dependencies :wrench:
To install all the necessary project dependencies, run the following command in the terminal (make sure you're running it from whithin your virtualenv):

```
pip install -r requirements.txt
```

### Creating the .env file :spiral_notepad:
In order to run the project, you must create a .env file to store the necessary environment variables (in this case, the UI injection).
To do so, open the file named ".env.tmpl" and follow the instructions inside it to create the .env file.

### Executing the Project :arrow_forward:
To run your project, go to `src` folder (`cd app/src`) and run the following command in the terminal (make sure you're running it from whithin your virtualenv):

```
python -m main
```


*********************

## How To Test :man_technologist: <a name="how-to-test"></a>

To run the unit tests, go to `src` folder (`cd app/src`) and run the following command in the terminal (make sure you're running it from whithin your virtualenv):

```
pytest
```

if you want a more verbose output, you can run the following command:

```
pytest -vv
```

Now, if you want to generate the test coverage report, run the following command:

```
pytest -vv --cov=. --cov-report=html --cov-config=.coveragerc
```
