import requests
from randommer import Randommer

class Finance(Randommer):
    def get_crypto_address_types(self, api_key: str) -> list:
        '''get available crypto types

        Args:
            api_key (str): api key

        Returns:
            list: list of types
        '''
        url = self.base_url + 'Finance/CryptoAddress/Types'
        headers={"X-Api-Key" : api_key}
        response=requests.get(url, headers=headers)
        return response.json()

    def get_crypto_address(self, crypto_type: str, api_key: str) -> dict:
        '''get available crypto address

        Args:
            crypto_type (str): crypto type
            api_key (str): api key

        Returns:
            dict: crypto address
        '''
        url = self.base_url + 'Finance/CryptoAddress'
        
        payload = {
                "cryptotype": crypto_type
            }
        headers = {
                "X-Api-Key": api_key
            }
        response = requests.get(url, params=payload, headers=headers)
        if response.status_code==200:
            return response.json()
        
        return False

    def get_countries(self, api_key: str) -> list:
        '''get available countries

        Args:
            api_key (str): api key

        Returns:
            list: crypto address
        '''
        url = self.base_url + 'Finance/CryptoAddress/Types'
        headers={"X-Api-Key" : api_key}
        response=requests.get(url, headers=headers)
        return response.json()

    def get_iban_by_country_code(self, country_code: str, api_key: str) -> dict:
        '''get available countries

        Args:
            country_code (str): country code
            api_key (str): api key

        Returns:
            dict: idan data
        '''
        url = self.base_url + 'Finance/Iban/{countrycode}'
        
        payload = {
                "crcountrycode": country_code
            }
        headers = {
                "X-Api-Key": api_key
            }
        response = requests.get(url, params=payload, headers=headers)
        if response.status_code==200:
            return response.json()
        
        return False

s=Finance()
print(s.get_countries("2d794c6f46094ceb96bd719c1c26c984"))