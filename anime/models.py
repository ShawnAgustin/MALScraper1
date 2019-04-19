from django.db import models

# Create your models here.
class Show(models.Model):

	title 		= models.CharField(max_length=100,null=True,blank=True)
	weebtitle 	= models.CharField(max_length=100)
	url 		= models.URLField()
	image_url	= models.URLField(null=True)
	showtype 	= models.CharField(max_length=10)
	episodes 	= models.IntegerField(blank=True,null=True)
	rating		= models.FloatField(blank=True,null=True)
	mal_id		= models.IntegerField(unique=True, primary_key=True)

	def __str__(self):
		return self.weebtitle

	