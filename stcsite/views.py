from django.shortcuts import render, get_object_or_404
from tours.models import Tour, Bgimg
from shop.models import Good
import random
from django.contrib import auth
# Create your views here.

def main(request):
	tours = Tour.objects.all()[:3]
	goods = Good.objects.all()[:3]
	bgimgs = Bgimg.objects.all()
	bgimg = random.choice(bgimgs)
	context = { 
		'tours' : tours,
		'bgimg' : bgimg,
		'username' : auth.get_user(request).username,
		'goods' : goods,
	}
	return render(request, 'stcsite/main.html', context)