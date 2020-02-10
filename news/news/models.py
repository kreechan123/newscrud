from django.db import models

# from newscontent.models import Category, Newsimage, Newsinfo
# Category.objects.all()

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Newsimage(models.Model):
    upload = models.FileField(upload_to='uploads/', null=True)
    caption = models.CharField(max_length=200)

class Newsinfo(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=200)
    pub_date = models.DateTimeField('date published', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    upload = models.FileField(upload_to='uploads/', null=True)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    def __str__(self):
        return f'{self.title} {self.content}'

# class User(models.Model):
#     name = models.CharField(max_length=50)
#     password = 
    

