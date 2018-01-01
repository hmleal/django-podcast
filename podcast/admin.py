from django.contrib import admin

from . import models


class EnclosureInLine(admin.StackedInline):
    model = models.Enclosure
    # display = ('user_questions_obj')


class ChannelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'link', 'image', 'description')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': (
                'language',
                'copyright',
                'managing_editor',
                'web_master',
                'pub_date',
                'last_build_date',
                'ttl',
                'generator'
            )
        }),
        ('iTunes', {
            'classes': ('collapse',),
            'fields': (
                'subtitle',
                'summary',
                'redirect',
                'keywords',
                'itunes',
                'explicit',
                'block'
            )
        })
    )


class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    inlines = [EnclosureInLine]


admin.site.register(models.Channel, ChannelAdmin)
admin.site.register(models.Item, ItemAdmin)
