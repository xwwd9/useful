

# django笔记

[返回上一级](../../README.md)



# django笔记

[返回上一级](../README.md)


* 创建项目 django-admin startproject service

* 启动项目 python manage.py runserver 127.0.0.1:8008


* 创建一个app python manage.py startapp movie   
    (注意：需要将这个app加入到INSTALLED_APPS)


* 跟新模型  
    python manage.py makemigrations 
    python manage.py migrate  
    
    
* 依赖安装
    pip install django_filter
    
* 给后台创建用户  
    python manage.py createsuperuser
    
    
* 主表查询子表  
    django 默认每个主表的对象都有一个是外键的属性，可以通过它来查询到所有属于主表的子表的信息。这个属性的名称默认是以子表的名称小写加上_set()来表示，也可以在创建外键的时候用related_name这个参数指定。
    ```python
    class Person(models.Model)
        name = models.CharField(verbose_name='作者姓名', max_length=10)
        age = models.IntegerField(verbose_name='作者年龄')


    class Book(models.Model):
        person = models.ForeignKey(Person, related_name='person_book')
        title = models.CharField(verbose_name='书籍名称', max_length=10)
        pubtime = models.DateField(verbose_name='出版时间')
      
    # 查询这个人的所有书
    person = Person.objects.fiter(你的条件)
    book = person.book_set.all()
  
    # 第二种方法
    person = models.ForeignKey(Person, related_name='person_books')
    person.person_books.all()
    ```

* Model
    * 自定义字段名称：title = models.CharField('标题', max_length=200, db_column='article_title')
    
    * 序列化有关联表的时候，可以用source字段指定序列化表的那个字段，或者直接在models中定义__str__函数直接返回需要字段
    ```
        1. cover_main_image = serializers.StringRelatedField(source="cover_main_image.cover_main_image_path")
        
        2. def __str__(self):
               return self.cover_main_image_path
    ```

* view
    * 指定lookup_field可以表明retrieve的时候查找的是哪个字段


* migration
    * python manage.py makemigrations & python manage.py migrate
前者是将model层转为迁移文件migration，后者将新版本的迁移文件执行，更新数据库。
    * python manage.py sqlmigrate movie 0001 查看创建语句



* [跨域请求](https://www.cnblogs.com/DI-DIAO/p/8977847.html)




## Django REST framework

*   给网址添加可选的格式后缀，诸如 http://localhost/book_list.json 之类的 URL。
    ```python
    # 首先在视图中添加一个 format 关键字参数：
    def book_list(request, format=None):
          pass
    
    # 现在更新 urls.py，给现有的 URL 后面添加一组 format_suffix_patterns：
    from rest_framework.urlpatterns import format_suffix_patterns
    
    # *****(urlpatterns具体代码)
    
    urlpatterns = format_suffix_patterns(urlpatterns)
    ```


*  创建一个外键  
    ```
    owner = models.ForeignKey('auth.User', related_name='books' ,on_delete=models.CASCADE)
    ```
    
*  有外键时候的序列化 
```
# 查出这本书属于哪个用户
owner = serializers.ReadOnlyField(source='ownere.username')

# 查出这个用户都有哪些书
books = serializers.PrimaryKeyRelatedField(many=True, queryset=Book.objects.all())
```


*  通过接口创建有外键的表的时候需要额外对这个外键进行操作  
    ```python
    #比如创建book的时候需要关联到创建的用户
    class BookList(generics.ListCreateAPIView):
        queryset = Book.objects.all()
        serializer_class = BookSerializer
        #添加访问权限
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
        def perform_create(self, serializer):
            serializer.save(owner=self.request.user)
    ```





* 跨域请求的时候前段设置localhost和127.0.0.1是有区别的





* 路由设置  
    * DefaultRouter的basename参数，创建url的名字，默认是viewset的queryset，所以如果viewset类中没用queryset属性，必须设置basename  
       ```
       router.register(r'guess', views.GuessYouLikeViewSet, "guess")
       ```

    
    
    




* 有用的文章
    * [restful 系列教程](https://www.cnblogs.com/yuzhenjie/p/10361880.html)
[返回上一级](../../README.md)


