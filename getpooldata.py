#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'lacina'

import sys
import os
import re
import urllib2
import datetime
import time



# #
# # # Preamble so we can use Django's DB API
# path = os.path.normpath(os.path.join(os.getcwd(), '..'))
# sys.path.append(path)
# sys.path.append(os.path.abspath(__file__))
# # #sys.path.append('/usr/share/pyshared/')
# os.environ['DJANGO_SETTINGS_MODULE'] = 'PoolWatch.settings'


def setup_environment():
    pathname = os.path.dirname(sys.argv[0])
    sys.path.append(os.path.abspath(pathname))
    sys.path.append(os.path.normpath(os.path.join(os.path.abspath(pathname), '../')))
    os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

# Must set up environment before imports.
setup_environment()


# Load up Django
from poolWatchApp.models import *


def getData(pool):
    address = pool.urlstats
    hdr = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}
    req = urllib2.Request(address, headers=hdr)
    html = ''
    pool.responseErr = ''
    start = time.time()
    #print start
    try:
        response = urllib2.urlopen(req)
    except urllib2.HTTPError, e:
        pool.responseErr = e.fp.read()
        pass
    konec = time.time()
    pool.pageLoad = konec - start
    pool.lastUpdate = datetime.datetime.now()
    pool.save()
    html = response.read()

    #Vyčistí od tagu
    cleanr = re.compile('<script>.*?</script>')
    cleantext = re.sub(cleanr, '', html)
    cleanr = re.compile('<head>.*</head>')
    cleantext = re.sub(cleanr, '', cleantext)
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', cleantext)
    #print cleantext

    # soup = BeautifulSoup(html)
    # blacklist = ["script", "style"]
    # for tag in soup.findAll():
    #     if tag.name.lower() in blacklist:
    #         # blacklisted tags are removed in their entirety
    #         tag.extract()
    # print unicode(soup)

    return html


def pageParser(pool, html):
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
        poolHashRate = float(poolHashRate) * 1000
    pool.poolHashRate = poolHashRate
    pool.poolEfficiency = float(poolEfficiency.replace('%', ''))
    pool.currency.cdif = float(CDiff)

    pool.save()
    curr = Currency.objects.get(pk=pool.currency.id)
    curr.cdif = float(CDiff)
    curr.save()
    print pool.currency.cdif


#print getData('https://cash.hash.so')
currencies = Currency.objects.all()
for currency in currencies:
    currency.cdif = 0
    currency.save()
poolList = Pool.objects.select_related()
for pool in poolList:
    pageParser(pool, html=getData(pool))



