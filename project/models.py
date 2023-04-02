from djongo import models

# Create your models here.
class Contact1(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    query=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name
# class Todo(models.Model):
#     task=models.CharField(max_length=30)
#     description=models.CharField(max_length=100)
# class Payments(models.Model):
# class Profile(models.Model):
    
#     id=models.ObjectIdField()
#     Email=models.CharField(max_length=100)
#     bio=models.BooleanField(default=False)

    