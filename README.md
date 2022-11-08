Python script for extracting povery data and saving it into CSV file (as per the task received).

## Installation guide:
Prerequisite: make sure you have Python3 installed on your local machine. 
If not, install from here: https://www.python.org/downloads/.

The version used for this script is Python 3.8.9.

1. Clone the project from Github: 

[https://github.com/anastasiya178/poverty_data.git](https://github.com/anastasiya178/poverty_data)

3. Set-up virtual environment:

`cd your-project`

`python -m venv env`

Activate virtual environment:

```source env/bin/activate```

3. Install dependencies from requirements.txt

`pip install -r requirements.txt`

4. Rename .env_example to .env to be able to access AUTH data.

Please note, at the moment auth data contains empty API KEY and SECRET as the service used for this script doesn't 
require authentication. 

5. Run poverty_script.py in the terminal or in the IDE of your choice. 

Example how to do in in macOS ternminal:

`python <absolute path to the file>/poverty_script.py

6. Check ***poverty_2018_Harris_TX_.csv*** file under the root folder of the project.
