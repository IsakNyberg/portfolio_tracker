#!/usr/bin/env python

class Stock:
    def __init__(self, symbol, buy_in_price=None, amount=1):
        self.symbol = symbol.upper()
        self.amount = amount
        self.buy_in_price = buy_in_price

        self._data = {}

    def __eq__(self, other):
        return self.symbol == other.symbol

    def __repr__(self):
        return '{0} {1} @ {2}'.format(self.amount, self.symbol, 00)#self.price)

    def set_data(self, data):
        self._data = data

    @property
    def price(self):
        return float(self._data['price'])

    @property
    def open(self):
        return float(self._data['price_open'])

    @property
    def close(self):
        return float(self._data['close_yesterday'])

    # day
    @property
    def day_change(self):
        return float(self._data['day_change'])

    @property
    def day_change_total(self):
        return self.day_change * self.amount

    @property
    def day_change_percent(self):
        return float(self._data['change_pct'])

    # totals
    @property
    def value(self):
        return self.price * self.amount

    @property
    def change(self):
        return self.price - self.buy_in_price

    @property
    def change_total(self):
        return self.change * self.amount

    @property
    def change_percent(self):
        return round(100 * self.change / self.buy_in_price, 2)
