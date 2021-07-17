from django.db import models
from django.utils import timezone

from . import managers


class Channel(models.Model):
    # RSS 2.0
    # title             REQUIRED
    # link              REQUIRED
    # description       REQUIRED
    # language          OPTIONAL
    # copyright         OPTIONAL
    # managingEditor    OPTIONAL
    # webMaster         OPTIONAL
    # pubDate           OPTIONAL
    # lastBuildDate     OPTIONAL
    # category          OPTIONAL
    # generator         OPTIONAL
    # docs              OPTIONAL
    # cloud             OPTIONAL
    # ttl               OPTIONAL
    # image             OPTIONAL
    # rating            OPTIONAL
    # textInput         OPTIONAL
    # skipHours         OPTIONAL
    # skipDays          OPTIONAL
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    link = models.URLField()
    description = models.TextField()

    language = models.CharField(max_length=5, blank=True)
    copyright = models.CharField(max_length=255, blank=True)
    managing_editor = models.EmailField(
        blank=True,
        help_text='Email address for person responsible for editorial content.'
    )
    web_master = models.EmailField(
        blank=True,
        help_text='Email address for person responsible for technical issues.'
    )
    pub_date = models.DateTimeField(blank=True, null=True)
    last_build_date = models.DateTimeField(blank=True, null=True)
    generator = models.CharField(max_length=255, blank=True)
    ttl = models.PositiveIntegerField(
        verbose_name='TTL',
        blank=True,
        null=True,
        help_text='The number of minutes a channel can be cached before refreshing.',
    )
    image = models.ImageField(
        upload_to='podcast/channel/', blank=True, null=True)

    # iTunes
    subtitle = models.CharField(max_length=255, blank=True)
    summary = models.TextField(blank=True)
    redirect = models.URLField(blank=True)
    keywords = models.CharField(max_length=255, blank=True)
    itunes = models.URLField('iTunes Store URL', blank=True)
    block = models.BooleanField(
        default=False, help_text='Block this podcast on iTunes.')
    explicit = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Item(models.Model):
    # title       REQUIRED
    # link        REQUIRED
    # description REQUIRED
    # enclosure   REQUIRED (new model)
    # pubDate     REQUIRED
    # author      OPTIONAL
    # category    OPTIONAL
    # comments    OPTIONAL
    # guid        OPTIONAL and UNIQUE
    # source      OPTIONAL

    STATUS_DRAFT = 1
    STATUS_PUBLIC = 2
    STATUS_PRIVATE = 3

    STATUS_CHOICES = (
        (STATUS_DRAFT, 'Draft'),
        (STATUS_PUBLIC, 'Public'),
        (STATUS_PRIVATE, 'Private'),
    )
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    status = models.PositiveIntegerField(choices=STATUS_CHOICES)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    link = models.URLField()
    description = models.TextField(help_text='The item synopsis.')
    pud_date = models.DateTimeField(default=timezone.now)
    author = models.EmailField(
        help_text='Email address of the author of the item.', blank=True)
    enclosure = models.FileField(upload_to='podcasts/items/')

    objects = models.Manager.from_queryset(managers.ItemQuerySet)()

    def __str__(self):
        return self.title
