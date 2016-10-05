# from datetime import timedelta
# from django.contrib.auth.models import User
# from django.test.testcases import TestCase
# from django.utils.timezone import now
# from event.models import Event, Registration
# from common.models import Author
# from django.core.exceptions import ObjectDoesNotExist


# class TestModels(TestCase):
#     def create_event(self):
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
#         return event

#     def create_registraion(self,event,user):
#         reg = Registration.objects.create(
#             event=event,
#             attendee=user,
#             skype_id='tareq.obaida'
#         )
#         return reg

#     def test_create_event(self):
#         new = self.create_event()
#         self.assertTrue(isinstance(new, Event))
#         print(new)

#     def test_create_registraion(self):
#         event = self.create_event()
#         user = User.objects.create_user('tareq', 'tareq@gmail.com', 'pass1234')
#         reg = self.create_registraion(event,user)
#         self.assertTrue(reg)
#         print(reg)
#         available_seats = reg.event.available_seats
#         self.assertEqual(available_seats, 19)
#         is_open = reg.event.is_registration_open
#         self.assertTrue(is_open)

#     def test_if_user_registered(self):
#         event = self.create_event()
#         user = User.objects.create_user('tareq', 'tareq@gmail.com', 'pass1234')
#         user2 = User.objects.create_user('tareq2', 'tareq2@gmail.com', 'pass1234')
#         reg = self.create_registraion(event,user)
#         registered = event.registration_set.get(attendee=user)
#         print('registered',registered.skype_id)
#         with self.assertRaises(ObjectDoesNotExist):
#             registered = event.registration_set.get(attendee=user2)
#             print('registered',registered.skype_id)


