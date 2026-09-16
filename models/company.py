from dataclasses import dataclass

@dataclass
class Company:
    name: str
    ticker: str
    industry: str
    market_cap: float
    current_price: float
    
    def display_info(self):
        print(f"회사명 : {self.name}")
        print(f"티커 : {self.ticker}")
        print(f"산업 : {self.industry}")
        print(f"시가 총액 : {self.market_cap}")
        print(f"현재 주가 : {self.current_price}")