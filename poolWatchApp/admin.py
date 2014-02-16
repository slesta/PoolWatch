from django.contrib import admin

from models import *


class PoolAdmin(admin.ModelAdmin):
    save_on_top = True
    #    readonly_fields = ('message_back', 'date_read', 'date_create',)
    list_display = (
        'name', 'currency', 'pageLoadPrint', 'poolHashRatePrint', 'poolEfficiencyPrint', 'lastUpdate', 'htmlErr')
    #list_editable = ( 'ip_id', 'ssh_type_id', 'activ', )
    list_filter = ('currency',)
    #search_fields = ['fwname', 'router']
    readonly_fields = (
        'pageLoadPrint', 'poolHashRate', 'htmlErr', 'poolEfficiencyPrint', 'lastUpdate', 'poolHashRatePrint')
    #raw_id_fields = ('router', )
    #inlines = [FwaclinlinesInline, FwfiltersInline, FwnatsInline]
    fieldsets = [
        (None, {'fields': ['name', 'currency', 'url', 'urlstats', 'urljson', 'pageLoadPrint',
                           'poolHashRatePrint', 'poolEfficiencyPrint', 'htmlErr', 'lastUpdate']}),
    ]

# currency name url urlstats urljson pageLoad poolHashRate poolEfficiency dateCreate lastUpdate responseErr


class CurrencyAdmin(admin.ModelAdmin):
    save_on_top = True
    #    readonly_fields = ('message_back', 'date_read', 'date_create',)
    list_display = (
        'name', 'shortname', 'cdif')
    #list_editable = ( 'ip_id', 'ssh_type_id', 'activ', )
    #list_filter = ('currency',)
    #search_fields = ['fwname', 'router']
    readonly_fields = ('cdif', 'date')
    #raw_id_fields = ('router', )
    #inlines = [FwaclinlinesInline, FwfiltersInline, FwnatsInline]
    fieldsets = [
        (None, {'fields': ['name', 'shortname', 'cdif', 'date']}),
    ]

# name shortname cdif date

admin.site.register(Pool, PoolAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(UrlStack)