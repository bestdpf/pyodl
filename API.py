#!/usr/bin/python
"""
"""
from ODL import *
from TopologyAPI import *
import requests

class API(object):
    def __init__(self,odl,container='default',format='json'):
        self.odl=odl
        self.container=container
        self.format=format
        self.topology=TopologyAPI(format=self.format)
        self.request_data=None
        self.base_uri='http://'+self.odl.domain+':'+ self.odl.port+'/controller/nb/v2'
        self.full_uri=None
        self.response=None
        self.method_table={'GET':requests.get,'PUT':requests.put, 'DELETE':requests.delete,'POST':requests.post}
        self.method=None

    def set_container(self,container):
        self.container=container

    def retrieve_the_topology(self,container=None):
        if container is None:
            container=self.container
        self.request_data=self.topology.retrieve_the_topology(container)
        return self.requestx(self.request_data)

    def requestx(self,request_data):
        self.full_uri=self.base_uri+request_data.uri
        self.method=self.method_table[request_data.method]
        self.response=self.method(self.full_uri,auth=self.odl.auth,data=request_data.data,headers=request_data.data)
        print('req uri: {2} \n{0}\n{1}'.format(self.response.status_code,self.response.text,self.full_uri))
        return self.response

