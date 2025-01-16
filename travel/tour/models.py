from django.db import models
from django.contrib.auth.models import User


class TourCategory(models.Model):
	name = models.CharField(max_length=255)
	picture = models.ImageField(upload_to='images/', blank=True, null=True)

	def get_image(self):
		if self.picture:
			return self.picture.url
		else:
			return ''

	def __str__(self):
		return self.name


class Tours(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	picture = models.ImageField(upload_to='images/', blank=True, null=True)
	price = models.DecimalField(decimal_places=2, max_digits=7)
	category = models.ManyToManyField(TourCategory, related_name='tours')

	def __str__(self):
		return f'Tour name: {self.name}, price: {self.price}$'

	def get_image(self):
		if self.picture:
			return self.picture.url
		else:
			return ''


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishlist')
    tour = models.ForeignKey(Tours, on_delete=models.CASCADE, related_name='wishlisted_by')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'tour')

    def __str__(self):
        return f"{self.user.username} - {self.tour.name}"



class Request(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"Request by {self.name}"