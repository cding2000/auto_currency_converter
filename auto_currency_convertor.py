import requests

API_KEY = 'fca_live_LvOa9ACV1c6nvVMLkwut5rdfnpUG8ERvQTUSXQ6d'
BASE_URL = "https://api.freecurrencyapi.com/v1/latest"

CURRENCIES = ["USD", "CAD", "EUR", "AUD", "CNY"]

def build_url(base):
    params = {
        'apikey': API_KEY,
        'base_currency': base,
        'currencies': ",".join(CURRENCIES)
    }
    return BASE_URL, params

def fetch_data(url, params):
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json().get("data", {})
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return {}

def convert_currency(base):
    url, params = build_url(base)
    return fetch_data(url, params)

def display_currency_rates(data, base):
    if not data:
        print("Invalid currency.")
        return

    del data[base]
    for ticker, value in data.items():
        print(f"{ticker}: {value}")

def list_all_currencies():
    print("Available currencies:")
    for currency in CURRENCIES:
        print(currency)

def add_currency(new_currency):
    if new_currency not in CURRENCIES:
        CURRENCIES.append(new_currency)
        print(f"{new_currency} added to the list of currencies.")
    else:
        print(f"{new_currency} already exists in the list.")

def remove_currency(currency_to_remove):
    if currency_to_remove in CURRENCIES:
        CURRENCIES.remove(currency_to_remove)
        print(f"{currency_to_remove} removed from the list of currencies.")
    else:
        print(f"{currency_to_remove} not found in the list.")

def main():
    while True:
        print("\nOptions:")
        print("1. Convert Currency")
        print("2. List All Currencies")
        print("3. Add Currency")
        print("4. Remove Currency")
        print("q. Quit")

        choice = input("Enter your choice: ").lower()

        if choice == "q":
            break
        elif choice == "1":
            base = input("Enter the base currency: ").upper()
            data = convert_currency(base)
            display_currency_rates(data, base)
        elif choice == "2":
            list_all_currencies()
        elif choice == "3":
            new_currency = input("Enter the new currency to add: ").upper()
            add_currency(new_currency)
        elif choice == "4":
            currency_to_remove = input("Enter the currency to remove: ").upper()
            remove_currency(currency_to_remove)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
