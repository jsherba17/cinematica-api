# from django.test import TestCase
# from movie.models import User


# class AuthenticationTestCase(TestCase):
#  def setUp(self):
#        User.objects.create(username='testuser')

#  def test_user_created(self):
#        user = User.objects.filter(username='testuser')
#        self.assertTrue(user.exists())

class TestClassDemoInstance():
    value = 0

    def test_one(self):
        self.value = 1
        assert self.value == 1

    def test_two(self):
        self.value = 2
        assert self.value != 1