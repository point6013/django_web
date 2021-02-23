from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Category(models.Model):
    """
    django  要求模型必须继承models.Model类
    Category 只需要一个简单的分类名称name就可以了
    CharField 指定了name字段的数据类型为文本，max_length规定了其名称的最大程度为200
    其他的数据类型可以参考Django的官方文档
    https://docs.djangoproject.com/en/2.2/ref/models/fields/#field-types

    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    """
    标签和Category一样，继承models.Model类

    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    文章的字段与内容较多
   Category,Tag:
    自 django 2.0 以后，ForeignKey 必须传入一个 on_delete 参数用来指定当关联的数据被删除时，
    被关联的数据的行为，我们这里假定当某个分类被删除时，该分类下全部文章也同时被删除，
    因此使用 models.CASCADE 参数，意为级联删除。
    user:
    文章作者，这里 User 是从 django.contrib.auth.models 导入的
    """
    title = models.CharField(max_length=70)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    # 多对多的字段不适用on_delete
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
