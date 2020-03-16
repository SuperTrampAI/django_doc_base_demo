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
    birth_date=models.DateField

    # 可以在model中增加一些方法，可以在某个对象实例上操作
    def baby_boomer_status(self):
        "Returns the person's baby-boomer status."
        import datetime
        if self.birth_date < datetime.date(1945, 8, 1):
            return "Pre-boomer"
        elif self.birth_date < datetime.date(1965, 1, 1):
            return "Baby boomer"
        else:
            return "Post-boomer"

    @property
    def full_name(self):
        return '%s %s' %(self.first_name,self.last_name)

    def __str__(self):
        pass

    def get_absolute_url(self):
        pass

    # z在类Meta中更改表名
    class Meta:
        db_table = 'db_person'


# 音乐家
class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)


# 专辑
class Album(models.Model):
    # ForeignKey 多对一的关系
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()


# class Demo(models.Model):
# tb_column1=models.AutoField()  通常情况下，无需直接使用，如果没有自动，主键将自动添加到模型中
# models.BigAutoField() 类似于autofield ，big可以保存1~数字9223372036854775807
# models.BinaryField() 用于存储原始二进制数据
# models.CharField() 用于存储字符串 ，如果是大量文本，使用TextField
# models.DateField() 日期。参数（auto_now=False,auto_now_add=False,**）.auto_now 通常使用在最后修改时间的字段上，在调用save时，自动更新

# Field() 通用参数：
# null 默认为False
# blank 默认为False 设置为True ,该字段允许为空
# choices 给定字段的枚举类型
# SHIRT_SIZES = (
#         ('S', 'Small'),
#         ('M', 'Medium'),
#         ('L', 'Large'),
#     )
#
# 使用 shirt_size='L'
# default 该字段的默认值，可以是一个值，或是可调用对象
# help_text 帮助文本
# primary_key 如果设置为True 将该字段设置为该模型的主键
# class Runer(models.Model):
#     MedalType = models.TextChoices('MedalType', 'GOLD SILVER BRONZE')
#     medal = models.CharField(blank=True, choices=MedalType.choices, max_length=10)
class Fruit(models.Model):
    name = models.CharField(max_length=100, primary_key=True)


# unique 如果设置为True 这个字段的值是整个表中唯一的

# 在想要设置的主键的字段上，设置参数 primary_key=True ，django不会再创建id
# 字段备注名：verbose_name 如果未指定该值，会自动使用字段的属性名作为该参数值，吧下划线转换为空格。

# 关联关系  多对一，多对多，一对一
# 一个car模型有一个制造者Manufacture ，一个Manufacture可以制造多辆车
class Manufacturer(models.Model):
    pass


# 多对一
class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)


# 多对多
# 一个pizza有多种Topping ，一种Topping可能存在多个pizza中
class Topping(models.Model):
    pass


# 一般来讲，应该吧ManyToMany实例放在需要从在表单中被编辑的对象中，
# 在这个例子中就是：相比较于配料放在不同的披萨当中，披萨当中有很多种配料更加符合常理
class Pizza(models.Model):
    toppings = models.ManyToManyField(Topping)


# monyTomony的拓展
# class Person(models.Model):
#     name = models.CharField(max_length=128)
#
#     def __str__(self):
#         return self.name


class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.name


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)

# >>> ringo = Person.objects.create(name="Ringo Starr")
# >>> paul = Person.objects.create(name="Paul McCartney")
# >>> beatles = Group.objects.create(name="The Beatles")
# >>> m1 = Membership(person=ringo, group=beatles,
# ...     date_joined=date(1962, 8, 16),
# ...     invite_reason="Needed a new drummer.")
# >>> m1.save()
# >>> beatles.members.all()
# <QuerySet [<Person: Ringo Starr>]>
# >>> ringo.group_set.all()
# <QuerySet [<Group: The Beatles>]>
# >>> m2 = Membership.objects.create(person=paul, group=beatles,
# ...     date_joined=date(1960, 8, 1),
# ...     invite_reason="Wanted to form a band.")
# >>> beatles.members.all()
# <QuerySet [<Person: Ringo Starr>, <Person: Paul McCartney>]>

# 一对一关联：一个GPS对应一个餐厅OneToOneField

class CommonInfo(models.Model):
    name=models.CharField(max_length=100)
    age=models.PositiveIntegerField()

    # 在Meta中填入了abstrate=True ,该模型不会创建数据库表
    class Meta:
        abstract=True
