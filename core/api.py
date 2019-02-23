import requests
import json


class ItbookApi(object):

    results = []

    def __init__(self):
        try:
            url = "https://api.itbook.store/1.0/search/mongodb"
            self.results = (requests.get(url)).json()['books']
        except:
            self.results = []

    def get_result(self):
        return [result for result in self.results]