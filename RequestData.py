"""
"""
import json


class RequestData(object):

    def __init__(self, uri, method, data, headers, sec=False):
        self.uri = uri
        self.method = method
        if type(data) is dict:
            self.data = json.dumps(data)
        else:
            self.data = data
        self.headers = headers
        self.sec = sec
