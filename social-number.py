import requests
from randommer import Randommer


class SocialNumber(Randommer):
    def get_SocialNumber(self, api_key: str) -> str:
        '''get SocialNumber

        Args:
            api_key (str): api key

        Returns:
            str: number as str
        '''
        url = self.base_url + 'SocialNumber'
        headers={"X-Api-Key" : api_key}
        response=requests.get(url, headers=headers)
        if response.status_code==200:
            return response.json()
        return False
