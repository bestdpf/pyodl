"""
"""
from BasicAPI import *
from RequestData import *

class BridgeDomainAPI(BasicAPI):
    def __init__(self,format):
        BasicAPI.__init__(self,format,app='bridgedomain')

    def create_bridge(self,nodeType,nodeID,bridgeName):
        self.uri = '/networkconfig/' + self.app + '/bridge/' + nodeType + '/' + nodeID + '/' + bridgeName
        self.method = 'POST'
        self.data = None
        self.headers = {'Content-type' : 'application/' + self.format}
        return RequestData(uri=self.uri,method=self.method,data=self.data,headers=self.headers)

    def del_bridge(self,nodeType,nodeID,bridgeName):
        self.uri = '/networkconfig/' + self.app + '/bridge/'+ nodeType + '/' + nodeID + '/' + bridgeName
        self.method = 'DELETE'
        self.data = None
        self.headers = {'Content-type' : 'application/' + self.format}
        return RequestData(uri = self.uri,method=self.method,data=self.data,headers=self.headers)

    def add_port_to_bridge(self,nodeType,nodeID,bridgeName,portName):
        self.uri = '/netowrkconfig/' + self.app + '/bridge/' + nodeType + '/'+ nodeID + '/' + bridgeName + '/' + portName
        self.method = 'POST'
        self.data = None
        self.headres = {'Content-type' : 'application/' + self.format }
        return RequestData(uri=self.uri,method=self.method,data=self.data,headers=self.headers)

    def del_port_from_bridge(self,nodeType,nodeID,bridgeName,portName):
        self.uri = '/netowrkconfig/' + self.app + '/bridge/' + nodeType + '/'+ nodeID + '/' + bridgeName + '/' + portName
        self.method = 'DELETE'
        self.data = None
        self.headers = {'Content-type' : 'application/' + self.format }
        return RequestData(uri=self.uri,method=self.method,data=self.data,headers=self.headers)

    def add_port_vlan_to_bridge(self,nodeType,nodeID,bridgeName,portName,vlan):
        self.uri = '/networkconfig/' + self.app + '/port/' + nodeType + '/' +nodeID + '/' + bridgeName + '/' +portName + '/' + vlan
        self.method = 'POST'
        self.data = None
        self.headers = {'Content-type' : 'application/' + self.format}
        return RequestData(uri=self.uri,method=self.method,data=self.data,headers=self.headers)

