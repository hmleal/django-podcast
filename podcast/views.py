from django.core import serializers
from django.http import HttpResponse
from django.views import generic

from . import models


class ChannelList(generic.TemplateView):
    def render_to_response(self, context, **kwargs):
        resp = self.get_data()
        return HttpResponse(resp, content_type='application/json', **kwargs)

    def get_data(self):
        qs = models.Channel.objects.all()
        return serializers.serialize('json', qs)


class ChannelDetail(generic.TemplateView):
    def render_to_response(self, context, **kwargs):
        resp = self.get_data()
        return HttpResponse(resp, content_type='application/json', **kwargs)


    def get_data(self):
        qs = models.Channel.objects.filter(slug=self.kwargs['slug'])
        return serializers.serialize('json', qs)


class ItemDetail(generic.TemplateView):
    def render_to_response(self, context, **kwargs):
        resp = self.get_data()
        return HttpResponse(resp, content_type='application/json', **kwargs)

    def get_data(self):
        qs = models.Item.objects.filter(slug=self.kwargs['item'])
        return serializers.serialize('json', qs)


class RSSFeed(generic.TemplateView):
    template_name = 'podcast/rss_feed.html'
    content_type = 'application/rss+xml'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['channel'] = models.Channel.objects.prefetch_related('item_set').get(slug=self.kwargs['channel'])

        return context
