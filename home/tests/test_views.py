from django.test import TestCase
from django.core.urlresolvers import reverse
# from common.models import Author, AuthorRole


# class TestViews(TestCase):

#     def test_model_call_advisors_return_correct_data(self):
#         role = AuthorRole(role='R')
#         role.save()
#         author = Author(first_name='abu', last_name='obaida', email='tareqbuet@gmail.com',)
#         author.save()
#         author = Author(first_name='abu', last_name='tareq', email='tareqbuet@gmail.com')
#         author.save()
#         advisors = Author.objects.all()
#         print('advisors',advisors)


class TestHomeView(TestCase):
    
    def test_status_code(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)


class TestDecesionMakingView(TestCase):
    
    def test_decesion_making_status_code(self):
        response = self.client.get(reverse("decision_making"))
        self.assertEqual(response.status_code, 200)



class TestPreparationView(TestCase):
    
    def test_preparation_status_code(self):
        response = self.client.get(reverse("preparation"))
        self.assertEqual(response.status_code, 200)



class TestStandardExamView(TestCase):
    
    def test_standard_exam_status_code(self):
        response = self.client.get(reverse("standard_exam"))
        self.assertEqual(response.status_code, 200)



class TestApplicationView(TestCase):
    
    def test_application_status_code(self):
        response = self.client.get(reverse("application"))
        self.assertEqual(response.status_code, 200)


class TestGoogleSearchView(TestCase):
    
    def test_decesion_making_status_code(self):
        response = self.client.get(reverse("google_search"))
        self.assertEqual(response.status_code, 200)




