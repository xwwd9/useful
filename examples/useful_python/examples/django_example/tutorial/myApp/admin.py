from django.contrib import admin

# Register your models here.


from .models import Book, MovieInfo, MovieImgs

admin.site.register(Book)

admin.site.register(MovieInfo)

admin.site.register(MovieImgs)







