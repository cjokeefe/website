from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	image = models.ImageField(blank=True, upload_to='post_images')
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title


	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})


	def save(self):
		super().save()

		if self.image:

			img = Image.open(self.image.path)

			if img.height > 600 or img.width > 600:
				output_size = (600, 600)
				img.thumbnail(output_size)
				img.save(self.image.path, quality=100)


class Comment(models.Model):
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.author.username + ' ' + str(self.date_posted))


class Tag(models.Model):
	name = models.CharField(max_length=64)
	posts = models.ManyToManyField(Post)

	def __str__(self):
		return str(self.name)