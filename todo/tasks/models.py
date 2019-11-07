from django.db import models
from datetime import datetime
from django.urls import reverse

class Tasklist(models.Model):
	title=models.TextField()
	text=models.TextField()
	created_at=models.DateField(default=datetime.now)


	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('detail', args=[self.id])
