#coding=utf-8
'''
Created on 2015-05-23

@author: Shawn
'''

__author__ = 'lamter'

import traceback

from flask import Flask, flash, redirect, render_template, \
     request, url_for

import serverdata

app = Flask(__name__)
# app.debug = True
app.secret_key = 'some_secret'
''' 全局的数据容器 '''
# app.serverData = serverdata.ServerData()

from block import *
from index import *


if __name__ == "__main__":
    app.debug = False
    app.run(debug=True)

