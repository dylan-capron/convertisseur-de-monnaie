from forex_python.converter import CurrencyRates
import json

def get_exchange_rate(from_currency, to_currency):
    c = CurrencyRates()
    try:
        rate = c.get_rate(from_currency, to_currency)
        return rate
    except:
        return None

def convert_currency(amount, from_currency, to_currency):
    rate = get_exchange_rate(from_currency, to_currency)
    if rate is not None:
        converted_amount = amount * rate
        return converted_amount
    else:
        return None

def save_conversion_history(history, filename='conversion_history.json'):
    with open(filename, 'w') as file:
        json.dump(history, file)

def load_conversion_history(filename='conversion_history.json'):
    try:
        with open(filename, 'r') as file:
            history = json.load(file)
        return history
    except FileNotFoundError:
        return []

def add_favorite_currency(favorites, currency, rate):
    favorites[currency] = rate

def display_favorite_currencies(favorites):
    print("\nDevises préférées :")
    for currency, rate in favorites.items():
        print(f"{currency}: {rate}")

def main():
    conversion_history = load_conversion_history()
    favorite_currencies = {}

    while True:
        print("\nOptions:")
        print("1. Convertir une somme")
        print("2. Ajouter une devise préférée")
        print("3. Afficher les devises préférées")
        print("4. Afficher l'historique des conversions")
        print("5. Quitter")

        choice = input("Choisissez une option (1/2/3/4/5): ")

        if choice == '1':
            amount = float(input("Entrez le montant à convertir : "))
            from_currency = input("Entrez la devise d'origine : ").upper()
            to_currency = input("Entrez la devise de destination : ").upper()

            converted_amount = convert_currency(amount, from_currency, to_currency)

            if converted_amount is not None:
                print(f"{amount} {from_currency} équivaut à {converted_amount:.2f} {to_currency}")
                conversion_history.append({
                    'amount': amount,
                    'from_currency': from_currency,
                    'to_currency': to_currency,
                    'converted_amount': converted_amount
                })
                save_conversion_history(conversion_history)
            else:
                print("Conversion impossible. Vérifiez les devises entrées.")

        elif choice == '2':
            currency = input("Entrez la devise à ajouter aux favoris : ").upper()
            rate = float(input("Entrez le taux de conversion : "))
            add_favorite_currency(favorite_currencies, currency, rate)
            print(f"{currency} ajoutée aux devises préférées avec un taux de conversion de {rate}")

        elif choice == '3':
            display_favorite_currencies(favorite_currencies)

        elif choice == '4':
            print("Historique des conversions :")
            for entry in conversion_history:
                print(f"{entry['amount']} {entry['from_currency']} équivaut à {entry['converted_amount']:.2f} {entry['to_currency']}")

        elif choice == '5':
            break

        else:
            print("Option invalide. Veuillez choisir une option valide.")

if __name__ == "__main__":
    main()
