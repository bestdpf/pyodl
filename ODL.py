#!/usr/bin/python
"""
OpenDaylight Python Northband API
author: Pengfei Tuan
email: pengfeituan at gamil dot com
school: Graduate School at Shenzhen, Tsinghua Univ.
"""
import simplejson
import requests
from requests.auth import *

class ODL(object):
    def __init__(self,auth,domain,port):
        self.domain=domain
        self.port=port
        self.auth=auth

