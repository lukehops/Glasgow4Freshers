from django.db import models

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=128, unique=True)
	
	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Categories"

class Place(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	name = models.CharField(max_length=128)
	description = models.TextField()

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


