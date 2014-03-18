"""
"""
from RequestData import *

class BasicAPI(object):
    def __init__(self,format,app):
        self.app=app
        self.uri=None
        self.data=None
        self.headers=None
        self.method=None
        self.format=format
        self.sec=False
