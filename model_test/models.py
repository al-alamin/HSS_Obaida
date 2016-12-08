from django.db import models


class ModelTest(models.Model):

    name = models.CharField(max_length=50)
    exam_type_choices = (
        ('gre', 'GRE'),
        ('tofel', 'TOFEL'),
        ('gmat', 'GMAT')
    )
    exam_type = models.CharField(choices=exam_type_choices, max_length=30,
                                 help_text='Select Exam Type: ')
    fee = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.name

