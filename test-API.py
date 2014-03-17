#!/usr/bin/python
"""
"""
from API import *

odl=ODL(auth=HTTPBasicAuth('admin','admin'),domain='localhost',port='8080')
api=API(odl=odl)

api.retrieve_the_topology()

