from test_util import TestUtil
from baseapi import BaseApi
import yaml

class WeWork(BaseApi):
    def __init__(self):
        self.token = TestUtil().test_get_token()
        self.params["token"] = self.token
        with open("wework.yaml",encoding="utf-8") as f:
            self.data = yaml.safe_load(f)

    def test_post_list_id(self,cursor):
        self.params["cursor"] = cursor
        return self.send(self.data["test_post_list_id"])
    
    def test_post_getuserid(self,mobile):
        self.params["mobile"] = mobile
        return self.send(self.data["test_post_getuserid"])
