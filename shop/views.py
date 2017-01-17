from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from shop.models import Good
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import random
from django.contrib import auth
from django.middleware.csrf import get_token
from datetime import datetime
from shop.forms import AppForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def shop(request, page_number = 1):

	if request.GET:
		s = request.GET['textarea'].strip()
		goods = Good.objects.filter(name = s.capitalize())
	else:
		goods = Good.objects.all()
	current_page = Paginator(goods, 4)
	context = {} 
	context.update(csrf(request))
	context['goods'] = current_page.page(page_number)
	context['username'] = auth.get_user(request).username

	return render(request,'shop/shop.html', context)

def get_good(request, good_id):

	good = get_object_or_404(Good, id = good_id)

	context = {} 
	context.update(csrf(request))

	context['good'] = good
	context['username'] = auth.get_user(request).username

	return render_to_response('shop/good.html', RequestContext(request, context))

def get_good_app(request, good_id):
	good = get_object_or_404(Good, id = good_id)
	form = AppForm(request.POST)

	print(form)

	context = {}
	context.update(csrf(request))
	context['form'] = form
	context['message'] = ''

	if request.POST and good.warhouse > 0:
		if form.is_valid():
			app = form.save(commit = False)

			if app.count > good.warhouse:
				context['message'] = 'Товаров на складе только ' + str(good.warhouse)
				return render_to_response('shop/goodapp.html', RequestContext(request, context))

			app.parent_user = request.user
			app.parent_good = good
			form.save()
			good.warhouse = good.warhouse - 1
			good.save()
			return render_to_response('shop/succes.html', RequestContext(request, context))
		else: 
			context['message'] = 'Некоторые данные заполнены неправильно'
			return render_to_response('shop/goodapp.html', RequestContext(request, context))
	else:
		if good.warhouse <= 0:
			context['message'] = 'К сожалению, товаров больше нет.'
		return render_to_response('shop/goodapp.html', RequestContext(request, context))
