# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Project, Occupation, Position, Accomplishment, CoverLetterParagraph, Media

# Register your models here.
admin.site.register(Project)
admin.site.register(Occupation)
admin.site.register(Position)
admin.site.register(Accomplishment)
admin.site.register(CoverLetterParagraph)
admin.site.register(Media)