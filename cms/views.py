from django.shortcuts import render
from django.views.generic import View, TemplateView
from .models import *
from banner.models import Banner

class BaseView(View):
    def get_context_data(self, **kwargs):
        context = super(BaseView, self).get_context_data(**kwargs)
        context['menu_list'] = Page.objects.root_nodes().filter(is_publish=True).order_by('sort')
        return context

class HomeView(BaseView, TemplateView):
    template_name = 'default/index.html'
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['home_banner'] = Banner.objects.filter(is_show=True, group_id=1)
        context['mini_banner'] = Banner.objects.filter(is_show=True, group_id=2)
        context['page_list'] = Page.objects.filter(is_publish=True)
        return context

class PageView(BaseView, TemplateView):
    def get_context_data(self, **kwargs):
        context = super(PageView, self).get_context_data(**kwargs)
        page = Page.objects.get(id=self.kwargs['pk'])
        self.page = page
        context['page'] = page
        context['current'] = self.page.get_root()
        context['children_list'] = page.get_children()
        return context
    def get_template_names(self, **kwargs):
        return 'default/%s.html' % self.page.template
