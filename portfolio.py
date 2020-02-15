from stock import Stock


class Portfolio(list):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def add(self, ticker_name, buy_in_price=None, amount=1):
        self.append(Stock(ticker_name, buy_in_price, amount))
        
    def update(self):
        # this function needs to be cleaned up
        updated_tickers = {}
        for stock in self:
            if stock.ticker in updated_tickers:
                values = updated_tickers[stock.ticker]
                stock.set_values(*values)
            else:
                updated_tickers[stock.ticker] = stock.update()

    @property
    def is_open(self):
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
