#!/usr/bin/env python

from yahoo_fin.stock_info import get_live_price, get_quote_table


class Stock:
    def __init__(self, ticker, buy_in_price=None, amount=1):
        self.ticker = ticker.upper()
        self.amount = amount
        self.buy_in_price = buy_in_price

        # these values are stored instead of live as each api request takes 0.5 seconds
        self._live, self._table = self.update()

        if buy_in_price is None:
            self.buy_in_price = self._live
        
    def __eq__(self, other):
        return self.ticker == other.ticker

    def __repr__(self):
        return "{0} {1} @ {2}".format(self.amount, self.ticker, self.price)

    def set_values(self, price, table):
        self._live = price
        self._table = table

    # fetch
    def update(self):
        self._live = float(round(get_live_price(self.ticker), 2)) # get_live_price returns numpy.float64
        self._table = get_quote_table(self.ticker)
        return self._live, self._table

    def is_open(self):
        # TODO this function is meant to check if the market for this stock is open or closed
        return None

    @property
    def price(self):
        return round(self._live, 2)

    @property
    def open(self):
        return round(self._table['Open'], 2)

    @property
    def close(self):
        return round(self._table['Previous Close'], 2)

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
        return int(100 * self.change / self.buy_in_price)

    # day
    @property
    def day_change(self):
        return round(self.price - self.close, 2)

    @property
    def day_change_total(self):
        return round(self.day_change * self.amount, 2)

    @property
    def day_change_percent(self):
        return round(100 * self.day_change/self.close, 2)
