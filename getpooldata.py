#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'lacina'

import sys, os, re, urllib2, datetime, random
import time
import socket


#
# # Preamble so we can use Django's DB API
path = os.path.normpath(os.path.join(os.getcwd(), '..'))
sys.path.append(path)
sys.path.append(os.path.abspath(__file__))
# #sys.path.append('/usr/share/pyshared/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'PoolWatch.settings'

# Load up Django
from django.db import models
from poolWatchApp.models import *
from django.contrib.auth.models import User as AuthUser





import urllib2

def getData(pool):
    address = pool.urlstats
    req = urllib2.Request(address, headers={'User-Agent' : "Magic Browser"})
    try:
        response = urllib2.urlopen(req)
    except urllib2.HTTPError, e:
        pool.responseErr= e.fp.read()
        pool.save()
    finally:
        pass


    html = response.read()
    return html

def pageParser(pool, html):
    import re

    # common variables

    rawstr = r"""(?:[\W\S]*Pool Hash Rate)(?:[\W\S]*e">)(?P<poolHashRate>[0-9.]*)(?:[\S]+>[ ]*)(?P<poolHashRateUnit>[\S]*)(?:<[\S\W]*)(?:Pool Efficiency[\W\S]*td>)(?P<poolEfficiency>[0-9.%]*)(?:<[\W\S]*Current Difficulty[\S\W]*ff">)(?P<CDiff>[0-9.]*)"""
    matchstr = html
    #print matchstr

    # method 1: using a compile object
    compile_obj = re.compile(rawstr)
    match_obj = compile_obj.search(matchstr)


    # Retrieve group(s) by name
    poolHashRate = match_obj.group('poolHashRate')
    poolHashRateUnit = match_obj.group('poolHashRateUnit')
    poolEfficiency = match_obj.group('poolEfficiency')
    CDiff = match_obj.group('CDiff')
    print poolEfficiency
    if poolHashRateUnit == 'MH/s':
        poolHashRate=float(poolHashRate)*1000
    pool.poolHashRate = poolHashRate
    pool.poolEfficiency = float(poolEfficiency.replace('%', ''))
    pool.currency.cdif=float(CDiff)
    pool.save()



#print getData('https://cash.hash.so')
poolList = Pool.objects.all()
for pool in poolList:
    pageParser(pool, html=getData(pool))



