from django.db import models


class contactform(models.Model):
    name=models.CharField(default='',max_length=50)
    email=models.EmailField(default='',max_length=100)
    contactNumber=models.IntegerField(default='')
    message=models.TextField()


    def __str__(self):
        return self.name


class training_course(models.Model):
    name=models.CharField(default='',max_length=100)
    image=models.ImageField(default='', upload_to='attachments/')
    description=models.TextField()
 
    def __str__(self):
        return self.name


class projects(models.Model):
    name=models.CharField(default='',max_length=100)
    image=models.ImageField(default='', upload_to='attachments/')
    description=models.TextField()
 
    def __str__(self):
        return self.name


class team(models.Model):
    name=models.CharField(default='',max_length=100)
    description=models.TextField()
 
    def __str__(self):
        return self.name

class gallery(models.Model):
    image=models.ImageField(default='', upload_to='attachments/')

 
