from django.contrib import admin
from tours.models import Tour, Bgimg, Quote, Image, Review, App, Room

# Register your models here.
class RoomInLine(admin.TabularInline):
	model = Room

class ImagesInLine(admin.TabularInline):
	model = Image

class TourAdmin(admin.ModelAdmin):
	inlines = [
		ImagesInLine,
		RoomInLine,
	]

admin.site.register(Tour, TourAdmin)
admin.site.register(Bgimg)
admin.site.register(Quote)
admin.site.register(Review)
admin.site.register(App)