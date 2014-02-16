#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'lacina'

import sys
import os
import re
import urllib2
import time



#
# # Preamble so we can use Django's DB API
path = os.path.normpath(os.path.join(os.getcwd(), '..'))
sys.path.append(path)
sys.path.append(os.path.abspath(__file__))
# #sys.path.append('/usr/share/pyshared/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'PoolWatch.settings'

# Load up Django
from poolWatchApp.models import *


class PoolT():
    url = ''
    currency = ''
    domain = ''
    httpURL = ''
    httpsURL = ''
    statsUrl = ''
    type = ''
    htmlOfGivenUrl = ''
    htmlOfGivenUrlClear = ''
    state = False
    stateStats = False
    statHtml = ''
    statHtmlClear = ''
    statUrlJSON = ''
    currencyCheckPage = ''

    # vycisti url
    def cleanURL(self):
        self.url = self.url.replace('http://', '')
        self.url = self.url.replace('https://', '')
        cleanr = re.compile('/[\S]*')
        self.url = re.sub(cleanr, '', self.url)
        self.domain = re.sub(r"""^[a-zA-Z0-9-_]*.""", '', self.url)
        self.httpURL = 'http://' + self.url
        self.httpsURL = 'https://' + self.url

    def getHtml(self, url):
        hdr = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'}
        #print url
        req = urllib2.Request(url, headers=hdr)
        error = False
        try:
            response = urllib2.urlopen(req)
        except urllib2.HTTPError, e:
            error = True
            pass
        except urllib2.URLError, e:
            error = True
            pass
        if not error:
            return response.read()
        else:
            return False


    def cleanHtml(self, html):
        cleanr = re.compile('<.*?>')
        return re.sub(cleanr, '', html)


    # Otestuje typ poolu
    def testPool(self):
        self.htmlOfGivenUrl = False
        self.htmlOfGivenUrl = self.getHtml(self.httpURL)
        if self.htmlOfGivenUrl:
            self.htmlOfGivenUrlClear = self.cleanHtml(self.htmlOfGivenUrl)
            if re.search("MPOS by TheSerapher", self.htmlOfGivenUrlClear):
                self.type = "MPOS"
                self.state = True
                self.statsUrl = self.httpURL + '/index.php?page=statistics&action=pool'
                self.statUrlJSON = self.httpURL + '/index.php?page=api&action=getpoolstatus&api_key='
                self.currencyCheckPage = self.httpURL + '/index.php?page=gettingstarted'

    def testPoolCurrency(self):
        if self.state:
            self.stateStats = False
            self.state = False
            self.htmlOfGivenUrl = False
            self.htmlOfGivenUrl = self.getHtml(self.currencyCheckPage)
            if self.htmlOfGivenUrl:
                self.htmlOfGivenUrlClear = self.cleanHtml(self.htmlOfGivenUrl)
                #print self.htmlOfGivenUrlClear
                if re.search(self.currency.shortname.lower(), self.htmlOfGivenUrlClear):
                    self.stateStats = True
                    self.state = True
                if re.search(self.currency.shortname, self.htmlOfGivenUrlClear):
                    self.stateStats = True
                    self.state = True


    # otestuje dostupnost statistik
    def testPoolStats(self):
        if self.state:
            self.htmlOfGivenUrl = False
            self.htmlOfGivenUrl = self.getHtml(self.statsUrl)
            if self.htmlOfGivenUrl:
                self.htmlOfGivenUrlClear = self.cleanHtml(self.htmlOfGivenUrl)
                #print self.htmlOfGivenUrlClear
                if re.search('General Statistics', self.htmlOfGivenUrlClear):
                    self.stateStats = True



                    # prida pool

    def addPool(self):
        #print 1
        if self.stateStats:
            #print 2
            if Pool.objects.filter(url=self.httpURL).count() == 0:
                #print 3
                pool = Pool()
                pool.name = self.url
                pool.url = self.httpURL
                pool.urlstats = self.statsUrl
                pool.urljson = self.statUrlJSON
                pool.currency = self.currency
                pool.save()


urlStack = UrlStack.objects.all() #filter(processed=False)
currencies = Currency.objects.all()

for urlItem in urlStack:
    poolT = PoolT()
    poolT.url = urlItem.url
    poolT.currency = urlItem.currency
    poolT.cleanURL()
    poolT.testPool()
    if poolT.state == False:
        urlItem.processed = True
        urlItem.save()
        pass
    poolT.testPoolStats()
    poolT.addPool()
    urlItem.processed = True
    urlItem.save()
    #print poolT.stateStats
    for currency in currencies:
        time.sleep(0.2)
        poolTry = PoolT()
        poolTry.url = 'http://' + currency.shortname.lower() + '.' + poolT.domain
        poolTry.currency = currency
        poolTry.cleanURL()
        poolTry.testPool()
        if poolTry.state == False:
            pass
        poolTry.testPoolCurrency()
        if poolTry.state == False:
            pass
        poolTry.testPoolStats()
        poolTry.addPool()
        urlItem.multipool = True
        urlItem.save()



