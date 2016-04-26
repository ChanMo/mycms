from django.shortcuts import render
from django.views.generic import View, TemplateView
from .models import *

class BaseView(View):
    def get_context_data(self, **kwargs):
        context = super(BaseView, self).get_context_data(**kwargs)
        context['menu_list'] = Menu.objects.root_nodes().order_by('sort')
        return context

class HomeView(BaseView, TemplateView):
    template_name = 'default/index.html'

class PageView(BaseView, TemplateView):
    def get_context_data(self, **kwargs):
        context = super(PageView, self).get_context_data(**kwargs)
        page = Page.objects.get(slug=self.kwargs['slug'])
        self.page = page
        context['page'] = page
        context['children_list'] = self.page.children.all()
        if self.page.parent:
            context['sibling_list'] = self.page.parent.children.all()
        return context

    def get_template_names(self, **kwargs):
        return 'default/%s.html' % self.page.template
