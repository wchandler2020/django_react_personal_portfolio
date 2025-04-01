from django.db import models

class Hero(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=150)
    summary = models.TextField()
    image = models.ImageField(upload_to='hero/images', default='default/default-user.jpg')
    
    def __str__(self) -> str:
        return self.name
    
class Experience(models.Model):
    company_name = models.CharField(max_length=250)
    job_title = models.CharField(max_length=100)
    duties_1 = models.CharField(max_length=150)
    duties_2 = models.CharField(max_length=150, blank=True, null=True)
    duties_3 = models.CharField(max_length=150, blank=True, null=True)
    duties_4 = models.CharField(max_length=150, blank=True, null=True)
    technologies_used = models.CharField(max_length=500)
    start_date = models.DateField()
    end_date = models.DateField()
    
    def __str__(self) -> str:
        return self.company_name
    
class About(models.Model):
    summary = models.TextField()
    image = models.ImageField(upload_to='hero/images', default='default/default-user.jpg')

    def __str__(self) -> str:
        return str(self.summary).split(' ')[:8]
    

    
    
