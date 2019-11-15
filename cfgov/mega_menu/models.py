from django.conf import settings
from django.db import models

from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailcore.fields import StreamField

from mega_menu.blocks import MenuStreamBlock


class Menu(models.Model):
    language = models.CharField(
        choices=settings.LANGUAGES,
        max_length=2,
        primary_key=True
    )

    submenus = StreamField(MenuStreamBlock())

    class Meta:
        ordering = ('language',)

    panels = [
        FieldPanel('language'),
        StreamFieldPanel('submenus'),
    ]

    def __str__(self):
        return str(dict(settings.LANGUAGES)[self.language])