from django.db import models

# Create your models here.
class Reporter(models.Model):
    name = models.CharField(max_length=70,verbose_name='Full Name')
    def __str__(self):
        return self.name
    
class Article(models.Model):
    pub_date =models.DateField()
    headline = models.CharField(max_length=100)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter,on_delete=models.CASCADE)

    def __str__(self):
        return self.headline