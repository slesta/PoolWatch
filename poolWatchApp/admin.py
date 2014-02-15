from django.contrib import admin
from models import *

class PoolAdmin(admin.ModelAdmin):
    save_on_top = True
    #    readonly_fields = ('message_back', 'date_read', 'date_create',)
    list_display = ( 'name', 'currency', 'pageLoad', 'poolHashRate', 'htmlErr' )
    #list_editable = ( 'ip_id', 'ssh_type_id', 'activ', )
    #list_filter = ('date_create',)
    #search_fields = ['fwname', 'router']
    readonly_fields = ( 'pageLoad', 'poolHashRate', 'htmlErr')
    #raw_id_fields = ('router', )
    #inlines = [FwaclinlinesInline, FwfiltersInline, FwnatsInline]
    fieldsets = [
        ( None, {'fields': ['name', 'currency', 'pageLoad', 'poolHashRate', 'url', 'urlstats', 'urljson', 'htmlErr']}),
        ]

# currency name url urlstats urljson pageLoad poolHashRate poolEfficiency dateCreate lastUpdate responseErr


admin.site.register(Pool, PoolAdmin)
admin.site.register(Currency)