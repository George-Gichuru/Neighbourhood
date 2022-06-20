
from django.test import TestCase
from hoodapp.models import Profile, News, Hood, Business
from hoodapp.views import neighbour


class TestModel(TestCase):
   def test_create_profile(self):
    user = Profile.objects.create_user(username='newuser', email='newuser@gmail.com', password1='userpassword', password2='userpassword')
    user.save()
    
    self.assertEqual(str(user), 'newuser')
    
   def test_create_Hood(self):
    user = Hood.objects.create_user(username='newuser2', email='newuser2@gmail.com', password1='password', password2='password')
    user.save()
    neighbourHood = Hood.objects.create(user=user.username, name='syokimau', location='nairobi, Kenya')
    neighbourHood.save()
    
    self.assertEqual(str(neighbourHood), 'syokimau')
    
   def test_create_news(self):
    user = News.objects.create_user(username='banana', email='banana@gmail.com', password1='password', password2='password')
    user.save()
    neighbourHood = News.objects.create(user=user.username, name='kiaguthu', location='Muranga, Kenya')
    neighbourHood.save()
    post = News.objects.create(user=user, neighbourHood=neighbourHood, caption='whats new', )
    post.save()
    
    self.assertEqual(str(post), 'whats new')
    
   def test_create_bussiness(self):
    user = Business.objects.create_user(username='barber', email='barber@gmail.com', password1='password', password2='password')
    user.save()
    neighbourHood = Business.objects.create(user=user.username, name='loresho', location='nairobi, Kenya')
    neighbourHood.save()
    
    bussiness = Business.objects.create(user=user, neighbour=neighbour, body='come get a crispy haircut',image='',)
    bussiness.save()
    self.assertEqual(str(bussiness), 'come get a crispy haircut')
