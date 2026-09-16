from api.finnhub_api import FinnhubAPI 
from services.company_service import CompanyService



def main():
    api = FinnhubAPI()
    service = CompanyService(api)
    
    symbol = input("조회할 기업의 티커를 입력하세요 : ")

    company = service.get_company(symbol)
    
    company.display_info()
    
    

if __name__ == "__main__":
    main()
