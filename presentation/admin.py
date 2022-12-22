from django.contrib import admin
from .models import *


@admin.register(Subject)
class SubjecteAdmin(admin.ModelAdmin):
    list_display = ['title', 'color']


@admin.register(Presentation)
class PresentationAdmin(admin.ModelAdmin):
    list_display = ['num', 'subject', 'title']
    list_filter = ('subject',)


@admin.register(PresentationDetail)
class PresentationDetailAdmin(admin.ModelAdmin):
    list_display = ['presentation']
    list_filter = ('presentation',)