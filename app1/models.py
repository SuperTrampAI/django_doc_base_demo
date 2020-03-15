import datetime

from django.db import models


# Create your models here.
from django.utils import timezone


class Book(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=1023)

    @classmethod
    def create(cls, title):
        book = cls(title=title)
        return book

    class Meta:
        db_table = 'tb_book'


# 使用：
# book= Book.create('Pride and Prejudice')

# 语法二
class BookManager(models.Model):
    def create_book(self, title):
        book = self.create(title=title)
        return book


class Book2(models.Model):
    title = models.CharField(max_length=100)
    objects = BookManager()

    class Meta:
        db_table = 'tb_book2'


# 使用：
# book=Book.objects.create_book('Pride and Prejudice')

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('deta published')

    # 通过增加str方法，可以把字段显示出来
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now=timezone.now()
        return now-datetime.timedelta(days=1)<=self.pub_date<=now
        #self.pub_date>=timezone.now()-datetime.timedelta(days=1)
        was_published_recently.admin_order_field='pub_date'
        was_published_recently.boolean=True
        was_published_recently.short_description='Published recently?'



class Choice(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text



