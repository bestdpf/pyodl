"""
"""
from BasicAPI import *
from RequestData import *


class ConnectionManagerAPI(BasicAPI):

    def __init__(self, format):
        BasicAPI.__init__(self, format, app='connectionmanager')

    def retrieve_all_nodes_of_controller(self, controllerIP):
        self.uri = '/' + self.app + '/nodes'
        if controllerIP is not None:
            self.uri = self.uri + '?controller=' + controllerIP
        self.method = 'GET'
        self.data = None
        self.headers = {'Content-type': 'application/' + self.format}
        return RequestData(uri=self.uri, method=self.method, data=self.data, headers=self.headers)

    def del_connection(self, connectionNodeId, connectionNodeType):
        self.uri = '/' + self.app + '/node/' + \
            connectionNodeType + '/' + connectionNodeId
        self.method = 'DELETE'
        self.data = None
        self.headers = {'Content-type': 'application/' + self.format}
        return RequestData(uri=self.uri, method=self.method, data=self.data, headers=self.headers)

    def add_management_connection_with_node(self, nodeId, nodeIPAddress, serverPort, nodeType):
        if nodeType is not None:
            self.uri = '/' + self.app + '/node/' + nodeId + \
                '/address/' + nodeIPAddress + '/' + '/port/' + serverPort
        else:
            self.uri = '/' + self.app + '/node/' + nodeType + '/' + nodeId + \
                '/address/' + nodeIPAddress + '/' + '/port/' + serverPort
        self.method = 'PUT'
        self.data = None
        self.headers = {'Content-type': 'application/' + self.format}
        return RequestData(uri=self.uri, method=self.method, data=self.data, headers=self.headers)
