from django.contrib import admin

from tasks.models import Task, Tag

admin.site.register(Tag)
admin.site.register(Task)
