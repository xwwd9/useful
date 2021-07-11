from django.db import models

# Create your models here.


from django.db import models


class Book(models.Model):
    title = models.CharField(null=True, blank=True, max_length=50)
    author = models.CharField(null=True, blank=True, max_length=50)
    amount = models.IntegerField()
    ownere = models.ForeignKey('auth.User', related_name='books',
                               on_delete=models.CASCADE)

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


class MovieInfo(models.Model):
    imdb = models.CharField(max_length=32, verbose_name="电影编号",
                            primary_key=True)
    name = models.CharField(max_length=32, verbose_name="名字", unique=True)
    def __str__(self):
        return self.name


class MovieImgs(models.Model):
    id = models.CharField(u'电影编号', max_length=50, primary_key=True)
    imdb = models.ForeignKey(MovieInfo, related_name='imgs',
                             on_delete=models.CASCADE, null=True)
    movie_name = models.CharField(u'中文名字', max_length=50, null=True)

    def __str__(self):
        return self.movie_name
