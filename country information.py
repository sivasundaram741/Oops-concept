import requests

class CountryInfo:
    def _init_(self, url):
        self.url = url
        self.data = self.fetch_data()

    # Fetch JSON data from the API
    def fetch_data(self):
        response = requests.get(self.url)
        return response.json()

    # Display all countries, currencies, and symbols
    def display_countries_and_currencies(self):
        for country in self.data:
            name = country.get("name", {}).get("common", "Unknown")
            currencies = country.get("currencies", {})
            print(f"Country: {name}")
            for code, details in currencies.items():
                print(f"  Currency: {details.get('name', 'Unknown')} ({code})")
                print(f"  Symbol: {details.get('symbol', 'N/A')}")

    # Display countries with specified currency
    def countries_by_currency(self, currency_name):
        result = []
        for country in self.data:
            currencies = country.get("currencies", {})
            for details in currencies.values():
                if details.get("name") == currency_name:
                    result.append(country.get("name", {}).get("common", "Unknown"))
        return result

# Main execution
url = "https://restcountries.com/v3.1/all"
country_info = CountryInfo(url)

print("Countries and Currencies:")
country_info.display_countries_and_currencies()

print("\nCountries using Dollar:")
print(country_info.countries_by_currency("Dollar"))

print("\nCountries using Euro:")
print(country_info.countries_by_currency("Euro"))
