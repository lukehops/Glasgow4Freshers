from django.contrib import admin
from G4F_APP.models import Category, Place, Review
from G4F_APP.models import UserProfile

class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')

# Register your models here.
admin.site.register(Category)
admin.site.register(Place,PlaceAdmin)
admin.site.register(Review)
admin.site.register(UserProfile)