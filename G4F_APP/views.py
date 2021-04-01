from django.shortcuts import render
from django.http import HttpResponse
from G4F_APP.models import Category, Place, Review

# Create your views here.
def index(request):
	return render(request, 'index.html')

def show_category(request, category_name_slug):
	context_dict = {}

	try:
		category = Category.objects.get(slug=category_name_slug)
		places = Place.objects.filter(category=category)
		context_dict['places'] = places
		context_dict['category'] = category
	except Category.DoesNotExist:
		context_dict['category'] = None
		context_dict['places'] = None

	return render(request, 'categories.html', context=context_dict)
