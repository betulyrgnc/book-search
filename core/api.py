import requests
import json


class ItbookApi(object):

    results = []

    def __init__(self, query):
        try:
            url = "https://api.itbook.store/1.0/search/{0}".format(query)
            self.results = (requests.get(url)).json()['books']
        except:
            self.results = []

    def get_result(self):
        return [result for result in self.results]
