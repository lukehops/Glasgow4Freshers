from django import forms
from django.contrib.auth.models import User
from G4F_APP.models import UserProfile
from G4F_APP.models import Review

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ('username', 'password',)

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('picture',)

class LeaveReviews(forms.ModelForm):
	review_rating = forms.IntegerField()
	review_text = forms.CharField()
	class Meta:
		model = Review
		fields = ('rating', 'review_text')
