from models.company import Company


class CompanyService:

    def __init__(self, api):
        self.api = api

    def get_company(self, symbol):

        data = self.api.get_company_profile(symbol)
        quote = self.api.get_quote(symbol)

        # TODO 1
        # 목표:
        # quote에서 현재 주가를 꺼내 Company에 넣는다.
        #
        # 힌트:
        # Finnhub /quote 응답에서 현재 주가는
        # 'c'라는 key에 들어 있다.
        #
        # Company 클래스에서 새로 추가한
        # current_price에 연결하면 된다.

        company = Company(
            name=data["name"],
            ticker=data["ticker"],
            industry=data["finnhubIndustry"],
            market_cap=data["marketCapitalization"],
            current_price=quote["c"]
        )

        return company