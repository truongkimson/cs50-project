from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
from django.views import generic
from django.utils import timezone


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latestQuestionList'

    def get_queryset(self):
        return Question.objects.filter(pubDate__lte=timezone.now()
                                       ).order_by('-pubDate')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        return Question.objects.filter(pubDate__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

    def get_queryset(self):
        return Question.objects.filter(pubDate__lte=timezone.now())


def vote(request, pk):
    question = get_object_or_404(Question, pk=pk)
    try:
        choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question,
                      'errorMessage': 'An error has occured!'})
    else:
        choice.votes += 1
        choice.save()
        return HttpResponseRedirect(reverse('polls:results',
                                            args=(pk,)))
