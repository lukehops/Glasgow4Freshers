from django.shortcuts import render
from django.http import HttpResponse
from G4F_APP.models import Category, Place, Review
from G4F_APP.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

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

def show_place(request, category_name_slug, place_name_slug):
	context_dict = {}

	try:
		place = Place.objects.get(slug=place_name_slug)
		context_dict['place'] = place
	except Place.DoesNotExist:
		context_dict['place'] = None


	try:
		reviews = Review.objects.filter(place=place)
		context_dict['reviews'] = reviews
	except Review.DoesNotExist:
		context_dict['reviews'] = None

	try:
		category = Category.objects.get(slug=category_name_slug)
		context_dict['category'] = category
	except Category.DoesNotExist:
		context_dict['category'] = None


	return render(request, 'place.html', context=context_dict)

def register(request):
	registered = False

	if request.method == 'POST':
		user_form = UserForm(request.POST)
		profile_form = UserProfileForm(request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			profile = profile_form.save(commit=False)
			profile.user = user

			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']

			profile.save()
			registered = True
		else:
			print(user_form.errors, profile_form.errors)
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	return render(request,'register.html',context = {'user_form': user_form,'profile_form': profile_form,'registered': registered})

def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				return redirect(reverse('index'))
			else:
				return HttpResponse("Your Rango account is disabled.")
		else:
			print(f"Invalid login details: {username}, {password}")
			return HttpResponse("Invalid login details supplied.")
	else:
		return render(request, 'login.html')

@login_required
def user_logout(request):
	logout(request)
	return redirect(reverse('index'))


from datetime import datetime

@login_required
def leave_review(request):
        context_dict = {}
        if request.method == "POST":
                rating = request.POST.get('rating')

                if int(rating) < 0 or int(rating) > 5:
                	return HttpResponse("Rating must be between 0 and 5.")

                review_text = request.POST.get('review_text')
                place = Place.objects.get(name=request.POST.get('place'))
                date = datetime.now()
                user = request.user
                print(request.POST.get('url'))
                context_dict['url'] = request.POST.get('url')
                Review.objects.create(place=place, rating=rating, review_text=review_text, name=user, review_date=date, likes=0, dislikes=0)
        return render(request, 'review-success.html', context=context_dict)






