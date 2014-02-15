#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'lacina'

import sys, os, re, urllib2, datetime, random
import time
import socket

PYTHONPATH=myprojectdir:$PYTHONPATH
DJANGO_SETTINGS_MODULE=project.settings.production virtualenv/bin/django-admin.py updateactivites


# Preamble so we can use Django's DB API
path = os.path.normpath(os.path.join(os.getcwd(), '..'))
sys.path.append(path)
sys.path.append(os.path.abspath(__file__))
#sys.path.append('/usr/share/pyshared/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'PoolWatch.settings'

# Load up Django
from django.db import models
from poolWatchApp.models import *
from django.contrib.auth.models import User as AuthUser


nastaveni=Generalset.objects.get(pk=1)

import urllib2

def getData(address):
    response = urllib2.urlopen(address)
    html = response.read()
    return html

def pageParser(html):
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
    print poolHashRate
    print poolHashRateUnit
    print poolEfficiency
    print CDiff


#print getData('https://cash.hash.so')
pageParser(getData('https://cash.hash.so/index.php?page=statistics&action=pool'))

