from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=128, unique=True)
	slug = models.SlugField(unique=True)
	
	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)

	class Meta:
		verbose_name_plural = "Categories"

class Place(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	name = models.CharField(max_length=128)
	description = models.CharField(max_length=10000)
	slug = models.SlugField(unique=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Place, self).save(*args, **kwargs)

	def __str__(self):
		return self.name

class Review(models.Model):
	place = models.ForeignKey(Place, on_delete=models.CASCADE)
	rating = models.IntegerField()
	review_text = models.TextField()
	name = models.CharField(max_length=128)
	review_date = models.DateField()
	likes = models.IntegerField()
	dislikes = models.IntegerField()

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	picture = models.ImageField(upload_to='profile_images', blank=True)
	def __str__(self):
		return self.user.username

