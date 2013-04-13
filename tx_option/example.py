#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2013 george 
#
# Distributed under terms of the MIT license.

from core import *
from source import get_options

opts = get_options()
result = -999999

#隨機取樣1000組找解
for i in xrange(10000):
    #隨機組合
    combination = random_combination(opts)
    #設定分數
    value = combination.wighted_arvage_gain([7000,7500]) * combination.arvage_gain
    if value > result:
        result = value
        comb = combination


combination = random_combination([opts[0]])
print value
print comb.arvage_gain
print comb.opts
