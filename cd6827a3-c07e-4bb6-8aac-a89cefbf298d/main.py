from surmount.base_class import Strategy, TargetAllocation
from surmount.data import Asset, Financials

class TradingStrategy(Strategy):
    def __init__(self):
        # Define a list of tickers you are interested in
        self.tickers = ["AAPL", "MSFT", "GOOGL", "AMZN"]
        # Data needed for calculations. Placeholder for fetching necessary financial data.
        self.data_list = [Financials(i) for i in self.tickers]

    @property
    def interval(self):
        # Assume daily data is sufficient for this strategy
        return "1day"

    @property
    def assets(self):
        return self.tickers

    @property
    def data(self):
        return self.data_list

    def quality_metric(self, financial_data):
        # Placeholder for calculating the quality based on industry profit margins
        # Ideally, fetch or calculate industry profit margins here
        return True if financial_data["profit_margin"] > industry_average else False

    def growth_metric(self, financial_data):
        # Placeholder for calculating growth based on EPS growth
        # Ideally, calculate EPS growth here
        return True if financial_data["eps_growth"] > 0 else False

    def price_fairness(self, financial_data):
        # Placeholder for determining price fairness based on industry P/E ratio
        # Ideally, compare the company's P/E ratio with the industry average here
        return True if financial_data["pe_ratio"] < industry_pe_average else False

    def run(self, data):
        allocation_dict = {}
        for ticker in self.tickers:
            # Placeholder financial data retrieval. You'll likely need to fetch real financials here.
            financial_data = data.get(ticker, {})
            
            # Assess quality, growth, and price fairness
            is_quality = self.quality_metric(financial_data)
            is_growing = self.growth_metric(financial_data)
            is_fair_price = self.price_fairness(financial_data)
            
            # If all criteria are met, we allocate a portion of the portfolio to this stock
            if is_quality and is_growing and is_fair_price:
                allocation_dict[ticker] = 1 / len(self.tickers)  # Equally weighted for simplicity
            else:
                allocation_dict[ticker] = 0

        return TargetAllocation(allocation_dict)