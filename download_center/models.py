from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=25, unique=True,help_text='e,g; SOP, Resume, Mail, Others')

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Document(models.Model):
    degree_choices = (
        ('Undergrad','Undergrad'),
        ('Masters', 'Masters'),
        ('PhD', 'PhD'),
    )
    type = models.ForeignKey(Type)
    department = models.ForeignKey(Department)
    degree = models.CharField(choices=degree_choices, max_length=20)
    comment = models.CharField(max_length=500, blank=True)
    download_link = models.URLField()

    def __str__(self):
        return '-'.join((self.type.name, self.department.name, str(self.id)))
