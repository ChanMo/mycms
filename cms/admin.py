#!/usr/bin/python
# vim: set fileencoding=utf8 :
from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import Page, Menu

class MenuAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('parent', 'name', 'slug', 'link')
    list_display_links = ('parent',)
    list_filter = ('parent',)
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}

class ParentListFilter(admin.SimpleListFilter):
    title = ('主菜单')
    parameter_name = 'parentpage'
    def lookups(self, request, model_admin):
        list = Page.objects.root_nodes()
        a = ()
        for item in list:
            a += ((item.id, item.title),)
        return a

    def queryset(self, request, queryset):
        if self.value():
            current = Page.objects.get(id=self.value())
            list = current.get_descendants()
            return queryset.filter(id__in=[i.id for i in list])
        else:
            return queryset

class PageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('parent_name', 'title', 'slug', 'is_publish', 'created')
    list_display_links = ('parent_name',)
    list_filter = (ParentListFilter, 'is_publish', 'created', 'updated')
    search_fields = ['title', 'intro']
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'parent', 'cover', 'intro', 'content')
        }),
        ('高级设置', {
            'classes': ('collapse',),
            'fields' : ('template', 'is_publish')
        }),
    )
    date_hierarchy = 'created'
    empty_value_display = '-empty-'

admin.site.register(Menu, MenuAdmin)
admin.site.register(Page, PageAdmin)
