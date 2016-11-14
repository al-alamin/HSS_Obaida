import pytz

BD_TZ = pytz.timezone("Asia/Dhaka")
time_format = '%b. %d, %Y, %I:%M %p'

FIRST_REMINDER_HOUR = 24
SECOND_REMINDER_MINUTE = 60
FEEDBACK_REMINDER_MINUTE = 30

SUBJECT_REMINDER = "Your Reminder Email For The Event {0}"
SUBJECT_FEEDBACK = "We Appreciate Your Feedback"

BODY_REMINDER = """
     Hi {0},
     Hope you are doing well. This is a reminder email for the event {1} which you are registered for.
     The event will be held on {2} Bangladesh time and the event duration is {3} minutes.
     If you have any query please don't hesitate to email at support@mystudynotebook.com.
     Please don't forget to receive call from our Skype account (Skype ID is 'MSNB') at the mentioned time.
     We hope a very good day to you.

     Thanks and Regards,
     Support Team
     My Study Notebook
     Web: http://www.mystudynotebook.com
     Facebook Group: https://www.facebook.com/groups/mystudynotebook/
     """

BODY_FEEDBACK = """
    Hi {0},
    Thank you for participating in the event {1}.We would appreciate if you could give us some feedback on how was the skype session, if it met your expectations, how can we improve it etc. Let us know if you feel the session was helpful enough and if you would recommend it to your friends.
    Your feedback would help us improve the endeavor for helping other students in their venture.
    Please feel free to write to us at support@mystudynotebook.com or our Facebook group https://www.facebook.com/groups/mystudynotebook/.
    Again thanks for joining the session.

    Thanks and Regards,
    Support Team
    My Study Notebook
    Web: http://www.mystudynotebook.com
    Facebook Group: https://www.facebook.com/groups/mystudynotebook/
    """
body_event_registration = """
    Hi {0},
    Your registration is confirmed for the event {1}.
    The event will be held on {2} Bangladesh time and the event duration is {3} minutes.
    If you have any query please don't hesitate to email at support@mystudynotebook.com.
    Please don't forget to receive call from our Skype account (Skype ID is 'MSNB') at the mentioned time.
    We hope a very good day to you.<br>
    {4}

    <br>
    Thanks and Regards,<br>
    Support Team <br>
    My Study Notebook <br>
    Web: http://www.mystudynotebook.com <br>
    Facebook Group: https://www.facebook.com/groups/mystudynotebook/ <br>
    """
body_new_user = """
    Hi,
    Congratulations and welcome to My Study Notebook. You have successfully created your account and now you have access to all the features of My Study Notebook. Below is your account information:
    Your Username : {0}
    Your Registered Email : {1}
    Your Authentication Provider: {2}

    Thanks again for joining. We hope a very good day to you.

    Thanks and Regards,
    Support Team
    My Study Notebook
    Web: http://www.mystudynotebook.com
    Facebook Group: https://www.facebook.com/groups/mystudynotebook/
    """