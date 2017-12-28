from django.contrib import admin
from . import models


class ChannelAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Channel, ChannelAdmin)