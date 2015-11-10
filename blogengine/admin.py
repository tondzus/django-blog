from django.contrib import admin
from blogengine import models


class PostAdmin(admin.ModelAdmin):
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title', )}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Tag, TagAdmin)

