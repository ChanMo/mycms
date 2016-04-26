#!/usr/bin/python
# vim: set fileencoding=utf8 :
from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import Page, Menu

class MenuAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'link')
    search_fields = ['name']


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created')
    list_filter = ('created', 'updated')
    search_fields = ['title', 'intro']
    prepopulated_fields = {'slug': ('title',)}
    view_on_site = True
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'content')
        }),
        ('高级设置', {
            'classes': ('collapse',),
            'fields' : ('parent', 'cover', 'intro', 'sort', 'template')
        }),
    )
    date_hierarchy = 'created'
    empty_value_display = '-empty-'

    def view_on_site(self, obj):
        return 'http://localhost:8000/%s' % obj.slug

admin.site.register(Menu, MenuAdmin)
admin.site.register(Page, PageAdmin)
