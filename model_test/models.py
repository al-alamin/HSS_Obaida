from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from ckeditor_uploader.fields import RichTextUploadingField


class ModelTest(models.Model):

    name = models.CharField(max_length=50)
    exam_type_choices = (
        ('gre', 'GRE'),
        ('tofel', 'TOFEL'),
        ('gmat', 'GMAT'),
        ('sat', 'SAT')
    )
    exam_type = models.CharField(choices=exam_type_choices, max_length=30,
                                 help_text='Select Exam Type: ')
    fee = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.name


class SubjectTest(models.Model):

    name = models.CharField(max_length=50)
    # can this field be bannk and null?
    model_test = models.ForeignKey(ModelTest)
    subject_type_choices = (
        ('analytical', 'GRE'),
        ('verbal', 'Verbal'),
    )
    subject_type = models.CharField(choices=subject_type_choices, max_length=30,
                                    help_text='Select Subject Type: ')
    fee = models.PositiveSmallIntegerField(default=0)
    # Duration is important becasue for gre/SAT/Tofel/gmat one subject test
    # time will be different
    duration = models.PositiveSmallIntegerField(default=30)
    # total marks or per mcq marks is important becasue for gre/SAT/Tofel
    # there will be different no of mcqs in a subject test total marks will be
    # differnt.
    per_mcq_marks = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return self.name


class MCQ(models.Model):

    subject_test = models.ForeignKey(SubjectTest)
    # file will be saved to media/ckeditor_uploads specified in base.py. There are
    # other options to customize upload location
    question = RichTextUploadingField("Question")
    choice_a = models.CharField(max_length=200, blank=True, null=True)
    choice_b = models.CharField(max_length=200, blank=True, null=True)
    choice_c = models.CharField(max_length=200, blank=True, null=True)
    choice_d = models.CharField(max_length=200, blank=True, null=True)
    choice_e = models.CharField(max_length=200, blank=True, null=True)
    choice_f = models.CharField(max_length=200, blank=True, null=True)

    answer = ArrayField(models.CharField(max_length=3))
    answer_explanation = RichTextUploadingField(
        "Answer Explanation: ", blank=True, null=True)

    def __str__(self):
        return self.question


class Result(models.Model):

    user = models.ForeignKey(User)

    # This table is mainly for storing subject test result but...
    # A complete model test might have 5 different subject
    # test(For Gre a model test consists of 5 differnt subject test).
    # when a user finishes a whole model test ie
    # all the subject test and store this whole result here then model
    # test wise position calculation will be very easy. Other wise model
    # test wise position calcuation might become very db expension operation
    # model_test = models.ForeignKey(ModelTest, blank=True, null=True)

    subject_test = models.ForeignKey(SubjectTest, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    submission_time = models.DateTimeField(blank=True, null=True)
    marks = models.IntegerField(default=0)
    # For saving the answer the user submitted during the test
    myanswers = ArrayField(
        models.PositiveSmallIntegerField(), blank=True, null=True)

    def __str__(self):
        return self.user.username
