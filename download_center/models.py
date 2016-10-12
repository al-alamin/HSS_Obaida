from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=25, help_text='e,g; SOP, Resume, Mail, Others')

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        self.name


class Document(models.Model):
    type = models.ForeignKey(Type)
    department = models.ForeignKey(Department)
    degree = models.CharField(choices=(('MS', 'MS'), ('PhD', 'PhD')), max_length=20)
    comment = models.CharField(max_length=500)
    download_link = models.URLField()

    def __str__(self):
        return '-'.join((self.type.name, self.department.name, self.id))
