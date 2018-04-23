import logging

try:
    import simplejson as json
except ImportError:
    import json
import requests


def log_request(response):
    url = ''
    request_method = ''
    http_code = ''
    payload = ''

    try:
        url = response.request.url
    except:
        pass

    try:
        payload = response.request.body
    except:
        pass

    try:
        resp = response.json()
    except:
        resp = str(response)

    try:
        request_method = response.request.method
    except:
        pass

    try:
        http_code = response.status_code
    except:
        pass

    logging.info(
        "\t\t\t Captured http request:"
        "\n** last response: HTTP {}"
        "\n** url: {}"
        "\n** method: {}"
        "\n** payload: {}"
        "\n** response: {}"
            .format(
            http_code,
            url,
            request_method,
            payload,
            resp,
        )
    )


def remove_none_from_dict(d):
    if type(d) is dict:
        return dict((k, remove_none_from_dict(v)) for k, v in zip(d.keys(), d.values())
                    if v is not None and remove_none_from_dict(v) != {})
    # elif type(d) is list:
    #     return [remove_none_from_dict(v) for v in d if v is not None and remove_none_from_dict(v)]
    else:
        return d


def extract_payload(data=None):
    payload = remove_none_from_dict(data) if data else None
    return json.dumps(payload) if payload else None


class Requestor(object):
    def __init__(self, host):
        self.host = host
        self._headers = {}

    def headers(self, headers=None):
        self._headers = {'Content-type': 'text/plain'}

        if headers:
            self._headers.update(headers)

        return self._headers

    def _post(self, data=None, headers=None, params=None):


        payload = extract_payload(data)
        params = params or {}
        response = requests.post(
            self.host,
            data=payload,
            params=params,
            headers=self.headers(headers=headers)
        )
        log_request(response)
        return response


class Api(Requestor):
    def __init__(self, host):
        super().__init__(host)

    def make_request(self, **kwargs):
        data = {}
        for name, value in kwargs.items():
            data[name] = value
        return self._post(data)

    def get_blocks(self, **kwargs):
        _data = {
            "method": "call",
            "id": 0,
            "params": [
                "database_api",
                "get_block", [
                    kwargs.get('block_id')
                ]
            ],
            "jsonrpc": "2.0"
        }
        return self._post(data=_data)

    def get_dynamic_global_properties(self, **kwargs):
        _data = {
            "method": "call",
            "id": 0,
            "params": [
                "database_api",
                "get_dynamic_global_properties", []
            ],
            "jsonrpc": "2.0"
        }

        return self._post(data=_data)
