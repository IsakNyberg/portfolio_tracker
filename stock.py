from yahoo_fin.stock_info import get_live_price, get_quote_table


class Stock:
    def __init__(self, ticker, buy_in_price=None, amount=1):
        self.ticker = ticker
        self.amount = amount
        self.buy_in_price = buy_in_price
        if buy_in_price is None:
            self.buy_in_price = self.price

    def __repr__(self):
        return "{0} {1} at {2}".format(self.amount, self.ticker, self.price)

    # fetch
    @property
    def price(self):
        return get_live_price(self.ticker)

    @property
    def open(self):
        return get_quote_table(self.ticker)['Open']

    @property
    def close(self):
        return get_quote_table(self.ticker)['Previous Close']

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
        return self.open - self.close

    @property
    def day_change_total(self):
        return self.day_change * self.amount

    @property
    def day_change_percent(self):
        return int(100 * self.day_change/self.close)
