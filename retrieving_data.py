import requests
from bs4 import BeautifulSoup
import os
import pdfkit
def get_companies_by_company_name(company_name):
    # URL for the SEC EDGAR search page
    search_url = f"https://www.sec.gov/cgi-bin/browse-edgar?company={company_name}&owner=exclude&action=getcompany"

    # Define headers to mimic a web browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    }

    # Send a GET request to the SEC EDGAR search page with headers
    response = requests.get(search_url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the table with class 'tableFile2'
        table = soup.find('table', {'class': 'tableFile2'})

        # Check if the table is found
        if table:
            # Find all rows in the table except the header row
            rows = table.find_all('tr')[1:]

            # Loop through rows and extract company information
            for row in rows:
                # Extract CIK, company name, and state/country
                cik_element = row.find('a')
                company_name_element = row.find_all('td')[1]
                state_country_element = row.find_all('td')[2]

                if cik_element and company_name_element and state_country_element:
                    cik = cik_element.text.strip()
                    company_name = company_name_element.text.strip()
                    state_country = state_country_element.text.strip()

                    print(f"CIK: {cik}, Company Name: {company_name}, State/Country: {state_country}")
                else:
                    print("Incomplete information found in a row.")
        else:
            print(f"No table with class 'tableFile2' found on the page.")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

# Function to get the 10-K filing link for a given CIK and filing date
def get_document_dates(cik, document_type):
    # URL for the SEC EDGAR search page
    dates = []
    links = []
    document_type = document_type.upper()
    search_url = f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={cik}&type={document_type}&count=1"

    # Define headers to mimic a web browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    }

    # Send a GET request to the SEC EDGAR search page with headers
    response = requests.get(search_url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        lines = response.text.splitlines()
    # Print each line
        for i in range(len(lines)):
            if '<td>' in lines[i] and '</td>' in lines[i] and ('Annual' in lines[i-1] or 'Quarterly' in lines[i-1]):
                date = lines[i].split('>')[1].split('<')[0]
                date = date.replace("-","")
                dates.append(date)
                link = lines[i-2].split('"')[3]
                links.append(link)
                print(date)
        
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return None
    
    if(len(dates) == 0):
        print(f"Failed to retrieve data. No such file")
        return None
    

    filing_date = input("Enter the date of the file you want: ")
    index_of_date = dates.index(filing_date)
    hyp_link = links[index_of_date]
    hyp_link = "https://www.sec.gov/" + hyp_link
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        }
    response = requests.get(hyp_link,headers=headers)
    doc_link = ""
    if response.status_code == 200:
        lines = response.text.splitlines()
    # Print each line
        for i in range(len(lines)):
            if document_type in lines[i-1] and 'a href=' in lines[i]:
                doc_link = lines[i].split('"')[3]
                doc_link = "https://www.sec.gov/" + doc_link
        
    else:
        print(f"Failed to download 10-K filing. Status Code: {response.status_code}")

    doc_link = doc_link.replace("//ix?doc=","") + "#i1cb1ba018cb1455aa66bd3f9ab0c5b1a_1499"
    url = doc_link
    path_wkhtmltopdf = '/usr/local/bin/wkhtmltopdf'  # Path of wkhtmltopdf on machine
    
# Convert the specific element to PDF with explicit configuration
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    pdfkit.from_url(url, 'output.pdf', configuration=config)
    print("The document has downloaded under the current path")

def main():
    # Get company name input from the user
    company_name = input("Enter the company name: ")

    # Get and print companies by company name
    get_companies_by_company_name(company_name)
    
    cik = input("Enter the cik of the company: ")
    document_type = input("Enter the type of the doc: ")
    get_document_dates(cik, document_type)
    

if __name__ == "__main__":
    main()
