from django.contrib import admin
from shop.models import Good, GoodImage, GoodApp

# Register your models here.

class ImagesInLine(admin.TabularInline):
	model = GoodImage

class GoodAdmin(admin.ModelAdmin):
	inlines = [
		ImagesInLine,
	]

admin.site.register(Good, GoodAdmin)
admin.site.register(GoodApp)

