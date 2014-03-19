"""
"""
from RequestData import *
from BasicAPI import *


class FlowProgrammerAPI(BasicAPI):

    def __init__(self, format):
        BasicAPI.__init__(self, format, app='flowprogrammer')

    def retrieve_flows(self, container):
        self.uri = '/' + self.app + '/' + container
        self.method = 'GET'
        self.data = None
        self.headers = {'Accept': 'application/' + self.format}
        return RequestData(uri=self.uri, method=self.method, data=self.data, headers=self.headers)

    def retrieve_node_flows(self, nodeId, nodeType, container):
        self.uri = '/' + self.app + '/' + container + \
            '/node/' + nodeType + '/' + nodeId
        self.method = 'GET'
        self.data = None
        self.headers = {'Accept': 'application/' + self.format}
        return RequestData(uri=self.uri, method=self.method, data=self.data, headers=self.headers)

    def retrieve_flow_by_name(self, nodeId, flowName, nodeType, container):
        self.uri = '/' + self.app + '/' + container + '/node/' + \
            nodeType + '/' + nodeId + '/staticFlow/' + flowName
        self.method = 'GET'
        self.data = None
        self.headers = {'Accept': 'application/' + self.format}
        return RequestData(uri=self.uri, method=self.method, data=self.data, headers=self.headers)

    def del_flow_by_name(self, nodeId, flowName, nodeType, container):
        self.uri = '/' + self.app + '/' + container + '/node/' + \
            nodeType + '/' + nodeId + '/staticFlow/' + flowName
        self.method = 'DELETE'
        self.data = None
        self.headers = {'Accept': 'application/' + self.format}
        return RequestData(uri=self.uri, method=self.method, data=self.data, headers=self.headers)

    def toggle_flow_by_name(self, nodeId, flowName, nodeType, container):
        self.uri = '/' + self.app + '/' + container + '/node/' + \
            nodeType + '/' + nodeId + '/staticFlow/' + flowName
        self.method = 'POST'
        self.data = None
        self.headers = {'Accept': 'application/' + self.format}
        return RequestData(uri=self.uri, method=self.method, data=self.data, headers=self.headers)

    def add_or_modify_flow(self, flowConfig, container):
        self.uri = '/' + self.app + '/' + container + '/node/' + \
            flowConfig['node']['type'] + '/' + flowConfig['node']['id'] + '/staticFlow/' + flowConfig['name'] 
        self.method = 'PUT'
        self.data = flowConfig
        self.headers = {'Accept': 'application/' + self.format,
        'Content-type': 'application/' + self.format
        }
        return RequestData(uri=self.uri, method=self.method, data=self.data, headers=self.headers)
