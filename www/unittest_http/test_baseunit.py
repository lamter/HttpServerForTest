#coding:utf-8
'''
Created on 2015-05-25

@author: Shawn
'''

import sys
import os

sys.path.append(os.path.split(os.getcwd())[0])

from flask import url_for
from unittest import TestCase, makeSuite, TestSuite

from service import *

def suite():
    testSuite1 = makeSuite(TestBaseUnit, "test")
    alltestCase = TestSuite([testSuite1, ])
    return alltestCase

class TestBaseUnit(TestCase):
    """
    单元测试的父类
    """
    def setUp(self):
        """
        :return:
        """
        self.app = app


    def test_index(self):
        with app.test_request_context():
            print url_for('index')

