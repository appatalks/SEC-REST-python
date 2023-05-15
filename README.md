# SEC Company Filing Search via REST API in Python

** WORK IN PROGRESS **

This script allows you to fetch data related to a company's SEC filings from the EDGAR database. It has two main functionalities: getting the company's filing history and getting the company's XBRL facts data.

## How to Use the Script

1. Clone or download the script to your local machine.
2. Install the necessary dependencies by running `pip install requests` in your terminal.
3. Run the script by running `python <path-to-script>` in your terminal.
4. When prompted, enter the number corresponding to the functionality you wish to use.
5. When prompted, enter the CIK (Central Index Key) of the company for which you wish to fetch data.

## Functions

### `fetch_data(url, headers=None)`

This function takes a URL and optional headers as input and returns the JSON response from the API. If the response status code is not 200, it prints an error message and returns `None`.

### `get_filing_history(cik)`

This function takes a CIK as input and fetches the company's filing history from the EDGAR database. It then prints the filing date, form type, and description for each filing in the company's history.

### `get_company_facts_data(cik)`

This function takes a CIK as input and fetches the company's XBRL facts data from the EDGAR database. It then prints the category, fact name, label, description, and units for each fact in the company's data.

### Main Script

The main script contains a `while` loop that prompts the user to select the functionality they wish to use and the CIK for the company they wish to fetch data for. It then calls the corresponding function and prints the resulting data. The script will continue to run until the user selects the "Exit" option.
