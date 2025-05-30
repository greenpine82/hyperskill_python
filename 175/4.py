rates = {'RUB': 2.98, 'ARS': 0.82, 'HNL': 0.17, 'AUD': 1.9622, 'MAD': 0.208}
number = float(input())
for currency in rates.keys():
    print(f'I will get {number * rates[currency]} {currency} from the sale of {number} conicoins.')