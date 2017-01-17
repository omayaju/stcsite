from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
from shop.views import shop, get_good, get_good_app

urlpatterns = [
	url(r'^shop/$', shop, name = 'shop'),
	url(r'^shop/page/(\d+)/$', shop, name = 'shop'),
	url(r'^shop/good(?P<good_id>[0-9]+)/$', get_good, name = 'good'),
	url(r'^shop/good/(?P<good_id>[0-9]+)/get_app/$', get_good_app, name = 'goodapp'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

