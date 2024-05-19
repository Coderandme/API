import requests

class GetData:
    
    def fetch_data(self, api_url):
        data = []
        page = 1
        response = requests.get(api_url)
        if response.status_code != 200:
            return
        page_data = response.json()
        if not page_data:
            return
        
        return page_data
    
    
    def process_api_data(self,api_url):
        data = self.fetch_data(api_url)
        data = data['data']['data']
        list_dir =[]
        for item in data:
            response_text = item['response']
            source = item['source']
            list_dir.append({'response':[response_text],'sources':source})
        return list_dir

    

# For debugging
# obj = GetData()
# data_list = obj.process_api_data('https://devapi.beyondchats.com/api/get_message_with_sources')
# print(data_list)
    
   
    


