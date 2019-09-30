from rest_framework import serializers
from .models import Book, Publish
from django.contrib.auth.models import User

class BookSerializer(serializers.ModelSerializer):


    ownere = serializers.ReadOnlyField(source='ownere.username')
    highlight = serializers.HyperlinkedIdentityField(
        view_name='book-highlight', format='html')
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'amount', 'ownere')




class UserSerializer(serializers.HyperlinkedModelSerializer):

    # 这里的 book 和模型中 related_name 定义的名字要相同
    books = serializers.HyperlinkedRelatedField(many=True, view_name='book-detail',queryset=Book.objects.all())
    # book_name = serializers.ReadOnlyField(source=books.username)
    print("*****", books)
    # bb = serializers.StringRelatedField()
    class Meta:
        model = User
        fields = ('id', 'username', 'books')




class PublishSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Publish
        fields = ("id", "name", "address")


