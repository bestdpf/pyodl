"""
"""
from BasicAPI import *
from RequestData import *


class SwitchManagerAPI(BasicAPI):

    def __init__(self, format):
        BasicAPI.__init__(self, format, app='switchmanager')

    def retrieve_all_nodes(self, container):
        self.uri = '/' + self.app + '/' + container + '/nodes'
        self.method = 'GET'
        self.data = None
        self.headers = {'Content-type': 'application/' + self.format}
        return RequestData(uri=self.uri, method=self.method, data=self.data, headers=self.headers)

    def save_nodes_config(self, container):
        self.uri = '/' + self.app + '/' + container + '/save'
        self.method = 'POST'
        self.data = None
        self.headers = {'Content-type': 'application/' + self.format}
        return RequestData(uri=self.uri, method=self.method, data=self.data, headers=self.headers)

    def retrieve_node_connectors_by_node(self, nodeId, nodeType, container):
        self.uri = '/' + self.app + '/' + container + \
            '/node/' + nodeType + '/' + nodeId
        self.method = 'GET'
        self.data = None
        self.headers = {'Content-type': 'application/' + self.format}
        return RequestData(uri=self.uri, method=self.method, data=self.data, headers=self.headers)

    def del_node_property(self, nodeId, propertyName, nodeType, container):
        self.uri = '/' + self.app + '/' + container + '/node/' + \
            nodeType + '/' + nodeId + '/property/' + propertyName
        self.method = 'DEL'
        self.data = None
        self.headers = {'Content-type': 'application/' + self.format}
        return RequestData(uri=self.uri, method=self.method, data=self.data, headers=self.headers)

    def add_node_property(self, nodeId, propertyName, propertyValue, nodeType, container):
        self.uri = '/' + self.app + '/' + container + '/node/' + nodeType + \
            '/' + nodeId + '/property/' + propertyName + '/' + propertyValue
        self.method = 'PUT'
        self.data = None
        self.headers = {'Content-type': 'application/' + self.format}
        return RequestData(uri=self.uri, method=self.method, data=self.data, headers=self.headers)

    def del_node_connector_property(self, nodeId, propertyName, nodeConnectorId, nodeType, nodeConnectorType, container):
        self.uri = '/' + self.app + '/' + container + '/nodeconnector/' + nodeType + '/' + \
            nodeId + '/' + nodeConnectorType + '/' + \
            nodeConnectorId + '/property/' + propertyName
        self.method = 'DEL'
        self.data = None
        self.headers = {'Content-type': 'application/' + self.format}
        return RequestData(uri=self.uri, method=self.method, data=self.data, headers=self.headers)

    def add_node_connector_property(self, nodeId, nodeConnectorId, nodeType, nodeConnectorType, propertyName, propertyValue, container):
        self.uri = '/' + self.app + '/' + container + '/nodeconnector/' + nodeType + '/' + nodeId + '/' + \
            nodeConnectorType + '/' + nodeConnectorId + \
            '/property/' + propertyName + '/' + propertyValue
        self.method = 'PUT'
        self.data = None
        self.headers = {'Content-type': 'application/' + self.format}
        return RequestData(uri=self.uri, method=self.method, data=self.data, headers=self.headers)
