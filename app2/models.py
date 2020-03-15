from django.db import models


# Create your models here.

# 在模型中，如果不指定pk，django则自动创建pk

# django 操作数据库api文档：https://docs.djangoproject.com/zh-hans/3.0/topics/db/queries/
# 数据库表明为app name_person  app名_类名  可以改写
# 同名的models在往数据库执行完一次操作以后，再次执行，需要把django_migrations 表里面的对应的数据删除掉
class Person(models.Model):
    # 如果显示的指定了pk，则django不会再创建
    # id=models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    # z在类Meta中更改表名
    class Meta:
        db_table = 'db_person'



