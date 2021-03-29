from django.db import models

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=128, unique=True)
	
	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Categories"

class Place(models.Model):


	def __str__(self):
		return self.title

class Review(models.Model):


	def __str__(self):
		return self.title


class UserProfile(models.Model):


	def __str__(self):
		return self.user.username