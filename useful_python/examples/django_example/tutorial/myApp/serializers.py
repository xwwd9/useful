from rest_framework import serializers
from .models import Book
from django.contrib.auth.models import User

class BookSerializer(serializers.ModelSerializer):


    ownere = serializers.ReadOnlyField(source='ownere.username')
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'amount', 'ownere')




class UserSerializer(serializers.ModelSerializer):

    # 这里的 book 和模型中 related_name 定义的名字要相同
    books = serializers.PrimaryKeyRelatedField(many=True, queryset=Book.objects.all())
    # book_name = books.title
    print("*****", books)
    # bb = serializers.StringRelatedField()
    class Meta:
        model = User
        fields = ('id', 'username', 'books')





