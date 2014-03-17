#!/usr/bin/python
"""
"""
class topologyUserLinkConfig():
    def __init__(self,srcNodeConnector,dstNodeConnector,status,name):
        self.srcNodeConnector=srcNodeConnector
        self.dstNodeConnector=dstNodeConnector
        self.status=status
        self.name=name
    def __repr__(self):
        
