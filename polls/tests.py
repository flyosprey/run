from django.test import TestCase
from django.utils import timezone
import datetime
from .models import Question


class QuestionModelTest(TestCase):
    """
    was_published_recently() returns False for questions whose pub_date
    is in the future.
    """
    def test_was_published_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
