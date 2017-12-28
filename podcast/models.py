from django.db import models


class Channel(models.Model):
    # RSS 2.0
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    link = models.URLField()
    description = models.TextField()

    language = models.CharField(max_length=5, blank=True)
    copyright = models.CharField(max_length=255, blank=True)

    managing_editor = models.EmailField(blank=True)
    web_master = models.EmailField(blank=True)

    pub_date = models.DateTimeField(blank=True, null=True)
    last_build_date = models.DateTimeField(blank=True, null=True)

    # iTunes
    subtitle = models.CharField(max_length=255, blank=True)
    summary = models.TextField(blank=True)
    # category = models.ManyToManyField(ChildCategory, related_name='show_categories', blank=True)
    # explicit = models.CharField(max_length=255, default='No', choices=EXPLICIT_CHOICES, blank=True)
    block = models.BooleanField(default=False,)
    redirect = models.URLField(blank=True)
    keywords = models.CharField(max_length=255, blank=True)
    itunes = models.URLField('iTunes Store URL', blank=True)

    def __str__(self):
        return self.title