from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from app1.models import Question, Choice


class IndexView(generic.ListView):
    template_name = 'app1/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]
        # return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'app1/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'app1/results.html'


# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # 1 template=loader.get_template('app1/index.html')
    context = {
        'latest_question_list': latest_question_list
    }
    # output=','.join([q.question_text for q in latest_question_list])
    # 2 return HttpResponse(template.render(context,request))
    # 1 2 处代码可以使用如下代码替换
    return render(request, 'app1/index.html', context)


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question does not exist')
    # return render(request, 'app1/detail.html', {'question': question})
    # return HttpResponse("You're looking at question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'app1/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'app1/results.html', {'question': question})
    # response = "You're looking at the results of question %s."


# return HttpResponse(response % question_id)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'app1/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('app1:results', args=(question.id,)))
    # return HttpResponse("You're voting on question %s." % question_id)


# ------------------------


def database_api():
    # 查询全部数据
    Question.objects.all()
    # from django.utils import timezone
    Question(question_text='what`s new', pub_date=timezone.now()).save()
    # 把数据差出来以后，通过重新赋值，调用save方法，插入数据库，进行更新操作

    # 查询 同时 字段名为id的，查询时，可以使用pk=id去查询
    Question.objects.filter(id=1)

    # 模糊查询
    Question.objects.filter(question_text__startswith='What')
    current_year = timezone.now().year
    # 更具时间字段的年份查询
    Question.objects.get(pub_date__year=current_year)
    Question.objects.get(pk=1).delete()
    # 更多关于和数据库的api查找文档：https://docs.djangoproject.com/zh-hans/3.0/topics/db/queries/


def main():
    database_api()


if __name__ == '__main__':
    main()
