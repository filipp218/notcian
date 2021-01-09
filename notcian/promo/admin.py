from django.contrib import admin

from promo.models import Advert
# Register your models here.

class AdvertAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("title",)}

admin.site.register(Advert,AdvertAdmin)

