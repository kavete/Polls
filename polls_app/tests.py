from django.test import TestCase
import datetime
from django.utils import timezone

from .models import Question

 # was_published_recently() should return False for questions with a date in the future 
class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_date(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

     # was_published_recently() should return False for a questions not published within the last # wa
    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    # was_published_recently() should return true for a question published within the last day
    def test_was_published_recently_wit_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)
