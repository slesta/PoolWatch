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


class PoolT():
    url=''
    domain=''
    httpURL=''
    httpsURL=''
    statsUrl=''
    type=''
    htmlOfGivenUrl=''
    htmlOfGivenUrlClear=''
    state=False
    statHtml=''
    statHtmlClear=''

# vycisti url
    def cleanURL(self):
        self.url=self.url.replace('http://', '')
        self.url=self.url.replace('https://', '')
        cleanr = re.compile('/[\S]*')
        self.url = re.sub(cleanr,'', self.url)
        self.domain = re.sub(r"""^[a-zA-Z0-9-_]*.""", '', self.url)

    def getHtml(url):
        hdr = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'}
        req = urllib2.Request(url, headers=hdr)
        error = False
        try:
            response = urllib2.urlopen(req)
        except urllib2.HTTPError, e:
            error=True
            pass
        if not error:
            return response.read()
        else:
            return False


    def cleanHtml(html):
        cleanr = re.compile('<.*?>')
        return re.sub(cleanr,'', html)


# Otestuje typ poolu
    def testPool(self):
        self.htmlOfGivenUrl = getHtml(url)
            cleanr = re.compile('<.*?>')
            self.htmlOfGivenUrlClear = re.sub(cleanr,'', self.htmlOfGivenUrl)
            #print poolT.htmlOfGivenUrlClear
            if re.search("MPOS by TheSerapher", self.htmlOfGivenUrlClear):
                self.type="MPOS"
                self.state = True
                self.statsUrl=poolT.httpURL+'/index.php?page=statistics&action=pool'

# otestuje dostupnost statistik
    def testPoolStats(self):





urlStack = UrlStack.objects.filter(processed=False)
for urlItem in urlStack:
    poolT=PoolT()
    poolT.url=urlItem.url
    html = poolT.getHtml(poolT.url)
    if html:
        poolT.htmlOfGivenUrl=url
        poolT.cleanHtml(html)
    poolT.cleanURL()
    poolT.testURL()
    print poolT.state

