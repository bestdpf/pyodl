#!/usr/bin/python
"""
OpenDaylight Python Northband API
author: Pengfei Tuan
email: pengfeituan at gamil dot com
school: Graduate School at Shenzhen, Tsinghua Univ.
"""
import json
import requests
from requests.auth import *

class ODL_Call(object):
    """
    ODL Callable base class, used to generate uri from
    attribute names. Users can ingore it.
    """
    def __init__(self,callable_cls):
        self.callable_cls=callable_cls

    def __getattr__(self,name):
        try:
            return object.__getattr__(self,name)
        except AttributeError:
            return self.callable_cls(self.callable_cls)
    """
    def __call__(self,kwargs):
        print('unkwon function named {0}'.format(kwargs))
    """
class ODL(ODL_Call):
    def __init__(self,domain='localhost',port='8080',auth,format):
        ODL_Call.__init__(self,callable_cls=ODL_Call)
        self.domain=domain
        self.port=port
        self.auth=auth
        self.format=format

