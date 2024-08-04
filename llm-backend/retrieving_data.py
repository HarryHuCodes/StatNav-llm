import requests

#keyword string is parsed from user input to give us an idea of what user wants...can change later
#count -> number of filings that we check (putting 5 for now)
def search_edgar(keyword, count=5):
    base_url = "https://www.sec.gov/Archives/edgar/full-index"
    

    # Perform a search for the keyword in the EDGAR full-index
    search_url = f"{base_url}/{keyword}/index.json"
    #append keyword to base url of EDGAR full index
    response = requests.get(search_url)
    #http GET request and stores response (200 is successful)
    if response.status_code == 200:
        data = response.json()
        #store as JSON


        # Retrieve the first 'count' filings
        filings = data["directory"]["item"][:count]
        #print(type(data))
        
        # Download and print the content of each filing
        for filing in filings:
            filing_url = f"{base_url}/{keyword}/{filing['name']}"
            filing_response = requests.get(filing_url)
            
            if filing_response.status_code == 200:
                print(f"\nFiling: {filing['name']}")
                print(filing_response.text)
            else:
                print(f"Failed to retrieve filing {filing['name']}. Status code: {filing_response.status_code}")
    else:
        print(f"Search failed. Status code: {response.status_code}")

# Example: Search for filings containing the keyword "apple" and retrieve the first 3 filings
search_edgar("apple", count=3)
