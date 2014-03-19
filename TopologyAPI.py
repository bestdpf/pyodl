"""
"""
from RequestData import *
from BasicAPI import *


class TopologyAPI(BasicAPI):

    def __init__(self, format):
        BasicAPI.__init__(self, format, app='topology')

    def retrieve_the_topology(self, container):
        self.uri = '/' + self.app + '/' + container
        self.method = 'GET'
        self.data = None
        self.headers = {'Accept': 'application/' + self.format}
        return RequestData(uri=self.uri, method=self.method, data=self.data, headers=self.headers)

    def retrieve_userLinks(self, container):
        self.uri = '/' + self.app + '/' + container + '/userLinks'
        self.method = 'GET'
        self.data = None
        self.headers = {'Accept': 'application/' + self.format}
        return RequestData(uri=self.uri, method=self.method, data=self.data, headers=self.headers)

    def add_userLink(self, container, topologyUserLinkConfig):
        self.uri = '/' + self.app + '/' + container + \
            '/userLink/' + topologyUserLinkConfig['name']
        self.method = 'PUT'
        self.data = topologyUserLinkConfig
        self.headers = {'Accept': 'application/' + self.format,
        'Content-type' : 'application/' +self.format
        }
        return RequestData(uri=self.uri, method=self.method, data=self.data, headers=self.headers)

    def del_userLink(self, container, linkName):
        self.uri = '/' + self.app + '/' + container + '/userLink/' + linkName
        self.method = 'DELETE'
        self.data = None
        self.headers = {'Accept': 'application/' + self.format}
        return RequestData(uri=self.uri, method=self.method, data=self.data, headers=self.headers)
