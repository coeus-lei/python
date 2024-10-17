from baseapi import BaseApi

class TestUtil:
    def test_get_token(self):
        data = {
            "method":"get",
            "url":"https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {
                "corpid":"wwa945654545454545",
                "corpsecret":"1234567890"
            }
        }
        print(type(data))
        return data
        # return BaseApi().send(data)['access_token']

x = TestUtil().test_get_token()
print(x)
# print(x.test_get_token())
