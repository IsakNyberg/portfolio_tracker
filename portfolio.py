from stock import Stock


class Portfolio(list):
    def __init__(self, name):
        self.name = name

    def add(self, ticker_name, buy_in_price=None, amount=1):
        self.append(Stock(ticker_name, buy_in_price, amount))

    @property
    def is_open(self):
        return sum(stock.value for stock in self)

    @property
    def value(self):
        return sum(stock.value for stock in self)

    @property
    def buy_in_price(self):
        return sum(stock.buy_in_price * stock.amount for stock in self)

    @property
    def close(self):
        return sum(stock.close * stock.amount for stock in self)

    @property
    def change(self):
        return sum(stock.change_total for stock in self)

    @property
    def change_percent(self):
        return int(100 * self.change / self.buy_in_price)

    # day
    @property
    def day_change(self):
        return sum([stock.day_change_total for stock in self])

    @property
    def day_change_percent(self):
        return int(100 * self.day_change / self.close)
