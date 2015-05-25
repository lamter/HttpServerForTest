#coding=utf-8
'''
Created on 2015-05-23

@author: Shawn
'''

import datetime

import gevent

from service import app



__author__ = 'lamter'

@app.route('/wait/<int:second>')
def wait(second):
    b = datetime.datetime.now()
    beginTime = '%s-%s-%s %s:%s:%s' % (b.year, b.month,b.day, b.hour, b.minute, b.second)
    gevent.sleep(second)
    e = datetime.datetime.now()
    endTIme = '%s-%s-%s %s:%s:%s' % (e.year, e.month,e.day, e.hour, e.minute, e.second)
    return "from %s to %s " % (beginTime, endTIme)