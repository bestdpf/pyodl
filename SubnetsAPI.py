"""
"""
from BasicAPI import *
from RequestData import *


class SubnetsAPI(BasicAPI):

    def __init__(self, format):
        BasicAPI.__init__(self, format, app='subnetservice')

    def retrieve_all_subnets(self, container):
        self.uri = '/' + self.app + '/' + container + '/subnets'
        self.method = 'GET'
        self.data = None
        self.headers = {'Accept': 'application/' + self.format}
        return RequestData(uri=self.uri, method=self.method, data=self.data, headers=self.headers)

    def retrieve_subnet_by_name(self, subnetName, container):
        self.uri = '/' + self.app + '/' + container + '/subnet/' + subnetName
        self.method = 'GET'
        self.data = None
        self.headers = {'Accept': 'application/' + self.format}
        return RequestData(uri=self.uri, method=self.method, data=self.data, headers=self.headers)

    def add_subnet(self, subnetName, subnetConfig, container):
        self.uri = '/' + self.app + '/' + container + '/subnet/' + subnetName
        self.method = 'PUT'
        self.data = subnetConfig
        self.headers = {'Accept': 'application/' + self.format,
        'Content-type': 'application/' + self.format
        }
        return RequestData(uri=self.uri, method=self.method, data=self.data, headers=self.headers)

    def del_subnet(self, subnetName, container):
        self.uri = '/' + self.app + '/' + container + '/subnet/' + subnetName
        self.method = 'DELETE'
        self.data = None
        self.headers = {'Accept': 'application/' + self.format}
        return RequestData(uri=self.uri, method=self.method, data=self.data, headers=self.headers)

    def modify_subnet(self, subnetName, subnetConfig, container):
        self.uri = '/' + self.app + '/' + container + '/subnet/' + subnetName
        self.method = 'POST'
        self.data = subnetConfig
        self.headers = {'Accept': 'application/' + self.format,
        'Content-type': 'application/' + self.format
        }
        return RequestData(uri=self.uri, method=self.method, data=self.data, headers=self.headers)
