from django.contrib import admin
from djangoblog.blog.models import Entry


class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date','enable_comments', 'status')
    search_fields = ['title', 'body_html']
    list_filter = ('pub_date', 'enable_comments', 'status')
    prepopulated_fields = {"slug" : ('title',)}
    fieldsets = (
		(None, {'fields': (('title', 'status'), 'body_html', ('pub_date', 'enable_comments'), 'slug')}),
    )

admin.site.register(Entry, EntryAdmin)
