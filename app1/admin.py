from django.contrib import admin

# Register your models here.
from app1.models import Question,Choice

class ChoiceInline(admin.TabularInline):
    model=Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # 定义admin页面的字段顺序

    #fields = ['pub_date','question_text']

    fieldsets = [
        (None,{'fields':['question_text']}),
        ('Date information',{'fields':['pub_date']}),
    ]
    list_display = ('question_text','pub_date','was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    inlines = [ChoiceInline]

admin.site.register(Question,QuestionAdmin)
# admin.site.register(Choice)