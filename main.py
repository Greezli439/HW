import aiohttp
import asyncio
import datetime
import sys
from pprint import pprint


def check_range_days():
    days = int(sys.argv[1])
    while 0 <= days > 10:
            days = int(input('Max count days is 10 >> '))
    return days


def get_dates(date_range):
    res = []
    for i in range(date_range):
        res.append((datetime.datetime.now() - datetime.timedelta(days=i+1)).strftime('%d.%m.%Y'))
    return res


def pars_data(data):
    res = {data['date']:
               {
                   'EUR':
                       {
                           'sale': [(i['saleRateNB']) for i in data['exchangeRate'] if i['currency'] == 'EUR'][0],
                           'purchase': [i['purchaseRateNB'] for i in data['exchangeRate'] if i['currency'] == 'EUR'][0]
                       },
                   'USD':
                       {
                           'sale': [i['saleRateNB'] for i in data['exchangeRate'] if i['currency'] == 'USD'][0],
                           'purchase': [i['purchaseRateNB'] for i in data['exchangeRate'] if i['currency'] == 'USD'][0]
                       }

               }
           }
    return res

async def main(days):
    result = []
    async with aiohttp.ClientSession() as session:
        for date_for_response in get_dates(days):
            async with session.get(f'https://api.privatbank.ua/p24api/exchange_rates?json&date={date_for_response}') as response:
                res_p = await response.json()
                result.append(pars_data(res_p))
        return result


if __name__ == "__main__":
    days = check_range_days()
    pprint(asyncio.run(main(days)))
