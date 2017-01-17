from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from tours.models import Tour, Bgimg, Quote, Review, App, Room, Image
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import random
from django.contrib import auth
from django.middleware.csrf import get_token
from datetime import datetime
from tours.forms import AppForm
# Create your views here.

def tours(request, page_number = 1):
	tours = Tour.objects.all()
	current_page = Paginator(tours, 3)

	bgimgs = Bgimg.objects.all()
	bgimg = random.choice(bgimgs)
	context = { 
		'tours' : current_page.page(page_number),
		'bgimg' : bgimg,
		'username' : auth.get_user(request).username,
	}
	return render(request, 'tours/tours.html', context)

def get_tour(request, tour_id):

	tour = get_object_or_404(Tour, id = tour_id)
	quotes = Quote.objects.all()
	quote = random.choice(quotes)
	reviews = Review.objects.filter(parent_tour = tour).values('text', 'parent_user__username', 'date')
	paginator = Paginator(reviews, 3)
	page = request.GET.get('page')
	rooms = Room.objects.filter(parent = tour)
	photos = Image.objects.filter(parent = tour)

	try:
		reviews = paginator.page(page)
	except PageNotAnInteger:
		reviews = paginator.page(1)
	except EmptyPage:
		reviews = paginator.page(paginator.num_pages)

	context = {} 

	context.update(csrf(request))

	context['tour'] = tour
	context['username'] = auth.get_user(request).username
	context['quote'] = quote
	context['reviews'] = reviews
	context['rooms'] = rooms
	context['photos'] = photos

	if request.POST and request.POST['textarea'] != '': 
		review = Review(parent_user=request.user, parent_tour=tour, text = request.POST['textarea'], date = datetime.now())
		review.save()
		return render_to_response('tours/tour.html', RequestContext(request, context))

	else:
		return render_to_response('tours/tour.html', RequestContext(request, context))

def get_app(request, tour_id):
	tour = get_object_or_404(Tour, id = tour_id)
	form = AppForm(request.POST)
	app = App.objects.filter(parent_user=request.user)
	empty_app = []
	context = {}
	context.update(csrf(request))
	context['form'] = form
	context['message'] = ''

	print('emptyapp = ', len(empty_app))
	print('app = ', len(app))

	if len(app) != len(empty_app):
		context['message'] = 'Вы уже отправляли заявку на этот тур'
		return render_to_response('tours/app.html', RequestContext(request, context))

	if request.POST and tour.places > 0:
		if form.is_valid():
			app = form.save(commit = False)
			app.parent_user = request.user
			app.parent_tour = tour
			form.save()
			tour.places = tour.places - 1
			tour.save()
			return render_to_response('tours/succes.html', RequestContext(request, context))
		else: 
			context['message'] = 'Некоторые данные заполнены неправильно'
			return render_to_response('tours/app.html', RequestContext(request, context))
	else:
		if tour.places <= 0:
			context['message'] = 'К сожалению, мест больше нет.'
		return render_to_response('tours/app.html', RequestContext(request, context))
