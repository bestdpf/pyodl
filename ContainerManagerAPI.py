"""
"""
from BasicAPI import *
from RequestData import *


class ContainerManagerAPI(BasicAPI):

    def __init__(self, format):
        BasicAPI.__init__(self, format, app='containermanager')

    def retrieve_all_containers(self):
        self.uri = '/' + self.app + '/containers'
        self.method = 'GET'
        self.data = None
        self.headers = {'Content-type': 'application/' + self.format}
        return RequestData(uri=self.uri, method=self.method, data=self.data, headers=self.headers)

    def retrieve_container_config(self, container):
        self.uri = '/' + self.app + '/container/' + container
        self.method = 'GET'
        self.data = None
        self.headers = {'Content-type': 'application/' + self.format}
        return RequestData(uri=self.uri, method=self.method, data=self.data, headers=self.headers)

    def create_container(self, containerConfig):
        self.uri = '/' + self.app + '/container/' + \
            containerConfig['container']
        self.method = 'PUT'
        self.data = containerConfig
        self.headers = {'Content-type': 'application/' + self.format}
        return RequestData(uri=self.uri, method=self.method, data=self.data, headers=self.headers)

    def del_container(self, container):
        self.uri = '/' + self.app + '/container/' + container
        self.method = 'DELETE'
        self.data = None
        self.headers = {'Content-type': 'application/' + self.format}
        return RequestData(uri=self.uri, method=self.method, data=self.data, headers=self.headers)

    def retrieve_flowspecs_by_container(self, container):
        self.uri = '/' + self.app + '/container/' + container + '/flowspecs'
        self.method = 'GET'
        self.data = None
        self.headers = {'Content-type': 'application/' + self.format}
        return RequestData(uri=self.uri, method=self.method, data=self.data, headers=self.headers)

    def add_node_connectors_to_container(self, nodeConnectors, container):
        self.uri = '/' + self.app + '/container/' + \
            container + '/nodeconnecotor'
        self.method = 'PUT'
        self.data = nodeConnectors
        self.headers = {'Content-type': 'application/' + self.format}
        return RequestData(uri=self.uri, method=self.method, data=self.data, headers=self.headers)

    def del_node_connectors_from_container(self, nodeConnectors, container):
        self.uri = '/' + self.app + '/container/' + \
            container + '/nodeconnector'
        self.method = 'DELETE'
        self.data = nodeConnectors
        self.headers = {'Content-type': 'application/' + self.format}
        return RequestData(uri=self.uri, method=self.method, data=self.data, headers=self.headers)

    def retrieve_flowspec(self, flowspec, container):
        self.uri = '/' + self.app + '/container/' + \
            container + '/flowspec/' + flowspec
        self.method = 'GET'
        self.data = None
        self.headers = {'Content-type': 'application/' + self.format}
        return RequestData(uri=self.uri, method=self.method, data=self.data, headers=self.headers)

    def add_flowspec_to_container(self, flowSpecConfig, container):
        self.uri = '/' + self.app + '/container/' + \
            container + '/flowspec/' + flowSpecConfig['name']
        self.method = 'PUT'
        self.data = flowSpecConfig
        self.headers = {'Content-type': 'application/' + self.format}
        return RequestData(uri=self.uri, method=self.method, data=self.data, headers=self.headers)

    def del_flowspec_from_container(self, flowspec, container):
        self.uri = '/' + self.app + '/container/' + \
            container + '/flowspec/' + flowspec
        self.method = 'PUT'
        self.data = None
        self.headers = {'Content-type': 'application/' + self.format}
        return RequestData(uri=self.uri, method=self.method, data=self.data, headers=self.headers)
