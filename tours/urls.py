from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
from tours.views import tours, get_tour, get_app
from stcsite.views import main

urlpatterns = [
	url(r'^tours/all/$', tours, name = 'tours'),
	url(r'^page/(\d+)/$', tours, name = 'tours'),
	url(r'^tours/(?P<tour_id>[0-9]+)/$', get_tour, name = 'tour'),
	url(r'^tours/(?P<tour_id>[0-9]+)/get_app/$', get_app, name = 'app'),	
	url(r'^tours/(?P<tour_id>[0-9]+)/page/(\d+)/$', get_tour, name = 'tour'),
        url(r'^$', main, name = 'main'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
