#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2013 george 
#
# Distributed under terms of the MIT license.
from collections import Counter
import random
from utils import memoized

__all__ = ['Option', 'OptionsCombination', 'random_combination']

class Option:
    def __init__(self, method, target, cost):
        self.method = method
        self.target = target
        self.cost = cost

        if method=="put":
            self.profit = self.put
        else:
            self.profit = self.call

    def __str__(self):
        return "method:{} target:{} cost:{}".format(self.method, self.target, self.cost)
    def __repr__(self):
        return "method:{} target:{} cost:{}".format(self.method, self.target, self.cost)
    def __unicode__(self):
        return "method:{} target:{} cost:{}".format(self.method, self.target, self.cost)
        
    #賣權獲利計算
    def put(self, point):
        result =  self.target - point
        result = result if result > 0 else 0
        return result

    #買權獲利計算
    def call(self, point):
        result = point - self.target
        result = result if result > 0 else 0
        return result

    


    def profit(self, point):
        pass



class OptionsCombination:
    now = 7791
    full = dict()
    quantity = 10
    width = 500
    ring_down_rate = 0.8
    wighted = 10


    def __init__(self, opts ):
        min_point = self.now - self.width
        max_point = self.now + self.width
        self.range = xrange(min_point, max_point, 5)

        self.opts = opts

    @property
    def min_gain(self):
        
        result=99999999999999
        for point in self.range:
            point_result=self.gain(point)
            result = min(result, point_result)

        return result
    @property
    def arvage_gain(self):

        result = 0
        for point in self.range:
            point_result=self.gain(point)
            result += point_result
        
        return result/ len(self.range)

    def wighted_arvage_gain(self, wighted_range):
        
        result=0
        for point in self.range:
            if point >= wighted_range[0] and point <= wighted_range[1]:
                wight=self.wighted
            else:
                wight=1

            point_result=self.gain(point)*wight
            result += point_result
        
        return result/ len(self.range)

    @memoized
    def gain(self, point):
        options = self.opts
        result = 0
        for option, quantity in options.items():
            result += option.profit(point)*quantity

        return result / self.cost
        
        

    @property
    def cost(self):
        result=0
        for option, quanty in self.opts.items():
            result += option.cost* quanty
        
        self.cost = result
        return self.cost


def random_combination(opts):
    quanty = 10
    result = []
    for i in xrange(quanty):
        result.append(random.choice(opts))
    return OptionsCombination(Counter(result))


