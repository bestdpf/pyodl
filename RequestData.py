#!/usr/bin/python
"""
"""
class RequestData(object):
    def __init__(self,uri,method,data,headers):
        self.uri=uri
        self.method=method
        self.data=data
        self.headers=headers
