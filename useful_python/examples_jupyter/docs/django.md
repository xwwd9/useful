

# django笔记

[返回上一级](../README.md)


* 创建项目 django-admin startproject service

* 启动项目 python manage.py runserver 0.0.0.0:8008


* 创建一个app python manage.py startapp movie   
    (注意：需要将这个app加入到INSTALLED_APPS)


* 跟新模型  
    python manage.py makemigrations 
    python manage.py migrate 
    
    
* 给后台创建用户  
    python manage.py createsuperuser
    
    
* 主表查询子表  
    django 默认每个主表的对象都有一个是外键的属性，可以通过它来查询到所有属于主表的子表的信息。这个属性的名称默认是以子表的名称小写加上_set()来表示，也可以在创建外键的时候用related_name这个参数指定。
    ```python
    class Person(models.Model);
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





