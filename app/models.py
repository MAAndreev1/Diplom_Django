from django.db import models

# Create your models here.
class Users(models.Model):
    pass
    username = models.CharField(max_length=20,)
    password = models.CharField(max_length=20,)

    def __str__(self):
        return self.username


class Posts(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    date_of_creation = models.DateField()
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return self.title