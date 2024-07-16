import requests


class CountryAPI:
    def __init__(self):
        self.url = "https://restcountries.com/v3.1/all?fields=name,flags,capital"

    def fetch_data(self):
        try:
            # Attempt to fetch data from the API
            response = requests.get(self.url)
            if response.status_code == 200:
                return response.json()  # Return JSON data if successful
            else:
                # Print error message if request fails
                print(
                    f"Failed to fetch data. Status code: {response.status_code}")
                return None
        except requests.exceptions.RequestException as e:
            # Handle any request exceptions (e.g., network issues)
            print(f"Error fetching data: {e}")
            return None

    def display_in_table(self):
        data = self.fetch_data()
        if data:
            # Iterate through each country's data and display relevant information
            for country in data:
                name = country["name"]["common"]
                capitals = country.get("capital", ["N/A"])
                flag_png = country["flags"]["png"]
                print(f"Country: {name}")
                print(f"Capital: {', '.join(capitals)}")
                print(f"Flag PNG URL: {flag_png}")
                print("-" * 20)


# Usage example
if __name__ == "__main__":
    api = CountryAPI()
    api.display_in_table()
