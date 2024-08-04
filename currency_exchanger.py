import requests
import re

API_ID = '8dcd05587fc861300e5ff8f9'
BASE_CURRENCY = 'USD'
# Fetch exchange rates from the API
exchange_rate_url = "https://v6.exchangerate-api.com/v6/{API_ID}/latest/{BASE_CURRENCY}"
response = requests.get(exchange_rate_url)
exchange_rates = response.json()["conversion_rates"]

def convert_to_usd(currency_code, amount):
    if currency_code in exchange_rates:
        relative_exchange_rate = exchange_rates[currency_code]
        usd_amount = amount / relative_exchange_rate
        return usd_amount
    else:
        return None

def convert_file_to_usd(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    pattern = re.compile(r'([0-9.]+)\s*(CAD|EUR|CNY|GBP|RUB|JPY|MXN|AUD|INR|HKD)')
    matches = pattern.findall(content)

    for amount, currency_code in matches:
        usd_amount = convert_to_usd(currency_code, float(amount))
        if usd_amount is not None:
            content = content.replace(f"{amount} {currency_code}", f"{usd_amount:.2f} USD")

    with open(file_path, 'w') as file:
        file.write(content)
