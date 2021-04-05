"""Glasgow4Freshers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from G4F_APP import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url 
from registration.backends.simple.views import RegistrationView
from django.urls import reverse, include, path
from G4F_APP.views import DeleteReviewView



class MyRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return reverse('register_profile')

app_name = 'G4F_APP'
urlpatterns = [
	path('', views.index, name="index"),
    path('admin/', admin.site.urls),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path('category/<slug:category_name_slug>/<slug:place_name_slug>', views.show_place, name='show_place'),
    path('register/', views.register, name='register'), 
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('accounts/register/', MyRegistrationView.as_view(), name='registration_register'),
    path('accounts/', include('registration.backends.simple.urls')),
    path('register_profile/', views.register_profile, name='register_profile'),
    path('profile/<username>/', views.ProfileView.as_view(), name='profile'),
    path('profiles/', views.ListProfilesView.as_view(), name='list_profiles'),
    path('delete/<int:pk>', DeleteReviewView.as_view(), name='delete_view'),
    path('leave_review/', views.leave_review, name='leave_review'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
