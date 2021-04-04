from django.contrib import admin
from G4F_APP.models import Category, Place, Review
from G4F_APP.models import UserProfile

# Register your models here.
admin.site.register(Category)
admin.site.register(Place)
admin.site.register(Review)
admin.site.register(UserProfile)