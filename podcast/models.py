from django.db import models


class Channel(models.Model):
    # RSS 2.0
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
    ttl = models.PositiveIntegerField(
        verbose_name='TTL',
        blank=True,
        null=True,
        help_text='The number of minutes a channel can be cached before refreshing.',
    )
    generator = models.CharField(max_length=255, blank=True)

    # iTunes
    subtitle = models.CharField(max_length=255, blank=True)
    summary = models.TextField(blank=True)
    redirect = models.URLField(blank=True)
    keywords = models.CharField(max_length=255, blank=True)
    itunes = models.URLField('iTunes Store URL', blank=True)
    block = models.BooleanField(
        default=False, help_text='Block this podcast on iTunes.')

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
    # guid        OPTIONAL
    # source      OPTIONAL
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    link = models.URLField()
    description = models.TextField(help_text='The item synopsis.')
    pud_date = models.DateTimeField()
    author = models.EmailField(
        help_text='Email address of the author of the item.', blank=True)
    guid = models.CharField(
        max_length=255,
        unique=True,
        blank=True,
        help_text='It\'s a string that uniquely identifies the item'
    )

    def __str__(self):
        return self.title


class Enclosure(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE)
    file = models.FileField(upload_to='podcasts/episodes/')

    def __str__(self):
        return self.file.name