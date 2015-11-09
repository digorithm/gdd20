# -*- coding: utf-8 -*-
import requests
import urlparse

from collections import namedtuple

CODES = requests.status_codes.codes

RESTClientResponse = namedtuple('RESTClientResponse', ['status', 'data'])

class RESTClientBase(object):

    def __init__(self, url, timeout=0.5):
        self.api_url = url
        self.timeout = timeout

        # session handles connection pooling
        self.session = requests.Session()

    def _configure_session(self, pool_size, max_retries):
        '''
          Replace default session http handler with one with this settings.
        '''
        adapter = requests.adapters.HTTPAdapter(
            pool_connections=pool_size,
            pool_maxsize=pool_size,
            max_retries=max_retries,
        )

        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)

    @property
    def extra_headers(self):
        return None

    def get(self, *args, **kwargs):
        return self._make_request('GET', *args, **kwargs)

    def post(self, *args, **kwargs):
        return self._make_request('POST', *args, **kwargs)

    def put(self, *args, **kwargs):
        return self._make_request('PUT', *args, **kwargs)

    def delete(self, *args, **kwargs):
        return self._make_request('DELETE', *args, **kwargs)

    def head(self, *args, **kwargs):
        return self._make_request('HEAD', *args, **kwargs)

    def patch(self, *args, **kwargs):
        return self._make_request('PATCH', *args, **kwargs)

    def _make_request(self, method, path, *args, **kwargs):
        url = self._url_for(path, *args)
        kwargs = self.prepare_kwargs(kwargs)
        kwargs['timeout'] = self.timeout

        response = self.call_request(method, url, **kwargs)
        return self.map_response(self._make_response(response))

    def _make_response(self, response):
        data = self.prepare_response(response)
        return RESTClientResponse(response.status_code, data)

    def _url_for(self, path, *args):
        url_path = (path % args) if args else path
        return self.api_url + url_path

    def prepare_kwargs(self, kwargs):
        headers = kwargs.get('headers', {})
        headers.update(self.extra_headers or {})

        kwargs['headers'] = headers
        return kwargs

    def prepare_response(self, response):
        return response.content

    def map_response(self, response):
        return response

    def call_request(self, method, url, **kwargs):
        return self.session.request(method, url, **kwargs)


class RESTClientJSONBase(RESTClientBase):

    extra_headers = {'content-type': 'application/json'}

    def prepare_response(self, response):
        return response.json()
