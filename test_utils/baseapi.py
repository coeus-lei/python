import requests
import json

class BaseApi:
    params = {}
    def send(self,data):
        raw_data = json.dumps(data)
        for key,value in self.params.items():
            raw_data = raw_data.replace("${"+key+"}",value)
        
        data = json.loads(raw_data)
        return requests.request(**data).json()
#     def type_test(self):
#         return type(self.params)
    
# x = BaseApi()
# print(x.type_test())
