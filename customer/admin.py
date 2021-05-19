from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'date',
        'title',
        'rate',
    )

    ordering = ('date',)


admin.site.register(Review, ReviewAdmin)
