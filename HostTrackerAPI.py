"""
"""
from BasicAPI import *
from RequestData import *

class HostTrackerAPI(BasicAPI):
    def __init__(self,format):
        BasicAPI.__init__(self,format,app='hosttracker')

    def retrieve_host_by_address(self,networkAddress,container):
        self.uri='/' + self.app + '/' + container + '/address/' + networkAddress
        self.methd = 'GET'
        self.data = None
        self.headers = {'Content-type' : 'application/' + self.format}
        return RequestData(uri=self.uri,method=self.method,data=self.data,headers=self.headers)

    def add_host(self,networkAddress,hostConfig,container):
        self.uri='/' + self.app + '/' + container + '/address/' + networkAddress
        self.method = 'PUT'
        self.data = hostConfig
        self.headers = {'Content-type' : 'application/' + self.format}
        return RequestData(uri=self.uri,method=self.method,data=self.data,headers=self.headers)

    def del_host(self,networkAddress,container):
        self.uri= '/' + self.app + '/' + container +'/address/' + networkAddress
        self.method = 'DELETE'
        self.data = None
        self.headers = {'Content-type' : 'application/' + self.format}
        return RequestData(uri=self.uri,method=self.method,data=self.data,headers=self.headers)

    def retrieve_active_hosts(self,container):
        self.uri = '/' + self.app + '/' + container + '/hosts/active'
        self.method = 'GET'
        self.data = None
        self.headers = {'Content-type' : 'application/' + self.format}
        return RequestData(uri=self.uri,method=self.method,data=self.data,headers=self.headers)

    def retrieve_inactive_hosts(self,container):
        self.uri = '/' + self.app + '/' + container + '/hosts/inactive'
        self.method = 'GET'
        self.data = None
        self.headers = {'Content-type' : 'application/' + self.format}
        return RequestData(uri=self.uri,method=self.method,data=self.data,headers=self.headers)


