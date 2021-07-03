from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from django.utils.timezone import now
# Create your models here.

class Blog(models.Model):
	post_id = models.AutoField(primary_key=True)
	autore_name= models.CharField(max_length=100)
	title = models.CharField(max_length=250)
	desc = RichTextUploadingField()
	views = models.IntegerField(default=0)
	slug = models.CharField(max_length = 130)
	pub_date = models.DateField(blank=True)

	def __str__(self):
		return self.title

class BlogComment(models.Model):
	sr_no= models.AutoField(primary_key = True)
	comment= models.TextField()
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	post=models.ForeignKey(Blog,on_delete=models.CASCADE)
	parent = models.ForeignKey('self' , on_delete=models.CASCADE,null=True)
	timestamp=models.DateTimeField(default=now)

	def __str__(self):
		return self.comment[:10]