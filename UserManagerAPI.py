"""
"""
from BasicAPI import *
from RequestData import *


class UserManagerAPI(BasicAPI):

    def __init__(self, format):
        BasicAPI.__init__(self, format, app='usermanager')
        self.sec = True

    def add_user(self, userConfig):
        self.uri = '/' + self.app + '/users'
        self.method = 'POST'
        self.data = userConfig
        self.headers = {'Accept': 'application/' + self.format,
        'Content-type': 'application/' + self.format
        }
        return RequestData(uri=self.uri, method=self.method, data=self.data, headers=self.headers, sec=self.sec)

    def del_user(self, userName):
        self.uri = '/' + self.app + '/users/' + userName
        self.method = 'DELETE'
        self.data = None
        self.headers = {'Accept': 'application/' + self.format}
        return RequestData(uri=self.uri, method=self.method, data=self.data, headers=self.headers, sec=self.sec)
