from django.contrib import admin

from .models import Review, WatchList


class WatchListAdmin(admin.ModelAdmin):
    list_display = ("title", "platform", "active", "created")


admin.site.register(WatchList, WatchListAdmin)
admin.site.register(Review)
