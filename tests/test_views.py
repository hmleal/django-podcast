from django.test import Client, TestCase

from podcast import models

# https://docs.djangoproject.com/en/2.0/topics/testing/advanced/#testing-reusable-applications


class TestChannelViews(TestCase):
    def setUp(self):
        self.client = Client()

    def test_channel_list_view(self):
        resp = self.client.get('/podcasts/')

        self.assertEqual(200, resp.status_code)
        self.assertEqual('application/json', resp['Content-type'])

    def test_channel_detail_view(self):
        channel = models.Channel.objects.create(
            title='Nerdcast',
            slug='nerdcast',
            link='http://jovemnerd.com.br/nerdcast',
            description='Dummy description'
        )

        resp = self.client.get(
            '/podcasts/{0}/'.format(channel.slug))

        self.assertEqual(200, resp.status_code)
        self.assertEqual('application/json', resp['Content-type'])


class TestItemViews(TestCase):
    def setUp(self):
        self.client = Client()

    def test_item_detail_view(self):
        channel = models.Channel.objects.create(
            title='NerdCast',
            slug='nerdcast',
            link='http://jovemnerd.com.br/nerdcast',
            description='Dummy description'
        )

        item = models.Item.objects.create(
            channel=channel,
            title='NerdCast 30 - I See Nerd People',
            status=2,
            slug='nerdcast-30-i-see-nerd-people',
            link='https://jovemnerd.com.br/?podcast=nerdcast-30-i-see-nerd-people',
            description='Dummy description'
        )

        resp = self.client.get(
            '/podcasts/{0}/{1}/'.format(channel.slug, item.slug))

        self.assertEqual(200, resp.status_code)
        self.assertEqual('application/json', resp['Content-type'])

class TestRSSFeedView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_rss_feed_view(self):
        channel = models.Channel.objects.create(
            title='NerdCast',
            slug='nerdcast',
            link='http://jovemnerd.com.br/nerdcast',
            description='Dummy description'
        )

        resp = self.client.get('/podcasts/{0}/feed/'.format(channel.slug))

        self.assertEqual(200, resp.status_code)
        self.assertEqual('application/rss+xml', resp['Content-type'])
