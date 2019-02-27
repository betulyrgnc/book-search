from django.contrib import admin

from core.models import Bookmark

class BookmarkAdmin(admin.ModelAdmin):
    fieldsets = (
        ('HashTag General Informations', {
            'fields' : ('title',)
        }),
    )

    list_display = ('title',)
    search_fields = ('title',)
    ordering = ('title',)

admin.site.register(Bookmark, BookmarkAdmin)
