"""
"""
from BasicAPI import *
from RequestData import *


class StatisticsAPI(BasicAPI):

    def __init__(self, format):
        BasicAPI.__init__(self, format, app='statistics')

    def retrieve_all_statistics(self, elementType, container):
        self.uri = '/' + self.app + '/' + container + '/' + elementType
        self.method = 'GET'
        self.data = None
        self.headers = {'Accept': 'application/' + self.format}
        return RequestData(uri=self.uri, method=self.method, data=self.data, headers=self.headers)

    def retrieve_node_statistics(self, nodeId, nodeType, elementType, container):
        self.uri = '/' + self.app + '/' + container + '/' + \
            elementType + '/node/' + nodeType + '/' + nodeId
        self.method = 'GET'
        self.data = None
        self.headers = {'Accept': 'application/' + self.format}
        return RequestData(uri=self.uri, method=self.method, data=self.data, headers=self.headers)
