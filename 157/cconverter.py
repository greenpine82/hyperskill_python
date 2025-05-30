# write your code here!
import json
import requests

cache = dict()
currency_code = input().lower()
data = f'http://www.floatrates.com/daily/{currency_code}.json'
response = requests.get(data).json()
if 'usd' in response.keys():
    cache['usd'] = response['usd']
if 'eur' in response.keys():
    cache['eur'] = response['eur']
while True:
    target_currency = input()
    if target_currency == "":
        break
    number = float(input())
    print('Checking the cache...')
    if target_currency not in cache.keys():
        print('Sorry, but it is not in the cache!')
        data = f'http://www.floatrates.com/daily/{currency_code}.json'
        response = requests.get(data).json()
        print(f'You received {response[target_currency]["rate"] * number} {target_currency}.')
        cache[target_currency] = response[target_currency]
    else:
        print('Oh! It is in the cache!')
        print(f'You received {cache[target_currency]["rate"] * number} {target_currency}.')
