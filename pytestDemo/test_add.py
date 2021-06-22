#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author ：Jian
@Date ：2021/6/22 9:58 下午 
"""
from Calculator import Calculator
class TestCal:

    def setup(self):
        print("setup")
        self.calc = Calculator()

    def teardown(self):
        print("teardown")

    def test_add(self):
        # calc = Calculator()
        assert 2 == self.calc.add(1, 1)

    def test_add1(self):
        # calc = Calculator()
        assert 0.2 == self.calc.add(0.1, 0.1)

