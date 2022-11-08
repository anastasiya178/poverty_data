""" Get data from the URL resource and save it to CSV file"""

import csv
import logging

import requests
from decouple import config
from requests.auth import HTTPBasicAuth


logging.basicConfig(level=logging.INFO)
# URL to the data resource
URL = "https://api.census.gov/data/timeseries/poverty/saipe"

# specify required data parameters
STATE_CODE = 48  # Texas
COUNTRY_CODE = 201  # Harris County
YEAR = 2018

indicators = ["NAME",  # county name
              "SAEPOV0_17_PT",  # Ages 0-17 in Poverty, Count Estimate
              "SAEPOVALL_PT",  # All ages in Poverty, Count Estimate
              "SAEMHI_PT",  # Median Household Income Estimate
              ]

# specify CSV header and filename to save data
csv_header = [
    "County name",
    "Estimate poverty under 18",
    "Estimate poverty any age",
    "Estimate median household income",
    "Year",
    "State code",
    "County code",
]

CSV_FILENAME = "poverty_2018_Harris_TX_.csv"

# build URL params
url_params = {
    "get": ",".join(indicators),
    "for": f"county:{COUNTRY_CODE}",
    "in": f"state:{STATE_CODE}",
    "time": YEAR,
}

# Set up auth if it's required. Edit API KEY and SECRET in your .env file
AUTH = HTTPBasicAuth(config("API_KEY"), config("SECRET"))


def get_data(url: str, params: dict, auth: requests.auth.HTTPBasicAuth) -> list:
    """
    Request data using GET method, get response.
    Returns the json-encoded content of a response.
    """
    response = requests.request("GET", url, params=params, auth=auth, timeout=5)
    response.raise_for_status()
    json_data = response.json()
    logging.info("JSON data received")
    return json_data[1]


def save_to_csv(header: list, csv_filename: str, json_data: list) -> None:
    """Save data to CSV file"""
    with open(csv_filename, "w", encoding="UTF8", newline="") as file:
        writer = csv.writer(file)
        # write CSV header
        writer.writerow(header)
        # write a row
        writer.writerow(json_data)
        logging.info(f"Data written to {csv_filename}")


if __name__ == "__main__":
    # get poverty data
    data = get_data(URL, url_params, AUTH)

    # save data to CSV
    save_to_csv(csv_header, CSV_FILENAME, data)
