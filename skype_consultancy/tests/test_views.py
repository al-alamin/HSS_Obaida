# from datetime import timedelta
# from django.contrib.auth.models import User
# from django.test.testcases import TestCase
# from django.test import RequestFactory
# from django.utils.timezone import now
# from event.models import Event, Registration
# from common.models import Author
# from django.core.exceptions import ObjectDoesNotExist
# from skype_consultancy.views import skype


# class TestViews(TestCase):

#     def setUp(self):
#         # Every test needs access to the request factory.
#         self.factory = RequestFactory()
#         self.user = User.objects.create_user('tareq', 'tareqbuet@gmail.com', 'pass1234')

#         presenter = Author.objects.create(first_name='tareq',
#                                           last_name='obaida',
#                                           email='tareqbuet@gmail.com')
#         event = Event.objects.create(
#             title='test event',
#             presenter=presenter,
#             start_time=now() + timedelta(days=2),
#             end_time=now() + timedelta(days=2, hours=2),
#             registration_limit=20,
#             fee=100
#         )


#     def test_user_can_register_event(self):
#         request = self.factory.post(
#             '/skype/',
#             data = {'skype_id': 'testskypeid'}
#         )
#         request.user = self.user
#         response = skype(request)
#         context = response.get(header='context')
#         print(context)


