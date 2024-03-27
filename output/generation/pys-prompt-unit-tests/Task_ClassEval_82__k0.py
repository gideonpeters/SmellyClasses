class StockPortfolioTracker:
    def __init__(self, cash_balance):
        self.cash_balance = cash_balance
        self.portfolio = []

    def add_stock(self, stock):
        for item in self.portfolio:
            if item['name'] == stock['name']:
                item['quantity'] += stock['quantity']
                return
        self.portfolio.append(stock)

    def remove_stock(self, stock):
        for item in self.portfolio:
            if item['name'] == stock['name']:
                if item['quantity'] >= stock['quantity']:
                    item['quantity'] -= stock['quantity']
                    if item['quantity'] == 0:
                        self.portfolio.remove(item)
                    return True
                else:
                    return False
        return False

    def buy_stock(self, stock):
        stock_value = stock['price'] * stock['quantity']
        if stock_value <= self.cash_balance:
            self.cash_balance -= stock_value
            self.add_stock(stock)
            return True
        return False

    def sell_stock(self, stock):
        for item in self.portfolio:
            if item['name'] == stock['name']:
                if item['quantity'] >= stock['quantity']:
                    item['quantity'] -= stock['quantity']
                    if item['quantity'] == 0:
                        self.portfolio.remove(item)
                    self.cash_balance += stock['price'] * stock['quantity']
                    return True
                else:
                    return False
        return False

    def calculate_portfolio_value(self):
        total_value = 0
        for item in self.portfolio:
            total_value += item['price'] * item['quantity']
        return total_value + self.cash_balance

    def get_portfolio_summary(self):
        summary = []
        total_value = 0
        for item in self.portfolio:
            value = item['price'] * item['quantity']
            total_value += value
            summary.append({'name': item['name'], 'value': value})
        return total_value + self.cash_balance, summary

    def get_stock_value(self, stock):
        return stock['price'] * stock['quantity']
