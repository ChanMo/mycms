#!/usr/bin/python
# vim: set fileencoding=utf8 :
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from mptt.models import MPTTModel, TreeForeignKey

class Page(MPTTModel):
    title = models.CharField(max_length=200, verbose_name='标题')
    slug = models.SlugField(allow_unicode=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    cover = models.ImageField(upload_to='page/%Y/%m/%d/', verbose_name='图片', null=True, blank=True)
    intro = models.TextField(verbose_name='描述', null=True, blank=True)
    content = RichTextUploadingField(verbose_name='内容', null=True, blank=True)
    template = models.CharField(max_length=50, default='default')
    is_publish = models.BooleanField(default=True, verbose_name='是否发布')
    sort = models.PositiveIntegerField(default=0, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    def __unicode__(self):
        return self.title
    def parent_name(self, parent=False):
        name = ''
        for item in self.get_ancestors():
            if parent:
                name += item.title + ','
            else:
                name += '---'
        name += ' ' + self.title
        return name
    class Meta(object):
        verbose_name = '文章'
        verbose_name_plural = '文章'
        ordering = ['sort']
    class MPTTMeta:
        order_insertion_by = ['title']


class Menu(MPTTModel):
    name = models.CharField(max_length=200, verbose_name='名称')
    slug = models.SlugField()
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True, verbose_name='上级菜单')
    link = models.URLField(verbose_name='网址')
    sort = models.PositiveIntegerField(default=0, blank=False, null=False)
    def __unicode__(self):
        return self.name
    class Meta(object):
        verbose_name = '菜单'
        verbose_name_plural = '菜单'
        ordering = ['sort']
    class MPTTMeta:
        order_insertion_by = ['name']
