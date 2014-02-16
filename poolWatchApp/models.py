# coding: utf-8

from HTMLParser import HTMLParser

from django.db import models


class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return ''.join(self.fed)


def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()


class Currency(models.Model):
    name = models.CharField('Name', max_length=200, help_text='Currency name')
    shortname = models.CharField('Short name', max_length=8, help_text='Currency short name')
    cdif = models.FloatField('Current difficulty', default=0, blank=True, help_text='Current Diff')
    date = models.DateTimeField('Datum', auto_now_add=True, editable=False)


    def __unicode__(self):
        return self.name


    def was_published_today(self):
        return self.date.date() == datetime.date.today()

    class Meta:
        verbose_name = 'Currency'
        verbose_name_plural = 'Currencies'


class Pool(models.Model):
    currency = models.ForeignKey(Currency, verbose_name='Currency', editable=True)
    name = models.CharField('Name', max_length=200, help_text='')
    url = models.CharField('Pool URL', max_length="250", help_text='')
    urlstats = models.URLField('Pool`s page URL', max_length="400", blank=True, help_text='')
    urljson = models.URLField('JSON URL', max_length="400", blank=True, help_text='')
    pageLoad = models.FloatField('Page loaded', default=0, blank=True, help_text='Page load time.')
    poolHashRate = models.FloatField('Pool rate', default=0, blank=True, help_text='Pool hash rate.')
    poolEfficiency = models.FloatField('Pool efficiency', default=0, blank=True, help_text='Pool efficiency.')
    dateCreate = models.DateTimeField('Date create', auto_now_add=True, editable=False)
    lastUpdate = models.DateTimeField('Date updated', editable=False, blank=True, null=True)
    responseErr = models.CharField('Error', max_length=5000, help_text='', blank=True)


    def __unicode__(self):
        return self.name

    def was_published_today(self):
        return self.dateCreate.date() == datetime.date.today()

    def poolHashRatePrint(self):
        return str(self.poolHashRate / 1000) + ' MH/s'

    poolHashRatePrint.allow_tags = True
    poolHashRatePrint.admin_order_field = 'poolHashRate'
    poolHashRatePrint.short_description = 'Pool rate'

    def pageLoadPrint(self):
        return str(self.pageLoad * 1000) + ' ms'

    pageLoadPrint.allow_tags = True
    pageLoadPrint.admin_order_field = 'pageLoad'
    pageLoadPrint.short_description = 'Page loaded'

    def poolEfficiencyPrint(self):
        return str(self.poolEfficiency) + ' %'

    poolEfficiencyPrint.allow_tags = True
    poolEfficiencyPrint.admin_order_field = 'poolEfficiency'
    poolEfficiencyPrint.short_description = 'Pool efficiency'

    def htmlErr(self):
        return '<div>' + strip_tags(self.responseErr) + '</div>'

    htmlErr.allow_tags = True
    htmlErr.admin_order_field = 'responseErr'
    htmlErr.short_description = 'Response error'


    class Meta:
        verbose_name = 'Pool'
        verbose_name_plural = 'Pools'


class UrlStack(models.Model):
    currency = models.ForeignKey(Currency, verbose_name='Currency', editable=True)
    url = models.URLField('Pool URL', max_length="400", help_text='')
    processed = models.BooleanField('Processed', default=False)
    multiPool = models.BooleanField('Multi pool', default=False)


    def __unicode__(self):
        return self.url


    class Meta:
        verbose_name = 'URL'
        verbose_name_plural = 'URLs'