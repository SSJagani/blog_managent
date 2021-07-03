from django.db import models

# Create your models here.

class Contact(models.Model):
	contact_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)
	email = models.CharField(max_length=70,default="")
	phone = models.CharField(max_length=70,default="")
	desc = models.TextField()
	timestmp = models.DateField(auto_now_add=True , blank=True)

	def __str__(self):
		return self.name