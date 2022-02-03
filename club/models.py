from django.db import models
from django.contrib.auth.user

class Meeting(models.Models):
    meetingtitle=models.CharField(max_length=255)
    meetingdate=models.DateField()
    

    def__str__(self):
        return self.meetingtitle

    class Meta:
        db_table='Meeting'
