"""
OpenDaylight Python Northband API
author: Pengfei Tuan
email: pengfeituan at gamil dot com
school: Graduate School at Shenzhen, Tsinghua Univ.
"""
from requests.auth import *

class ODL(object):
    def __init__(self,auth,domain,port,sec_port='8443'):
        self.domain=domain
        self.port=port
        self.sec_port=sec_port
        self.auth=auth

