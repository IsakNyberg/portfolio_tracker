from yahoo_finance import Share


class Stock:
    def __init__(self, ticker, buy_in_price=None, amount=1):
        self.ticker = Share(ticker)
        self.amount = amount
        self.buy_in_price = buy_in_price
        if buy_in_price is None:
            self.buy_in_price = self.price

    def __repr__(self):
        return "{0} {1} at {2}".format(self.amount, self.ticker, self.price)

    # fetch
    @property
    def price(self):
        self.ticker.refresh()
        return self.ticker.get_price()

    @property
    def open(self):
        self.ticker.refresh()
        return self.ticker.get_open()

    @property
    def close(self):
        self.ticker.refresh()
        return self.ticker.get_prev_close()

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
