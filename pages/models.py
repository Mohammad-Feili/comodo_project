from django.db import models

# this calss or table is for frequently questions that asked from admin or between users


class Questions(models.Model):

    subject = models.TextField()
    context = models.TextField()
    sneder_id = models.CharField(max_length=40)
    sender_name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.sender_name
