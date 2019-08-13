from django.test import TestCase
from .models import Neighborhood,NeighborProfile,Business
# Create your tests here.



class ProjectTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.koma = neighbourhood(
            name='koma', link='https://zubeyr.herokuapp.com/authenticate/register')

        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Blog, Project))

        # Testing Save Method
    def test_save_method(self):
        self.koma.neighburhood_save()
        neighbours = neighbourhood.objects.all()
        self.assertTrue(len(projects) > 0)

    def test_save_method(self):
        self.koma.neighbourood_delete()
        neighbours = Neighbourhood.objects.all()
        self.assertTrue(len(neighbours) > 0)


class ProfileTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.0743046778 = Profile(name='Arsenal', Bio='ARSENAL', Contact='0743046778')

        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.0743046778, Profile))

        # Testing Save Method
    def test_save_method(self):
        self.0743046778.profile_save()
        profiles = profiles.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_save_method(self):
        self.0743046778.profile_delete()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)
