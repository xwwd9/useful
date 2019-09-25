from django.db import models

# Create your models here.



from django.db import models

class Book(models.Model):
    title = models.CharField(null=True, blank=True, max_length=50)
    author = models.CharField(null=True, blank=True, max_length=50)
    amount = models.IntegerField()
    ownere = models.ForeignKey('auth.User', related_name='books' ,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

