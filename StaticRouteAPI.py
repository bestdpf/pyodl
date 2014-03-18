"""
"""
from BasicAPI import *
from RequestData import *


class StaticRouteAPI(BasicAPI):

    def __init__(self, format):
        BasicAPI.__init__(self, format, app='staticroute')

    def retrieve_all_static_routes(self, container):
        self.uri = '/' + self.app + '/' + container + '/routes'
        self.method = 'GET'
        self.data = None
        self.headers = {'Content-type': 'application/' + self.format}
        return RequestData(uri=self.uri, method=self.method, data=self.data, headers=self.headers)

    def retrieve_static_route_by_name(self, route, container):
        self.uri = '/' + self.app + '/' + container + '/route/' + route
        self.method = 'GET'
        self.data = None
        self.headers = {'Content-type': 'application/' + self.format}
        return RequestData(uri=self.uri, method=self.method, data=self.data, headers=self.headers)

    def add_static_route(self, route, staticRoute, container):
        self.uri = '/' + self.app + '/' + container + '/route/' + route
        self.method = 'PUT'
        self.data = staticRoute
        self.headers = {'Content-type': 'application/' + self.format}
        return RequestData(uri=self.uri, method=self.method, data=self.data, headers=self.headers)

    def del_static_route(self, route, container):
        self.uri = '/' + self.app + '/' + container + '/route/' + route
        self.method = 'DELETE'
        self.data = None
        self.headers = {'Content-type': 'application/' + self.format}
        return RequestData(uri=self.uri, method=self.method, data=self.data, headers=self.headers)
