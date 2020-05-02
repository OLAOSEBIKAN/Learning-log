from django.contrib import admin
from learning_logs.models import Topic, Entry
# Register your models here.


class TopicAdmin(admin.ModelAdmin):
    list_display = ['text']
    prepopulated_fields = {'slug': ('text',)}


class EntryAdmin(admin.ModelAdmin):
    list_display = ('topic', 'text',)
    prepopulated_fields = {'slug': ('text',)}


admin.site.register(Topic, TopicAdmin)
admin.site.register(Entry, EntryAdmin)

