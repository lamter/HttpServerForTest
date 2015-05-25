#coding=utf-8
'''
Created on 2015-05-23

@author: Shawn
'''

from service import app
from gevent.pywsgi import WSGIServer

__author__ = 'lamter'


if __name__ == "__main__":
    # wsgi 的 Gevent 模式
    http = WSGIServer(('', 5000), app)
    http.serve_forever()