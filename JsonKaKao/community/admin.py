from django.contrib import admin
from .models import Community, Comment, Like

# Register your models here.
admin.site.register(Community)
admin.site.register(Comment)
admin.site.register(Like)
