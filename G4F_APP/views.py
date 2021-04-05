from django.shortcuts import render,redirect
from django.http import HttpResponse
from G4F_APP.models import Category, Place, Review, UserProfile
from G4F_APP.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic.edit import DeleteView


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


@login_required
def register_profile(request):
	form = UserProfileForm()

	if request.method == 'POST':
		form = UserProfileForm(request.POST, request.FILES)

		if form.is_valid():
			user_profile = form.save(commit=False)
			user_profile.user = request.user
			user_profile.save()
			return redirect(reverse('index'))
		else:
			print(form.errors)
	context_dict = {'form': form}
	return render(request, 'profile_registration.html', context_dict)

class ProfileView(View):
	def get_user_details(self, username):
		try:
			user = User.objects.get(username=username)
		except User.DoesNotExist:
			return None
		user_profile = UserProfile.objects.get_or_create(user=user)[0]
		form = UserProfileForm({'picture': user_profile.picture})
		return (user, user_profile, form)

	@method_decorator(login_required)
	def get(self, request, username):
		context_dict = {}
		try:
			(user, user_profile, form) = self.get_user_details(username)
		except TypeError:
			return redirect(reverse('index'))
		context_dict = {'user_profile': user_profile, 'selected_user': user, 'form': form}
		try:
			reviews = Review.objects.filter(name=username)
			context_dict['reviews'] = reviews
		except Review.DoesNotExist:
			context_dict['reviews'] = None
		return render(request, 'profile.html', context_dict)


	@method_decorator(login_required)
	def post(self, request, username):
		try:
			(user, user_profile, form) = self.get_user_details(username)
		except TypeError:
			return redirect(reverse('index'))
		form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
		if form.is_valid():
			form.save(commit=True)
			return redirect('profile', user.username)
		else:
			print(form.errors)
		context_dict = {'user_profile': user_profile, 'selected_user': user, 'form': form}
		return render(request, 'profile.html', context_dict)

class ListProfilesView(View):
	@method_decorator(login_required)
	def get(self, request):
		profiles = UserProfile.objects.all()
		return render(request, 'list_profiles.html', {'userprofile_list': profiles})

class DeleteReviewView(DeleteView):
	model = Review
	template_name = 'delete_view.html'
	success_url = reverse_lazy('index')


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


