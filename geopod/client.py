#!/usr/bin/env python
# encoding: utf-8
"""
client.py

Copyright (c) 2011 Indie Energy Systems Company, LLC.. All rights reserved.
"""

import oauth2 as oauth
import simplejson
import urllib
import urllib2


API_HOST = "indiegeopod.com"
API_PORT = 80
API_VERSION = "v1"


class Client(object):
    
    def __init__(self, token_key, token_secret, consumer_key, consumer_secret, host=API_HOST, port=API_PORT):
        self.token = oauth.Token(token_key, token_secret)
        self.host = host
        self.port = port
        self.consumer = oauth.Consumer(consumer_key, consumer_secret)
        
    def request(self, target, method='GET', params={}):
        assert method in ['GET', 'POST'], "Only 'GET' and 'POST' are allowed for method."
        
        body = ''
        client = oauth.Client(self.consumer, self.token)
        
        if method == 'GET':
            base = self.build_full_url(target, params)
        else:
            base = self.build_full_url(target)
            body = self._urlencode(params)
        
        resp, content = client.request(base, method=method, body=body)
        
        if resp.get('status', '') == '200':
            try:
                response = simplejson.loads(content)
            except simplejson.decoder.JSONDecodeError, err:
                response = dict(error="JSON Parse Error (%s):\n%s" % (err, content))
        else:
            response = dict(error=content)
        return response
        
    def build_full_url(self, target, params={}):
        port = "" if self.port == 80 else ":%d" % self.port
        base_full_url = "http://%s%s" % (self.host, port)
        return base_full_url + self.build_url(target, params)
        
    def build_url(self, url, params={}):
        target_path = urllib2.quote(url)
        
        if params:
            return "/api/%s%s?%s" % (API_VERSION, target_path, self._urlencode(params))
        else:
            return "/api/%s%s" % (API_VERSION, target_path)

    def _urlencode(self, params):
        p = []
        for key, value in params.iteritems():
            if isinstance(value, (list, tuple)):
                for v in value:
                    p.append((key+'[]', v))
            else:
                p.append((key, value))
        return urllib.urlencode(p)


class UserClient(Client):
    
    def geopods(self):
        return self.request("/geopods/")


class GeopodClient(Client):
    
    def __init__(self, geopod, token_key, token_secret, consumer_key, consumer_secret, host=API_HOST, port=API_PORT):
        super(self.__class__, self).__init__(token_key, token_secret, consumer_key, consumer_secret, host, port)
        self.geopod = geopod
        
    def build_full_url(self, target, params={}):
        port = "" if self.port == 80 else ":%d" % self.port
        base_full_url = "http://%s.%s%s" % (self.geopod, self.host, port)
        return base_full_url + self.build_url(target, params)
    
    def info(self):
        return self.request("/")

