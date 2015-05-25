#coding:utf-8
'''
Created on 2015-05-25

@author: Shawn
'''

__author__ = 'lamter'

from unittest import TestCase, makeSuite, TestSuite

from test_baseunit import *

from block import wait


def suite():
    testSuite1 = makeSuite(TestBlock, "test")
    alltestCase = TestSuite([testSuite1, ])
    return alltestCase

class TestBlock(TestBaseUnit):
    """
    单元测试
    """
    def test_block(self):
        """
        :return:
        """
        wait(1)


