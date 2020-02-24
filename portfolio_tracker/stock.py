#!/usr/bin/env python


class Stock:
    def __init__(self, symbol, buy_in_price=None, amount=1):
        self.symbol = symbol.upper()
        self.amount = amount
        self.buy_in_price = buy_in_price

        self._data = {
            "symbol": "Not fetched",
            "name": "Not fetched",
            "currency": "USD",
            "price": "0",
            "price_open": "0",
            "day_high": "0",
            "day_low": "0",
            "52_week_high": "0",
            "52_week_low": "0",
            "day_change": "0",
            "change_pct": "0",
            "close_yesterday": "0",
            "market_cap": "0",
            "volume": "0",
            "volume_avg": "0",
            "shares": "0",
            "stock_exchange_long": "Not fetched",
            "stock_exchange_short": "Not fetched",
            "timezone": "EST",
            "timezone_name": "America/New_York",
            "gmt_offset": "-18000",
            "last_trade_time": "2020-02-19 10:08:03",
            "pe": "Not fetched",
            "eps": "Not fetched"
        }

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
