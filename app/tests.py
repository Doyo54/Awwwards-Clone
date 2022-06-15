from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile,Post
# Create your tests here.
class testPost(TestCase):
    def setUp(self):
        self.profile = Profile(name='doyo')
        self.profile.save_profile()

        self.image_test = Post(id=1, title='food', description='this is a test image',user=self.profile,
                                date= 'june 06 2022',image='default.png')
        self.image_test.save_post()

    def test_instance(self):
        self.assertTrue(isinstance(self.image_test, Post))

    def test_delete_post(self):
        self.image_test.delete_post()
        images = Post.objects.all()
        self.assertTrue(len(images) == 0)


    def tearDown(self):
        Post.objects.all().delete()
        Profile.objects.all().delete()


class TestProfile(TestCase):
    def setUp(self):
        self.user = User(username='doyo')
        self.user.save()

        self.profile_test = Profile(id=10, name='image', profile_picture='default.jpg', bio='this is a test profile',
                                    user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile_test, Profile))

    def test_save_profile(self):
        self.profile_test.save_profile()
        after = Profile.objects.all()
        self.assertTrue(len(after) == 0)
    
    def test_update_profile(self):
        self.profile_test.save_profile()
        self.profile_test.update_profile(self.profile_test.id, 'image/test.jpg')
        changed_img = Profile.objects.filter(profile_picture='image/test.jpg')
        self.assertTrue(len(changed_img) == 0)