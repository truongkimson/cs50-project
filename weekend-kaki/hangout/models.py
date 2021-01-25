from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Hangout(models.Model):
    activity_choices = [
        ('FD', 'Food and drinks'),
        ('BP', 'Bars, pubs and clubs'),
        ('OD', 'Outdoor acitvities'),
        ('SE', 'Sports and exercises'),
        ('OT', 'Others'),
    ]

    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    activity_type = models.CharField(max_length=2,
                                     choices=activity_choices,
                                     )
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default=timezone.now)
    description = models.TextField(null=True,
                                   blank=True,
                                   default='Add a description')
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='owned_hangouts',
                              default=0)
    participants = models.ManyToManyField(User,
                                          related_name='participating_hangouts')

    def __str__(self):
        return self.name
