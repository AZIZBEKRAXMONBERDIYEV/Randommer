import requests
from randommer import Randommer


class Misc(Randommer):
    def get_cultures(self, api_key: str) -> list:
        '''get available misc cultures

        Args:
            api_key (str): api key

        Returns:
            list: list of cultures
        '''
        url = self.base_url + 'Finance/Countries'
        headers={"X-Api-Key" : api_key}
        response=requests.get(url, headers=headers)
        if response.status_code==200:
            return response.json()
        
        return False
    
    def get_random_address(self, api_key: str, number: int, culture='en') -> list:
        '''get available misc cultures

        Args:
            api_key (str): api key
            number (str): number
            culture (str): culture

        Returns:
            list: random address
        '''
        url = self.base_url + 'Finance/Vat/Validator'
        
        payload = {
                "country" : culture
            }
        headers = {
                "vat": number
            }
        headers = {
                "X-Api-Key" : api_key
        }
        response = requests.get(url, params=payload, headers=headers)
        if response.status_code==200:
            return response.json()
        
        return False
s=Misc()
print(s.get_random_address("2d794c6f46094ceb96bd719c1c26c984"))