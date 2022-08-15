from django.db import models


class Post(models.Model):
	title = models.CharField(max_length=50)
	body = models.TextField(max_length=300)
	resource_name = models.CharField(max_length=40)
	resource_url = models.URLField()

	def __str__(self):
		return self.title