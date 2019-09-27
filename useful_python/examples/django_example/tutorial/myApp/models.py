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



class Publish(models.Model):
    name = models.CharField(max_length=32, verbose_name="名字", unique=True)
    address = models.CharField(max_length=32, verbose_name="地址")

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "出版社"
        verbose_name_plural = verbose_name