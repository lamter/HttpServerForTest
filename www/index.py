#coding=utf-8
'''
Created on 2015-05-25

@author: Shawn
'''

import datetime

from flask import render_template
import gevent

from service import app

__author__ = 'lamter'

@app.route('/')
def index():
    return 'hello world'