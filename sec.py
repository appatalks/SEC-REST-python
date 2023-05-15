import requests

# Function to fetch data from the API
def fetch_data(url, headers=None):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data. Please try again.")
        return None

# Function to get the company filing history
def get_filing_history(cik):
    url = f"https://data.sec.gov/submissions/{cik}.json"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36 YourCompany/1.0"
    }
    data = fetch_data(url, headers=headers)
    if data:
        print("Filing History:")
        print("----------------")
        if isinstance(data.get("filings"), list):
            for filing in data["filings"]:
                if isinstance(filing, dict):
                    print(f"Filing Date: {filing.get('filingDate')}")
                    print(f"Form Type: {filing.get('form')}")
                    print(f"Description: {filing.get('description')}")
                    print("----------------")
        else:
            print("No filing history found.")
    print()
    print(data)

# Function to get XBRL company facts data
def get_company_facts_data(cik):
    url = f"https://data.sec.gov/api/xbrl/companyfacts/{cik}.json"
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36 YourCompany/1.0"
    }
    data = fetch_data(url, headers=headers)
    if data:
        print("Company Facts Data:")
        print("------------------")
        if "facts" in data:
            facts = data["facts"]
        else:
            print("No facts data found.")
    print()
    print(data)

# Main script
if __name__ == "__main__":
    while True:
        print("Select an option:")
        print("1. Get Company Filing History")
        print("2. Get XBRL Company Facts Data")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            cik = input("Enter the CIK of the company: ")
            get_filing_history(cik)
        elif choice == "2":
            cik = input("Enter the CIK of the company: ")
            get_company_facts_data(cik)
        elif choice == "3":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")
        print()
