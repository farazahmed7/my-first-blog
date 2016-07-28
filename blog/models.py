from django.db import models
from django.utils import timezone

class Post(models.Model):
    
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
		
		
class Userdetail(models.Model):
    name = models.CharField(max_length=100)
    email_id = models.CharField(max_length=100)	
	
class Search(models.Model):	
	sem=models.CharField(max_length=100)
	def _str_(self):
		return self.title
	
       	
		
class SubjectBtechCS_1(models.Model):
	english=models.CharField(max_length=100)
	phy=models.CharField(max_length=100)
	chem=models.CharField(max_length=100)
	def _str_(self):
		return self.title
	
      