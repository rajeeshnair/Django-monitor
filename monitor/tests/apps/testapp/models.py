from django.db import models
from django.contrib import admin
import monitor

class Author(models.Model):
    """ Moderated model """
    name = models.CharField(max_length = 100)
    age = models.IntegerField()

    class Meta:
        app_label = 'testapp'

    def __unicode__(self):
        return self.name

monitor.nq(Author)

class Publisher(models.Model):
    """ Not moderated model """
    name = models.CharField(max_length = 255)
    num_awards = models.IntegerField()

    class Meta:
        app_label = 'testapp'

    def __unicode__(self):
        return self.name

class Book(models.Model):
    """ Moderated model with related objects """
    isbn = models.CharField(max_length = 9)
    name = models.CharField(max_length = 255)
    pages = models.IntegerField()
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    
    class Meta:
        app_label = 'testapp'

monitor.nq(Book, ['supplements', ])

class Supplement(models.Model):
    """ Objects of this model get moderated along with Book"""
    serial_num = models.IntegerField()
    book = models.ForeignKey(Book, related_name = 'supplements')

monitor.nq(Supplement)

