#!/usr/bin/env python
import requests
import json

from stock import Stock

class Portfolio(list):
    def __init__(self, name, api_token):
        super().__init__()
        self.api_token = api_token
        self.name = name

    def save(self):
        path = 'data_{0}.txt'.format(self.name)
        data = ['{0}_{1}_{2}'.format(stock.symbol, round(stock.buy_in_price, 2), stock.amount) for stock in self]

        open(path, 'w').close()  # delete old file
        with open(path, "a") as saveFile:  # recreate new file
            saveFile.write('\n'.join(data))  # puts massive string in file

    def load(self):
        with open('data_{0}.txt'.format(self.name)) as file:
            for stock in file:
                data = stock.rstrip().split("_")
                self.add(data[0], float(data[1]), int(data[2]))

    def add(self, symbol_name, buy_in_price=None, amount=1):
        self.append(Stock(symbol_name, buy_in_price, amount))

    def fetch(self):
        url = 'https://api.worldtradingdata.com/api/v1/stock'
        symbols = set(stock.symbol for stock in self)
        data_table = []
        while len(symbols):
            params = {
              'symbol': ','.join(symbols),
              'api_token': self.api_token
            }
            response = requests.request('GET', url, params=params).json()['data']

            if response is None:
                raise ValueError("No response from worldtradingdata, you may be out of requests")

            data_table += response

            for symbol_data in response:
                symbols.remove(symbol_data['symbol'])
            
        return data_table
        
    def update(self):
        data_table = self.fetch()

        for symbol_data in data_table:
            symbols = [stock for stock in self if stock.symbol == symbol_data['symbol']]
            for stock in symbols:
                stock.set_data(symbol_data)

    @property
    def is_open(self):
        # TODO this function is meant to check if market is open or closed
        return None

    @property
    def value(self):
        return round(sum(stock.value for stock in self), 2)

    @property
    def buy_in_price(self):
        return round(sum(stock.buy_in_price * stock.amount for stock in self), 2)
    
    @property
    def open(self):
        return round(sum(stock.open * stock.amount for stock in self), 2)

    @property
    def close(self):
        return round(sum(stock.close * stock.amount for stock in self), 2)

    @property
    def change(self):
        return round(sum(stock.change_total for stock in self), 2)

    @property
    def change_percent(self):
        return round(100 * self.change / self.buy_in_price, 2)

    # day
    @property
    def day_change(self):
        return round(sum([stock.day_change_total for stock in self]), 2)

    @property
    def day_change_percent(self):
        return round(100 * self.day_change / self.close, 2)
