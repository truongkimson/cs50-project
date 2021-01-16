import datetime
from django.utils import timezone
from django.test import TestCase
from .models import Question
from django.urls import reverse


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        futureDate = timezone.now() + datetime.timedelta(days=30)
        futureQuestion = Question(pubDate=futureDate)
        self.assertIs(futureQuestion.wasPublishedRecently(), False)


def create_question(questionText, days):
    return Question.objects.create(questionText=questionText,
                                   pubDate=timezone.now() +
                                   datetime.timedelta(days=days)
                                   )


class QuestionIndexViewTest(TestCase):
    def test_no_question(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No polls are available.')
        self.assertQuerysetEqual(response.context['latestQuestionList'], [])

    def test_past_question(self):
        create_question('Past question', days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latestQuestionList'],
                                 ['<Question: Past question>']
                                 )

    def test_future_question(self):
        create_question('Future question', days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, 'No polls are available.')
        self.assertQuerysetEqual(response.context['latestQuestionList'], [])

    def test_future_and_past_question(self):
        create_question('Past question', days=-30)
        create_question('Future question', days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latestQuestionList'],
                                 ['<Question: Past question>']
                                 )

    def test_two_past_questions(self):
        create_question('Past question 1', days=-30)
        create_question('Past question 2', days=-10)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latestQuestionList'],
                                 ['<Question: Past question 2>',
                                  '<Question: Past question 1>']
                                 )
