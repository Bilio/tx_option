#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2013 george 
#
# Distributed under terms of the MIT license.

from core import Option
import urllib2
from lxml import html

__all__ = ['get_options']

def get_value(td):
    try:
        result = td.cssselect('a')[0] if td.cssselect('a') else td
        result = float(result.text.strip())
    except Exception,e:
        result = False
    finally:
        return result


def get_options():
    body = html.fromstring(urllib2.urlopen('http://tw.screener.finance.yahoo.net/future/aa03?opmr=optionfull&opcm=WTXO&opym=201312').read())
    datas = body.cssselect('tr')[4:]

    result = []
    for row in datas:
        values = [ get_value(td) for td in row.cssselect('td')]
        strike_price = values[7]
        if values[1]:
            result.append(Option(method="call", target=strike_price, cost=values[1]))

        if values[9]:
            result.append(Option(method="put", target=strike_price, cost=values[9]))

    return result

