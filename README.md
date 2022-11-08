Using the most timely and accurate data available on [https://www.census.gov/en.html](https://www.census.gov/en.html), write a python script that pulls the following poverty data for Harris County, TX in the year 2018:

- Estimate of the number of people under the age of 18 in poverty
- Estimate of the number of people of any age in poverty
- Estimate of the median household income

Your script should then write this data to a .csv file, including appropriately named headers. When finished, push your code to a public git repo.

**Requirements**:

- Use an api key to authenticate your requests
- Use the [requests](https://docs.python-requests.org/en/latest/) library (no custom libraries that pull Census data)

Installation guide:

1. Clone from Github: 
2. Set-up virtual environment:

`cd your-project`

`python -m venv env`

Activate virtual environment:

`source env/bin/activate`

3. Install dependencies from requirements.txt

`pip install -r requirements.txt`

4. Rename .env_example to .env to be able to access AUTH data.
Please note, at the moment auth data contains dummy API KEY and SECRET as the service used for this script doesn't 
require authentication

5. Run poverty_script.py in terminal or in the IDE of your choice. 

Example how to do in in ternminal:

`python <path to the file>/poverty_script.py


