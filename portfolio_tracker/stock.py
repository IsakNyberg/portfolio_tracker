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
            "price": "-1",
            "price_open": "-1",
            "day_high": "-1",
            "day_low": "-1",
            "52_week_high": "-1",
            "52_week_low": "-1",
            "day_change": "-1",
            "change_pct": "-1",
            "close_yesterday": "-1",
            "market_cap": "-1",
            "volume": "-1",
            "volume_avg": "-1",
            "shares": "-1",
            "stock_exchange_long": "-1",
            "stock_exchange_short": "-1",
            "timezone": "EST",
            "timezone_name": "America/New_York",
            "gmt_offset": "-18000",
            "last_trade_time": "1990-01-01 09:30:01",
            "pe": "0",
            "eps": "0"
        }

    def __eq__(self, other):
        return self.symbol == other.symbol

    def __repr__(self):
        return '{0} {1} @ {2}'.format(self.amount, self.symbol, self.price)

    def set_data(self, data):
        self._data = data
        error = False
        for fetched_value in ['price', 'price_open', 'close_yesterday', 'day_change']:
            if self._data[fetched_value] == 'N/A':
                self._data[fetched_value] = '-1'
                error = True
                
        return error

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
