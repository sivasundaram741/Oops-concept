import requests

# Fetch data from Open Brewery DB API
def fetch_brewery_data(state):
    url = f"https://api.openbrewerydb.org/breweries?by_state={state}"
    response = requests.get(url)
    return response.json()

# List all breweries in specified states
def list_breweries(states):
    breweries = {}
    for state in states:
        data = fetch_brewery_data(state)
        breweries[state] = [brewery['name'] for brewery in data]
    return breweries

# Count breweries in each state
def count_breweries(breweries):
    return {state: len(names) for state, names in breweries.items()}

# Count types of breweries by city
def count_brewery_types(state):
    data = fetch_brewery_data(state)
    brewery_types = {}
    for brewery in data:
        city = brewery['city']
        brewery_type = brewery['brewery_type']
        if city not in brewery_types:
            brewery_types[city] = {}
        brewery_types[city][brewery_type] = brewery_types[city].get(brewery_type, 0) + 1
    return brewery_types

# List breweries with websites
def breweries_with_websites(states):
    breweries = {}
    for state in states:
        data = fetch_brewery_data(state)
        breweries[state] = [brewery['name'] for brewery in data if brewery.get('website_url')]
    return breweries

# Main execution
states = ["Alaska", "Maine", "New York"]
brewery_data = list_breweries(states)
print("Breweries:", brewery_data)
print("Counts:", count_breweries(brewery_data))
print("Types in Alaska:", count_brewery_types("Alaska"))
print("With Websites:", breweries_with_websites(states))
